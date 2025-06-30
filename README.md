# 🌸 Iris Flower Classifier

This is a machine learning-based web application that predicts the species of an Iris flower based on user inputs. The app takes four parameters: **sepal length**, **sepal width**, **petal length**, and **petal width**, and predicts whether the flower is **Setosa**, **Versicolor**, or **Virginica**.

> 🔗 **Live App**: [Try it on Streamlit](https://iris-flower-classifier-u6s2xjj5txb8xbyxrybsg8.streamlit.app/)  
> 💻 **GitHub Repository**: [View on GitHub](https://github.com/HarshTomar2006/Iris-Flower-Classifier)

---

## 📌 Features

- 🌼 Predicts Iris species using a trained ML model
- 🧠 Built using `scikit-learn` and `Streamlit`
- 🎯 Real-time predictions with friendly UI
- 🚀 Deployed on Streamlit Cloud

---

## 🎥 Demo Preview

### 🔹 App Interface:
![App UI](https://chat.openai.com/mnt/data/A_digital_screenshot_showcases_an_%22Iris_Flower_Cla.png)

### 🔹 Classifier Working Video:
https://chat.openai.com/mnt/data/A_screen_recording_video_showcases_the_user_interf.png

---

## 🚀 How It Works

1. User enters 4 features:
   - Sepal Length (cm)
   - Sepal Width (cm)
   - Petal Length (cm)
   - Petal Width (cm)

2. These inputs are passed to a trained machine learning model.

3. Based on the inputs, the model predicts one of the three Iris flower species:
   - **Iris-setosa**
   - **Iris-versicolor**
   - **Iris-virginica**

---

## 🧰 Tech Stack

| Tool            | Description                          |
|-----------------|--------------------------------------|
| Python          | Programming Language                 |
| Scikit-learn    | For model training and prediction    |
| Streamlit       | For creating the web interface       |
| Pickle (.pkl)   | For saving the trained model         |
| GitHub          | Version control and hosting code     |
| Streamlit Cloud | Deployment platform for the app      |

---

## 🗂️ Project Structure

├── app.py               # Main Streamlit app script ├── model.pkl            # Trained ML model (serialized) ├── requirements.txt     # Python dependencies └── .devcontainer/       # (Optional) Dev container configs

---

## 💾 Installation (Run Locally)

To run the app on your machine:

```bash
# Clone the repository
git clone https://github.com/HarshTomar2006/Iris-Flower-Classifier

# Change directory
cd Iris-Flower-Classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
