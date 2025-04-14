import streamlit as st
from supabase import create_client, Client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

st.set_page_config(
    page_title="Admin Panel",  # Change this to the desired name
    page_icon="🛠️"  # Optional: Add an icon for the page
)

# Initialize session state for login and auth
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "auth_session" not in st.session_state:
    st.session_state.auth_session = None


def init_connection():
    url = SUPABASE_URL
    key = SUPABASE_KEY
    client = create_client(url, key)
    # Set auth if we have a session
    if st.session_state.auth_session:
        client.auth.set_session(st.session_state.auth_session.access_token, st.session_state.auth_session.refresh_token)
    return client

def sidebar():
    if st.sidebar.button("Logout", icon="🚪"):
        st.session_state.logged_in = False
        st.session_state.auth_session = None
        st.success("Logged out successfully")

def admin_page():
    # Get a fresh client with the current session
    supabase = init_connection()
    
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
                # Debug information
                st.write("Session state:", st.session_state.auth_session)
                user = st.session_state.auth_session.user
                user_id = user.id
                st.write("User ID:", user_id)
                
                # First, let's try to read from the table to verify permissions
                try:
                    read_response = supabase.table("top_skills").select("*").execute()
                    st.write("Read response:", read_response)
                except Exception as read_error:
                    st.write("Read error:", str(read_error))
                
                # Include both skill and user_id
                data = {
                    "skill": str(skill).strip(),
                    "user_id": user_id  # Include user_id to satisfy RLS
                }
                st.write("Inserting data:", data)
                
                response = supabase.table("top_skills").insert(data).execute()
                
                if response.data:
                    st.cache_resource.clear()
                    st.success("Skill added successfully")
                else:
                    st.error("Failed to add skill")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.write("Full error details:", str(e))

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
            # Get a fresh client
            supabase = init_connection()
            response = supabase.auth.sign_in_with_password({
                "email": form_email,
                "password": form_password
            })
            st.session_state.auth_session = response.session
            st.session_state.logged_in = True
            st.success("Login successful")
            placeholder.empty()
            admin_page()
        except Exception as e:
            if "Invalid login credentials" in str(e):
                st.error("Invalid Login or Password")
            else:
                st.error(f"An unexpected error occurred: {e}")
else:
    admin_page()