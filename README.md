This repository contains the implementation of the final year project by Viduni Ukwatta (20210087) at the Informatics Institute of Technology, in collaboration with Robert Gordon University, Aberdeen. The project aims to build an intelligent system that detects drug names from handwritten prescriptions and retrieves relevant medical information including usage, side effects, and interaction cautions.

Project Overview
Medical prescriptions are often handwritten, which leads to misinterpretation and medication errors. This project integrates object detection, OCR, and NLP-based information retrieval to automatically extract and analyze prescription data.

The core components of the system include:

Faster R-CNN for detecting drug name regions in prescription images

CRNN with CTC Loss for Optical Character Recognition (OCR)

BERT-based NLP model for retrieving drug information

Curated drug knowledge base for matching and verification

Gradio-based UI and batch pipeline support

