def convert_weight(value, from_unit, to_unit):
    if from_unit == "mg" and to_unit == "g":
        return float(value) / 1000
    elif from_unit == "g" and to_unit == "mg":
        return float(value) * 1000
    elif from_unit == "g" and to_unit == "kg":
        return float(value) / 1000
    elif from_unit == "kg" and to_unit == "g":
        return float(value) * 1000 
    elif from_unit == "kg" and to_unit == "lb":
        return  float(value) * 2.205
    elif from_unit == "lb" and to_unit == "kg":
        return float(value) / 2.205
    else:
        return None