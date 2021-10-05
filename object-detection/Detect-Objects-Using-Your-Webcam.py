
# Initialize environment
import tensorflow as tf
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

# Load the model
model_path = "/Users/rakesh_poduval/Projects/Object-detection/pre-trained/ssd_resnet152_v1_fpn_640x640_coco17_tpu-8/saved_model"

print('Starting loading model...', end='')
start_time = time.time()

model = tf.saved_model.load(model_path)

print('Finishing loading model...', end='')
end_time = time.time()
elapsed_time = end_time - start_time
print('Took {} seconds for loading the model into the environment...'.format(elapsed_time))

# Load label map data (for plotting)
# Label maps correspond index numbers to category names, so that when our convolution network 
# predicts 5, we know that this corresponds to airplane. Here we use internal utility functions, 
# but anything that returns a dictionary mapping integers to appropriate string labels would be fine.
label_path = "/Users/rakesh_poduval/Projects/Object-detection/models/research/object_detection/data/mscoco_label_map.pbtxt"
category_index = label_map_util.create_category_index_from_labelmap(label_path,use_display_name=True)

# Define the video stream
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, image_np = cap.read()
    # image_np = np.array(Image.open(image_path))
    input_tensor = tf.convert_to_tensor(image_np)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis, ...]
    # input_tensor = np.expand_dims(image_np, 0)
    detections = model(input_tensor)
    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                   for key, value in detections.items()}
    detections['num_detections'] = num_detections
    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    image_np_with_detections = image_np.copy()
    viz_utils.visualize_boxes_and_labels_on_image_array(
          image_np_with_detections,
          detections['detection_boxes'],
          detections['detection_classes'],
          detections['detection_scores'],
          category_index,
          use_normalized_coordinates=True,
          max_boxes_to_draw=200,
          min_score_thresh=0.3,
          agnostic_mode=False,
          line_thickness=8)
    cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800,600)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break