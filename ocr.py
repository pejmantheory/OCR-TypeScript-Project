import pytesseract
import cv2
from PIL import Image
import sys
from textblob import TextBlob
import re
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
EXCLUDED_WORDS = ["Nicole", "Thomas", "Dell", "LMK", "Village", "September", "Andrews"]

CUSTOM_CORRECTIONS = {
    "Sickle": "Nicole",
    "Well": "Dell",
    "nice@thomas.com": "nicole@thomas.com",
    "Or.": "Mr.",
    "Ate": "Ste"
}

def correct_text(text):
    blob = TextBlob(text)
    corrected_blob = blob.correct()

    corrected_words = str(corrected_blob).split()
    final_words = []

    for word in corrected_words:
        if word in EXCLUDED_WORDS or re.match(r'\b[A-Za-z]+\b', word) and word in EXCLUDED_WORDS:
            final_words.append(word)
        elif word in CUSTOM_CORRECTIONS:
            final_words.append(CUSTOM_CORRECTIONS[word])
        else:
            final_words.append(word)

    return " ".join(final_words)

def perform_ocr(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=30)
    blurred = cv2.GaussianBlur(denoised, (5, 5), 0)
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    resized = cv2.resize(adaptive_thresh, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    processed_image_path = 'processed_image.png'
    cv2.imwrite(processed_image_path, resized)

    image = Image.open(processed_image_path)
    
    custom_config = '--oem 3 --psm 6'

    text = pytesseract.image_to_string(image, config=custom_config)

    text_with_linebreaks = text.replace(" | ", "\n")

    corrected_text = correct_text(text_with_linebreaks)

    print("Corrected OCR Output (with Formatting):\n")
    print(corrected_text)

    with open("ocr_output.txt", "w") as f:
        f.write(corrected_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    perform_ocr(image_path)
