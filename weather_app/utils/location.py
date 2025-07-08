import geocoder

def detect_location():
    g = geocoder.ip('me')
    return g.city if g.city else None