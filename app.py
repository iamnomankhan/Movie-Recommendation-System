import streamlit as st
import pickle
import requests
import os
import gdown

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="🎬 CineVerse AI",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# Load Data
# -------------------------------
movies = pickle.load(open("models/movies.pkl", "rb"))

SIMILARITY_PATH = "models/similarity.pkl"

if not os.path.exists(SIMILARITY_PATH):
    url = "https://drive.google.com/uc?id=1YaHAnJqV8L4eKl0cPVCcbV-12KlqeT56"
    gdown.download(url, SIMILARITY_PATH, quiet=False)

similarity = pickle.load(open(SIMILARITY_PATH, "rb"))

# -------------------------------
# TMDB API KEY
# -------------------------------
API_KEY = "2f728e36a7a7ecb6c28cba7abfb885d5"

# -------------------------------
# Fetch Poster
# -------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    data = requests.get(url).json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


# -------------------------------
# UI
# -------------------------------

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
    background:#0f0f0f;
}

/* Hide Streamlit menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* App background */
.stApp{
    background:
    linear-gradient(rgba(0,0,0,.78),rgba(0,0,0,.88)),
    url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1800&q=80");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

/* Hero Banner */
.hero{
    padding:40px 80px;
    text-align:center;
    border-radius:30px;

    background:rgba(255,255,255,.05);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,.15);

    box-shadow:0 10px 50px rgba(0,0,0,.6);

    margin-bottom:20px;
}

.hero h1{

    font-size:70px;

    color:white;

    margin-bottom:10px;

}

.hero span{

    color:#E50914;

}

.hero p{

    color:#cccccc;

    font-size:22px;

}

/* Glass Container */

.glass{

background:rgba(255,255,255,.08);

padding:30px;

border-radius:25px;

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.15);

margin-top:20px;

}

/* Selectbox */

.stSelectbox label{

font-size:22px;

color:white;

font-weight:600;

}

/* Button */

.stButton>button{

width:100%;

padding:16px;

font-size:22px;

font-weight:bold;

border:none;

border-radius:15px;

background:linear-gradient(90deg,#E50914,#ff416c);

color:white;

transition:.4s;

}

.stButton>button:hover{

transform:scale(1.05);

box-shadow:0 0 30px #E50914;

}

/* Poster */

img{

border-radius:18px;

transition:.4s;

}

img:hover{

transform:scale(1.08);

box-shadow:0 0 25px rgba(255,0,0,.6);

}

/* Movie title */

.movie-title{

text-align:center;

font-size:18px;

font-weight:bold;

color:white;

margin-top:10px;

}

/* Loading */

.loader{

width:70px;

height:70px;

border:8px solid #333;

border-top:8px solid red;

border-radius:50%;

animation:spin 1s linear infinite;

margin:auto;

}

@keyframes spin{

0%{transform:rotate(0deg);}

100%{transform:rotate(360deg);}

}

/* Success */

.success{

padding:20px;

background:#1e4620;

border-radius:12px;

text-align:center;

color:#fff;

font-size:20px;

font-weight:bold;

}

/* Footer */

.footer{

margin-top:80px;

text-align:center;

color:#888;

font-size:16px;

}
.stSpinner>div{
    border-top-color:#E50914 !important;
}

div[data-testid="stSuccess"]{
    border-radius:15px;
    font-size:20px;
}

</style>
</style>
""",unsafe_allow_html=True)


st.markdown("""
<div class='hero'>

<h1>🎬 <span>CineVerse AI</span></h1>

<p>Discover Your Next Favorite Movie with Artificial Intelligence</p>

</div>
""",unsafe_allow_html=True)

# st.markdown("Find movies similar to your favorite one!")

selected_movie = st.selectbox(
    "🔍 Search Your Favorite Movie",
    movies['title'].values
)

if st.button("🎯 Recommend"):

    with st.spinner("🎬 Finding perfect movies for you..."):

        names, posters = recommend(selected_movie)

    st.success("Recommendations Ready! 🍿")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0], use_container_width=True)
        st.markdown(f"<div class='movie-title'>{names[0]}</div>", unsafe_allow_html=True)

    with col2:
        st.image(posters[1], use_container_width=True)
        st.markdown(f"<div class='movie-title'>{names[1]}</div>", unsafe_allow_html=True)

    with col3:
        st.image(posters[2], use_container_width=True)
        st.markdown(f"<div class='movie-title'>{names[2]}</div>", unsafe_allow_html=True)

    with col4:
        st.image(posters[3], use_container_width=True)
        st.markdown(f"<div class='movie-title'>{names[3]}</div>", unsafe_allow_html=True)

    with col5:
        st.image(posters[4], use_container_width=True)
        st.markdown(f"<div class='movie-title'>{names[4]}</div>", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">

<h3 style="color:white;">🎬 CineVerse AI</h3>

<p>Made with ❤️ by Noman Khan</p>

<p>Powered by Python • Streamlit • Scikit-Learn • TMDB API</p>

</div>
""", unsafe_allow_html=True)