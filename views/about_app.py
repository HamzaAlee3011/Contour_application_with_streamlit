import streamlit as st

col0a, col0b, col0c = st.columns([0.6, 1, 0.6])
with col0b:
    st.title("About Application")
    st.write('\n')


st.write("### :blue-background[**:material/code_blocks: Developer**]")
st.write("""

***Ameer Hamza Ali***  
***Batch 2022***  
***Department of Civil Engineering***  
***NED University of Engineering & Technology, Karachi, Pakistan***  
  
Check out my profile:  
https://about-hamza-ali.streamlit.app/
""")

st.write('\n')
st.write("###  :blue-background[**:material/communities: Purpose**]")
st.write("""
This application is designed to help users generate and visualize contour plots from data inputs. 
Users can choose between 2D and 3D visualizations, customize various plot settings, and export the plots in different formats.

I created this application because, during my time, I couldn't find any free and accessible contour plotting software that met my needs. 
Now, it's available as an open-source tool for everyone to use and benefit from.
""")

st.write('\n')
st.write("### :blue-background[**:material/featured_play_list: Key Features**]")
st.write("""
- **:grey-background[Contour Plotting]:** Generate both 2D and 3D contour plots using either Plotly or Matplotlib.
- **:grey-background[Customization]:** Adjust contour intervals, color maps, grid settings, and more.
- **:grey-background[Export Options]:** Save your plots as PNG or PDF files.
- **:grey-background[Interactive Interface]:** Make real-time adjustments to plot settings and see the results instantly.
""")

st.write("### :blue-background[**:material/view_module: Modules Used**]")
st.write("""
This application is built entirely on Python using the following Python modules:

- **:grey-background[Streamlit]:** For creating the interactive web application interface. [Streamlit Documentation](https://docs.streamlit.io/)
- **:grey-background[Pandas]:** For handling and processing the data inputs. [Pandas Documentation](https://pandas.pydata.org/)
- **:grey-background[NumPy]:** For numerical computations and data manipulation. [NumPy Documentation](https://numpy.org/doc/)
- **:grey-background[SciPy]:** For interpolation to generate grid data for contour plots. [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- **:grey-background[Plotly]:** For creating interactive and dynamic 2D and 3D contour plots. [Plotly Documentation](https://plotly.com/python/)
- **:grey-background[Matplotlib]:** For generating static 2D contour plots with customization options. [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
""")

st.write('\n')
st.write("###  :blue-background[**:material/call: Contact**]")
st.write("""
For further assistance, feedback, or to report any bugs, please contact me at ameer.hamza.alee3011@gmail.com.
""")

