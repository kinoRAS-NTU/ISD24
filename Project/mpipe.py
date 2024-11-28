'''
Reference:
google-ai-edge / mediapipe
https://chuoling.github.io/mediapipe/solutions/holistic.html
https://github.com/google-ai-edge/mediapipe/tree/master
https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/pose.md
'''
import mediapipe as mp
import cv2
import numpy as np
import pyrealsense2 as rs

class MediaPipe:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils          # mediapipe drawing
        self.mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe drawing style
        self.mp_holistic = mp.solutions.holistic              # mediapipe pose detection
        self.holistic = self.mp_holistic.Holistic(
                        model_complexity=2,
                        enable_segmentation=True,
                        refine_face_landmarks=True)

    def detect(self, frame):
        return self.holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def draw_landmarks_on_image(self, rgb_image, detection_result):
        "Draw skeleton on image"
        annotated_image = np.copy(rgb_image)
        self.mp_drawing.draw_landmarks(
                annotated_image,
                detection_result.face_landmarks,
                self.mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_tesselation_style())
        self.mp_drawing.draw_landmarks(
                annotated_image,
                detection_result.pose_landmarks,
                self.mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())
        return annotated_image
    
    def print_result(self, image, results):
        "Print LEFT_SHOULDER pixel coordinates"
        image_height, image_width, _ = image.shape
        if results.pose_landmarks:
            print(f'Left Shoulder coordinates: ('
                f'{results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_SHOULDER].x * image_width}, '
                f'{results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_SHOULDER].y * image_height})'
            )

    def point_to_3D(self, landmark, image, depth_frame):
        "Convert Pixel coordinates to RealSense 3D coordinates"
        depth_intrinsics = depth_frame.profile.as_video_stream_profile().intrinsics
        image_height, image_width, _ = image.shape
        x = int(landmark.x * image_width)
        x = min(image_width-1, max(x, 0))
        y = int(landmark.y * image_height)
        y = min(image_height-1, max(y, 0))
        depth = depth_frame.get_distance(x, y)
        return rs.rs2_deproject_pixel_to_point(depth_intrinsics, [x, y], depth) if depth > 0 else None