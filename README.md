<!-- T20 WORLD CUP PREDICTION README -->

<div align="center">

## 🏏 **T20 World Cup Match Prediction**
#### *Predicting T20 Cricket Match Outcomes using Machine Learning*

> A **Machine Learning model** that predicts the **winning probability of teams in a T20 cricket match** using historical match data, team statistics, and match conditions.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/MachineLearning-ScikitLearn-orange?style=for-the-badge)
![Pandas](https://img.shields.io/badge/DataProcessing-Pandas-green?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-LogisticRegression-red?style=for-the-badge)

</div>

---

## 🪄 About the Project

**T20 World Cup Match Prediction** is a machine learning project that predicts the **probability of a team winning a cricket match** during a T20 game.

The model analyzes various match parameters such as:

- Batting team
- Bowling team
- Runs scored
- Overs completed
- Wickets fallen
- Target score

Using these features, the model calculates **real-time win probabilities for both teams**.

This project demonstrates how **data science and machine learning can be applied to sports analytics**.

---

## ⚡ Key Features

| ✨ Feature | 💬 Description |
|------------|---------------|
| 🏏 **Match Outcome Prediction** | Predicts the winning probability of teams |
| 📊 **Sports Analytics** | Uses historical cricket match data |
| 🧠 **Machine Learning Model** | Logistic Regression based prediction |
| 📈 **Real-time Probability** | Updates win probability based on match situation |
| ⚡ **Fast Predictions** | Efficient ML model with quick predictions |
| 💾 **Model Serialization** | Model saved using `pickle` |
| 🌐 **Easy Deployment** | Can be integrated with web apps or dashboards |

---

## 🧰 Technologies Used

<div align="center">

| Layer | Technologies |
|------|--------------|
| 🐍 **Programming Language** | Python |
| 📊 **Data Processing** | Pandas · NumPy |
| 🧠 **Machine Learning** | Scikit-learn |
| 📈 **Model Training** | Logistic Regression |
| 📓 **Development Environment** | Jupyter Notebook |
| 💾 **Model Storage** | Pickle |

</div>

---

## 🧠 Model Workflow

The prediction system follows the steps below:

1️⃣ **Dataset Collection**

Historical T20 match data is collected containing match statistics.

2️⃣ **Data Preprocessing**

- Handling missing values
- Feature selection
- Encoding categorical variables

3️⃣ **Feature Engineering**

Important match features are generated such as:

- Runs left
- Balls remaining
- Required run rate
- Current run rate

4️⃣ **Model Training**

A **Logistic Regression model** is trained using the processed dataset.

5️⃣ **Prediction**

The trained model predicts:

- Winning probability for **Team A**
- Winning probability for **Team B**

---

## 📁 Project Structure

```bash
T20-WorldCup-Prediction/
│
├── dataset/                # Match datasets
│
├── model/
│   └── pipe.pkl             # Trained ML pipeline
│
├── t20_prediction.ipynb     # Model training notebook
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 📊 Model Features

The prediction model uses the following features:

- Batting Team
- Bowling Team
- Runs Scored
- Wickets Fallen
- Overs Completed
- Target Score
- Runs Left
- Balls Left
- Current Run Rate
- Required Run Rate

These features allow the model to calculate **accurate win probabilities**.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/t20-worldcup-prediction.git
cd t20-worldcup-prediction
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the notebook

Open:

```
t20_prediction.ipynb
```

Run all cells to:

- preprocess the dataset
- train the model
- evaluate performance
- save the trained model

---

## 💾 Model Output

The trained model is saved as:

```
pipe.pkl
```

This pipeline can be used for:

- Match prediction dashboards
- Sports analytics tools
- Web applications

---

## 📌 Future Improvements

Possible enhancements for the project:

- 📊 Add more historical match datasets
- 🎯 Improve accuracy using advanced models
- 🌐 Deploy using **Streamlit**
- 📈 Add real-time match prediction dashboard
- 🤖 Use advanced models like **XGBoost or Random Forest**

---

## 👨‍💻 Author

**Saksham Garg**  
💻 Machine Learning & Data Science Enthusiast

<div align="center">

⭐ If you like this project, consider giving it a **star**!

Made with ❤️ by **Saksham Garg**

</div>
