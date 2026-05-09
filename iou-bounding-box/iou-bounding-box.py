def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    Requirements
    Compute the intersection area from the overlap of the two rectangles
    Compute the union using the inclusion-exclusion principle
    Handle the case where boxes do not overlap
    Support floating-point coordinates
    Constraints
    Boxes are [x1, y1, x2, y2] with x1 <= x2 and y1 <= y2
    Coordinates can be integers or floats
    -10000 <= coordinates <= 10000
    Time limit: 300 ms
    """
  # 1. Identify the coordinates of the intersection rectangle
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    # 2. Compute the area of intersection
    # If x_right < x_left or y_bottom < y_top, there is no overlap
    intersection_width = max(0.0, x_right - x_left)
    intersection_height = max(0.0, y_bottom - y_top)
    intersection_area = intersection_width * intersection_height

    # 3. Compute the area of both bounding boxes
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    # 4. Compute the union area using Inclusion-Exclusion Principle
    # Union = Area A + Area B - Intersection Area
    union_area = area_a + area_b - intersection_area

    # 5. Handle division by zero (if both boxes have zero area)
    if union_area == 0:
        return 0.0

    return intersection_area / union_area

'''
import numpy as np

def iou_numpy(box_a, box_b):
    """
    Compute IoU using NumPy. 
    Supports single boxes or arrays of boxes.
    """
    # Ensure inputs are numpy arrays
    box_a = np.array(box_a)
    box_b = np.array(box_b)

    # 1. Determine intersection coordinates
    x_left = np.maximum(box_a[0], box_b[0])
    y_top = np.maximum(box_a[1], box_b[1])
    x_right = np.minimum(box_a[2], box_b[2])
    y_bottom = np.minimum(box_a[3], box_b[3])

    # 2. Intersection area
    # Use np.maximum(0, ...) to handle non-overlapping cases
    inter_area = np.maximum(0, x_right - x_left) * np.maximum(0, y_bottom - y_top)

    # 3. Individual box areas
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    # 4. Union area
    union_area = area_a + area_b - inter_area

    # 5. Compute IoU (adding epsilon to avoid division by zero)
    return inter_area / (union_area + 1e-7)
'''