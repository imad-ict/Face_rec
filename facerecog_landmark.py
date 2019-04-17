import PIL.Image
import PIL.ImageDraw
import face_recognition

#Load your image from location
image = face_recognition.load_image_file('samp.jpg')

facemarks = face_recognition.face_landmarks(image)

number_faces = len(facemarks)

print('{} face found.'.format(number_faces))

image_array = PIL.Image.fromarray(image)

draw = PIL.ImageDraw.Draw(image_array)

for marks in facemarks:
    for name, listofpoints in marks.items():
        print("{} in this face has the following points:{}".format(name,listofpoints))
        draw.line(listofpoints, fill='blue',width=4)

image_array.show()
