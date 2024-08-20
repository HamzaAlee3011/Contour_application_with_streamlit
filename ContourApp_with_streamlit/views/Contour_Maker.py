import streamlit as st
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import plotly.graph_objects as go

# List of available colorscales for Plotly
color_scales = [
    'Viridis', 'Cividis', 'Inferno', 'Magma', 'Plasma', 'Rainbow',
    'Hot', 'Jet', 'Earth', 'Twilight', 'HSV', 'YlGnBu'
]

# List of aspect ratio options
aspect_ratio_values = ['unequal', 'equal']

# Title for app
st.title("Contour Maker", anchor=False)
st.write("\n")

# File upload widget
uploaded_file = st.file_uploader('Upload File', type=['xlsx', 'csv'])

if uploaded_file is not None:
    # Determine the file type and read the file accordingly
    if uploaded_file.name.endswith('.xlsx'):
        st.subheader('Preview Data')
        data = pd.read_excel(uploaded_file, na_filter=False, na_values=True)
    elif uploaded_file.name.endswith('.csv'):
        st.subheader('Preview Data')
        data = pd.read_csv(uploaded_file, na_filter=False, na_values=True)

    if data is not None:
        # Clean the data by dropping columns where all elements are NaN
        data_cleaned = data.dropna(axis=1, how='all')
        st.write(data_cleaned)
else:
    st.info("Waiting for file upload...")

st.write("\n")
st.write("\n")
st.subheader('Select Columns with Respective Values')

col1, col2, col3 = st.columns(3, gap='small')
with col1:
    x_column_num = st.number_input('Column containing x-values', value=st.session_state.get('x_column_num', 0), placeholder="Input...", min_value=0)
with col2:
    y_column_num = st.number_input('Column containing y-values', value=st.session_state.get('y_column_num', 0), placeholder="Input...", min_value=0)
with col3:
    z_column_num = st.number_input('Column containing Elevations', value=st.session_state.get('z_column_num', 0), placeholder="Input...", min_value=0)

st.write("\n")
st.write("\n")
st.subheader('Plot Contour Map')

containor_1 = st.container(border=True)
col4, col5 = containor_1.columns(2)

with col4:
    contour_interval = st.number_input('Contour Interval', value=st.session_state.get('contour_interval', 0.01), placeholder="Type a number...", format=f"%0.4f")
    label_size = st.number_input('Label Size', value=st.session_state.get('label_size', 12), min_value=1, max_value=50)
    plot_button = st.button('Plot', type='secondary')
with col5:
    color_select = st.selectbox('Colormap', options=color_scales, index=color_scales.index(st.session_state.get('color_select', 'Viridis')))
    aspect_ratio = st.selectbox('Aspect Ratio', options=aspect_ratio_values, index=aspect_ratio_values.index(st.session_state.get('aspect_ratio', 'unequal')))

# Store the values in session state
st.session_state['x_column_num'] = x_column_num
st.session_state['y_column_num'] = y_column_num
st.session_state['z_column_num'] = z_column_num
st.session_state['contour_interval'] = contour_interval
st.session_state['label_size'] = label_size
st.session_state['color_select'] = color_select
st.session_state['aspect_ratio'] = aspect_ratio

if plot_button:
    if uploaded_file is not None:
        # Extract X, Y, Z columns from the DataFrame
        x = data.iloc[:, x_column_num - 2].tolist()
        y = data.iloc[:, y_column_num - 2].tolist()
        z = data.iloc[:, z_column_num - 2].tolist()

        # Create a regular grid for interpolation
        xi = np.linspace(min(x), max(x), 100)
        yi = np.linspace(min(y), max(y), 100)
        XI, YI = np.meshgrid(xi, yi)

        # Interpolate the data onto the regular grid
        ZI = griddata((x, y), z, (XI, YI), method='cubic')

        # Create the contour plot using Plotly
        fig = go.Figure(data=go.Contour(
            z=ZI,
            x=xi,  # x-coordinates for the contour
            y=yi,  # y-coordinates for the contour
            contours=dict(
                start=min(z),
                end=max(z),
                size=contour_interval,  # Set contour interval
                showlabels=True,  # show labels on contours
                labelfont={'size': label_size, 'color': "black"},
            ),
            colorscale=color_select,  # Apply selected color scale
            colorbar=dict(title='Elevation')
        ))

        if aspect_ratio == 'equal':
            # Set aspect ratio to equal
            fig.update_layout(
                xaxis=dict(scaleanchor="y", scaleratio=1),
                yaxis=dict(scaleanchor="x", scaleratio=1)
            )

        # Display the plot in Streamlit
        st.plotly_chart(fig)
        st.write(f'''
        - Minimum Reduced Level: {min(z)}
- Maximum Reduced Level: {max(z)}''')
    else:
        st.error('Please upload file first!')
