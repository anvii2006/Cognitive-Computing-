import pandas as pd

# Q1: Build Your Personalized Knowledge Base

roll_number = "23"   

last_two = roll_number[-2:]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

categories = ["billing", "account", "general"]

personalized_entries = []

for digit in last_two:
    d = int(digit)

    category = categories[d % 3]

    if category == "billing":
        question = "how can I check my fee payment status"
        answer = "You can check your fee payment status in the billing section."
        keywords = "fee payment billing status"

    elif category == "account":
        question = "how do I update my registered mobile number"
        answer = "You can update your registered mobile number from account settings."
        keywords = "mobile number update account phone"

    else:
        question = "what are the college office working hours"
        answer = "The college office is open from 9 AM to 5 PM."
        keywords = "office hours timing working"

    personalized_entries.append({
        "question": question,
        "answer": answer,
        "keywords": keywords,
        "category": category
    })

all_entries = fixed_entries + personalized_entries

df = pd.DataFrame(all_entries)

print("Q1: Final 6-row DataFrame")
print(df)

# Q2: Generate and Score a Hypothesis

def score_query(query, df):
    query_words = set(query.lower().split())

    results = []

    for index, row in df.iterrows():

        text = row["question"].lower() + " " + row["keywords"].lower()
        text_words = set(text.split())

        matches = query_words.intersection(text_words)

        score = len(matches)

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results

query = "fee payment"

print("\nQ2: Query Results")
results = score_query(query, df)

for result in results:
    print(result)

# Q3: Find Entries from Same Category

def same_category(category_name, df):
    return df[df["category"] == category_name]

category_to_search = personalized_entries[0]["category"]

print("\nQ3: Entries in category:", category_to_search)
print(same_category(category_to_search, df))


# Q4: Add a New Keyword and Save DataFrame

print("\nQ4")

entry_number = int(input("Enter entry number (1-6): "))

new_keyword = input("Enter a new keyword: ")

index = entry_number - 1

df.loc[index, "keywords"] = df.loc[index, "keywords"] + " " + new_keyword

filename = f"{roll_number}_faq_data.csv"
df.to_csv(filename, index=False)

print("\nUpdated DataFrame:")
print(df)

print("\nFile saved as:", filename)

# Q5: Count FAQ Entries Per Category

print("\nQ5: Number of FAQ entries per category")

category_counts = df.groupby("category").size()

print(category_counts)

# Q6: Modified Scoring Function with Ties

def score_query_with_ties(query, df):

    query_words = set(query.lower().split())

    results = []

    for index, row in df.iterrows():

        text = row["question"].lower() + " " + row["keywords"].lower()
        text_words = set(text.split())

        matches = query_words.intersection(text_words)

        score = len(matches)

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })
    if not results:
        return []
    highest_score = max(result["score"] for result in results)

    best_results = [
        result for result in results
        if result["score"] == highest_score
    ]

    return best_results


# Q6 Demonstration 1: Query producing a tie

print("\nQ6: Tie Query")

tie_query = "fee"

tie_results = score_query_with_ties(tie_query, df)

print("Query:", tie_query)

for result in tie_results:
    print(result)

# Q6 Demonstration 2: Query without a tie

print("\nQ6: Non-Tie Query")

non_tie_query = "password reset"

non_tie_results = score_query_with_ties(non_tie_query, df)

print("Query:", non_tie_query)

for result in non_tie_results:
    print(result)