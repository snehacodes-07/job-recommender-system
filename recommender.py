import pandas as pd

# load dataset
df = pd.read_csv("jobs.csv")

# rename columns
df = df.rename(columns={
    "Job Title": "title",
    "Job Description": "description"
})

# remove empty rows
df = df.dropna()

# function
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
    
    # sort highest score first
    scores.sort(reverse=True)
    
    # remove duplicates
    results = []
    
    for score, title in scores:
        if title not in results and score > 0:
            results.append(title)
        
        if len(results) == 5:
            break
    
    return results


# test 
print(get_recommendations("python sql"))