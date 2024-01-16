import tensorflow as tf
import os

# GPU 할당
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 모델 정의
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# 모델 설정
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# x_train을 정의
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 모델 학습
with tf.device("/GPU:0"):
    model.fit(x_train, y_train, batch_size=128, epochs=10)

# 모델 평가
model.evaluate(x_test, y_test)