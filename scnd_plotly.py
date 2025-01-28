import pandas as pd
import plotly.graph_objects as go

# Load the actual dataset from a CSV file (replace with your file path or URL)
url = 'https://data.cityofnewyork.us/api/views/vx8i-nprf/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

# Filter the data to include only scores between 65.0 and 127.27
df_filtered = df[(df['Adj. FA'] >= 65.0) & (df['Adj. FA'] <= 127.27)]

# Convert 'Established Date' to datetime
df_filtered['Established Date'] = pd.to_datetime(df_filtered['Established Date'])

# Extract year and month
df_filtered['Year'] = df_filtered['Established Date'].dt.year
df_filtered['Month'] = df_filtered['Established Date'].dt.to_period('M').dt.to_timestamp('M')

# Create a list of unique exam titles
exam_titles = df_filtered['List Title Desc'].unique()


# Function to assign colors based on 'Adj. FA' score
def get_color(score):
    if score < 90:
        return 'orange'
    elif 90 <= score <= 110:
        return 'yellow'
    elif 110 < score <= 120:
        return 'green'
    return 'gray'


# Initialize color column
df_filtered['color'] = df_filtered['Adj. FA'].apply(get_color)


# Function to create bar chart for given sorting (monthly or yearly) and exam title
def create_bar_chart(sort_by, title):
    if sort_by == 'Monthly':
        sorted_df = df_filtered[df_filtered['List Title Desc'] == title].sort_values('Month')
        x_values = sorted_df['Month']
    else:  # Yearly
        sorted_df = df_filtered[df_filtered['List Title Desc'] == title].sort_values('Year')
        x_values = sorted_df['Year']

    # Create bar chart
    return go.Bar(
        x=x_values,
        y=sorted_df['Adj. FA'],
        marker_color=sorted_df['color'],
        name=title
    )


# Initial bar chart (monthly, first exam title)
initial_title = exam_titles[0]
initial_sort = 'Monthly'
bar_chart = create_bar_chart(initial_sort, initial_title)

# Create figure
fig = go.Figure(data=[bar_chart])

# Add layout and dropdown menus
fig.update_layout(
    title=f"Average Scores for {initial_title} ({initial_sort})",
    xaxis_title="Date",
    yaxis_title="Adjusted Final Average (Adj. FA)",
    updatemenus=[
        # Dropdown for sorting by monthly or yearly
        {
            'buttons': [
                {
                    'label': 'Monthly',
                    'method': 'update',
                    'args': [
                        {'x': [
                            df_filtered[df_filtered['List Title Desc'] == initial_title].sort_values('Month')['Month']],
                         'y': [df_filtered[df_filtered['List Title Desc'] == initial_title].sort_values('Month')[
                                   'Adj. FA']],
                         'marker': [{'color': df_filtered[df_filtered['List Title Desc'] == initial_title].sort_values(
                             'Month')['color']}]},
                        {'title': f'Average Scores for {initial_title} (Monthly)'}
                    ]
                },
                {
                    'label': 'Yearly',
                    'method': 'update',
                    'args': [
                        {'x': [
                            df_filtered[df_filtered['List Title Desc'] == initial_title].sort_values('Year')['Year']],
                         'y': [df_filtered[df_filtered['List Title Desc'] == initial_title].sort_values('Year')[
                                   'Adj. FA']],
                         'marker': [{'color': df_filtered[df_filtered['List Title Desc'] == initial_title].sort_values(
                             'Year')['color']}]},
                        {'title': f'Average Scores for {initial_title} (Yearly)'}
                    ]
                }
            ],
            'direction': 'down',
            'showactive': True,
            'x': 0.17,
            'xanchor': 'left',
            'y': 1.15,
            'yanchor': 'top'
        },
        # Dropdown for selecting exam title
        {
            'buttons': [
                {
                    'label': title,
                    'method': 'update',
                    'args': [
                        {'x': [df_filtered[df_filtered['List Title Desc'] == title].sort_values('Month')['Month']],
                         'y': [df_filtered[df_filtered['List Title Desc'] == title].sort_values('Month')['Adj. FA']],
                         'marker': [{'color': df_filtered[df_filtered['List Title Desc'] == title].sort_values('Month')[
                             'color']}]},
                        {'title': f'Average Scores for {title} (Monthly)'}
                    ]
                } for title in exam_titles
            ],
            'direction': 'down',
            'showactive': True,
            'x': 0.01,
            'xanchor': 'left',
            'y': 1.15,
            'yanchor': 'top'
        }
    ]
)

# Show the figure
fig.show()

# # Load the actual dataset from a CSV file (replace the URL with the path to your dataset)
# url = 'https://data.cityofnewyork.us/api/views/vx8i-nprf/rows.csv?accessType=DOWNLOAD'
# df = pd.read_csv(url)
#
# # Filter the data to include only scores between 65.0 and 127.27
# df_filtered = df[(df['Adj. FA'] >= 65.0) & (df['Adj. FA'] <= 127.27)]
#
# # Create a list of unique exam titles
# exam_titles = df_filtered['List Title Desc'].unique()
#
# # Create a list of dropdown options for the exam titles
# dropdown_options = [{'label': title, 'value': title} for title in exam_titles]
#
# # Initial chart setup: Bar chart for the first exam title
# initial_title = exam_titles[0]  # Use the first exam title as default
# df_initial = df_filtered[df_filtered['List Title Desc'] == initial_title]
#
# # Create the initial bar chart
# fig = go.Figure(data=[
#     go.Bar(x=df_initial['Established Date'], y=df_initial['Adj. FA'], name=initial_title)
# ])
#
# # Update layout with appropriate titles and labels
# fig.update_layout(
#     title=f"Average Scores for {initial_title}",
#     xaxis_title="Established Date",
#     yaxis_title="Adjusted Final Average (Adj. FA)",
#     updatemenus=[
#         {
#             'buttons': [
#                 {
#                     'label': title,
#                     'method': 'update',
#                     'args': [
#                         {'y': [df_filtered[df_filtered['List Title Desc'] == title]['Adj. FA']],
#                          'x': [df_filtered[df_filtered['List Title Desc'] == title]['Established Date']]},
#                         {'title': f'Average Scores for {title}'}
#                     ]
#                 } for title in exam_titles
#             ],
#             'direction': 'down',
#             'showactive': True
#         }
#     ]
# )
#
# # Show the chart
# fig.show()
