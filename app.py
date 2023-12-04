import dash
from dash import dcc, html

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.Header(
        children=[
            html.H1("Business Presentation", style={'color': '#fff', 'textAlign': 'center', 'padding': '1em', 'background-color': '#007BFF'})
        ]
    ),

    html.Section(
        children=[
            html.H2("Welcome", style={'color': '#333'}),
            html.P("Welcome to our business presentation. We are excited to share our story with you.", style={'color': '#666'}),
        ],
        style={'margin': '2em', 'padding': '2em', 'background-color': '#fff', 'border-radius': '8px', 'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'}
    ),

    html.Section(
        children=[
            html.H2("Our Vision", style={'color': '#333'}),
            html.P("Our vision is to transform the industry by delivering innovative solutions.", style={'color': '#666'}),
        ],
        style={'margin': '2em', 'padding': '2em', 'background-color': '#fff', 'border-radius': '8px', 'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'}
    ),

    html.Section(
        children=[
            html.H2("Key Achievements", style={'color': '#333'}),
            html.P("We are proud of our achievements, including:", style={'color': '#666'}),
            html.Ul([
                html.Li("Increased market share by 20%"),
                html.Li("Launched successful product X"),
                html.Li("Received industry recognition"),
            ]),
        ],
        style={'margin': '2em', 'padding': '2em', 'background-color': '#fff', 'border-radius': '8px', 'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'}
    ),

    html.Section(
        children=[
            html.H2("Our Team", style={'color': '#333'}),
            html.P("We have a dedicated team of professionals committed to excellence.", style={'color': '#666'}),
        ],
        style={'margin': '2em', 'padding': '2em', 'background-color': '#fff', 'border-radius': '8px', 'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'}
    ),

    html.Section(
        children=[
            html.H2("Contact Us", style={'color': '#333'}),
            html.P("If you have any questions or would like to discuss opportunities, please contact us.", style={'color': '#666'}),
            dcc.Link("Contact Us", href="#", className="cta-button"),
        ],
        style={'margin': '2em', 'padding': '2em', 'background-color': '#fff', 'border-radius': '8px', 'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'}
    ),

    html.Section(
        children=[
            html.H2("Image", style={'color': '#333'}),
            html.Div([
                html.Img(src='https://via.placeholder.com/800x400', alt='Business Presentation', style={'max-width': '100%', 'height': 'auto', 'border-radius': '8px'}),
            ], style={'text-align': 'center'}),
        ],
        style={'margin': '2em', 'padding': '2em', 'background-color': '#fff', 'border-radius': '8px', 'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'}
    ),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
