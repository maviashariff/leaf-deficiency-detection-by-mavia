# Leaf Nutrient Deficiency Detector

An intelligent machine learning-based web application designed to detect nutrient deficiencies (Nitrogen, Phosphorus, Potassium) in plant leaves through image analysis. Built with Python, Flask, and TensorFlow Lite, and features a responsive UI styled with Tailwind CSS.

Developed by [Mavia shariff](https://maviashariff.github.io/MavsPortfolio/#home).

## Features
- **Nutrient Detection**: Accurately classifies images into Healthy, Nitrogen, Phosphorus, or Potassium deficient.
- **Image Validation**: Automatically detects if the uploaded image is too dark, too blurry, or does not resemble a leaf.
- **Lightweight Inference**: Uses TensorFlow Lite (`tflite-runtime`) for fast predictions with low memory usage (< 100MB RAM), making it perfect for free-tier cloud hosting.

---

## 1. Running the Project Locally

Follow these steps to set up and run the application on your local machine.

### Prerequisites
- Python 3.7 or higher installed on your system.
- Git (optional, for cloning).

### Setup Instructions
1. **Open Command Prompt (CMD)** and navigate to the project directory:
   ```cmd
   cd path\to\leaf-deficiency-detector
   ```

2. **Create a virtual environment (recommended):**
   ```cmd
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```
   *(Note: The project uses `tflite-runtime` for lightweight inference. If you encounter issues installing it locally, the app will automatically fall back to standard `tensorflow.lite` if you have `tensorflow` installed).*

5. **Run the Flask application:**
   ```cmd
   python app.py
   ```

6. **Access the Web App:**
   Open your web browser and go to `http://127.0.0.1:10000` (or the port shown in your terminal).

---

## 2. Pushing to GitHub (via CMD)

To upload this project to your GitHub account as a new repository named `leaf-nutrient-deficiency-by-Mavia`, follow these steps:

1. **Create an empty repository on GitHub**:
   - Go to [github.com/new](https://github.com/new).
   - Name it `leaf-nutrient-deficiency-by-Mavia`.
   - Leave it public or private. **Do NOT** initialize it with a README, .gitignore, or License.
   - Click "Create repository".

2. **Push the code via CMD**:
   Open Command Prompt in your project folder and run the following commands one by one:

   ```cmd
   :: Initialize a fresh Git repository
   git init

   :: Add all files to staging
   git add .

   :: Commit the files
   git commit -m "Initial commit: Leaf Nutrient Deficiency Detector"

   :: Rename the default branch to 'main'
   git branch -M main

   :: Link your local repository to the GitHub repository you just created
   :: Replace YOUR_USERNAME with your actual GitHub username!
   git remote add origin https://github.com/YOUR_USERNAME/leaf-nutrient-deficiency-by-Mavia.git

   :: Push the code to GitHub
   git push -u origin main
   ```

---

## 3. Hosting on Render (Free Tier)

This application is optimized for [Render's Free Tier](https://render.com/), specifically using `tflite-runtime` to keep memory usage well below the 512MB limit, preventing build and runtime crashes.

### Deployment Steps:
1. **Log in to Render**: Go to [Render's Dashboard](https://dashboard.render.com/).
2. **Create a New Web Service**: Click the **New +** button in the top right and select **Web Service**.
3. **Connect GitHub**: Choose **Build and deploy from a Git repository** and connect your GitHub account if you haven't already.
4. **Select Repository**: Select the `leaf-nutrient-deficiency-by-Mavia` repository you just pushed.
5. **Configure the Service**:
   - **Name**: `leaf-nutrient-deficiency` (or any name you prefer)
   - **Region**: Select the region closest to you.
   - **Branch**: `main`
   - **Runtime**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. **Select Plan**: Choose the **Free** instance type.
7. **Deploy**: Click the **Create Web Service** button at the bottom.

Render will now automatically clone your repository, install the dependencies, and start the app. Once the deployment finishes (usually 1-2 minutes), you can access your live application using the URL provided at the top of the Render dashboard (e.g., `https://leaf-nutrient-deficiency-xxxx.onrender.com`).
