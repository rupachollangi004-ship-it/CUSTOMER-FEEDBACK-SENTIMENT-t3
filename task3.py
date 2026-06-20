import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard Title
st.title("Customer Feedback Sentiment Dashboard")

# Sample Feedback Data
data = {
    "Customer": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    "Sentiment": ["Positive", "Negative", "Positive", "Neutral",
                  "Positive", "Negative", "Neutral", "Positive"]
}

df = pd.DataFrame(data)

# Display Data
st.subheader("Customer Feedback Data")
st.dataframe(df)

# Sentiment Count
sentiment_count = df["Sentiment"].value_counts()

# Display Statistics
st.subheader("Sentiment Summary")
st.write("Positive Feedback:", sentiment_count.get("Positive", 0))
st.write("Neutral Feedback:", sentiment_count.get("Neutral", 0))
st.write("Negative Feedback:", sentiment_count.get("Negative", 0))

# Bar Chart
st.subheader("Sentiment Distribution")

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(sentiment_count.index, sentiment_count.values)
ax.set_title("Customer Feedback Sentiment Analysis")
ax.set_xlabel("Sentiment")
ax.set_ylabel("Count")

st.pyplot(fig)

# Pie Chart
st.subheader("Sentiment Percentage")

fig2, ax2 = plt.subplots()
ax2.pie(
    sentiment_count.values,
    labels=sentiment_count.index,
    autopct="%1.1f%%"
)
ax2.set_title("Sentiment Breakdown")

st.pyplot(fig2)

# Overall Result
st.subheader("Overall Customer Satisfaction")

if sentiment_count.get("Positive", 0) > sentiment_count.get("Negative", 0):
    st.success("Customer satisfaction is generally positive.")
elif sentiment_count.get("Positive", 0) < sentiment_count.get("Negative", 0):
    st.error("Customer satisfaction needs improvement.")
else:
    st.warning("Customer satisfaction is neutral.")