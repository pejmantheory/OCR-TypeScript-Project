import { exec } from 'child_process';

const runOCR = (imagePath: string) => {
  exec(`python3 ocr.py ${imagePath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return;
    }
    console.log(`OCR Output: ${stdout}`);
  });
};

const imagePath = './MWJroVr-1280.jpg'; 
runOCR(imagePath);
