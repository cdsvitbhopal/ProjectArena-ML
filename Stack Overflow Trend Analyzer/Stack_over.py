# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the Stack Overflow data (example: Stack Overflow Survey Data)
df = pd.read_csv('stackoverflow_survey_data.csv')

# Filter relevant columns for analysis (e.g., language popularity)
language_cols = ['LanguageWorkedWith', 'LanguageDesireNextYear']
df_languages = df[language_cols]

# Count the occurrences of each programming language
language_counts = {}
for col in language_cols:
    for row in df_languages[col]:
        if isinstance(row, str):
            languages = row.split(';')
            for lang in languages:
                if lang in language_counts:
                    language_counts[lang] += 1
                else:
                    language_counts[lang] = 1

# Sort the languages by popularity in descending order
sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
top_languages = sorted_languages[:10]  # Select the top 10 languages

# Extract the language names and popularity counts
languages = [lang[0] for lang in top_languages]
popularity = [lang[1] for lang in top_languages]

# Create a bar chart to visualize the popularity of programming languages
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity)
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Top 10 Popular Programming Languages')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
