# OCR-TypeScript-Project
OCR TypeScript Project
This project demonstrates how to perform Optical Character Recognition (OCR) using TypeScript. The project integrates Python for image processing tasks using the Tesseract OCR engine and outputs recognized text from various image formats like `.jpg` and `.webp`.

## Project Structure
```javascript
├── TheBalanceLetter.jpg        # Sample image to process
├── coverletter.webp            # Another sample image for OCR
├── index.ts                    # Main TypeScript file to run the project
├── ocr.py                      # Python script for OCR processing using Tesseract
├── ocr_output.txt              # Output file containing extracted text from images
├── processed_image.png         # Processed image after OCR operation
├── node_modules/               # Project dependencies installed via npm
├── package.json                # Project configuration and dependencies
├── package-lock.json           # Lockfile for npm dependencies
├── tsconfig.json               # TypeScript configuration file
├── venv/                       # Python virtual environment
```

## Prerequisites
Make sure you have the following installed:
- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/)
- [Python 3](https://www.python.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Setup

1. **Install dependencies**:
   - Install Node.js dependencies:

     ```javascript
     npm install
     ```

   - Create and activate a Python virtual environment:

     ```javascript
     python3 -m venv venv
     source venv/bin/activate   # For Linux/Mac
     .\venv\Scripts\activate    # For Windows
     ```

   - Install Python dependencies:

     ```bash
     pip install -r requirements.txt
     ```

2. **Install Tesseract OCR**:
   - [Follow the installation instructions](https://github.com/tesseract-ocr/tesseract#installation) for your platform.

## Running the Project

### Running OCR with TypeScript

1. Ensure you are in the project root directory.
2. Compile and run the TypeScript code:

   ```javascript
   npx ts-node index.ts
   ```

  ## Running OCR with Python
  Use the provided Python script for OCR:
   ```javascript
   python ocr.py
   ```

The OCR results will be saved in `ocr_output.txt` and any processed images will be saved as `processed_image.png`.


## Configuration
The project uses TypeScript and Tesseract for OCR. Modify the index.ts file to change the images being processed. Similarly, the Python script (ocr.py) can be updated for additional image processing logic.

## TypeScript Configuration
The project uses a tsconfig.json file for TypeScript settings, ensuring compatibility with modern JavaScript features and Node.js versions.


## License
This project is licensed under the MIT License. see the [LICENSE](./LICENSE) file for details.

## Contributions
Feel free to open issues or submit pull requests to improve this project.
