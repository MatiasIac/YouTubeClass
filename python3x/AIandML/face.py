import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN

class FaceDetector(object):

    def __init__(self, mtcnn):
        self.mtcnn = mtcnn

    def overlay_transparent(self, background_img, img_to_overlay_t, x, y, overlay_size=None):
        bg_img = background_img.copy()
        
        if overlay_size is not None:
            img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

        b,g,r,a = cv2.split(img_to_overlay_t)
        overlay_color = cv2.merge((b,g,r))
        
        mask = cv2.medianBlur(a,5)

        h, w, _ = overlay_color.shape
        roi = bg_img[y:y+h, x:x+w]

        img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask = cv2.bitwise_not(mask))
        img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)
        bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)
        return bg_img

    def _draw(self, frame, boxes, probs, landmarks):
        try:
            for box, prob, ld in zip(boxes, probs, landmarks):
                # Draw rectangle on frame
                cv2.rectangle(frame,
                              (box[0], box[1]),
                              (box[2], box[3]),
                              (0, 0, 255),
                              thickness=2)

                # Show probability
                cv2.putText(frame, str(
                    prob), (box[2], box[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                # Draw landmarks
                cv2.circle(frame, tuple(ld[0]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[1]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[2]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[3]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[4]), 5, (0, 0, 255), -1)
        except:
            pass

        return frame

    def run(self):
        cap = cv2.VideoCapture(2)
        overlay = cv2.imread('eyeball.png', -1)

        while True:
            ret, frame = cap.read()
            try:
                # detect face box, probability and landmarks
                boxes, probs, landmarks = self.mtcnn.detect(frame, landmarks=True)
                # draw on frame
                self._draw(frame, boxes, probs, landmarks)

            except:
                pass

            # Show the frame
            cv2.imshow('Face Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        
# Run the app
mtcnn = MTCNN()
fcd = FaceDetector(mtcnn)
fcd.run()