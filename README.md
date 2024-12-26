**Prescription Detection System with Drug Interaction Caution**

**Overview**
The Prescription Detection System is an AI-powered solution designed to detect, interpret, and analyze handwritten and printed medical prescriptions. 
This project aims to:

-Identify drug names, dosages, and other prescription details using object detection.
-Extract text using OCR (Optical Character Recognition).
-Provide drug-related information (purpose, side effects, interactions) with NLP (Natural Language Processing).

**Key Features**

-High-accuracy object detection with Faster R-CNN.
-Handwritten and printed text recognition with Tesseract OCR.
-Drug information retrieval using a BERT-based NLP model.
-Focus on real-time processing and user-friendly design.

**Project Goals**

1. Prescription Detection:
  Identify drug names and dosages with bounding boxes.

2. Drug Information:
  Provide details on drug purposes, side effects, and interactions.

3. Usability:
  Optimize the system for healthcare professionals and patient use.

**Technologies Used**

1. Object Detection: Faster R-CNN (fine-tuned on prescription datasets).

2. OCR: Tesseract for text extraction from bounding boxes.

3. NLP: BERT-based model fine-tuned for drug information retrieval.

4. Libraries/Tools:
PyTorch, Hugging Face Transformers, OpenCV, and LabelImg.
