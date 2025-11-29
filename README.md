# 🎯 Sentiment Analysis & Topic Modeling of a Product (Persian) 🇮🇷

Welcome! ✨ This repository contains a Colab/Jupyter notebook that demonstrates a complete pipeline for analyzing Persian product comments — from data loading and Persian text normalization to sentiment labeling and topic modeling. It's a compact, hands-on project ideal for exploration, experimentation, and quick reproduction. 🚀

probably this is my first practice in AI.

---

## 📁 Project Structure
- note_book.ipynb — Main notebook with the full code, outputs, and visualizations (open in Colab or Jupyter).  
  - View notebook: https://github.com/sghamilouei/sentiment-analysis-and-topic-modeling-of-a-product/blob/main/note_book.ipynb
- data collection/ — folder containing the dataset:
  - data collection/comments.csv — collected comments with ratings (Persian).  
    - View CSV: https://github.com/sghamilouei/sentiment-analysis-and-topic-modeling-of-a-product/blob/main/data%20collection/comments.csv
- LICENSE — licensing details.

---

## 🧾 Summary (What this does)
- Loads product comments (Persian) using pandas. 🐼
- Creates binary sentiment labels from numeric `rate`:
  - rate >= 3 → positive (1) 👍
  - rate < 3  → negative (0) 👎
- Applies Persian normalization and spacing fixes using the shekar library (Normalizer, SpacingNormalizer). 🛠️
- Explores data and runs experiments for sentiment analysis and topic modeling (LDA / gensim, or other approaches). 📊
- All step-by-step outputs and plots are shown in the notebook. 🧩

---

## 🚀 Quick Start

### 🔁 Open in Google Colab (recommended)
1. Click to open the notebook in Colab:
   https://colab.research.google.com/github/sghamilouei/sentiment-analysis-and-topic-modeling-of-a-product/blob/main/note_book.ipynb
2. Ensure the CSV is available in the Colab session (upload or mount Drive).
3. Run the cells — notebook contains pip installs (e.g., shekar) where needed.

### 🖥️ Run locally
1. Clone:
   `git clone https://github.com/sghamilouei/sentiment-analysis-and-topic-modeling-of-a-product.git`
2. (Optional) Create virtual env:
  ` python -m venv venv`
   `source venv/bin/activate  # macOS/Linux`
   `venv\Scripts\activate     # Windows`
3. Install packages (minimum):
   `pip install pandas shekar`
   # You might also need:
   `pip install scikit-learn gensim nltk matplotlib seaborn jupyterlab`
4. Start Jupyter and open note_book.ipynb:
   `jupyter notebook note_book.ipynb`

---

## 📦 Key Dependencies
- Python 3.8+
- pandas
- shekar (Persian text normalization) — used in the notebook
- scikit-learn (modeling / metrics)
- gensim (topic modeling, LDA)
- nltk (tokenization / stopwords)
- matplotlib / seaborn (visualizations)
- pyLDAvis (optional — interactive LDA viz)

Tip: The notebook uses inline `!pip install` for shkear and other libs; check first cells for exact commands. 🔎

---

## 🛠️ Notes on Preprocessing (Persian)
- Normalization and spacing are handled with shekar's Normalizer and SpacingNormalizer to fix common Persian text issues (e.g., zero-width chars, spacing, diacritics). ✨
- Consider adding hazm or other Persian NLP tools for richer tokenization / lemmatization. 🔬

---


## 📜 License
See LICENSE file in the repo. ⚖️

---

## 📬 Contact / Support
Questions, suggestions, or contributions are welcome — open an issue or a PR. 💬

Happy analyzing! 🧠📚🌟



