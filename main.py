from face_detection import FaceDetection
from gender_detection import GenderDetection
from sunglass_modal import match_glass
import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

image = 'image-1.jpg'

gender = GenderDetection.detect(image)
face_data = FaceDetection.detect(image)

face_ratio = face_data.face_ratio
face_color = closest_colour(face_data.face_color)
nose = face_data.nose_rating
eye_color = closest_colour(face_data.eye_color)

matched_glass = match_glass(gender,face_ratio,eye_color,nose)

print(matched_glass)