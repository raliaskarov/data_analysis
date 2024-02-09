def to_float_or_nan(value):
    try:
        return float(value)
    except ValueError:
        return np.nan 
