# Interactive Linear Regression Analyzer

A web application built with Streamlit, designed for visually teaching and demonstrating simple linear regression models.

---

## Project Description

This tool allows users to dynamically adjust parameters (like slope, number of data points, and noise level) through an interactive interface and observe in real-time how a linear regression model fits the data. It is ideal for educational purposes, demonstrations, or any scenario where one wants to intuitively understand the fundamental principles of linear regression.

The development process of this project follows the [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) methodology. For a detailed development log, please refer to `log.md`.

## ✨ Features

- **Interactive Parameter Tuning**: Use sliders to adjust the model's slope `a`, the number of data points, and the noise level in real-time.
- **Real-time Data Generation**: Dynamically generates data points based on user-defined parameters.
- **On-the-fly Model Fitting**: Trains a `LinearRegression` model instantly using Scikit-learn.
- **Rich Visualization**:
  - Raw data points (scatter plot)
  - The true underlying relationship (dashed green line)
  - The model's fitted prediction line (solid red line)
- **Responsive Web Interface**: Built with Streamlit for a great user experience on both desktop and mobile.

## 🚀 How to Run Locally

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

- Python 3.8+ installed
- pip installed

### 2. Installation Steps

**a. Clone or Download the Project**

Download all files from this project into a folder on your computer (e.g., `C:\Users\user\Desktop\hw1`).

**b. Install Dependencies**

Open your terminal (Command Prompt, PowerShell, etc.), navigate to the project directory, and run the following command to install all necessary Python packages:

```bash
cd path\to\your\project\folder
pip install -r requirements.txt
```

**c. Launch the Application**

In the same terminal window, run the following command:

```bash
streamlit run app.py
```

After running the command, your default browser should automatically open a new tab pointing to `http://localhost:8501`, where you will see the running application.

## ☁️ How to Deploy to the Cloud

This project is ready for deployment on the [Streamlit Community Cloud](https://share.streamlit.io/).

1.  Upload all project files (especially `app.py` and `requirements.txt`) to a **public GitHub repository**.
2.  Log in to your Streamlit Community Cloud account.
3.  Click "New app" and select the GitHub repository you just created.
4.  Confirm that the "Main file path" is `app.py`.
5.  Click "Deploy!", and your application will be live on the internet in a few minutes!

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Framework for building the interactive web application
- **Scikit-learn**: For building and training the linear regression model
- **Pandas**: For data manipulation and structuring
- **NumPy**: For efficient numerical computation and data generation
- **Altair**: For creating beautiful and interactive data visualizations

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).