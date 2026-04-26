import pandas as pd
import os

# -----------------------------
# LOAD DATASET (RENDER SAFE)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'jobs.csv')

df = pd.read_csv(csv_path)

# -----------------------------
# CLEAN DATA
# -----------------------------
df = df.rename(columns={
    "Job Title": "title",
    "Job Description": "description"
})

df = df.dropna()


# -----------------------------
# RECOMMENDATION FUNCTION
# -----------------------------
def get_recommendations(user_input):
    user_words = user_input.lower().split()

    scores = []

    for i in range(len(df)):
        description = df.iloc[i]['description'].lower()
        title = df.iloc[i]['title']

        score = 0

        for word in user_words:
            if word in description:
                score += 1

        scores.append((score, title))

    # sort by score
    scores.sort(reverse=True)

    results = []

    for score, title in scores:
        if title not in results and score > 0:
            results.append(title)

        if len(results) == 5:
            break

    return results


# -----------------------------
# TEST (optional)
# -----------------------------
if __name__ == "__main__":
    print(get_recommendations("python sql"))
