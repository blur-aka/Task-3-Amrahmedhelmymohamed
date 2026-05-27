# AI Recommendation System

## Project Overview
This project is a simple AI recommendation system that helps users discover suitable tech career paths based on their skills and interests.

The user enters a few skills, and the system compares them with different job roles using AI recommendation logic. After calculating the similarity between the user profile and available career paths, the system displays the most relevant recommendations.

The project was built to practice recommendation systems, text processing, and similarity matching concepts in Artificial Intelligence.

---

## Technologies Used
- Python
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

## Project Files

| File Name | Format | Purpose |
|------------|---------|----------|
| Task3_decode.py | .py | Main project source code |
| README.md | .md | Project documentation and instructions |

---

## How the System Works

1. The user enters skills or interests.
2. The system converts text data into numerical vectors using TF-IDF.
3. Cosine Similarity is used to compare the user's skills with job role descriptions.
4. The system recommends the top matching career paths.

---

## How to Run the Project

Install the required library:

```bash
pip install scikit-learn
```

Run the project:

```bash
python Task3_decode.py
```

---

## Example

### Input
```text
Skill 1: python
Skill 2: machine learning
Skill 3: cloud
```

### Output
```text
Top 3 Recommended Career Paths:

1. AI Engineer --> Similarity Score: 0.52
2. Data Scientist --> Similarity Score: 0.44
3. Cloud Engineer --> Similarity Score: 0.18
```
