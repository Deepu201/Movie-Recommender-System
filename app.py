# # # import pandas as pd
# # # import streamlit as st
# # # import  pickle
# # # st.title("Movie Recommender System")
# # #
# # #
# # #
# # # similarity=pickle.load(open('similarity.pkl','rb'))
# # #
# # #
# # # import streamlit as st
# # # movie_dict=pickle.load(open('movie_dict.pkl','rb'))
# # # movies=pd.DataFrame(movie_dict)
# # #
# # #
# # # selected_movie_name = st.selectbox(
# # #     "How would you like to be contacted?",
# # #     movies['title'].values,
# # # )
# # #
# # #
# # # def recommend(movie):
# # #     movie_index=movies[movies['title']==movie].index[0]
# # #     distance=similarity[movie_index]
# # #     movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]
# # #     recommend_movie=[]
# # #     for i in movie_list:
# # #         recommend_movie.append(movies.iloc[i[0]].title)
# # #     return  recommend_movie
# # #
# # #git remote add origin https://github.com/YOUR_USERNAME/Movie-Recommender-System.git
# git branch -M main
# git push origin main
# # #
# # # if st.button('Recommend'):
# # #     recommendations=recommend(selected_movie_name)
# # #     for i in recommendations:
# # #      st.write(i)
# #
# # import pandas as pd
# # import streamlit as st
# # import pickle
# #
# # import requests
# #
# # def fetch_poster(movie_id):
# #  response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
# #  data = response.json()
# #  return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
# # # 8265bd1679663a7ea12ac168da84d2e8
# # # --- Title ---
# # st.title("Movie Recommender System")
# #
# # # --- Load data ---
# # similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
# # movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# # movies_df = pd.DataFrame(movie_dict)
# #
# # # --- Movie selection ---
# # selected_movie = st.selectbox(
# #     "Select a movie:",
# #     movies_df['title'].values
# # )
# #
# #
# # # --- Recommendation function ---
# # def recommend(movie_name):
# #     # Find the index of the selected movie
# #     movie_index = movies_df[movies_df['title'] == movie_name].index[0]
# #
# #     # Get similarity scores for this movie
# #     distances = similarity_matrix[movie_index]
# #
# #     # Sort movies based on similarity (descending) and get top 10
# #     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
# #     recommend_movie = []
# #     recommend_movie_poster=[]
# #
# #
# #     for i in movie_list:
# #         movie_id=movies_df.iloc[i[0]].movie_id
# #         # fetch poster from api
# #         recommend_movie.append(movies_df.iloc[i[0]].title)
# #         recommend_movie_poster.append(fetch_poster(movie_id))
# #     return  recommend_movie,recommend_movie_poster
# #
# #
# # # --- Show recommendations ---
# # if st.button('Recommend'):
# #     names,recommendations = recommend(selected_movie)
# #     coll, col2, col3 = st.columns(3)
# #     with coll:
# #         st.header("A cat")
# #     st.image("https://static.streamlit.io/examples/cat.jpg")
# #     with col2:
# #         st.header("A cat")
# #     st.image("https://static.streamlit.io/examples/cat.jpg")
# #     with col3:
# #         st.header("A cat")
# #     st.image("https://static.streamlit.io/examples/cat.jpg")
# #     #
# #     # st.subheader("Top 10 Recommendations:")
# #     # for i, movie in enumerate(recommendations, start=1):
# #     #     st.write(f"{i}. {movie}")
# import pandas as pd
# import streamlit as st
# import pickle
# import requests
#
# # Function to fetch poster from TMDB API
# def fetch_poster(movie_id):
#     response = requests.get(
#         f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     )
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
#
# # --- Title ---
# st.title("Movie Recommender System")
#
# # --- Load data ---
# similarity_matrix = pickle.load(open("similarity.pkl", "rb"))
# movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
# movies_df = pd.DataFrame(movie_dict)
#
# # --- Movie selection ---
# selected_movie = st.selectbox(
#     "Select a movie:",
#     movies_df["title"].values
# )
#
# # --- Recommendation function ---
# def recommend(movie_name):
#     movie_index = movies_df[movies_df["title"] == movie_name].index[0]
#     distances = similarity_matrix[movie_index]
#
#     # Get top 10 similar movies (excluding the selected movie)
#     movie_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )[1:10]
#
#     recommended_movies = []
#     recommended_posters = []
#
#     for i in movie_list:
#         movie_id = movies_df.iloc[i[0]].movie_id
#         recommended_movies.append(movies_df.iloc[i[0]].title)
#         recommended_posters.append(fetch_poster(movie_id))
#
#     return recommended_movies, recommended_posters
#
# # --- Show recommendations ---
# if st.button("Recommend"):
#     names, posters = recommend(selected_movie)
#
#     # Display movies in rows of 3
#     for i in range(0, len(names), 3):
#         cols = st.columns(3)
#         for col, name, poster in zip(cols, names[i:i+3], posters[i:i+3]):
#             with col:
#                 st.text(name)
import pandas as pd
import streamlit as st
import pickle
import requests

# Function to fetch poster from TMDB API with error handling
def fetch_poster(movie_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url, timeout=5)  # 5-second timeout
        response.raise_for_status()  # Raise exception if HTTP status != 200
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"  # fallback image
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"  # fallback image

# ----- UI Title -----
st.title("🎬 Movie Recommender System")

# ----- Load data -----
similarity_matrix = pickle.load(open("similarity.pkl", "rb"))
movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies_df = pd.DataFrame(movie_dict)

# ----- Movie selection -----
selected_movie = st.selectbox(
    "Select a movie:",
    movies_df["title"].values
)

# ----- Recommendation function -----
def recommend(movie_name):
    movie_index = movies_df[movies_df["title"] == movie_name].index[0]
    distances = similarity_matrix[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:10]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ----- Show recommendations -----
if st.button("🔎 Recommend"):
    st.subheader("⭐ Recommended for You")
    names, posters = recommend(selected_movie)

    # Display movies in rows of 3
    for i in range(0, len(names), 3):
        cols = st.columns(3)
        for col, name, poster in zip(cols, names[i:i+3], posters[i:i+3]):
            with col:
                st.image(poster)
                st.caption(name)
