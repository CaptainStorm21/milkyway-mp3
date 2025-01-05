# AE_conversion.py

def km_to_au(kilometers):
    """
    Converts kilometers to Astronomical Units (AU).
    
    Args:
        kilometers (float): The distance in kilometers.
    
    Returns:
        float: The distance in AU.
    """
    AU_IN_KM = 149597870.7  # 1 AU in kilometers
    return kilometers / AU_IN_KM
