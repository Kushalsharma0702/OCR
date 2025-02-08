# OCR Text Extractor

A web application to extract text from images using **PaddleOCR** and save the result as a CSV file. The app provides a user-friendly interface to upload images, process them, and download the extracted text as CSV.

## Features

- Upload `.png`, `.jpg`, or `.jpeg` image files.
- OCR processing using **PaddleOCR** to extract text.
- Organize the extracted text into rows and columns based on its position.
- Provides a download link for the resulting CSV file.
- Displays a progress bar to track OCR processing.

## Prerequisites

Before you start, make sure you have the following installed on your system:

- **Python 3.7+**
- **Pip** (Python's package installer)

### Dependencies

To install the necessary libraries, you can use the `requirements.txt` file. The required dependencies are:

- Flask
- PaddleOCR
- PaddlePaddle

## Setup Instructions

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Kushalsharma0702/OCR-Implementation.git
cd OCR-Implementation
```

### 2. Set up a virtual environment (optional but recommended)

You can create a virtual environment to keep your project dependencies isolated.

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies

Once you have the virtual environment set up, install the dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Install PaddleOCR

PaddleOCR requires PaddlePaddle to be installed. Follow the [official installation guide](https://www.paddlepaddle.org.cn/install/quick) to ensure PaddlePaddle is installed correctly for your environment (e.g., CPU or GPU support).

Install PaddleOCR:

```bash
pip install paddleocr
```

### 5. Running the Application

After installing the dependencies, run the application:

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to access the application.

### 6. Using the Application

1. **Upload Image**: Select an image file (.png, .jpg, .jpeg).
2. **Run OCR**: Click "Run OCR and Generate CSV" to start the text extraction process.
3. **Download CSV**: Once the OCR is complete, you will see a link to download the CSV file containing the extracted text.

### 7. Folder Structure

```
OCR-Implementation/
│
├── app.py                # Flask app
├── requirements.txt      # Project dependencies
├── static/               # Static assets (CSS, images)
│   └── style.css         # Custom styles for the frontend
├── templates/            # HTML templates
│   └── index.html        # Frontend of the OCR app
├── uploads/              # Folder to store uploaded images
├── outputs/              # Folder for generated CSV files
└── README.md             # This README file
```

### 8. Output CSV Format

The resulting CSV file will contain the extracted text from the image. Each row in the CSV corresponds to a line of text in the image, and the columns are determined by the horizontal alignment of the text.

### 9. Error Handling

- If an unsupported file type is uploaded, the app will notify the user.
- If the OCR process encounters an error, an error message will be displayed.
  
### 10. Troubleshooting

- **OCR Issues**: If you face issues with OCR, make sure that PaddleOCR and PaddlePaddle are correctly installed. You may need to install additional dependencies for GPU support.
- **CSV Not Downloading**: Ensure that the `outputs` folder is writable and exists.

### 11. License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Happy OCR-ing! 🎉
# Proofs
FIle that has been tested ![image](https://github.com/user-attachments/assets/3f42aa89-b4f2-43d9-b60c-89efc2aaa1dd)

# RESULTS!!

![image](https://github.com/user-attachments/assets/40731535-58de-4974-862a-f69d51767650)
