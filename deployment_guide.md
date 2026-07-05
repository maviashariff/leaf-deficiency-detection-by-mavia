# Rebranding & Deployment Guide

This guide describes how to push your updated project to GitHub and deploy it to Render.

---

## 1. Pushing to a New GitHub Repository

You requested to create a repository named `leaf-nutrient-deficiency-by-Mavia`. Follow these commands in your Windows CMD (Command Prompt) inside the project folder:

### Option A: Using the Web UI to Create the Repository (Recommended)
1. Go to [github.com/new](https://github.com/new) and create a repository named `leaf-nutrient-deficiency-by-Mavia`. **Do not** initialize it with a README, `.gitignore`, or License (since your project already has them).
2. Open your Command Prompt (`cmd`) in your project root `d:\Freelance-projects\kevin\leaf-deficiency-detector-new\leaf-deficiency-detector` and run:

```cmd
:: 1. Remove the old git configuration (optional, if you want a clean history)
rmdir /s /q .git

:: 2. Initialize a fresh Git repository
git init

:: 3. Stage all files (this will stage requirements, app.py, templates, and the lightweight TFLite model)
git add .

:: 4. Commit the rebranded code
git commit -m "Initial commit: Rebranded to Mavia shariff and optimized for Render deployment"

:: 5. Rename the branch to main
git branch -M main

:: 6. Link to your new repository (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/leaf-nutrient-deficiency-by-Mavia.git

:: 7. Push the code to GitHub
git push -u origin main
```

---

### Option B: Creating the Repository via CMD using GitHub CLI
If you have the **GitHub CLI (`gh`)** installed and authenticated, you can create the repository and push it directly from CMD:

```cmd
:: 1. Remove the old git configuration (optional)
rmdir /s /q .git

:: 2. Initialize Git and commit files
git init
git add .
git commit -m "Initial commit: Rebranded to Mavia shariff and optimized for Render deployment"
git branch -M main

:: 3. Create the repo on GitHub and push immediately
gh repo create leaf-nutrient-deficiency-by-Mavia --public --source=. --push
```

---

## 2. Deploying to Render

We have optimized the application to use TensorFlow Lite (`tflite-runtime`), which uses **under 100MB of RAM** (instead of standard TensorFlow which exceeds 1GB RAM). This ensures full compatibility with **Render's Free Tier** (512MB RAM) and avoids Out-Of-Memory (OOM) build crashes.

### Deployment Steps:
1. Log in to [Render](https://render.com/).
2. In the dashboard, click the **New +** button and select **Web Service**.
3. Choose **Connect a repository** and select your newly created GitHub repository `leaf-nutrient-deficiency-by-Mavia`.
4. Configure the service settings:
   - **Name**: `leaf-nutrient-deficiency`
   - **Region**: Choose the region closest to you (e.g., Singapore or Oregon).
   - **Branch**: `main`
   - **Runtime**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Select the **Free** instance type ($0/month).
6. Click **Deploy Web Service**.

Render will automatically fetch the code, install the lightweight dependencies (which takes under 1-2 minutes now), and start the Gunicorn server. You can monitor the live logs in the Render console. Once deployed, Render will provide you with a public URL (e.g., `https://leaf-nutrient-deficiency.onrender.com`).
