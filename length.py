def convert_length(value, from_unit, to_unit):
    """Convert between centimeters and meters."""
    if from_unit == "cm" and to_unit == "m":
        return float(value) / 100
    elif from_unit == "m" and to_unit == "cm":
        return float(value) * 100
    elif from_unit == "mili" and to_unit == "cm":
        return float(value) / 10
    elif from_unit == "cm" and to_unit == "mili":
        return float(value) * 10
    elif from_unit == "m" and to_unit == "km":
        return float(value) / 1000
    elif from_unit == "km" and to_unit == "m":
        return float(value) * 1000
    elif from_unit == "km" and to_unit == "mile":
        return float(value) / 1.609
    elif from_unit == "mile" and to_unit == "km":
        return float(value) * 1.609
    else:
        return None
    



