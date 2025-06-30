import streamlit as st

# ----- Session state to store daily data -----
if 'total_today' not in st.session_state:
    st.session_state.total_today = 0

# ----- Function to calculate daily water need -----
def calculate_water_intake(weight, activity_level):
    base = weight * 35
    if activity_level == "Low":
        return base
    elif activity_level == "Moderate":
        return base + 300
    elif activity_level == "High":
        return base + 600

# ----- UI -----
st.markdown(
    """
    <h1 style='text-align: center; color: #00BFFF; font-size: 50px;'>
        💧 <span style='color:#1DB954;'>Water Intake</span> <span style='color:#F9A825;'>Tracker</span> 💧
    </h1>
    """,
    unsafe_allow_html=True
)

# ----- Step 1 -----
st.markdown("<h3 style='color:#1E90FF;'>Step 1: Calculate your daily need</h3>", unsafe_allow_html=True)
weight = st.number_input("Enter your weight (in kg):", min_value=20, max_value=200, step=1)
activity_level = st.selectbox("Select your activity level:", ["Low", "Moderate", "High"])

if weight:
    daily_need = calculate_water_intake(weight, activity_level)
    st.success(f"Your recommended daily intake: **{int(daily_need)} ml** 💧")

    # ----- Step 2 -----
    st.markdown("<h3 style='color:#1E90FF;'>Step 2: Log your water intake</h3>", unsafe_allow_html=True)
    drink = st.number_input("How much water did you drink? (in ml)", min_value=50, step=50)

    if st.button("Log Water Intake"):
        st.session_state.total_today += drink
        st.success(f"{drink} ml added!")

    # ----- Step 3 -----
    st.markdown("<h3 style='color:#1E90FF;'>Step 3: Your Progress Today</h3>", unsafe_allow_html=True)
    total_today = st.session_state.total_today
    percent = min(100, int((total_today / daily_need) * 100))
    remaining = max(0, int(daily_need - total_today))

    st.progress(percent)
    st.info(f"Total water consumed today: **{total_today} ml**")
    st.info(f"Remaining: **{remaining} ml**")

    if percent >= 100:
        st.balloons()
        st.success("You're fully hydrated today! 💪💦")
