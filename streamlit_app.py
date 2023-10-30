import streamlit as st
import pandas as pd

st.set_page_config(page_title="yyc-community-game", page_icon=":question:")
_, center, _ = st.columns([2, 1, 2])
with center:
    st.image(
        "https://cdn3.iconfinder.com/data/icons/brain-games/128/Quiz-Games-red.png",
        use_column_width=True,
    )
st.title("yyc-community-game")
st.caption("A Streamlit app for YYC community guessing game")


@st.cache_data
def load_df():
    url = "https://raw.githubusercontent.com/zehengl/yyc-community-metrics/main/output/data.csv"
    return pd.read_csv(url)


@st.cache_data
def get_area_sample(df):
    return df.sample(4)


@st.cache_data
def get_bikeways_sample(df):
    return df.sample(4)


@st.cache_data
def get_schools_sample(df):
    return df.sample(4)


df = load_df()

with st.expander("Study the dataset"):
    df


st.header("Questions")

score, total = 0, 3

df_area = get_area_sample(df)
ans_area = st.radio(
    ":blue[Which community has the largest area?]",
    df_area["name"],
    index=None,
)
if ans_area in df_area["name"][df_area["area"] == df_area["area"].max()].tolist():
    score += 1

df_bikeways = get_bikeways_sample(df)
ans_bikeways = st.radio(
    ":blue[Which community has the longest bikeways?]",
    df_bikeways["name"],
    index=None,
)
if (
    ans_bikeways
    in df_bikeways["name"][
        df_bikeways["bikeways"] == df_bikeways["bikeways"].max()
    ].tolist()
):
    score += 1

df_schools = get_schools_sample(df)
ans_schools = st.radio(
    ":blue[Which community has the most schools?]",
    df_schools["name"],
    index=None,
)
if (
    ans_schools
    in df_schools["name"][df_schools["schools"] == df_schools["schools"].max()].tolist()
):
    score += 1

if score == total:
    thumb = ":100:"
else:
    thumb = ":thumbsup:" if score / total > 0.4 else ":thumbsdown:"

if all(
    [
        ans_area,
        ans_bikeways,
        ans_schools,
    ]
):
    st.write(f"You score {score} out of {total} {thumb}")

refresh = st.button("Refresh")
if refresh:
    st.cache_data.clear()
    st.rerun()
