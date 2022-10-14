import numpy as np
from tensorflow_model_optimization.sparsity import keras as sparsity
import tensorflow as tf


###先构建Sequential_keras模型
def buildNet():
    l = tf.keras.layers
    model = tf.keras.Sequential([
        l.Conv2D(32, 5, padding='same', activation='relu', input_shape=[224, 224, 3]),
        l.MaxPooling2D((2, 2), (2, 2), padding='same'),
        l.BatchNormalization(),
        l.SeparableConv2D(64, 5, padding='same', activation='relu'),
        l.MaxPooling2D((2, 2), (2, 2), padding='same'),
        l.BatchNormalization(),
        l.SeparableConv2D(32, 5, padding='same', activation='relu'),
        l.MaxPooling2D((2, 2), (2, 2), padding='same'),
        l.BatchNormalization(),
        l.SeparableConv2D(32, 5, padding='same', activation='relu'),
        l.MaxPooling2D((2, 2), (2, 2), padding='same'),
        l.GlobalAveragePooling2D(),
        l.Dense(32, activation='relu'),
        l.Dropout(0.4),
        l.Dense(2, activation='softmax')])
    return model


model = buildNet()
###载入weight
#model.load_weights('keras_model_weights.h5')
###将keras各个layer转换成pruned_layer
'''
###可将整个keras_model直接转换成pruned_layer     
new_pruning_params = {
      'pruning_schedule': sparsity.PolynomialDecay(initial_sparsity=0.50,
                                                   final_sparsity=0.90,
                                                   begin_step=0,
                                                   end_step=end_step,
                                                   frequency=100)
}
new_pruned_model = sparsity.prune_low_magnitude(model, **new_pruning_params)
new_pruned_model.summary()
'''
###但当存在不支持转换的layer，将会报错，那么我们必须一个layer一个layer进行转换
pruning_schedule = sparsity.PolynomialDecay(
    initial_sparsity=0.50,
    final_sparsity=0.90,
    begin_step=0,
    end_step=10000,
    frequency=100)

pruned_model = tf.keras.Sequential()
for layer in model.layers:
    layerName = layer.name
    if ('conv2d' in layerName):
        print('conv')
        print(layerName)
        pruned_model.add(sparsity.prune_low_magnitude(
            layer,
            pruning_schedule
        ))
    elif ('dense' in layerName):
        print('dense')
        print(layerName)
        pruned_model.add(sparsity.prune_low_magnitude(
            layer,
            pruning_schedule
        ))

    else:
        pruned_model.add(layer)
pruned_model.summary()

pruned_model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer='adam',
    metrics=['accuracy'])

callbacks = [
    sparsity.UpdatePruningStep()
]

pruned_model.fit(
    train_generator,
    steps_per_epoch=4000,
    validation_data=validation_generator,
    validation_steps=200,
    initial_epoch=0,
    epochs=10,
    callbacks=callbacks)