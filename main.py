import streamlit as st
import datetime

photo = "./profile-pic.jpeg"

def calculate_months_difference(start_date):
    today = datetime.date.today()
    months_difference = (today.year - start_date.year) * 12 + today.month - start_date.month
    if months_difference < 12:
        return f"{months_difference} months"
    else:
        years = months_difference // 12
        remaining_months = months_difference % 12
        if remaining_months == 0:
            return f"{years} year" if years == 1 else f"{years} years"
        else:
            return f"{years} year and {remaining_months} months" if years == 1 else f"{years} years and {remaining_months} months"

st.set_page_config(
    page_title="Alan Frigo - Resume",
    page_icon=photo,
    layout="wide",
    initial_sidebar_state="expanded",
)


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
    st.sidebar.markdown("- Software Development\n- Python\n- FastAPI\n- LangChain\n- Wordpress\n- N8N\n- Low Code Development")
    st.sidebar.header("Languages")
    st.sidebar.markdown("- English (Bilingual)\n- Portuguese (Native)\n- Spanish (Conversational)")
    st.sidebar.header("Certifications")
    st.sidebar.markdown("""
                        - [AI Applications: Building Agents with LangChain](https://hub.asimov.academy/validar-certificado/4febe151-c486-405d-924d-36a6e2570e87)
                        - [AI Applications with LangChain](https://hub.asimov.academy/validar-certificado/9207f1f6-42ce-4b88-8bf2-0cce9d869b47)
                        - [Prompt Engineering](https://hub.asimov.academy/validar-certificado/863289ab-0123-48f8-945e-cf3adaef29d3)
                        - [Web Apps with Streamlit](https://hub.asimov.academy/validar-certificado/078bc8b7-08ea-4e74-a7ed-f6b7e6296188)
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

def experience():
    st.header("Experience")
    
    # Pixel Peninsula
    st.markdown(f"""
        #### Pixel Peninsula - {calculate_months_difference(datetime.date(2024, 11, 1))} - *Sheridan, Wyoming, United States (Remote)*
    """)
    st.markdown(f"""
        ##### :rocket: Python Developer
        March 2025 - Present ({calculate_months_difference(datetime.date(2025, 3, 1))})

        ##### :rocket: Search Engine Optimization Manager
        November 2024 - Present ({calculate_months_difference(datetime.date(2024, 11, 1))})
    """)
    with st.container(border=True):
        st.markdown("""
            **Achievements**:
            - Achieved a 20% increase in site traffic since acquiring and restructuring the gaming blogs.
            - Successfully executed a complete server migration to a Bare Metal solution from OVHCloud, ensuring enhanced performance and scalability.

            **Context**:
            As Co-Founder and CTO at Pixel Peninsula, I played a pivotal role in acquiring three major gaming blogs: outsidergaming.com, Leaguefeed.net, and Leaguetips.gg in November 2024. The acquisition required a comprehensive overhaul, including a new WordPress theme implementation and a full server migration, to support the evolving digital landscape.

            **Technologies**:
            - CMS & Server: WordPress, OVHCloud Bare Metal servers, Docker and EasyPanel
            - Analytics & Automation: Matomo, Google Analytics, N8N
            - SEO Tools: SEMRUSH, AHREFS, MOZ, KWFINDER
            - Custom Development: Developed personalized plugins and implemented Web Stories to enhance website functionality and engagement.

            **Activities**:
            - Lead the on-page and off-page SEO management, consistently optimizing content and structure to boost search engine rankings.
            - Identify and execute strategic link building and backlink opportunities.
            - Monitor and manage server performance, ensuring a seamless and robust hosting environment.
            - Produce and contribute high-quality articles during spare time to support content marketing initiatives.
                """)
    

    # AT2E-USA
    st.markdown(f"""
        #### AT2E-USA - {calculate_months_difference(datetime.date(2023, 11, 1))} - *Chicago, Illinois, United States*
    """)
    st.markdown(f"""
        ##### :rocket: Search Engine Optimization Manager
        March 2024 - Present ({calculate_months_difference(datetime.date(2024, 3, 1))})
        """)
    container = st.container(border=True)
    container.markdown(f"""
                            **Achievements**:
                            - Increased daily Google search clicks from 6 to 65 and secured over 20 keywords ranking in the top position.
                            - Successfully restructured and migrated the website from Weebly to WordPress, achieving a perfect 100% score on Pagespeed Tools.

                            **Context**:
                            Promoted to SEO Manager at AT2E-USA following the successful website reconstruction. Oversaw SEO initiatives for both the U.S. operations and the Brazilian subsidiary.

                            **Technologies**:
                            - CMS & Page Builders: WordPress, Elementor Pro
                            - SEO Tools: SEMRUSH, AHREFS, MOZ, KWFINDER
                            - Automation: N8N for automations and notifications
                            - Analytics: Google Analytics, Matomo

                            **Activities**:
                            - Implemented robust tracking solutions to monitor website performance and user engagement across multiple regions.
                            - Utilized industry-leading SEO tools daily to identify and capitalize on new growth opportunities.
                            - Led extensive link-building campaigns, acquiring valuable backlinks that enhanced domain authority and search rankings.
                            - Developed custom WordPress plugins to meet the unique requirements of the business.
                        """)
    st.markdown(f"""
        ##### :rocket: Web Developer
        November 2023 - March 2024 (5 months)
    """)

    container = st.container(border=True)
    container.markdown(f"""
                       Achievements

- Successfully restructured and migrated the website from Weebly to
WordPress, achieving a perfect 100% score on Pagespeed Tools.
- Developed custom WordPress plugins and automated key processes,
significantly improving site performance and operational efficiency.

Context

Worked as a WordPress Developer at AT2E-USA, a U.S.-based supplier of
quality testing equipment for beverage packaging.
Initially focused on transitioning an e-commerce site—built on Weebly—to
WordPress using WooCommerce. Later, at the company's request, the site
was reoriented to serve as a comprehensive product catalog.

Technologies

- CMS & Page Builders: WordPress, Elementor Pro
- E-commerce & Catalog: WooCommerce
- Infrastructure: VPS hosting
- Communication & Automation: WooChat (self-hosted), WhatsApp API, N8N
- Custom Development: Custom WordPress plugins

Activities

- Led the complete website overhaul, migrating the platform from Weebly to
WordPress, ensuring enhanced functionality and performance.
- Rebuilt the site with Elementor Pro and WooCommerce, transitioning from
an e-commerce platform to a product catalog as per the company’s strategic
direction.
- Rewrote all product descriptions to boost on-page SEO, contributing to
improved search engine rankings.


- Monitored VPS infrastructure to maintain optimal performance and reliability.
- Implemented a self-hosted webchat solution via WooChat and developed
automation workflows for WhatsApp notifications using the WhatsApp API and
N8N.
- Delivered custom WordPress plugins to meet the unique requirements of the
business.
    """)

    # Apollo Podcasts
    st.markdown(f"""
        #### Apollo Podcasts - {calculate_months_difference(datetime.date(2024, 7, 1))} - *Los Angeles, California, United States*
    """)
    st.markdown(f"""
        ##### :rocket: Search Engine Optimization Manager
        July 2024 - November 2024 (5 months)
    """)
    container = st.container(border=True)
    container.markdown(f"""
        **Achievements**:
        - Boosted Google search clicks from 5 to 105 daily through comprehensive SEO strategies.
        - Improved website performance dramatically, elevating the Pagespeed Tools score from 70% to 99%.

        **Context**:
        Hired as SEO Manager at Apollo Podcasts, a niche app dedicated to fiction podcasts facing challenges in increasing listener engagement.

        **Technologies**:
        - CMS & Website Performance: Migrated the site from Webflow to WordPress.
        - SEO Tools & Analytics: SEMRUSH, MOZ, AHREFS, UBERSUGGEST
        - Email Marketing: Implemented AWS SES for newsletter delivery.

        **Activities**:
        - Initiated and led the migration of the website from Webflow to WordPress.
        - Developed and implemented on-page SEO strategies that significantly increased daily search clicks.
        - Launched and managed email marketing campaigns, including the creation of engaging newsletters via AWS SES.
    """)

    # Rocket Jump Marketing
    st.markdown(f"""
        #### Rocket Jump Marketing - 5 Years - *Curitiba, Brazil*
    """)
    st.markdown(f"""
        ##### :rocket: Founder
        December 2019 - November 2024 (5 years)
    """)
    container = st.container(border=True)
    container.markdown(f"""
        **Achievements**:
        - Successfully launched multiple digital products and helped content creators establish a strong online presence.
        - Managed strategic paid ad campaigns across Facebook, Instagram, LinkedIn, and TikTok, driving lead generation and sales growth.

        **Context**:
        Founder of Rocket Jump, a digital marketing company focused on co-producing and launching infoproducts in partnership with content creators.

        **Technologies**:
        - Website & Landing Pages: WordPress, Elementor
        - Automation & Notifications: N8N, WhatsApp API
        - Paid Ads & Analytics: Facebook Ads, Instagram Ads, LinkedIn Ads, TikTok Ads, Google Analytics

        **Activities**:
        - Acted as the lead strategist, planning and executing content production and marketing campaigns for digital product creators.
        - Designed and optimized landing pages to maximize conversion rates.
        - Planned and managed paid ad strategies across multiple platforms.
    """)

    # Rebbel
    st.markdown(f"""
        #### Rebbel - 3 Years and 1 Month - *Cascavel, Brazil*
    """)
    st.markdown(f"""
        ##### :rocket: Founder
        March 2016 - March 2019 (3 years 1 month)
    """)
    container = st.container(border=True)
    container.markdown(f"""
        **Achievements**:
        - Successfully migrated the e-commerce platform from PrestaShop to WordPress and WooCommerce, enhancing user experience and operational efficiency.
        - Boosted local SEO performance and increased organic traffic through targeted optimization strategies.

        **Context**:
        Founded Rebbel as a men's watch store, later evolving into a broader men's apparel brand with a focus on t-shirts.

        **Technologies**:
        - E-commerce Platforms: PrestaShop, WordPress, WooCommerce
        - SEO Tools: Ubersuggest (for local SEO optimization)

        **Activities**:
        - Oversaw the end-to-end migration of the online store, ensuring a seamless transition from PrestaShop to WordPress and WooCommerce.
        - Implemented local SEO strategies to improve visibility in regional search results and attract a targeted audience.
    """)

sidebar()
header()
tab1, tab2 = st.tabs(["Summary", "Experience"])
with tab1:
    summary()
with tab2:
    experience()
