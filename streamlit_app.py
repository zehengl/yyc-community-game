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


@st.cache_data
def get_recreation_facilities_sample(df):
    return df.sample(4)


@st.cache_data
def get_transit_stops_sample(df):
    sample = df.sample(4)
    sample["transit_stops"] = sample["bus_stops"] + sample["lrt_stations"]
    return sample


@st.cache_data
def get_tree_coverage_sample(df):
    sample = df.sample(4)
    sample["tree_coverage"] = sample["tree_canopy_2022"] / sample["area"]
    return sample


df = load_df()

with st.expander("Study the dataset"):
    df


st.header("Questions")

score, ans = 0, []

df_area = get_area_sample(df)
ans_area = st.radio(
    ":blue[Which community has the largest area?]",
    df_area["name"],
    index=None,
)
ans.append(ans_area)
if ans_area in df_area["name"][df_area["area"] == df_area["area"].max()].tolist():
    score += 1

df_bikeways = get_bikeways_sample(df)
ans_bikeways = st.radio(
    ":blue[Which community has the longest bikeways?]",
    df_bikeways["name"],
    index=None,
)
ans.append(ans_bikeways)
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
ans.append(ans_schools)
if (
    ans_schools
    in df_schools["name"][df_schools["schools"] == df_schools["schools"].max()].tolist()
):
    score += 1

df_recreation_facilities = get_recreation_facilities_sample(df)
ans_recreation_facilities = st.radio(
    ":blue[Which community has the most recreation facilities?]",
    df_recreation_facilities["name"],
    index=None,
)
ans.append(ans_recreation_facilities)
if (
    ans_recreation_facilities
    in df_recreation_facilities["name"][
        df_recreation_facilities["recreation_facilities"]
        == df_recreation_facilities["recreation_facilities"].max()
    ].tolist()
):
    score += 1

df_transit_stops = get_transit_stops_sample(df)
ans_transit_stops = st.radio(
    ":blue[Which community has the most transit stops?]",
    df_transit_stops["name"],
    index=None,
)
ans.append(ans_transit_stops)
if (
    ans_transit_stops
    in df_transit_stops["name"][
        df_transit_stops["transit_stops"] == df_transit_stops["transit_stops"].max()
    ].tolist()
):
    score += 1

df_tree_coverage = get_tree_coverage_sample(df)
ans_tree_coverage = st.radio(
    ":blue[Which community has the most tree coverage?]",
    df_tree_coverage["name"],
    index=None,
)
ans.append(ans_tree_coverage)
if (
    ans_tree_coverage
    in df_tree_coverage["name"][
        df_tree_coverage["tree_coverage"] == df_tree_coverage["tree_coverage"].max()
    ].tolist()
):
    score += 1

total = len(ans)
if score == total:
    thumb = ":100:"
else:
    thumb = ":thumbsup:" if score / total > 0.4 else ":thumbsdown:"

if all(ans):
    st.write(f"You score {score} out of {total} {thumb}")


st.button("Refresh", on_click=st.cache_data.clear)
