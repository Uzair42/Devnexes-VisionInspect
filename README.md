# Surface Defect Classification System

## Project Overview
This repository contains a complete computer-vision solution designed to classify surface defects on various materials (like bridge cracks, PCB defects, and magnetic tiles). It includes cross-platform Kaggle-ready PyTorch notebooks for training and a robust Django web application for running real-time inference locally.

## Architecture
- **Machine Learning:** PyTorch (MobileNetV2 Transfer Learning)
- **Backend & Frontend:** Django (Python), HTML5/CSS3/Vanilla JS
- **Environment:** Linux native development / Kaggle / Google Colab

## Repository Structure
```text
.
├── backend/                  # Django project handling frontend UI and ML inference
├── notebooks/                # Cross-platform Notebooks for model training & fine-tuning
├── DATA_CARD.md              # Dataset documentation and audit
├── EXPERIMENT_PLAN.md        # Modeling methodology and targets
├── .gitignore
└── README.md
```

## How to Train the Model (Kaggle/Colab)

The `notebooks/` directory contains two scripts: `01_model_training.ipynb` and `02_model_finetuning.ipynb`. 

1. Create a new notebook in Kaggle attached to your target dataset.
2. Click **File > Import Notebook** and upload `01_model_training.ipynb`.
3. Set the **Accelerator** to **GPU T4 x2** (or GPU P100) for fast training.
4. Run the notebook. Once training finishes, it will provide a link to download the resulting `model_weights.pth` file.

> **Note:** If you run into a CUDA architecture mismatch (`no kernel image is available`), simply switch the Kaggle Accelerator to a different GPU type (e.g., from P100 to T4).

## How to Run the Local Web App

Once you have trained the model and downloaded the weights:

1. **Install Dependencies**:
   Open a terminal in the root directory and install the required Python packages:
   ```bash
   pip install django torch torchvision pillow
   ```

2. **Add Model Weights**:
   Rename your downloaded weights file to `model_weights.pth` and place it directly inside the `backend/` folder.

3. **Start the Django Server**:
   Navigate to the `backend/` directory and run:
   ```bash
   cd backend
   python3 manage.py runserver
   ```

4. **Run Inference**:
   Open your browser and navigate to `http://localhost:8000`. You can drag and drop images into the premium UI to get instant defect classification results from your trained PyTorch model.
