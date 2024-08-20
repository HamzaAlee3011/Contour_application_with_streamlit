import streamlit as st

# PAGE SETUP


# contourmaker_page1 = st.Page(
#     page="views/Contour_Maker.py",
#     title="Contour Maker1",
#     icon=":material/bid_landscape:",
#     default=True
# )

contourmaker_page2 = st.Page(

    page="views/Contour_maker2.py",
    title="Contour Maker",
    icon=":material/bid_landscape:",
)

about_me = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
)

about_app = st.Page(
    page="views/about_app.py",
    title="About Application",
    icon=":material/info:",
)

instructions = st.Page(
    page="views/Instructions.py",
    title="Instructions",
    icon=":material/help_outline:",
)

# NAVIGATION SETUP (WITHOUT SECTIONS)
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# NAVIGATION SETUP (WITH SECTIONS)
pg = st.navigation({
    'Application': [contourmaker_page2],
    'Usage': [instructions],
    'Info': [about_me, about_app],
})

# SHARED ON ALL PAGES

# st.logo('assets/example_logo.png')
# st.sidebar.text('''Made by Ameer Hamza Ali
# with 💥''')

#RUN NAVIGATION
pg.run()
