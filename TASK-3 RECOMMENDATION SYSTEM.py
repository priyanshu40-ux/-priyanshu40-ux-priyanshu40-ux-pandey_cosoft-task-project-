import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item ratings
data = {
    'User1': [5, 3, 0, 0, 2],
    'User2': [4, 0, 0, 5, 1],
    'User3': [1, 1, 0, 5, 0],
    'User4': [1, 0, 0, 4, 0],
    'User5': [0, 1, 5, 4, 0],
}

df = pd.DataFrame(data, index=['Inception', 'The Matrix', 'Interstellar', 'The Prestige', 'LOTR'])

# Transpose to user-item matrix
df_T = df.T.fillna(0)

# Cosine similarity between users
user_sim = cosine_similarity(df_T)
user_sim_df = pd.DataFrame(user_sim, index=df_T.index, columns=df_T.index)

# Recommendation for a user
def recommend_for_user(user):
    similar_users = user_sim_df[user].sort_values(ascending=False)[1:]
    most_similar = similar_users.index[0]
    recommended_items = df_T.loc[most_similar][df_T.loc[user] == 0].sort_values(ascending=False)
    return recommended_items.head(3).index.tolist()

# Example usage
print(recommend_for_user('User1'))
