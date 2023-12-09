import sys
import os
import shutil
import cv2
from datetime import datetime
import time
import threading
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFileDialog, QTabWidget, QListWidget,
    QTextEdit, QCheckBox, QSplitter, QMessageBox, QProgressBar, QComboBox, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from flask import Flask, render_template
from flaskwebgui import FlaskUI
from threading import Thread
from waitress import serve

app=Flask(__name__)
ui=FlaskUI(app)

# Function for camera data part
camera_locations = []

class CameraDataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        background_label = QLabel(self)
        pixmap = QPixmap("background_image.jpg")  # Replace with your image file
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        num_cameras_label = QLabel("Enter the number of cameras:")
        font= num_cameras_label.font()
        font.setBold(True)
        num_cameras_label.setFont(font)
        self.layout.addWidget(num_cameras_label)

        self.num_cameras_entry = QLineEdit()
        self.num_cameras_entry.setPlaceholderText("Number of Cameras")
        self.num_cameras_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        self.layout.addWidget(self.num_cameras_entry)

        camera_id_label = QLabel("Camera ID:")
        font= camera_id_label.font()
        font.setBold(True)
        camera_id_label.setFont(font)
        self.layout.addWidget(camera_id_label)

        self.camera_id_entry = QLineEdit()
        self.camera_id_entry.setPlaceholderText("Enter Camera ID")
        self.camera_id_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        self.layout.addWidget(self.camera_id_entry)

        latitude_label = QLabel("Latitude:")
        font= latitude_label.font()
        font.setBold(True)
        latitude_label.setFont(font)
        self.layout.addWidget(latitude_label)

        self.latitude_entry = QLineEdit()
        self.latitude_entry.setPlaceholderText("Enter Latitude")
        self.latitude_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        self.layout.addWidget(self.latitude_entry)

        longitude_label = QLabel("Longitude:")
        font= longitude_label.font()
        font.setBold(True)
        longitude_label.setFont(font)
        self.layout.addWidget(longitude_label)

        self.longitude_entry = QLineEdit()
        self.longitude_entry.setPlaceholderText("Enter Longitude")
        self.longitude_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        self.layout.addWidget(self.longitude_entry)

        add_camera_button = QPushButton("Add Camera Data")
        add_camera_button.clicked.connect(self.add_camera)
        add_camera_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(add_camera_button)

        self.camera_listbox = QListWidget()
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.camera_listbox.setSizePolicy(size_policy)

        # Set a fixed height for the camera_listbox
        self.camera_listbox.setMaximumHeight(500)
        self.layout.addWidget(self.camera_listbox)

        run_button = QPushButton("Run Code")
        run_button.clicked.connect(self.run_code)
        run_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(run_button)

        self.result_text = QLabel()
        self.layout.addWidget(self.result_text)

        self.setLayout(self.layout)

    def add_camera(self):
        camera_id = self.camera_id_entry.text()
        latitude_str = self.latitude_entry.text()
        longitude_str = self.longitude_entry.text()

        try:
            latitude = float(latitude_str)
            longitude = float(longitude_str)
        except ValueError:
            self.result_text.setText("Invalid latitude or longitude. Please enter valid numerical values.")
            return

        camera_locations.append({"camera_id": camera_id, "latitude": latitude, "longitude": longitude})

        self.camera_id_entry.clear()
        self.latitude_entry.clear()
        self.longitude_entry.clear()

        self.update_camera_list()

    def update_camera_list(self):
        self.camera_listbox.clear()
        for location in camera_locations:
            self.camera_listbox.addItem(f"Camera ID: {location['camera_id']} | Latitude: {location['latitude']} | Longitude: {location['longitude']}")

    def run_code(self):
        folder_name = "Camera_loc_database"
        os.makedirs(folder_name, exist_ok=True)
        existing_files = [file for file in os.listdir(folder_name) if file.endswith(".csv")]
        counter = len(existing_files) + 1
        timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M")
        csv_filename = os.path.join(folder_name, f"{timestamp}_{counter}.csv")

        with open(csv_filename, mode="w", newline="") as csv_file:
            fieldnames = ["Camera ID", "Latitude", "Longitude"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for location in camera_locations:
                writer.writerow({"Camera ID": location["camera_id"], "Latitude": location["latitude"], "Longitude": location["longitude"]})

        self.result_text.setText(f"Camera data has been saved to {csv_filename}.")

# Function for video processing part
output_webcam_snippets_folder = 'output_webcam_snippets'
os.makedirs(output_webcam_snippets_folder, exist_ok=True)
webcam_capture_flag = False

class VideoProcessingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        control_layout = QHBoxLayout()

        self.video_preview_label = QLabel()
        self.video_preview_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.video_preview_label)

        video_label = QLabel("Video File:")
        font = video_label.font()
        font.setBold(True)
        video_label.setFont(font)
        self.layout.addWidget(video_label)

        self.video_entry = QLineEdit()
        self.video_entry.setPlaceholderText("Enter or Browse Video File")
        self.video_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        self.layout.addWidget(self.video_entry)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_video)
        browse_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(browse_button)

        self.layout.addLayout(control_layout)

        frame_width_label = QLabel("Frame Width:")
        font= frame_width_label.font()
        font.setBold(True)
        frame_width_label.setFont(font)
        self.layout.addWidget(frame_width_label)

        self.frame_width_entry = QLineEdit()
        self.frame_width_entry.setPlaceholderText("Frame Width (eg: 224)")
        self.frame_width_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        self.layout.addWidget(self.frame_width_entry)

        frame_height_label = QLabel("Frame Height:")
        self.layout.addWidget(frame_height_label)

        self.frame_height_entry = QLineEdit()
        self.frame_height_entry.setPlaceholderText("Frame Height (eg: 224)")
        self.frame_height_entry.setStyleSheet("background-color: lightyellow; color: purple;")
        font= frame_height_label.font()
        font.setBold(True)
        frame_height_label.setFont(font)
        self.layout.addWidget(self.frame_height_entry)

        snippet_duration_label = QLabel("Snippet Duration (seconds):")
        font = snippet_duration_label.font()
        font.setBold(True)
        snippet_duration_label.setFont(font)
        self.layout.addWidget(snippet_duration_label)

        self.snippet_duration_combo = QComboBox()
        self.snippet_duration_combo.addItem("1")
        self.snippet_duration_combo.addItem("2")
        self.snippet_duration_combo.addItem("3")
        self.snippet_duration_combo.addItem("4")
        self.snippet_duration_combo.addItem("5")
        self.snippet_duration_combo.addItem("6")
        self.snippet_duration_combo.addItem("7")
        self.snippet_duration_combo.addItem("8")
        self.snippet_duration_combo.addItem("9")
        self.snippet_duration_combo.addItem("10")
        self.snippet_duration_combo.addItem("15")
        self.snippet_duration_combo.addItem("20")
        self.snippet_duration_combo.addItem("25")
        self.snippet_duration_combo.addItem("30")
        self.snippet_duration_combo.setPlaceholderText("Select Snippet Duration")
        self.snippet_duration_combo.setStyleSheet("background-color: lightyellow; color: purple;")
        self.snippet_duration_combo.setFixedWidth(200)
        self.layout.addWidget(self.snippet_duration_combo)

        self.result_text = QLabel()
        self.layout.addWidget(self.result_text)

        

        create_snippets_button = QPushButton("Create Snippets")
        create_snippets_button.clicked.connect(self.create_snippets)
        create_snippets_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(create_snippets_button)

        create_frames_button = QPushButton("Create Frames")
        create_frames_button.clicked.connect(self.create_frames)
        create_frames_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(create_frames_button)

        self_capture_button = QPushButton("Self Capture")
        self_capture_button.clicked.connect(self.self_capture)
        self_capture_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(self_capture_button)

        browse_images_button = QPushButton("Browse Images and Paste")
        browse_images_button.clicked.connect(self.browse_images_and_paste)
        browse_images_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(browse_images_button)

        transfer_folder_button = QPushButton("Transfer Folder")
        transfer_folder_button.clicked.connect(self.transfer_folder)
        transfer_folder_button.setStyleSheet("background-color: lightgreen; color: black; font-weight: bold;")
        self.layout.addWidget(transfer_folder_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #3498db;
                border-radius: 5px;
                background-color: #ecf0f1;
                color: black;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                width: 1px;  /* Adjust the width as needed */
            }
        """)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress_bar)

        self.video_preview_label = QLabel()
        self.video_preview_label.setAlignment(Qt.AlignCenter)
        self.video_preview_label.setMinimumSize(250, 280)
        self.layout.addWidget(self.video_preview_label)

        self.setLayout(self.layout)

    def browse_video(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(filter="Video files (*.mp4 *.avi *.mkv)")
        self.video_entry.setText(file_path)

        self.update_video_preview(file_path)

    def update_video_preview(self, video_path):
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        cap.release()

        if ret:
            # Convert the frame from BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to QImage
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Resize the QImage to fit the QLabel (fit the entire preview box)
            scaled_image = q_image.scaled(self.video_preview_label.size(), aspectRatioMode=Qt.KeepAspectRatio)

            # Set the preview image and resize the QLabel
            self.video_preview_label.setPixmap(QPixmap.fromImage(scaled_image))
            self.video_preview_label.setFixedSize(scaled_image.size())
        else:
            self.result_text.setText("Error loading video preview.")
    
    def create_snippets(self):
        video_path = self.video_entry.text()
        frame_width = int(self.frame_width_entry.text()) if self.frame_width_entry.text().isdigit() else 224
        frame_height = int(self.frame_height_entry.text()) if self.frame_height_entry.text().isdigit() else 224

    # Use the current index of the combo box to get the selected snippet duration
        snippet_duration_index = self.snippet_duration_combo.currentIndex()
        snippet_durations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
        snippet_duration = snippet_durations[snippet_duration_index]

        output_folder = 'output_resized'
        os.makedirs(output_folder, exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            self.result_text.setText("Error opening video file.")
            return

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        snippet_frame_count = snippet_duration * fps
        snippets = []
        snippet_idx = 0

        while True:
            snippet_frames = []
            for _ in range(snippet_frame_count):
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.resize(frame, (frame_width, frame_height))
                snippet_frames.append(frame)

            if not snippet_frames:
                break

            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            snippet_path = os.path.join(output_folder, f'snippet_{timestamp}.avi')

            while os.path.exists(snippet_path):
                snippet_idx += 1
                snippet_path = os.path.join(output_folder, f'snippet_{timestamp}_{snippet_idx}.avi')

            snippet = cv2.VideoWriter(snippet_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

            for snippet_frame in snippet_frames:
                snippet.write(snippet_frame)

            snippet.release()
            snippets.append(snippet_path)
            snippet_idx += 1

            current_progress = len(snippets) / total_frames * 100
            self.progress_bar.setValue(int(current_progress))

        cap.release()
        self.progress_bar.setValue(0)
        self.result_text.setText("Snippets extraction and saving completed.")

    def create_frames(self):
        video_path = self.video_entry.text()
        output_folder = 'output_frames'
        os.makedirs(output_folder, exist_ok=True)
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            self.result_text.setText("Error opening video file.")
            return
        frame_idx = 0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            frame_path = os.path.join(output_folder, f'frame_{timestamp}.png')
            while os.path.exists(frame_path):
                frame_idx += 1
                frame_path = os.path.join(output_folder, f'frame_{timestamp}_{frame_idx}.png')
            cv2.imwrite(frame_path, frame)
            frame_idx += 1
            current_progress = frame_idx / total_frames * 100
            self.progress_bar.setValue(int(current_progress))
        cap.release()
        self.progress_bar.setValue(0)
        self.result_text.setText("Frames extraction and saving completed.")

    def browse_images_and_paste(self):
        file_dialog = QFileDialog()
        image_paths, _ = file_dialog.getOpenFileNames(filter="Image files (*.jpg *.png *.jpeg)")
        if not image_paths:
            return
        output_folder = 'output_images'
        os.makedirs(output_folder, exist_ok=True)
        for image_path in image_paths:
            image_name = os.path.basename(image_path)
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            destination_path = os.path.join(output_folder, f'image_{timestamp}_{image_name}')
            shutil.copy(image_path, destination_path)
        self.result_text.setText("Images copied to the designated folder.")

    def transfer_folder(self):
        source_folder = QFileDialog.getExistingDirectory(directory=os.path.expanduser("~"), caption="Select Source Folder")
        if not source_folder:
            return
        destination_folder = QFileDialog.getExistingDirectory(directory=os.path.expanduser("~"), caption="Select Destination Folder")
        if not destination_folder:
            return
        folder_name = os.path.basename(source_folder)
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        destination_folder = os.path.join(destination_folder, f"{folder_name}_{timestamp}")
        shutil.copytree(source_folder, destination_folder)
        self.result_text.setText(f"Folder '{folder_name}' copied to '{destination_folder}'.")

    def self_capture(self):
        frame_width = int(self.frame_width_entry.text()) if self.frame_width_entry.text().isdigit() else 224
        frame_height = int(self.frame_height_entry.text()) if self.frame_height_entry.text().isdigit() else 224

        snippet_duration_index = self.snippet_duration_combo.currentIndex()
        snippet_durations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
        snippet_duration = snippet_durations[snippet_duration_index]

        os.makedirs(output_webcam_snippets_folder, exist_ok=True)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            self.result_text.setText("Error opening webcam.")
            return

        fps = 30
        snippet_frame_count = snippet_duration * fps
        snippets = []
        snippet_idx = 0
        global webcam_capture_flag

        if not webcam_capture_flag:
            webcam_capture_flag = True
            self_capture_button = self.sender()  # Get the button that triggered this method
            self_capture_button.setText("Stop Capture")
            capture_thread = threading.Thread(target=self.webcam_capture_task, args=(cap, frame_width, frame_height, fps, snippet_frame_count))
            capture_thread.start()
        else:
            webcam_capture_flag = False
            self_capture_button = self.sender()  # Get the button that triggered this method
            self_capture_button.setText("Self Capture")
            self.result_text.setText("Webcam Snippet Capture Stopped.")

    def webcam_capture_task(self, cap, frame_width, frame_height, fps, snippet_frame_count):
        snippets = []
        snippet_idx = 0
        while webcam_capture_flag:
            snippet_frames = []
            for _ in range(snippet_frame_count):
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.resize(frame, (frame_width, frame_height))
                snippet_frames.append(frame)
            if not snippet_frames:
                break
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            snippet_path = os.path.join(output_webcam_snippets_folder, f'snippet_{timestamp}.avi')
            while os.path.exists(snippet_path):
                snippet_idx += 1
                snippet_path = os.path.join(output_webcam_snippets_folder, f'snippet_{timestamp}_{snippet_idx}.avi')
            snippet = cv2.VideoWriter(snippet_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
            for snippet_frame in snippet_frames:
                snippet.write(snippet_frame)
            snippet.release()
            snippets.append(snippet_path)
            snippet_idx += 1
        cap.release()
        self.result_text.setText("Webcam Snippet Capture Stopped.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Combined Application")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QSplitter {
                background-color: #ecf0f1;
                border: 1px solid #bdc3c7;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 4px 12px;
                border: 1px solid #3498db;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
                border: 1px solid #2980b9;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
        """)

        # Create a QSplitter
        splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(splitter)

        # Create panes for Camera Data and Video Processing
        self.camera_data_widget = CameraDataWidget()
        self.video_processing_widget = VideoProcessingWidget()

        # Add the panes to the splitter
        splitter.addWidget(self.camera_data_widget)
        splitter.addWidget(self.video_processing_widget)

        # Set the splitter handle width (optional)
        splitter.setHandleWidth(10)

        # Set the splitter color to light blue using style sheet
        splitter.setStyleSheet("""
            QSplitter {
                background-color: lightblue;
            }
            QWidget {
                color: purple;
            }
        """)
        self.camera_data_widget.layout.setAlignment(Qt.AlignTop)
        self.video_processing_widget.layout.setAlignment(Qt.AlignTop)
        self.show()

def index():
    return render_template('index.html')


def run_flask_app():
    app.run(port=5000)


if __name__ == "__main__":
    #ui.run()
    waitress_thread = Thread(target=run_flask_app)
    waitress_thread.start()

    # Use FlaskWebGui for creating a GUI window
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())