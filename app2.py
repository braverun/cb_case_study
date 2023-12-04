import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('C:\\Users\\Gabi\\Downloads\\threek_outcome.csv')

# Use the Bootstrap theme
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# First set of data
data1 = [['Original Sales', 2328281],
         ['Original Revenue', 1257281],
         ['Our Sales', 3284551],
         ['Our Revenue', 2012813]]

# Second set of data
data2 = [['Our cost', 48000],
         ['Final Revenue', 707532]]

# Create DataFrames
df1 = pd.DataFrame(data1, columns=['Metrics', 'Value'])
df2 = pd.DataFrame(data2, columns=['Metrics', 'Value'])

# Define the layout for the first page
page_1_layout = html.Div(style={'textAlign': 'center', 'margin': 'auto'}, children=[
    html.H1(children='Assignment'),
    html.Br(),
    html.H5(children='- Historical performance from the first round of the investment campaign'),
    html.H5(children='- In the second round, clients were offered a cash-back bonus of 1,000 CZK'),
    html.H5(children='- To select 3,000 clients and consider the trade off'),
    html.Br(),  
    html.Br(),
    html.H3(children='Why employ us, you ask?'),

    # Bar chart for the first set of data
    dbc.Table.from_dataframe(df.sample(10), striped=True, bordered=True, hover=True, responsive=True),

])

# Define the layout for the second page
page_2_layout = html.Div(children=[
    html.H1(children='What we can do for you'),

    dcc.Graph(
        id='Non model vs Model',
        figure={
            'data': [
                {'x': df1['Metrics'], 'y': df1['Value'], 'type': 'bar', 'name': 'Metrics 1'},
            ],
            'layout': {
                'title': 'Non model vs Model',
                'xaxis': {'title': 'Metrics'},
                'yaxis': {'title': 'Value'},
            }
        }
    ),

    # Bar chart for the second set of data
    dcc.Graph(
        id='Your cost vs benefit',
        figure={
            'data': [
                {'x': df2['Metrics'], 'y': df2['Value'], 'type': 'bar', 'name': 'Metrics 2'},
            ],
            'layout': {
                'title': 'Your cost vs benefit',
                'xaxis': {'title': 'Metrics'},
                'yaxis': {'title': 'Value'},
            }
        }
    ),

])

# Define the layout for the second page
page_3_layout = html.Div(children=[
    html.H1(children='Metrics Visualization - EDA'),

dbc.Carousel(
    items=[
        {"key": "1", "src": "assets/output_1.png", "img_style": {"width":"90px","height":"550px"}},
        {"key": "2", "src": "assets/Screen Shot 2023-11-24 at 11.43.19.png"},
    ],
    className="carousel-fade",
),

dcc.Graph(
        id='balance-outcome-boxplot',
        figure={
            'data': [
                {
                    'x': df['poutcome'],
                    'y': df['average_balance'],
                    'mode': 'markers',
                    'type': 'box',
                    'marker': {'size': 10, 'opacity': 0.8}
                }
            ],
            'layout': {
                'title': 'Balance vs Outcome',
                'xaxis': {'title': 'Outcome'},
                'yaxis': {'title': 'Average Balance'},
                'hovermode': 'closest',
            }
        }
    )
])

# Define the layout for the second page
page_4_layout = html.Div(children=[
    html.H1(children='Metrics Visualization - Model Evaluation'),

dbc.Carousel(
    items=[
        {"key": "1", "src": "assets/output_modelevaluation.png", "img_style": {"width":"450px","height":"450px"}},
        {"key": "2", "src": "assets/Screen Shot 2023-11-23 at 16.35.42.png", "img_style": {"width":"450px","height":"450px"}},
    ],
    className="carousel-fade",
)
])

# Define the layout for the second page
page_5_layout = html.Div(style={'textAlign': 'center', 'margin': 'auto'}, children=[
    html.H1(children='Our Workflow'),

    # Add images using html.Img
    html.Img(src='assets/Screen Shot 2023-11-24 at 10.54.03.png', alt='Image 1', style={"width":"1000px","height":"450px", 'text-align': 'center'}),
])


# Define the layout for the second page
page_6_layout = html.Div(style={'textAlign': 'center', 'padding': 0, 'margin': 0, 'width': '60%', 'margin-left': 'auto', 'margin-right': 'auto', 'font-size': '20px'}, children=[
    html.H1(children='Our future promise'),
    html.H1(),
    html.Img(src='assets/VZvx.gif', style={'position': 'absolute', 'width': '100%', 'height': '100%', 'opacity': '0.2', 'left': '0', 'z-index': '-1'}),
    html.Li(children='We know the importance of cleaning and preparing data in order to produce viable results.'),
    html.Li(children='We know how to use pipelines and grid frameworks to select the best method for making predictions.'),
    html.Li(children='We know how to choose model and hyper parameters the successfully generate profit for our client.'),
    html.Li(children='From now one, we would continuously collect data and update the model with them, tuning it further in order to make the continuously improving predictions.'),
    html.Li(children='We would help with the embedding of the model within the company and tune the model and proceeedures accordingly.'),
    html.Li(children='We would periodically check on the performance and stay on call the first few months.'),
    html.Li(children='The cost vs revenues would continue differencing with time.'),
    html.Li(children='This course and case study have been invaluable in teaching us the ins and outs of data science and giving us a place to solidify what we’ve learned.')

])


# Set the initial layout
app.layout = html.Div(children=[
    dcc.Location(id='url'),
    html.Div(id='page-content'),
    html.Div([
        dcc.Link('Page 1', href='/page-one', style={'margin-right': '10px', 'font-weight': 'bold', 'color': '#007BFF', 'font-size': '18px'}),
        dcc.Link('Page 2', href='/page-two', style={'margin-right': '10px', 'font-weight': 'bold', 'color': '#007BFF', 'font-size': '18px'}),
        dcc.Link('Page 3', href='/page-three', style={'margin-right': '10px', 'font-weight': 'bold', 'color': '#007BFF', 'font-size': '18px'}),
        dcc.Link('Page 4', href='/page-four', style={'margin-right': '10px', 'font-weight': 'bold', 'color': '#007BFF', 'font-size': '18px'}),
        dcc.Link('Page 5', href='/page-five', style={'margin-right': '10px', 'font-weight': 'bold', 'color': '#007BFF', 'font-size': '18px'}),
        dcc.Link('Page 6', href='/page-six', style={'margin-right': '10px', 'font-weight': 'bold', 'color': '#007BFF', 'font-size': '18px'})
    ], style={'margin-top': '20px', 'text-align': 'center'})
], style={'margin': '20px'})

 # Define callback to switch between pages based on URL
@app.callback(Output('page-content', 'children'),
               [Input('url', 'pathname')])
def display_page(pathname):
     print(pathname)
     if pathname == '/page-one':
         return page_1_layout
     elif pathname == '/page-two':
         return page_2_layout
     elif pathname == '/page-three':
         return page_3_layout
     elif pathname == '/page-four':
         return page_4_layout
     elif pathname == '/page-five':
         return page_5_layout
     elif pathname == '/page-six':
         return page_6_layout
     else:
        return '404'

 # Run the app
if __name__ == '__main__':
   app.run_server(debug=True)
