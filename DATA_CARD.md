# Data Card: NEU Surface Defect Database

## 1. Dataset Overview
- **Name:** NEU Surface Defect Database (NEU-CLS)
- **Source:** Kaggle (`yidazhang07/bridge-cracks-image`)
- **Domain:** Industrial Quality Control / Manufacturing
- **Description:** A dataset containing high-quality grayscale images of hot-rolled steel strips, categorized into six distinct typical surface defects.

## 2. Class Definitions
The dataset defines 6 defect categories:
1. **Cracking (Cr):** Surface fractures or linear breaks.
2. **Inclusions (In):** Foreign matter or non-metallic particles embedded in the steel.
3. **Pitting Surface (PS):** Small, localized depressions or holes.
4. **Plaque (Pa):** Patches or scale on the surface.
5. **Rolling Scale (RS):** Flaking or scaling caused during the rolling process.
6. **Scratches (Sc):** Linear marks or abrasions on the surface.

## 3. Data Audit Summary
- **Total Image Count:** 1,800 images
- **Image Dimensions:** 200 x 200 pixels
- **Color Space:** Grayscale (1-channel)
- **Class Balance:** **Perfectly Balanced**
  - Cracking: 300 images
  - Inclusions: 300 images
  - Pitting Surface: 300 images
  - Plaque: 300 images
  - Rolling Scale: 300 images
  - Scratches: 300 images
- **Label Quality:** Verified. Images are cleanly sorted into respective class folders with consistent naming conventions.

## 4. Split Strategy
Given the perfect class balance, the dataset will be partitioned using a standard stratified split to maintain the uniform distribution across all phases:
- **Training Set:** 70% (1,260 images; 210 per class)
- **Validation Set:** 15% (270 images; 45 per class)
- **Test Set:** 15% (270 images; 45 per class)

*Note: The split will be executed using `scikit-learn`'s `train_test_split` with a fixed random seed to ensure reproducibility.
