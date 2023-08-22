
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class NLPModel(tf.keras.Model):
    def __init__(self):
        super(NLPModel, self).__init__()
        self.embedding = layers.Embedding(input_dim=5000, output_dim=16)
        self.global_average = layers.GlobalAveragePooling1D()
        self.output_layer = layers.Dense(1, activation='sigmoid')

    def call(self, inputs, training=False):
        x = self.embedding(inputs)
        x = self.global_average(x)
        return self.output_layer(x)

def train_model():
    model = NLPModel()
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(train_data,
                        train_labels,
                        epochs=40,
                        batch_size=512,
                        validation_data=(test_data, test_labels),
                        verbose=1)
    return model, history

if __name__ == "__main__":
    train_model()
