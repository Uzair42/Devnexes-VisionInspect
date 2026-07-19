# Experiment Plan

## 1. Primary Goal
Develop a transfer-learning-based computer vision model capable of classifying six types of steel surface defects with high accuracy, culminating in a deployable Python backend and React/Vite interactive demo.

## 2. Baseline Targets & Success Metrics
Because the dataset is perfectly balanced, standard accuracy is a viable primary metric.
- **Target Accuracy:** > 95% on the test set.
- **Target Macro F1-Score:** > 0.95 (Ensuring no single defect class is lagging).
- **Secondary Metric:** Inference speed. The model must process an uploaded image in under 500ms to ensure a responsive frontend user experience.

## 3. Preprocessing & Augmentation Strategy
- **Channel Conversion:** Pre-trained architectures expect 3-channel RGB images. The 1-channel grayscale images will be duplicated across 3 channels.
- **Resizing:** Images will be resized from 200x200 to 224x224 to match standard ImageNet input dimensions.
- **Normalization:** Standard ImageNet mean `[0.485, 0.456, 0.406]` and standard deviation `[0.229, 0.224, 0.225]` will be applied.
- **Augmentation:** To prevent overfitting on the 1,260 training images, the following augmentations will be applied:
  - Random Horizontal and Vertical Flips
  - Random Rotation (up to 15 degrees)

## 4. Model Architecture & Transfer Learning
We will evaluate lightweight, highly efficient convolutional neural networks suitable for rapid API deployment:
1. **Model A:** EfficientNet-B0 (Primary candidate due to excellent accuracy-to-parameter ratio).
2. **Model B:** ResNet-18 or ResNet-50 (Established baselines for industrial datasets).

**Training Phases:**
1. **Feature Extraction:** Freeze all convolutional base layers and train only a new fully connected classification head (output features = 6) using the Adam optimizer.
2. **Fine-Tuning:** Unfreeze the top 20% of the base network and train with a significantly reduced learning rate (e.g., 1e-5) to adapt feature maps to steel textures.

## 5. Evaluation & Quality Gates
- Tracking Validation Loss to prevent overfitting.
- Generating a Confusion Matrix to analyze misclassifications between visually similar defects (e.g., Scratches vs. Cracking).