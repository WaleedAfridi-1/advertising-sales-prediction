# advertising-sales-prediction
A Streamlit-based machine learning web app that predicts sales based on advertising budgets for TV, Radio, and Newspaper. Built with Linear Regression and StandardScaler preprocessing, the project provides real-time predictions, budget breakdown visualization, and a modern UI for data-driven marketing decisions.


# 📊 Advertising Sales Prediction  

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Model-Linear%20Regression-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>
</p>

---

👉 **Live Demo:** [Advertising Sales Prediction App](https://advertising-sales-prediction-waleedafridi.streamlit.app/)

---
## 🚀 Overview  
This project is a **machine learning web app** built with **Streamlit** that predicts **Sales Revenue** based on advertising budgets across **TV, Radio, and Newspaper**.  

The model is trained using **Linear Regression** with feature scaling for better performance.  
It provides businesses and analysts with **quick insights** into how marketing spend affects sales.  

---

## ✨ Key Features  
- 🎨 **Modern UI** with custom CSS & animations  
- 📈 **Predict sales instantly** by entering ad budgets  
- 📝 **Budget breakdown** displayed clearly  
- 🔥 **Pre-trained ML model** (Linear Regression)  
- 📊 Interactive & lightweight deployment ready  

---

## 📂 Project Structure  

```bash
├── app.py                  # Streamlit app for prediction
├── train_model.py          # Training script for model
├── Advertising_dataset.csv # Dataset used
├── model.pkl               # Trained model (Linear Regression)
├── scaler.pkl              # StandardScaler for preprocessing
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---
## ⚙️ Installation
- **1️⃣ Clone Repository**
```bash
git clone https://github.com/WaleedAfridi-1/advertising-sales-prediction.git
cd advertising-sales-prediction
```
- **2️⃣ Install Dependencies**
```bashpip
install -r requirements.txt
```
- **3️⃣ Run App**
```bash
streamlit run app.py
```

---

# 🧠 Model Workflow

**Dataset →** Advertising_dataset.csv  
**Features →** TV, Radio, Newspaper  
**Target →** Sales  
**Preprocessing →** StandardScaler  
**Model →** Linear Regression  
**Saved as →** model.pkl and scaler.pkl  

---

# 📊 Example Predictions

| TV (k) | Radio (k) | Newspaper (k) | Predicted Sales (k units) |
|--------|-----------|---------------|----------------------------|
| 100    | 25        | 30            | 14.52                      |
| 200    | 40        | 20            | 25.34                      |
| 50     | 10        | 5             | 6.72                       |

---

# 🌍 Deployment  

You can deploy easily on **Streamlit Cloud**:  
```bash
streamlit run app.py
```
---

# 🛠️ Tech Stack

Python 🐍

Streamlit 🚀

Scikit-learn 🤖

Pandas / NumPy 📊

Matplotlib & Seaborn 🎨

# 🔮 Future Enhancements

Add Ridge / Lasso / XGBoost models for comparison

Include more datasets (social media, digital ads, etc.)

Deploy with Docker or AWS/GCP

# 👨‍💻 Author

Waleed Afridi
📍 BSCS Student | Data Science & ML Enthusiast

# 🌐 Feel free to fork, star ⭐, and contribute!
