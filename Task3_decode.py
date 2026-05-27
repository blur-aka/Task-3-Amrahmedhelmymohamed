from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jobs = {
    "Data Scientist": "python machine learning data analysis statistics sql pandas numpy",
    "Backend Developer": "python java databases sql api django flask nodejs",
    "Frontend Developer": "html css javascript react design ui ux",
    "DevOps Engineer": "cloud docker kubernetes linux automation aws git",
    "AI Engineer": "python machine learning deep learning neural networks tensorflow pytorch",
    "Cybersecurity Analyst": "network security linux ethical hacking encryption firewall",
    "Mobile App Developer": "java kotlin flutter dart android ios mobile apps",
    "Cloud Engineer": "cloud aws azure docker kubernetes linux networking",
    "Database Administrator": "sql databases mysql postgresql oracle data backup",
    "Software Engineer": "java python algorithms data structures problem solving git"
}

print("=== AI Recommendation System ===")
print("Enter your interests or skills")

skill1 = input("Skill 1: ")
skill2 = input("Skill 2: ")
skill3 = input("Skill 3: ")

user_profile = skill1 + " " + skill2 + " " + skill3

documents = [user_profile] + list(jobs.values())

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

user_vector = tfidf_matrix[0]

job_vectors = tfidf_matrix[1:]

similarities = cosine_similarity(user_vector, job_vectors)[0]

results = []

for job_name, score in zip(jobs.keys(), similarities):
    results.append((job_name, score))

results.sort(key=lambda x: x[1], reverse=True)

print("\nTop 3 Recommended Career Paths:\n")

for i, (job, score) in enumerate(results[:3], start=1):
    print(f"{i}. {job} --> Similarity Score: {score:.2f}")