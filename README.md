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

# Workflow of the Application
![Flowchart (2)](https://github.com/Atharva0177/Test-Git/assets/118592869/30663d9a-c41f-4d81-8897-4ad3603c2ad5)  
* **Video Processing:** This component is responsible for processing video feeds from cameras installed in the railway environment. The video processing component analyzes the video feeds to detect any suspicious activity or behavior.  
* **Crowd Monitoring:** This component is responsible for monitoring the crowd in the railway environment. The crowd monitoring component uses sensors and cameras to detect any unusual crowd behavior or movement.  

* **Mobile App:** This component is a mobile application that is used by railway authorities to report and respond to incidents of crime in the railway environment. The mobile app allows railway authorities to receive alerts, view video feeds, and communicate with other authorities.  

* **Incident Detection:** This component is responsible for detecting incidents of crime in the railway environment. The incident detection component receives data from the video processing and crowd monitoring components and uses machine learning algorithms to detect any suspicious activity or behavior.    

* **Incident Reporting:** This component is responsible for reporting incidents of crime to the railway authorities. The incident reporting component sends alerts to the mobile app used by railway authorities, along with video feeds and other relevant information.  

* **Incident Response:** This component is responsible for responding to incidents of crime in the railway environment. The incident response component allows railway authorities to communicate with each other and coordinate their response to incidents of crime.  





# Operating the application for the Camera Data Input and Video Processing
Let's start by opening the .exe file for the data input and processing

* **Opening the Application**  
We will start by opening the application for the data input and video processing by clicking on the `GUI.exe` file.
Open the highlighted file by Double-Clicking on the Icon. 
![Screenshot 2023-11-26 144042](https://github.com/Atharva0177/Test-Git/assets/118592869/46d2dd57-90da-4830-9271-690ad21293c1)  



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
After entering all the details CLICK on `ADD CAMERA DATA` to be viewed in the Data Window  
![Screenshot 2023-11-26 151016](https://github.com/Atharva0177/Test-Git/assets/118592869/91d0c585-156f-4106-b0dc-b5c45350829f)  
Then CLICK on `RUN CODE` which will display ` Camera Data has been saved to _Location_` prompt to indicate that the entered data is stored locally as an Excel Sheet in .csv Format.  
![Screenshot 2023-11-26 151304](https://github.com/Atharva0177/Test-Git/assets/118592869/605e1027-e35d-425b-a22c-92a0f30431eb)  
Then we can see locally that a New Folder is Created under the title `Camera_loc_database` and in that a .csv file has been created  
![Screenshot 2023-11-26 151815](https://github.com/Atharva0177/Test-Git/assets/118592869/2c533f6d-8154-43c1-b84c-a3f92fe1ee16)  
 
![Screenshot 2023-11-26 151856](https://github.com/Atharva0177/Test-Git/assets/118592869/e662ddea-ce00-47ef-94cc-c0a934bd94ef)
 

* **Video Proceesing Window**  
Now, we move to the Video Processing Window in which the Feed from the CCTV will be processed as per the requirements.
To open the Video Processing Tab CLICK on `VIDEO PROCESSING`  
![Screenshot 2023-11-26 152340](https://github.com/Atharva0177/Test-Git/assets/118592869/9e8672d7-3dd9-45e7-96d2-25fc41ec0fb5)  
The First Parameter is to SELECT the Video which is to be proceesed.
To SELECT the Video CLICK on `BROWSE VIDEO` which will open the File Explorer and then select the required video.  
![Screenshot 2023-11-26 152606](https://github.com/Atharva0177/Test-Git/assets/118592869/5977258f-6625-481a-b5c1-0ed891113308)    
![Screenshot 2023-11-26 152708](https://github.com/Atharva0177/Test-Git/assets/118592869/6e1fb3b4-0e20-4a4d-b92c-03bc104abb26)  
 
Also the application can accept the Video in multiple formats such as .mp4, .avi, .mkv
  
The next step is to decide the snippet's parameters which are the Frame Width and Height as well as the Duration, if none of the parameters are entered it will take default values as 
224x224 pixels and a duration of 2 seconds.  
![Screenshot 2023-11-26 153239](https://github.com/Atharva0177/Test-Git/assets/118592869/b724a20b-bbe4-4ea0-94e2-1b5aa23b7ace)    
Then we can select from the following BUTTONS as per our requirement  
- **Create Snippets:** After clicking on this `Create Snippets` the entered Video will be processed as per the specifications and the created SNIPPETS are stored locally  
  ![Screenshot 2023-11-26 153840](https://github.com/Atharva0177/Test-Git/assets/118592869/b6813a8b-d2fd-4c84-8d8e-a584ae55b3fb)  
A new Folder is Created under the Title `output_resized` in which the snippets are saved in .avi format  
![Screenshot 2023-11-26 154007](https://github.com/Atharva0177/Test-Git/assets/118592869/b7ca8c20-76b9-4a6c-ae21-6221b463052e)
![Screenshot 2023-11-26 154300](https://github.com/Atharva0177/Test-Git/assets/118592869/cea6e000-e60e-4d36-a63a-95d85bebd625)  



- **Create Frames:** When CLICKED on the `Create Frames` button all the individual frames for the selected video will be created and stored locally
![Screenshot 2023-11-30 215744](https://github.com/Atharva0177/Test-Git/assets/118592869/0343a87d-6cb7-4f1c-a06b-68ae18b3c865)
A new Folder is Created under the Title `output_frames` in which the extracted frames will be stored
![Screenshot 2023-11-30 215927](https://github.com/Atharva0177/Test-Git/assets/118592869/79132361-4b34-4760-83bc-192a586bbb80)

![Screenshot 2023-11-30 215957](https://github.com/Atharva0177/Test-Git/assets/118592869/6c5f03bd-0a16-43eb-bcc5-b676e08100f1)

- **Self Capture:** The `Self Capture` button when clicked on accesses the webcam of your device and when provided with specified time duration will start to capture from the camera and convert into snippets of desired duration  
Once clicked on `Self Capture` the button changes to `Stop Capture` denoting the capture has started and when again clicked will show a prompt `Webcam Capture has Stopped` and stop the capturing   
![Screenshot 2023-11-30 215249](https://github.com/Atharva0177/Test-Git/assets/118592869/19ca7a6f-3e72-4d64-b235-cc9bac6cb3a1)  
A new Folder is Created under the Title `output_webcam_snippets` in which the snippets from the webcam will be stored  
![Screenshot 2023-11-30 220736](https://github.com/Atharva0177/Test-Git/assets/118592869/b372c268-ade6-494e-9bad-2311743856ea)
![Screenshot 2023-11-30 220817](https://github.com/Atharva0177/Test-Git/assets/118592869/888f9c18-c466-4e63-9f50-d041c2865de9)  

- **Browse Images and Paste:** When CLICKED on `Browse Images and Paste` the user is able to transfer any type of images from any location in the device to the root folder of the application
![Screenshot 2023-11-30 221250](https://github.com/Atharva0177/Test-Git/assets/118592869/a2af22d0-55a2-41c6-bf81-42ef43061bfb)
A new Folder is Created under the title `output_images` in the root folder of the application where the transfered images are stored
![Screenshot 2023-11-30 221614](https://github.com/Atharva0177/Test-Git/assets/118592869/28bc5afb-d5f9-4455-8340-7724bf03ab3c)
![Screenshot 2023-11-30 221648](https://github.com/Atharva0177/Test-Git/assets/118592869/3aee919f-4b5d-49e9-b14f-9c97b8389322)

- **Transfer Folder:** This `Transfer Folder` button allows the user to transfer any type of folder from anywhere in the device to anywhere in the device
![Screenshot 2023-11-30 221943](https://github.com/Atharva0177/Test-Git/assets/118592869/9a0124c2-20dc-4096-8b3e-b51bdce12881)  
For Example: I want to transfer a Folder named "Dice_30-11-2023_22-22-23" to a specifed destination lets say the root folder of the application
For that I will select the folder to be copied
![Screenshot 2023-11-30 222121](https://github.com/Atharva0177/Test-Git/assets/118592869/61d93668-007f-4dd4-b63f-a2eca1533dbc)
Then I will select the Destination Folder and the selected folder will be transferred to the Location
![Screenshot 2023-11-30 222420](https://github.com/Atharva0177/Test-Git/assets/118592869/bc95b69f-ed90-4783-82c6-29abcb4e874c)

# Going Further  
Thank you for going through this Tutorial! We hope that you found it valuable.  






 







  













