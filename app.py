# # from paddleocr import PaddleOCR
# # import pandas as pd

# # # Initialize PaddleOCR
# # ocr = PaddleOCR(use_angle_cls=True, lang='en')

# # def extract_aligned_text_to_csv(image_path, output_csv_path):
# #     # Run OCR
# #     result = ocr.ocr(image_path, cls=True)

# #     # Collect text and coordinates
# #     text_data = []
# #     for line in result[0]:
# #         box, (text, _) = line
# #         x_min = box[0][0]  # x-coordinate of top-left corner
# #         y_min = box[0][1]  # y-coordinate of top-left corner
# #         text_data.append((text, x_min, y_min))

# #     # Sort data by y-coordinate first, then x-coordinate
# #     text_data.sort(key=lambda item: (item[2], item[1]))

# #     # Group text into rows using y-coordinate proximity
# #     threshold_y = 10  # Threshold for row grouping
# #     rows = []
# #     current_row = []
# #     prev_y = None

# #     for text, x, y in text_data:
# #         if prev_y is None or abs(y - prev_y) < threshold_y:
# #             current_row.append((text, x))
# #         else:
# #             rows.append(current_row)
# #             current_row = [(text, x)]
# #         prev_y = y
# #     if current_row:
# #         rows.append(current_row)

# #     # Align text into columns using x-coordinates
# #     aligned_rows = []
# #     for row in rows:
# #         row.sort(key=lambda item: item[1])  # Sort by x-coordinate
# #         aligned_row = [text for text, _ in row]
# #         aligned_rows.append(aligned_row)

# #     # Convert to DataFrame and save to CSV
# #     max_cols = max(len(row) for row in aligned_rows)
# #     df = pd.DataFrame(aligned_rows, columns=[f"Column_{i+1}" for i in range(max_cols)])
# #     df.to_csv(output_csv_path, index=False, header=False)

# #     print(f"Aligned text saved to {output_csv_path}")

# # # Example usage
# # image_path = r"C:\Users\sharm\Desktop\update-table.png"  # Replace with your image path
# # output_csv_path = r"C:\Users\sharm\Desktop\aligned_output11.csv"  # Output file path
# # extract_aligned_text_to_csv(image_path, output_csv_path)

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from paddleocr import PaddleOCR
# import pandas as pd

# # Initialize PaddleOCR
# ocr = PaddleOCR(use_angle_cls=True, lang='en')

# def extract_aligned_text_to_csv(image_path, output_csv_path):
#     # Run OCR
#     result = ocr.ocr(image_path, cls=True)

#     # Collect text and coordinates
#     text_data = []
#     for line in result[0]:
#         box, (text, _) = line
#         x_min = box[0][0]  # x-coordinate of top-left corner
#         y_min = box[0][1]  # y-coordinate of top-left corner
#         text_data.append((text, x_min, y_min))

#     # Sort data by y-coordinate first, then x-coordinate
#     text_data.sort(key=lambda item: (item[2], item[1]))

#     # Group text into rows using y-coordinate proximity
#     threshold_y = 10
#     rows = []
#     current_row = []
#     prev_y = None

#     for text, x, y in text_data:
#         if prev_y is None or abs(y - prev_y) < threshold_y:
#             current_row.append((text, x))
#         else:
#             rows.append(current_row)
#             current_row = [(text, x)]
#         prev_y = y
#     if current_row:
#         rows.append(current_row)

#     # Align text into columns using x-coordinates
#     aligned_rows = []
#     for row in rows:
#         row.sort(key=lambda item: item[1])
#         aligned_row = [text for text, _ in row]
#         aligned_rows.append(aligned_row)

#     # Convert to DataFrame and save to CSV
#     max_cols = max(len(row) for row in aligned_rows)
#     df = pd.DataFrame(aligned_rows, columns=[f"Column_{i+1}" for i in range(max_cols)])
#     df.to_csv(output_csv_path, index=False, header=False)

# def select_image():
#     file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
#     if file_path:
#         input_entry.delete(0, tk.END)
#         input_entry.insert(0, file_path)

# def save_csv():
#     file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
#     if file_path:
#         output_entry.delete(0, tk.END)
#         output_entry.insert(0, file_path)

# def run_ocr():
#     image_path = input_entry.get()
#     output_csv_path = output_entry.get()

#     if not image_path or not output_csv_path:
#         messagebox.showerror("Error", "Please provide both image path and CSV save location!")
#         return

#     try:
#         extract_aligned_text_to_csv(image_path, output_csv_path)
#         messagebox.showinfo("Success", f"Text data saved to {output_csv_path}")
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")

# # GUI Setup
# root = tk.Tk()
# root.title("OCR Text Extractor")
# root.geometry("500x300")

# # Input image selection
# tk.Label(root, text="Select Image File:", font=("Arial", 12)).pack(pady=10)
# input_entry = tk.Entry(root, width=40, font=("Arial", 10))
# input_entry.pack(padx=10, pady=5)
# tk.Button(root, text="Browse", command=select_image, font=("Arial", 10)).pack()

# # Output CSV location
# tk.Label(root, text="Save CSV File As:", font=("Arial", 12)).pack(pady=10)
# output_entry = tk.Entry(root, width=40, font=("Arial", 10))
# output_entry.pack(padx=10, pady=5)
# tk.Button(root, text="Save As", command=save_csv, font=("Arial", 10)).pack()

# # Run OCR Button
# tk.Button(root, text="Run OCR and Save", command=run_ocr, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

# # Start the GUI
# root.mainloop()
from flask import Flask, request, render_template, jsonify, send_from_directory
from paddleocr import PaddleOCR
import os
import csv
import time

# Initialize the Flask app and PaddleOCR
app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Directory to save uploaded images and output CSV files
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded image to the uploads folder
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    # Run OCR on the image
    result = ocr.ocr(image_path, cls=True)

    # Collect text and coordinates
    text_data = []
    for line in result[0]:
        box, (text, _) = line
        x_min = box[0][0]
        y_min = box[0][1]
        text_data.append((text, x_min, y_min))

    # Sort data by y-coordinate first, then x-coordinate
    text_data.sort(key=lambda item: (item[2], item[1]))

    # Group text into rows using y-coordinate proximity
    threshold_y = 10
    rows = []
    current_row = []
    prev_y = None

    for text, x, y in text_data:
        if prev_y is None or abs(y - prev_y) < threshold_y:
            current_row.append((text, x))
        else:
            rows.append(current_row)
            current_row = [(text, x)]
        prev_y = y
    if current_row:
        rows.append(current_row)

    # Align text into columns using x-coordinates
    aligned_rows = []
    for row in rows:
        row.sort(key=lambda item: item[1])
        aligned_row = [text for text, _ in row]
        aligned_rows.append(aligned_row)

    # Convert to CSV and save
    output_csv_path = os.path.join(OUTPUT_FOLDER, f"{file.filename.split('.')[0]}.csv")
    max_cols = max(len(row) for row in aligned_rows)
    try:
        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in aligned_rows:
                writer.writerow(row)
    except Exception as e:
        return jsonify({"error": f"Error writing CSV: {e}"}), 500

    # Return the path to download the CSV
    return jsonify({
        "download_url": f"/download/{os.path.basename(output_csv_path)}"
    })

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)



