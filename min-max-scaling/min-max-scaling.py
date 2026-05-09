def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    Requirements
    Scale each column independently to [0, 1]
    If a column has zero range (all values identical), set scaled values to 0.0
    Return a list of lists with the same shape as the input
    Return floats
    Constraints
    data is a non-empty rectangular matrix
    Values are numbers (int or float)
    Return a list of lists of floats
    Time limit: 300 ms
    """
    
    if not data or not data[0]:
        return []

    # zip(*data) groups elements by column, making it easy to find mins and maxs
    columns = list(zip(*data))
    
    mins = [min(col) for col in columns]
    ranges = [max(col) - min(col) for col in columns]
    
    scaled_data = []
    
    for row in data:
        scaled_row = []
        for j, val in enumerate(row):
            # If the column has zero range, set the scaled value to 0.0
            if ranges[j] == 0:
                scaled_row.append(0.0)
            else:
                # Apply the min-max scaling formula
                scaled_val = (val - mins[j]) / ranges[j]
                scaled_row.append(float(scaled_val))
        
        scaled_data.append(scaled_row)
        
    return scaled_data

'''
import numpy as np

def min_max_scale(X):
    x_min = np.min(X)
    x_max = np.max(X)
    
    # Chuẩn hóa về đoạn [0, 1]
    return (X - x_min) / (x_max - x_min)
'''