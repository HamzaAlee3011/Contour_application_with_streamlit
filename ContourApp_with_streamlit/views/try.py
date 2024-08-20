# # def create_matplotlib_contourfig():
# #     fig, ax = plt.subplots()
# #
# #     # Specify custom contour levels
# #     contourf_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
# #
# #     # Check if the user wants filled contours
# #     if color_select == 'None':
# #         # Create regular contour plot
# #         CS = ax.contour(XI, YI, ZI, levels=contourf_levels, colors='black')
# #         ax.clabel(CS, inline=True, fontsize=label_size, fmt='%1.1f')
# #
# #     else:
# #         # Create filled contour plot with custom levels and a colormap
# #         contourf = ax.contourf(XI, YI, ZI, levels=contourf_levels, cmap=color_scales_dict[color_select])
# #         fig.colorbar(contourf, ax=ax, label='Elevations')
# #
# #     # Adding grid lines based on user input
# #     if show_grids_sb == 'Show':
# #         ax.set_xticks(np.arange(min(x), max(x), grid_size_button))
# #         ax.set_yticks(np.arange(min(y), max(y), grid_size_button))
# #         ax.grid(True, which='both', color=grid_color_dict[grids_color], linestyle='-', linewidth=0.8)
# #
# #     # Setting aspect ratio if equal
# #     if aspect_ratio == 'equal':
# #         ax.set_aspect('equal')
# #
# #     # Display the plot
# #     st.pyplot(fig)
# #     # # Save the plot to a buffer
# #     # buffer = io.BytesIO()
# #     # fig.savefig(buffer, format='png')
# #     # buffer.seek(0)
# #     # st.pyplot(fig)
# #     #
# #     # # Download the plot as a PNG
# #     # st.download_button(
# #     #     label="Download Contour Plot",
# #     #     data=buffer,
# #     #     file_name="contour_plot.png",
# #     #     mime="image/png"
# #     # )
#
# def create_matplotlib_contourfig():
#     fig, ax = plt.subplots()
#
#     # Create contour levels based on user input
#     contour_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
#
#     # Create contour plot with custom contour levels and set linecolor to black
#     contour_lines = ax.contour(XI, YI, ZI, levels=contour_levels,
#                                colors='black')  # Store the contour object for labeling
#
#     # Label the contour lines using the stored object
#     ax.clabel(contour_lines, fmt='%1.2f', inline=True, fontsize=label_size, colors='black')
#
#     # Set major tick locations for both x and y axes
#     ax.set_xticks(np.arange(min(x), max(x) + grid_size_button, grid_size_button))
#     ax.set_yticks(np.arange(min(y), max(y) + grid_size_button, grid_size_button))
#
#     if color_select != 'None':
#         # Specify custom contour levels for filled contours
#         contourf_levels = np.arange(min(z), max(z) + contour_interval, contour_interval)
#         # Create filled contours with custom levels and a colormap
#         contourf = ax.contourf(XI, YI, ZI, levels=contourf_levels, cmap=color_scales_dict[color_select])
#         fig.colorbar(contourf, ax=ax, label='Elevations')
#
#     if show_grids_sb == 'Show':
#         # Show or hide the grids based on the state of the show_grids_var
#         ax.grid(True, linestyle='-', linewidth=0.8),
#                 color=grid_color_dict[grids_color])
#
#     # Ensure the aspect ratio is equal for square grid cells
#     ax.set_aspect('equal', adjustable='box')
#     # Display the plot
#         st.pyplot(fig)