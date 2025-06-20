import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from googleapiclient.discovery import build

# Load API keys
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Set page config
st.set_page_config(page_title="SkillBuilder AI", page_icon="📘")

st.title("📘 SkillBuilder AI")
st.markdown("Get personalized learning paths with YouTube recommendations!")

# Input fields
skill = st.text_input("Enter your current skill (e.g., Python, Excel):")
goal = st.text_input("Enter your learning goal (e.g., Become a Data Analyst):")

# Function to fetch YouTube videos
def get_youtube_videos(query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=max_results,
        type="video"
    )
    response = request.execute()
    return [
        {
            "title": item["snippet"]["title"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        for item in response.get("items", [])
    ]

if st.button("Get Learning Path"):
    if not skill or not goal:
        st.warning("Please enter both skill and goal.")
    else:
        with st.spinner("Generating learning path..."):
            # GPT prompt
            prompt = f"""You are a learning assistant. Given the skill: '{skill}' and the goal: '{goal}',
            generate a personalized learning path with bullet points and simple explanations for a beginner.
            Do not include YouTube links. Just the structured steps."""

            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[{"role": "user", "content": prompt}]
                )

                plan = response.choices[0].message.content
                st.subheader("\U0001F4DA Learning Path:")
                st.markdown(plan)
                # Add download button
                st.download_button(
                    label="📥 Download Learning Path",
                    data=plan,
                    file_name=f"{skill.lower()}_to_{goal.lower().replace(' ', '_')}_learning_path.txt",
                    mime="text/plain"
                    )
                # YouTube video recommendations
                search_query = f"{skill} to {goal} tutorial"
                videos = get_youtube_videos(search_query)

                st.subheader("📺 YouTube Tutorials:")
                for video in videos:
                    st.markdown(f"[{video['title']}]({video['url']})")

            except Exception as e:
                st.error(f"Something went wrong: {e}")  
