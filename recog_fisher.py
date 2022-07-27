import numpy as np
import cv2
import sys
import os

RESIZE_FACTOR = 4

class RecogFisherFaces:
    def __init__(self):
        cascPath = "haarcascades/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.face_dir = 'face_data'
        self.model = cv2.face.FisherFaceRecognizer_create()
        self.face_names = []

    def load_trained_data(self):
        names = {}
        key = 0
        for (subdirs, dirs, files) in os.walk(self.face_dir):
            for subdir in dirs:
                names[key] = subdir
                key += 1
        self.names = names 
        self.model.read('trained_data/fisher_trained_data.xml')

    def show_video(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            inImg = np.array(frame)
            outImg, self.face_names = self.process_image(inImg)
            cv2.imshow('Video', outImg)

            # When everything is done, release the capture on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_capture.release()
                cv2.destroyAllWindows()
                return

    def process_image(self, inImg):
        frame = cv2.flip(inImg,1)
        resized_width, resized_height = (112, 92)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        
        gray_resized = cv2.resize(gray, (gray.shape[1]//RESIZE_FACTOR, gray.shape[0]//RESIZE_FACTOR))        
        faces = self.face_cascade.detectMultiScale(
                gray_resized,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )
        persons = []
        for i in range(len(faces)):
            face_i = faces[i]
            x = face_i[0] * RESIZE_FACTOR
            y = face_i[1] * RESIZE_FACTOR
            w = face_i[2] * RESIZE_FACTOR
            h = face_i[3] * RESIZE_FACTOR
            face = gray[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (resized_width, resized_height))
            confidence = self.model.predict(face_resized)
            print(confidence)
            if confidence[1]<100:
                person = self.names[confidence[0]]
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
                cv2.putText(frame, "%s - %.0f%%" % (person, 100-(confidence[1])//100), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,2,(0, 255, 0),2)
            else:
                person = 'Unknown'
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(frame, (person), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,2,(0, 255, 0),2)
            persons.append(person)
        return (frame, persons)


if __name__ == '__main__':
    recognizer = RecogFisherFaces()
    recognizer.load_trained_data()
    print("Press 'q' to quit video")
    recognizer.show_video()

