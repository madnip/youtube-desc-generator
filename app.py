import streamlit as st
from groq import Groq

# --- SETUP ---
try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("⚠️ Error: Groq API Key not found. Please set it in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=API_KEY)

# --- PAGE CONFIG ---
st.set_page_config(page_title="YouTube SEO Pro", page_icon="🚀", layout="centered")

st.title("🚀 YouTube SEO Master Tool")
st.write("Generate viral Descriptions & Tags in seconds.")

# --- SIDEBAR (MONEY MAKER) ---
with st.sidebar:
    st.header("💸 Monetization")
    st.info("💡 Tip: Add your affiliate links here to earn extra money!")
    st.markdown("[👉 **Get CapCut Pro 50% Off**](#)") # Change this link
    st.divider()
    st.write("Created by [Your Name]")

# --- TABS ---
tab1, tab2 = st.tabs(["📝 Description Gen", "🏷️ Tag Generator"])

# === TAB 1: DESCRIPTION GENERATOR ===
with tab1:
    st.subheader("📝 Write Viral Descriptions")
    desc_title = st.text_input("Video Title", placeholder="e.g. How to cook biryani", key="desc_title")
    desc_keywords = st.text_input("Keywords", placeholder="e.g. spicy, chicken, easy recipe", key="desc_keywords")
    
    if st.button("Generate Description 🪄", key="btn_desc"):
        if desc_title:
            with st.spinner("AI is writing..."):
                try:
                    prompt = f"""
                    Write a professional YouTube description for a video titled '{desc_title}'.
                    Include these keywords: {desc_keywords}.
                    Include timestamps, 3 hashtags, and a hook.
                    """
                    completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama3-8b-8192",
                    )
                    st.text_area("Copy Result:", value=completion.choices[0].message.content, height=300)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a title first.")

# === TAB 2: TAG GENERATOR (NEW!) ===
with tab2:
    st.subheader("🏷️ Generate High-CPC Tags")
    tag_title = st.text_input("Video Title", placeholder="e.g. Earn money online in Pakistan", key="tag_title")
    
    if st.button("Generate Tags 🚀", key="btn_tags"):
        if tag_title:
            with st.spinner("Finding best tags..."):
                try:
                    prompt = f"""
                    Generate 25 high-traffic, SEO-optimized YouTube tags for a video titled '{tag_title}'.
                    Separate them with commas. Do not write a list, just comma separated text.
                    Example: tag1, tag2, tag3
                    """
                    completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama3-8b-8192",
                    )
                    tags = completion.choices[0].message.content
                    st.success("Copy these tags into YouTube:")
                    st.code(tags, language=None)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Enter a title to get tags.")