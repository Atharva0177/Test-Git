# EnvisionAI: Using Exisiting CCTV Infrastructrure for Crime Detection, Crowd Management and Cleanliness

# Problem Statement:  
Develop an AI-based video surveillance system to detect potential criminal activities from existing security camera footage. Keeping records of critical information about the incident, assesses its nature and risk level, and communicates real-time alerts to authorities via APIs to facilitates swift response during disasters to stop the situation from escalating, enhancing overall situational awareness and public safety.

# Proposed Solution  
A Smart system that can help detect criminal activities using existing security cameras. This system will use advanced Artificial Intelligence (AI) and Machine Learning Algorithms to spot potential crimes as they happen and send alerts to the authorities via a mobile app, allowing faster response from authorities during times of disaster/ preventing a disaster.
Your proposed smart system that can detect criminal activities using existing security cameras is a promising solution for enhancing public safety and preventing disasters. By leveraging the power of advanced Artificial Intelligence (AI) and Machine Learning Algorithms, the system can proactively detect and respond to criminal activities in real-time, allowing for swift action by authorities during emergencies.
The system can be seamlessly integrated with existing security cameras, which can identify potential crimes as they occur and send alerts to the authorities through a mobile app. This ensures rapid response during emergencies and the prevention of disasters, making it an essential asset for law enforcement and security agencies.
While AI and machine learning algorithms can be effective in detecting criminal activities, they are not perfect and can sometimes produce false positives. Therefore, it is important to use these technologies in conjunction with human intelligence (Human Validation Mechanism) and expertise to ensure the best possible outcomes. proposed smart system has the potential to be a game-changer in enhancing security, safeguarding communities, and improving overall safety in various settings.

# Prerequisites
* **Hardware**   
__Existing CCTV Infrastructure:__  
Ensure the availability and deployment of a network of CCTV cameras in strategic locations, covering the areas targeted for crime detection.     
__Edge Devices:__  
Integrate edge devices such as edge servers or edge computing devices to enable distributed processing of data locally, reducing the need for centralized processing and enhancing system efficiency.  
__Hardware Resources:__  
Provide sufficient hardware resources, including Graphics Processing Units (GPUs) or Tensor Processing Units (TPUs), to support the computational demands of running advanced machine learning models for real-time crime detection.  

* **Software**  
__Machine Learning Frameworks:__  
Access and utilize cutting-edge machine learning frameworks, including 3D Convolutional Neural Networks (CNN), Multiple Instance Learning, and Video Transformer models, to analyze and identify patterns in CCTV footage.  
__Data Storage Infrastructure:__  
Implement a robust software infrastructure for data storage, ensuring scalability to handle large volumes of recorded crime data and historical CCTV footage. Include backup mechanisms to prevent data loss.  
__Communication Infrastructure:__  
Develop reliable software for network infrastructure to facilitate seamless communication and data transmission between CCTV cameras, machine learning models, databases, and the alerting utility.  
__Geolocation Services:__  
Integrate with geolocation services or Application Programming Interfaces (APIs) to accurately determine the geographical location of CCTV cameras and detected crime incidents.  


# Operating the application for the Camera Data Input and Video Processing
Let's start by opening the .exe file for the data input and processing

* **Opening the Application**  
We will start by opening the application for the data input and video processing by clicking on the .exe file.
Open the highlighted file by Double-Clicking on the Icon. 
![Screenshot 2023-11-26 144042](https://github.com/Atharva0177/Test-Git/assets/118592869/1231cfa9-2d4f-4fe4-8bbb-f4b4e15abb0a)

* **View of the Application**
After opening the Application, it should open the a Window in your PC with 2 Tabs for Camera Data and Video Processing respectively.
![Screenshot 2023-11-26 144754](https://github.com/Atharva0177/Test-Git/assets/118592869/ce3e4f3e-f4a7-416b-929e-88bcc0822c6d)

* **Camera Data Window**  
After opening the Window, the first tab is by Default the Camera Data Input Tab.  
The First Step is to Input the all the Camera Details.  
The Input Parameters include:
The Number of Cameras
Camera ID
Coordinates of the Cameras (i.e. Latitude and Longitude)
![Screenshot 2023-11-26 145136](https://github.com/Atharva0177/Test-Git/assets/118592869/235e5211-398b-4cd4-861d-d45e54ff4387)
After entering all the details CLICK on ADD CAMERA DATA to be viewed in the Data Window
![Screenshot 2023-11-26 151016](https://github.com/Atharva0177/Test-Git/assets/118592869/91d0c585-156f-4106-b0dc-b5c45350829f)
Then CLICK on RUN CODE which will display " Camera Data has been saved to _Location_" prompt to indicate that the entered data is stored locally as an Excel Sheet in .csv Format.
![Screenshot 2023-11-26 151304](https://github.com/Atharva0177/Test-Git/assets/118592869/605e1027-e35d-425b-a22c-92a0f30431eb)
Then we can see locally that a New Folder is Created under the title "Camera_loc_database" and in that a .csv file has been created
![Screenshot 2023-11-26 151815](https://github.com/Atharva0177/Test-Git/assets/118592869/abe62377-bd00-4699-85b7-093e145a1d81)
![Screenshot 2023-11-26 151856](https://github.com/Atharva0177/Test-Git/assets/118592869/63dca788-7eba-489e-a9be-74bffed65840)

* **Video Proceesing Window**
Now, we move to the Video Processing Window in which the Feed from the CCTV will be processed as per the requirements.
To open the Video Processing Tab CLICK on VIDEO PROCESSING
![Screenshot 2023-11-26 152340](https://github.com/Atharva0177/Test-Git/assets/118592869/9e8672d7-3dd9-45e7-96d2-25fc41ec0fb5)
The First Parameter is to SELECT the Video which is to be proceesed.
To SELECT the Video CLICK on BROWSE VIDEO which will open the File Explorer and then select the required video.
![Screenshot 2023-11-26 152606](https://github.com/Atharva0177/Test-Git/assets/118592869/5977258f-6625-481a-b5c1-0ed891113308)
![Screenshot 2023-11-26 152708](https://github.com/Atharva0177/Test-Git/assets/118592869/1944b831-ee8c-472c-a16f-ba7f7755728c)
Also the application can accept the Video in multiple formats such as .mp4, .avi, .mkv
  
The next step is to decide the snippet's parameters which are the Frame Width and Height as well as the Duration, if none of the parameters are entered it will take default values as 
224x224 pixels and a duration of 2 seconds.
![Screenshot 2023-11-26 153239](https://github.com/Atharva0177/Test-Git/assets/118592869/b724a20b-bbe4-4ea0-94e2-1b5aa23b7ace)  
Then we can select from the following BUTTONS as per our requirement
_* **Create Snippets**












