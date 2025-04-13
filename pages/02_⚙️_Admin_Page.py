import streamlit as st
from supabase import create_client, Client, SupabaseAuthClient
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

st.set_page_config(
    page_title="Admin Panel",  # Change this to the desired name
    page_icon="🛠️"  # Optional: Add an icon for the page
)

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def init_connection():
    url = SUPABASE_URL
    key = SUPABASE_KEY
    return create_client(url, key)

supabase = init_connection()
auth_client = supabase.auth 

def sidebar():
    if st.sidebar.button("Logout", icon="🚪"):
        st.session_state.logged_in = False
        st.success("Logged out successfully")

def admin_page():
    sidebar()
    st.title("Admin Panel")
    st.write("This is the admin panel. You can manage your data here.")
    adminform = st.empty()
    with adminform.form("admin_form"):
        st.markdown("#### Add a new Top skill")
        skill = st.text_input("Skill")
        submit_skill = st.form_submit_button("Add Skill")
    if submit_skill:
        if skill:
            try:
                response = supabase.table("top_skills").insert({"skill": skill}).execute()
                if response.status_code == 201:
                    st.success("Skill added successfully")
                else:
                    st.error("Failed to add skill")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if not st.session_state.logged_in:
    # Create an empty container
    placeholder = st.empty()
    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        form_email = st.text_input("Email")
        form_password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        try:
            response = auth_client.sign_in_with_password(credentials={
                "email": form_email,
                "password": form_password
            })
            st.success("Login successful")
            st.write(response)
            user = response.get_user()
            user_id = user.id
            st.session_state.logged_in = True  # Update session state
            placeholder.empty()
            admin_page()  # Clear the login form
        except Exception as e:
            # Handle invalid login credentials
            if "Invalid login credentials" in str(e):
                st.error("Invalid Login or Password")
            else:
                st.error(f"An unexpected error occurred: {e}")
else:
    admin_page()