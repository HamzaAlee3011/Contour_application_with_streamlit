import streamlit as st
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import io
import openpyxl

st.set_page_config(layout="wide")

# Function for creating contour maps using matplotlib

def create_matplotlib_contourfig_plotting():
    # Create the plot
    fig, ax = plt.subplots()

    # Create contour levels based on user input
    contour_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
    contour_lines = ax.contour(XI, YI, ZI, levels=contour_levels, colors='black')
    ax.clabel(contour_lines, fmt='%1.2f', inline=True, fontsize=label_size, colors='black')
    ax.set_xticks(np.arange(min(x), max(x) + grid_size_button, grid_size_button))
    ax.set_yticks(np.arange(min(y), max(y) + grid_size_button, grid_size_button))

    if color_select != 'None':
        contourf_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
        contourf = ax.contourf(XI, YI, ZI, levels=contourf_levels, cmap=color_scales_dict[color_select])
        fig.colorbar(contourf, ax=ax, label='Elevations')

    if show_grids_sb == 'Show':
        ax.grid(True, linestyle='-', linewidth=0.8, color=grid_color_dict[grids_color])
        ax.set_aspect('equal', adjustable='box')

    if contour_elev == 'Show':
        for i in range(len(x)):
            ax.text(x[i], y[i], z[i], fontsize=label_size-2)

    # Display the plot
    st.pyplot(fig, clear_figure=False)


def create_matplotlib_contourfig_saving():
    # Create the plot
    fig, ax = plt.subplots()

    # Create contour levels based on user input
    contour_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
    contour_lines = ax.contour(XI, YI, ZI, levels=contour_levels, colors='black')
    ax.clabel(contour_lines, fmt='%1.2f', inline=True, fontsize=label_size, colors='black')
    ax.set_xticks(np.arange(min(x), max(x) + grid_size_button, grid_size_button))
    ax.set_yticks(np.arange(min(y), max(y) + grid_size_button, grid_size_button))

    if color_select != 'None':
        contourf_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
        contourf = ax.contourf(XI, YI, ZI, levels=contourf_levels, cmap=color_scales_dict[color_select])
        fig.colorbar(contourf, ax=ax, label='Elevations')

    if show_grids_sb == 'Show':
        ax.grid(True, linestyle='-', linewidth=0.8, color=grid_color_dict[grids_color])
        ax.set_aspect('equal', adjustable='box')

    if contour_elev == 'Show':
        for i in range(len(x)):
            ax.text(x[i], y[i], z[i], fontsize=label_size - 2)

    return fig

@st.fragment
def saving_form():    # Form for download
    st.write('### Save Plot')
    col1a, col1b = st.columns(2, gap='medium', vertical_alignment='bottom')

    with col1a:
        file_format = st.selectbox('Select file format:', ['pdf', 'png', 'jpeg','svg'])

    with col1b:
        buffer = io.BytesIO()
        if file_format == 'pdf':
            create_matplotlib_contourfig_saving().savefig(buffer, format='pdf')
        elif file_format == 'png':
            create_matplotlib_contourfig_saving().savefig(buffer, format='png')
        elif file_format == 'svg':
            create_matplotlib_contourfig_saving().savefig(buffer, format='svg')
        elif file_format == 'jpeg':
            create_matplotlib_contourfig_saving().savefig(buffer, format='jpeg')
        buffer.seek(0)

        st.download_button(
            label=f"Download plot as {file_format.upper()}",
            data=buffer,
            file_name=f"plot.{file_format}",
            mime=f"application/{file_format}"
        )


# Function for creating contour maps using plotly
def create_plotly_contourfig():
    # Create the contour plot using Plotly
    fig = go.Figure()

    # Add contour trace
    fig.add_trace(go.Contour(
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
        colorscale=color_scales_dict[color_select],  # Apply selected color scale
        colorbar=dict(title='Elevation')
    ))

    # Adding grids lines based on user input
    if show_grids_sb == 'Show':
        # Define the range for the grid lines based on user input
        hx, hy = compute_horizontal_lines(min(x), max(x), np.arange(min(y), max(y), grid_size_button))
        vx, vy = compute_vertical_lines(min(y), max(y), np.arange(min(x), max(x), grid_size_button))

        # Add the gridlines to the figure
        add_box(fig, hx, hy)
        add_box(fig, vx, vy)

    # Adding elevation labels
    if contour_elev == 'Show':
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="text",
            text=z,
            textposition="bottom right",
            textfont={'size': label_size - 2, 'color': "black"}
        ))

    # Adjust the layout if needed
    if aspect_ratio == 'equal':
        fig.update_layout(
            xaxis=dict(
                scaleanchor="y",
                scaleratio=1,
                constrain='domain'
            ),
            yaxis=dict(
                scaleanchor="x",
                scaleratio=1,
                constrain='domain'
            ),
            margin=dict(l=0, r=0, t=0, b=0)
        )
    st.plotly_chart(fig)

def create_3d_plotly_contourfig():
    fig = go.Figure()

    # Add 3D surface plot trace
    fig.add_trace(go.Surface(
        z=ZI,
        x=xi,
        y=yi,
        colorscale=color_scales_dict[color_select],
        contours=dict(
            z=dict(show=True, start=min(z), end=max(z), size=contour_interval, color="black")
        )
    ))

    # Define the initial aspect ratio
    initial_z_aspect_ratio = 0.1

    # Update the layout with the initial aspect ratio and add the slider
    fig.update_layout(
        scene=dict(aspectratio=dict(x=1, y=1, z=initial_z_aspect_ratio)),
        sliders=[{
            'active': 0,
            'currentvalue': {"prefix": "Z-Axis(Elevation) Aspect Ratio: "},
            'steps': [
                {'label': f'{val:.1f}', 'method': 'relayout', 'args': ['scene.aspectratio.z', val]}
                for val in np.arange(0.1, 1.1, 0.1)
            ]
        }]
    )

    st.plotly_chart(fig)

# Function for creating grid lines
def add_box(lfig, x, y):
    lfig.add_trace(go.Scatter(
        x=x,
        y=y,
        opacity=0.5,
        marker_color=grid_color_dict[grids_color],
        line_width=1,
        showlegend=False,
    ))

# Function for creating horizontal grid lines
def compute_horizontal_lines(x_min, x_max, y_data):
    x = np.tile([x_min, x_max, None], len(y_data))
    y = np.ndarray.flatten(np.array([[a, a, None] for a in y_data]))
    return x, y

# Function for creating vertical grid lines
def compute_vertical_lines(y_min, y_max, x_data):
    y = np.tile([y_min, y_max, None], len(x_data))
    x = np.ndarray.flatten(np.array([[a, a, None] for a in x_data]))
    return x, y

# List of available colorscales for Plotly
color_scales = [
    'None', 'Viridis', 'Cividis', 'Inferno', 'Magma', 'Plasma', 'Rainbow',
    'Hot', 'Jet', 'Twilight', 'HSV', 'YlGnBu'
]

# colo scale dictionary for accessing the colors
color_scales_dict = {
    'None': [[0, 'white'], [1, 'white']],  # No color, white background
    'Viridis': 'viridis',
    'Cividis': 'cividis',
    'Inferno': 'inferno',
    'Magma': 'magma',
    'Plasma': 'plasma',
    'Rainbow': 'rainbow',
    'Hot': 'hot',
    'Jet': 'jet',
    'Twilight': 'twilight',
    'HSV': 'hsv',
    'YlGnBu': 'YlGnBu'
}

# List of aspect ratio options
aspect_ratio_values = ['equal', 'unequal']

# Dictionary of Contour types
contour_type_dict = {'Straight': 'linear',
                     'Smooth': 'cubic'}

# Dictionary of grid size color
grid_color_dict = {'black': 'black',
                   'white': 'Lightgrey'}

# Title for app
st.title("Contour Maker", anchor=False)
st.write("\n")

# File upload widget
uploaded_file = st.file_uploader('Upload File', type=['xlsx'])

if uploaded_file is not None:
    # Determine the file type and read the file accordingly
    if uploaded_file.name.endswith('.xlsx'):
        st.subheader('Preview Data')
        dataset = pd.read_excel(uploaded_file, na_filter=False, na_values=True)
    elif uploaded_file.name.endswith('.csv'):
        st.subheader('Preview Data')
        dataset = pd.read_csv(uploaded_file, na_filter=False, na_values=True)

    if dataset is not None:
        # Clean the data by dropping columns where all elements are NaN
        data_cleaned = dataset.dropna(axis=1, how='all')
        st.write(data_cleaned)
else:
    st.info("Waiting for file upload...")

st.write("\n")
st.write("\n")
st.subheader('Select Columns with Respective Values')

# Form to input column numbers
with st.form(key='Inputs'):
    col1, col2, col3 = st.columns(3, gap='medium')

    with col1:
        x_column_num = st.number_input('Column no. containing x-values', value=0, min_value=0)

    with col2:
        y_column_num = st.number_input('Column no. containing y-values', value=0, min_value=0)
        save = st.form_submit_button('Save', use_container_width=True)
    with col3:
        z_column_num = st.number_input('Column no. containing Elevations', value=0, min_value=0)

# Button functionality
    if save:
        if x_column_num > 0 and y_column_num > 0 and z_column_num > 0:
            st.success('Entries saved successfully!')
        else:
            st.error("Please fill all the fields! Column number can't be 0")

st.write("\n")
st.write("\n")
st.subheader('Plot Contour Map')

col3a, col3b = st.columns(2, gap='medium')

# Form to input Plot Settings
with st.form(key='Plot_Inputs'):
    engine_type = st.radio(
        "Select Visualization Engine",
        ["**Plotly**", "**MATLAB**"],
        captions=[
            "For advanced visualization and interactive plots.",
            "For basic visualization and for exporting plots."
        ], horizontal=True
    )
    st.divider()

    col4a, col4b, col4c = st.columns(3, gap='small')
    with col4a:
        st.markdown(':blue-background[Map Settings]')
        contour_interval = st.number_input('Contour Interval', value=1.0, format=f"%0.4f")
        contour_type = st.selectbox('Contour Type', options=['Straight', 'Smooth'])
        contour_elev = st.selectbox('Elevation Labels', options=['Show', 'Hide'])
    with col4b:
        st.markdown(':blue-background[Plot Settings]')
        color_select = st.selectbox('Colormap', options=color_scales)
        label_size = st.number_input('Label Size', value=12, min_value=1,
                                     max_value=50)
        if engine_type == "**Plotly**":
            aspect_ratio = st.selectbox('Aspect Ratio', options=aspect_ratio_values, help='if "equal", makes the grids of graph of equal size ')
        else:
            aspect_ratio = st.selectbox('Aspect Ratio', options=aspect_ratio_values,
                                        help='if "equal", makes the grids of graph of equal size ',
                                        disabled=True)

    with col4c:
        st.markdown(':blue-background[Grids Settings]')
        show_grids_sb = st.selectbox('Grid lines', options=['Show', 'Hide'], help='whether to show grid lines or not')
        grid_size_button = st.number_input('Grid Size', min_value=1, max_value=100, value=10, step=1)
        grids_color = st.selectbox('Grids Color', options=['black', 'white'])

    st.divider()
    col5a, col5b, col5c = st.columns(3, gap='small')
    if engine_type == "**Plotly**":
        with col5a:
            # Option for 3D visualization
            view_3d = st.toggle('Enable 3D Visualization')

    with col5b:
        plot_button = st.form_submit_button('Plot', type='primary', use_container_width=True)

if plot_button:
    if uploaded_file is not None:
        if x_column_num and y_column_num and z_column_num != 0:
            # Extract X, Y, Z columns from the DataFrame
            x = dataset.iloc[:, x_column_num - 2].tolist()
            y = dataset.iloc[:, y_column_num - 2].tolist()
            z = dataset.iloc[:, z_column_num - 2].tolist()

            # z_rounded_list = []
            # # print(z)
            # for values in z:
            #     z_rounded_values = round(values, 3)
            #     z_rounded_list.append(z_rounded_values)
            # Create a regular grid for interpolation
            xi = np.linspace(min(x), max(x), 100)
            yi = np.linspace(min(y), max(y), 100)
            XI, YI = np.meshgrid(xi, yi)

            # Interpolate the data onto the regular grid
            ZI = griddata((x, y), z, (XI, YI), method=contour_type_dict[contour_type])

            # Show the maximum and minimum elevations
            st.write("\n")
            col6, col7 = st.columns(2, gap='small')

            with col6:
                st.metric('Minimum Elevation', value=round(min(z), 3))
            with col7:
                st.metric('Maximum Elevation', value=round(max(z), 3))

            if engine_type == "**Plotly**":
                # Display 2D plotly graph
                create_plotly_contourfig()

                if view_3d:
                    create_3d_plotly_contourfig()
            else:
                create_matplotlib_contourfig_plotting()
                saving_form()
        else:
            st.warning('Please enter appropriate column no values')
    else:
        st.error('Please upload file first!')