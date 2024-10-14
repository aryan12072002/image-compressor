# Image Upload and Compression App

![Image Compression](https://img.shields.io/badge/Django-5.0.7-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10.11-blue) ![Pillow](https://img.shields.io/badge/Pillow-10.0.0-orange)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Image Upload and Compression App** is a Django-based web application that allows users to upload images, compress them, and manage their uploaded images efficiently. This project aims to provide a user-friendly interface for handling image uploads while ensuring optimized storage through image compression.

## Features

- **Image Upload:** Users can upload images directly from their devices.
- **Image Compression:** Uploaded images are automatically compressed to reduce file size.
- **Image Gallery:** View all uploaded images in a responsive gallery.
- **Download Option:** Easily download individual images.
- **Delete Functionality:** Remove images from the gallery.

## Technologies Used

- **Django**: A high-level Python web framework for building robust web applications.
- **Pillow**: A Python Imaging Library used for opening, manipulating, and saving image files.
- **HTML/CSS**: For building the front-end interface.
- **JavaScript**: For interactive features (if any are added).

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/image-upload-compression.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd image-upload-compression
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
8. **Open your browser and navigate to:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage

1. **Upload an Image:** Use the upload form on the homepage to select and upload an image.
2. **View Images:** After uploading, you'll be redirected to the gallery page where you can see all your uploaded images.
3. **Download or Delete Images:** Click on the corresponding buttons for each image to download or delete them.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.





```

