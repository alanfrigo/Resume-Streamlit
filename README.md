# Alan Frigo's Resume

Welcome to my interactive resume application—a modern, web-based platform designed to showcase my professional background and technical expertise in Python development. This project not only serves as an online curriculum vitae but also demonstrates my ability to build engaging applications with cutting-edge technologies.

---

## Overview

**Alan Frigo's Resume** is built with Python and Streamlit to provide a dynamic and responsive user interface. The application leverages cloud-based services to fetch and display data, ensuring that the content (such as skills, certifications, and work experience) is always up-to-date. With a clean design and interactive elements, this project effectively highlights my journey from SEO and automation to advanced Python development.

---

## Features

- **Interactive UI:** Developed using [Streamlit](https://streamlit.io/), the app offers a responsive and user-friendly interface.
- **Cloud-Integrated Data:** Uses [Supabase](https://supabase.com/) for backend data storage, retrieving information on my top skills, certifications, and professional experience.
- **Dynamic Calculations:** Implements custom logic for date and duration calculations, enhancing the presentation of my career timeline.
- **Custom Sidebar:** Features personalized contact links (email, LinkedIn, GitHub) and skill listings, making it easy for employers to connect.
- **Structured Layout:** Organized sections for a professional summary and detailed work experience ensure clear, engaging storytelling.

---

## Technologies Used

- **Python:** The primary programming language for rapid development and robust back-end processing.
- **Streamlit:** Enables quick creation of interactive, data-driven web apps with minimal code.
- **Supabase:** Acts as the backend service for storing and retrieving resume data, illustrating real-world integration of cloud databases.
- **Datetime Module:** Utilized for calculating work durations, showcasing attention to detail in presenting experience.
- **Custom Modules:** Utilizes specialized libraries like `st_supabase_connection` for seamless connectivity with Supabase.

---

## Getting Started

### Prerequisites

- **Python 3.8+**
- **pip** package manager
- The following Python packages (listed in `requirements.txt`):
  - `streamlit`
  - `supabase`
  - `st_supabase_connection`

### Environment Variables

Ensure your Supabase credentials are set before running the application:
- `SUPABASE_URL` — Your Supabase project URL.
- `SUPABASE_KEY` — Your Supabase API key.

You can define these in your system environment or via a `.env` file using a package like [python-dotenv](https://pypi.org/project/python-dotenv/).

### Installation

1. **Clone the Repository:**

       git clone https://github.com/your_username/alan-frigo-resume.git
       cd alan-frigo-resume

2. **Install Dependencies:**

       pip install -r requirements.txt

### Running the Application

Launch the interactive resume with Streamlit:

       streamlit run main.py

> Replace `main.py` with the name of your main Python file if it is different.

---

## Project Structure

Project Structure:
    
    ├── app.py                  # Main application file containing all Streamlit code.
    ├── README.md               # Project overview and instructions.
    ├── requirements.txt        # List of Python dependencies.
    ├── profile-pic.jpeg        # Profile image displayed in the sidebar.
    └── .env                    # (Optional) Environment variables for Supabase credentials.

---

## Future Enhancements

- **Additional Content:** Integrate a project portfolio or case studies to further highlight my capabilities.
- **UI Enhancements:** Continue refining the design for a more polished look and feel.
- **Advanced Integrations:** Explore incorporating advanced frameworks (e.g., FastAPI, LangChain) for deeper functionality and demonstrations of technical versatility.

---

## About Me

I am a dedicated Software Engineer with a passion for Python development. With years of experience in SEO, web automation, and WordPress development, I bring a comprehensive and innovative approach to every project. My goal is to create impactful, scalable, and efficient solutions that merge technical excellence with strategic business insights.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

Feel free to reach out to discuss opportunities or to learn more about my work:

- **Email:** [alanfrigo@gmail.com](mailto:alanfrigo@gmail.com)
- **LinkedIn:** [Alan Frigo](https://www.linkedin.com/in/alanfrigo/)

---

*Developed with :heart: by Alan Frigo*  
_Last updated: April 13, 2025_
