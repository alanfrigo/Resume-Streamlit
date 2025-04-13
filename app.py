import streamlit as st
import datetime
from st_supabase_connection import SupabaseConnection
from supabase import create_client, Client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

st.set_page_config(
    page_title="Alan Frigo - Resume",
    page_icon="./profile-pic.jpeg",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache_resource
def init_connection():
    url = SUPABASE_URL
    key = SUPABASE_KEY
    return create_client(url, key)

supabase = init_connection()

@st.cache_resource
def fetch_top_skills():
    return supabase.table("top_skills").select("skill").execute()

@st.cache_resource
def fetch_certifications():
    return supabase.table("certifications").select("*").execute()

@st.cache_resource
def fetch_experience():
    return supabase.table("experience").select("*").execute()

@st.cache_resource
def fetch_company():
    return supabase.table("company").select("*").execute()

top_skills = fetch_top_skills()
certifications = fetch_certifications()
experience_sql = fetch_experience()
company = fetch_company()

photo = "./profile-pic.jpeg"

def calculate_months_difference(start_date):
    today = datetime.date.today()
    months_difference = (today.year - start_date.year) * 12 + today.month - start_date.month
    if months_difference == 1:
        return f"{months_difference} month"
    if months_difference < 12:
        return f"{months_difference} months"
    else:
        years = months_difference // 12
        remaining_months = months_difference % 12
        if remaining_months == 0:
            return f"{years} year" if years == 1 else f"{years} years"
        else:
            return f"{years} year and {remaining_months} months" if years == 1 else f"{years} years and {remaining_months} months"


def header():
        st.header("Alan Frigo")
        st.subheader("Software Engineer", divider="gray")

def sidebar():
    st.sidebar.image(photo, width=150)
    st.sidebar.header("Contact")
    st.sidebar.markdown("""
                        <style>
                        a:link, a:visited {
                            color: #ff4b4b;
                            text-decoration: none;
                            margin-right: 15px; /* Add spacing between icons */
                        }
                        .fa {
                            margin-right: 8px;
                        }
                        </style>
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                        <a href="mailto:alanfrigo@gmail.com"><i class="fa fa-envelope"></i></a> 
                        <a href="https://www.linkedin.com/in/alanfrigo/" target="_blank"><i class="fab fa-linkedin"></i></a> 
                        <a href="https://github.com/alanfrigo" target="_blank"><i class="fab fa-github"></i></a> 
                        """, unsafe_allow_html=True)
    st.sidebar.header("Top Skills")
    skills = [skill["skill"] for skill in top_skills.data]
    st.sidebar.markdown("\n".join(f"- {skill}" for skill in skills))
    st.sidebar.header("Languages")
    st.sidebar.markdown("- English (Bilingual)\n\n- Portuguese (Native)\n- Spanish (B1)")
    st.sidebar.header("Certifications")
    certifications_list = [cert["title"] for cert in certifications.data]
    certification_url = [cert["url"] for cert in certifications.data]
    st.sidebar.markdown("\n".join(f"- [{cert}]({url})" for cert, url in zip(certifications_list, certification_url)))
    st.sidebar.markdown(f"""
    """)

def summary():
    st.header("Summary")
    st.markdown("""
                Entrepreneur and passionate developer transitioning into Python development, leveraging extensive experience in SEO, automation and web development to build efficient, scalable solutions. My professional journey includes over 9 years in WordPress development, 5 years managing SEO strategies, and 4 years creating robust automations with N8N—skills that provide me with a unique, holistic perspective on digital solutions.
                
                Currently focused on Python development, I've been actively working with modern frameworks and tools such as FastAPI for building performant APIs, and LangChain for integrating advanced AI capabilities into applications. My background ensures that I approach programming challenges with a strategic mindset, emphasizing both technical proficiency and business impact.

                **Core Technologies & Skills:**
                - Python
                - FastAPI
                - LangChain
                - N8N (automation and integration)
                - WordPress
                - SEO best practices and strategy
                - Online sales funnels
                - Traffic management

                Beyond technical expertise, I bring strong problem-solving abilities
                and adaptability, thriving in dynamic, collaborative environments. I'm
                eager to contribute to Python-based projects, continuously learning
                and applying best practices to deliver high-quality, impactful software
                solutions.
                """)
    st.divider()

def experience():
    st.header("Experience")
    
    experience_data = sorted(experience_sql.data, key=lambda x: x["date_start"], reverse=True)
    company_data = {comp["id"]: comp for comp in company.data}

    displayed_companies = set()

    for exp in experience_data:
        company_id = exp["company_id"]
        company_name = company_data[company_id]["name"]
        company_location = company_data[company_id]["location"]
        date_start = datetime.datetime.strptime(exp["date_start"], "%Y-%m-%d").date()
        date_end = (
            datetime.datetime.strptime(exp["date_end"], "%Y-%m-%d").date()
            if exp["date_end"]
            else None
        )
        duration = calculate_months_difference(date_start) if not date_end else calculate_months_difference(date_start) + " - " + calculate_months_difference(date_end)

        if company_id not in displayed_companies:
            st.markdown(f"""
                #### {company_name} - *{company_location}*
            """)
            displayed_companies.add(company_id)

        st.markdown(f"""
            ##### :rocket: {exp["job_title"]}
            {date_start.strftime('%B %Y')} - {"Present" if not date_end else date_end.strftime('%B %Y')} ({calculate_months_difference(date_start)})
        """)
        if exp["acta"] is not None:
            with st.container(border=True):
                st.markdown(exp["acta"])
            st.divider()



sidebar()
header()
tab1, tab2 = st.tabs(["Summary", "Experience"])
with tab1:
    summary()
with tab2:
    experience()


st.write(f"Developed with :heart: by Alan Frigo")
st.write(f"Last updated: 2025, April 13th")