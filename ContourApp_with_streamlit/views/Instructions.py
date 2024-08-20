import streamlit as st


st.set_page_config(layout="wide")

col0a, col0b, col0c = st.columns(3)
with col0b:
    st.write('# Instructions')
    st.write('\n')

st.write('## **1) :orange-background[Preparing Data In Excel Sheet]**')
st.write("""
- **Important:** Ensure there are no blank rows at the top of your table in the Excel sheet. Blank rows can cause errors when reading the file.
- Organize your data properly by placing the headers in the first row, and ensure all relevant data starts immediately below.
- Always double-check for any unintentional empty rows or columns within the data to avoid issues during file processing.
""")

col1a, col1b, col1c = st.columns(3, gap='medium')
with col1a:
    st.image('./assets/instruction-example1.png', caption='Correct ✅')
with col1b:
    st.image('./assets/instruction-example2.png', caption='Correct ✅')
with col1c:
    st.image('./assets/instruction-example3.png', caption='Wrong ❌')

st.write('\n')
st.write('\n')
st.write('## **2) :orange-background[Selecting Columns From Sheet]**')
st.markdown("""The program treats the first column in ***Preview Data Sheet*** as column number 1, the second column as
            number 2, and so on.  
            •) This numbering is important when selecting columns for processing.  
            •) Incorrect column selection can lead to errors or inaccurate results.  
            •) Double-check that the column numbers align with your data layout to avoid processing issues.""")

col1a, col1b = st.columns(2, gap='medium')
with col1a:
    st.image('./assets/column-select-example1.png', caption="Example-1")
    st.markdown("""• Column no. containing x-values = 2  
    • Column no. containing y-values = 3  
    • Column no. containing elevations = 4""")

with col1b:
    st.image('./assets/column-select-example2.png', caption='Example-2')
    st.markdown("""• Column no. containing x-values = 4  
    • Column no. containing y-values = 5  
    • Column no. containing elevations = 6""")

st.write('\n')
st.write('\n')
st.write('## **3) :orange-background[Customizations for Plot]**')

with st.expander('### **Selecting Visualization Engine**'):
    st.write("""
    - :grey-background[**Plotly**]: Offers advanced visualization with interactive features and 3D Visualization.
    - :grey-background[**MATLAB**]: Provides basic visualization and export options.""")
    st.image('./assets/visualization-engine-example.png', caption='Reference Image')

with st.expander('### **Map Settings**'):
    st.write("""
   - :grey-background[**Contour Interval**]: Adjust the interval between contour lines. The input box and buttons let you set this value precisely.
- :grey-background[**Contour Type**]: Choose the contour style (e.g., Straight or Curved).
- :grey-background[**Elevation Labels**]: Toggle the display of elevation labels on the contours.""")
    st.image('./assets/map-setting-example.png', caption='Reference Image')

with st.expander('### **Plot Settings**'):
    st.write("""
   - :grey-background[**Colormap**]: Select a colormap to apply color gradients to your plot. "None" leaves the plot uncolored.
- :grey-background[**Label Size**]: Adjust the font size of labels on the contours.
- :grey-background[**Aspect Ratio**]: Define the aspect ratio for your plot, e.g., "equal" ensures that one unit on the x-axis is equal to one unit on the y-axis.""")
    st.image('./assets/plot-setting-example.png', caption='Reference Image')

with st.expander('### **Grids Settings**'):
    st.write("""
   - :grey-background[**Grid lines**]: Toggle between showing or hiding grid lines.
- :grey-background[**Grid Size**]: Set the spacing between grid lines.
- :grey-background[**Grids Color**]: Choose the color of the grid lines.""")
    st.image('./assets/grid-setting-example.png', caption='Reference Image')

with st.expander('### **3D Visualization Toggle**'):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
       - :grey-background[**Enable 3D Visualization**]: Activate this option to generate 3D contour plots.""")

    with col2:
        st.image('./assets/3d-vis-example.jpeg', caption='Reference Image')

st.write("""
### **Important Note**
- After making any changes to the settings, make sure to press the :red-background[**Plot**] button to apply the changes and update the contour map.
""")