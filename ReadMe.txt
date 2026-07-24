# 🎬 Movie Recommendation System

An AI-powered Movie Recommendation System built with **Python**, **Streamlit**, and **Machine Learning**. This application recommends movies similar to the one selected by the user using **Content-Based Filtering** and **Cosine Similarity**.

---

## 🚀 Features

- 🎥 Search and select a movie
- 🤖 AI-powered movie recommendations
- 🖼️ Movie posters fetched using the TMDB API
- ⚡ Fast and interactive Streamlit interface
- 📚 Content-based recommendation algorithm

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle
- TMDB API

---

## 🧠 Machine Learning Algorithm

This project uses **Content-Based Filtering**.

### How it works

1. Movie metadata is collected from the TMDB dataset.
2. Important features such as genres, keywords, cast, crew, and overview are combined.
3. Text features are converted into vectors.
4. Cosine Similarity is used to calculate the similarity between movies.
5. The system recommends the most similar movies based on the selected title.

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│── app.py
│── Movies_recommendation_system.ipynb
│── dataset/
│── models/
│   └── movies.pkl
│── notebooks/
│── assets/
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone git@github.com:iamnomankhan/Movie-Recommendation-System.git
```

### Move into the project

```bash
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📊 Dataset

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

---

## ⚠️ Note

The file `similarity.pkl` is **not included** in this repository because it exceeds GitHub's file size limit (100 MB).

You can regenerate it by running the notebook:

```
Movies_recommendation_system.ipynb
```

---

## 📸 Screenshots

Add screenshots of the application here.

Example:

- Home Page
- Movie Selection
- Recommended Movies

---

## 👨‍💻 Author

**Noman Khan**

BS Computer Science Student

Aspiring AI & Machine Learning Engineer

GitHub: https://github.com/iamnomankhan

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
