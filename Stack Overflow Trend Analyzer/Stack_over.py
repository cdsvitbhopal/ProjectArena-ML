import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the Stack Overflow data (example: Stack Overflow Survey Data)
df = pd.read_csv('stackoverflow_survey_data.csv')

# Filter relevant columns for analysis (e.g., language popularity)
language_cols = ['LanguageWorkedWith', 'LanguageDesireNextYear']
df_languages = df[language_cols]

# Count the occurrences of each programming language
language_counts = Counter(lang for col in language_cols for row in df_languages[col] if isinstance(row, str) for lang in row.split(';'))

# Get the top 10 languages
top_languages = language_counts.most_common(10)

# Extract the language names and popularity counts
languages, popularity = zip(*top_languages)

# Create a bar chart to visualize the popularity of programming languages
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity)
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Top 10 Popular Programming Languages')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
