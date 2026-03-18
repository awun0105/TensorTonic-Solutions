def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    max_val = max(values)
    min_val = min(values)
    
    # Handle the case where all values are identical
    if max_val == min_val:
        return [0] * len(values)
    
    bin_width = (max_val - min_val) / num_bins
    bins = []
    
    for v in values:
        # Calculate the raw index using floor division (int conversion)
        # We subtract min_val to shift the range to start at 0
        bin_idx = int((v - min_val) / bin_width)
        
        # Clamp the index. This handles the edge case where v == max_val
        # which would otherwise result in an index equal to num_bins.
        clamped_idx = min(bin_idx, num_bins - 1)
        bins.append(clamped_idx)
        
    return bins