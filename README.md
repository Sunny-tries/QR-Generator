# QR-Generator
## Overview
This is a QR Code Generator is a Python application designed to create QR codes from user-provided website links. I uitilized **qrcode** and **PySimpleGUI** libraries, it offers a simple GUI where users can enter URLS to generate QR codes. Generated QR codes are saved as PNG files, and then application provides functionality to delete these files upon exiting. This was done to ensure no unnecessary files are left behind. This project serves as a refresher to Python programming, focusing on GUI development and handling QR Codes.

## Features
- Simple GUI: Easy to submit website link to generate QR Code.
- Automatic QR Code Generation: Creates QR code for the submitted link and displays it with the GUI.
- File Management: Saves each generated QR code as a PNG file and deletesthese files when the application is closed or when the user chooses to cancel.

  ## Dependencies
  - Python 3.x
  - PySimpleGUI
  - qrcode
  - os
 
To install PySimpleGUI and qrcode run:
```bash
pip3 install PySimpleGUI qrcode[pil]
```

## Usage
1) **Start the application**: Run the script to launch the QR Code Generator GUI.
2) **Enter a website link**: Paste or type in the URL which you want the QR Code for.
3) **Submit**: Click "submit" button to generate the QR code. The QR code will appear in the GUI, and a corresponding PNG file will be saved.
4) **Close or Cancel**: To exit, close the window or click the "Cancel" button. Upon exiting, all generated QR code files will be automatically deleted.


## Project Notes
- This project was created as quick exercise to refresh Python skills, specifically focusing on GUI creation and QR code generation.
- The application is not considered final and may be revisited for further improvements and features.

 ## Future Improvements
 - Enhance the file manangement system to allow the user to choose whether to keep the generated QR code files.
 - Change the GUI library to support a more efficient and cleaner experience while using the application.
 - Implemenet additional QR code customization options, such as changing colors, and adding logos.
 - Improve error handling for invalid URLS or other user inputs.

This application is a work-in-progess and was developed as a learning exercise. It demonstrates basic principles of GUI development and QR code generation in Python.
