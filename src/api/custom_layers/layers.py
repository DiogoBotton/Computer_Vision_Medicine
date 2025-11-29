import tensorflow as tf
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Layer, GlobalMaxPooling2D, Conv2D

@tf.keras.utils.register_keras_serializable()
class ChannelAttention(Layer):
    def __init__(self, ratio=8, **kwargs):
        super(ChannelAttention, self).__init__(**kwargs)
        self.ratio = ratio
        self.avg_pool = GlobalAveragePooling2D() # Reduz a dimensionalidade, é uma camada que é utilizada após as camadas convolucionais
        self.max_pool = GlobalMaxPooling2D()

    def build(self, input_shape):
        # Camada densa de rede neural regulado pelo ratio
        self.fc1 = Dense(units=input_shape[-1]//self.ratio, activation='relu')
        self.fc2 = Dense(units=input_shape[-1], activation='sigmoid')

    def call(self, inputs):
        avg_out = self.avg_pool(inputs)
        max_out = self.max_pool(inputs)

        avg_out = self.fc2(self.fc1(avg_out))
        max_out = self.fc2(self.fc1(max_out))

        out = avg_out + max_out
        out = tf.expand_dims(tf.expand_dims(out, axis=1), axis=1)

        return inputs * out

class SpatialAttention(Layer):
    def __init__(self, kernel_size=7, **kwargs):
        super(SpatialAttention, self).__init__(**kwargs)
        self.conv2d = Conv2D(1, kernel_size, padding='same', activation='sigmoid')

    def call(self, inputs):
        avg_out = tf.reduce_mean(inputs, axis=-1, keepdims=True)
        max_out = tf.reduce_max(inputs, axis=-1, keepdims=True)
        concat = tf.concat([avg_out, max_out], axis=-1)
        return inputs * self.conv2d(concat)