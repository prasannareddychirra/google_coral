import numpy as np
import tensorflow as tf
from PIL import Image
from tflite_runtime.interpreter import load_delegate
from tflite_runtime.interpreter import Interpreter

# Path to your TensorFlow Lite model file
TFLITE_MODEL_PATH = '../models/model.tflite'
LABELS_PATH = '../labels.txt'

# Load labels
with open(LABELS_PATH, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Initialize TensorFlow Lite interpreter
interpreter = Interpreter(model_path=TFLITE_MODEL_PATH, 
                          experimental_delegates=[load_delegate('libedgetpu.so.1')])
interpreter.allocate_tensors()

# Get model details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

def run_inference(image_path):
    # Load image
    image = Image.open(image_path)
    image = image.resize((input_shape[1], input_shape[2]))
    input_data = np.expand_dims(load_image_into_numpy_array(image), axis=0)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Retrieve results
    output_data = interpreter.get_tensor(output_details[0]['index'])
    results = np.squeeze(output_data)
    top_k = results.argsort()[-5:][::-1]
    
    for i in top_k:
        if results[i] > 0.5:
            print(f"{labels[i]}: {results[i] * 100}%")

# Test the function
run_inference('../images/test_image.jpg')
