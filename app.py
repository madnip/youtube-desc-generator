import streamlit as st
from groq import Groq

# --- SETUP ---
# We use st.secrets to keep your API key safe
try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("Groq API Key not found. Please set it in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=API_KEY)

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Description Generator", page_icon="✨")

st.title("✨ YouTube Description Maker")
st.markdown("Paste your video title below and get a SEO-optimized description instantly.")

# --- SIDEBAR ADS (LIFETIME INCOME) ---
with st.sidebar:
    st.header("🚀 Grow Your Channel")
    st.image("https://cdn-icons-png.flaticon.com/512/174/174883.png", width=50)
    st.write("Want to edit videos faster?")
    # REPLACE THE '#' BELOW WITH YOUR ACTUAL AFFILIATE LINKS
    st.markdown("[**👉 Click here to get 50% off CapCut Pro**](#)") 
    st.divider()
    st.write("☕ **Support this free tool:**")
    st.markdown("[Buy me a Coffee](#)") 

# --- THE TOOL ---
video_title = st.text_input("Video Title:", placeholder="e.g. How to make money online 2025")
keywords = st.text_input("Keywords to include:", placeholder="e.g. passive income, easy cash")

if st.button("Generate Description 🪄"):
    if video_title:
        with st.spinner("Writing magic..."):
            try:
                # Using Llama3 model via Groq
                prompt = f"""
                Write a professional YouTube video description for a video titled '{video_title}'.
                Include these keywords naturally: {keywords}.
                Add timestamps, 3 hashtags, and a catchy first line.
                """
                
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama3-8b-8192",
                )
                
                result = chat_completion.choices[0].message.content
                st.subheader("Your Description:")
                st.text_area("Copy this:", value=result, height=400)
                st.balloons()
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a title first!")