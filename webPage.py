import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

# Install libraries before running program
# pip install flask  -- idk if you actually need it tho
# pip install dash
# pip install pandas
# pip install dash-bootstrap-components
# pip install plotly-express

# used link below to develop a base for the application
# https://dash-bootstrap-components.opensource.faculty.ai/examples/

# using one of the preset bootstrap themes - LUX
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

# the style arguments for the sidebar. 
# position:fixed - ensures that side bar stays on the page even when main page is scrolled
# currently using fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#91d5e6",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#sidebar option links
sidebar = html.Div(
    [
        html.H2("Menu", className="display-5"),
        html.Hr(style={'border-top': '3px solid black'}),
        html.P(
            "My Pool Monitor System", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("History", href="/history", active="exact"),
                dbc.NavLink("Recommendations", href="/recs", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

# separates the 3 components of the website into a div container
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# whenever the pathname of the URL changes, and it will update the children of the "page-content" component based on the new URL path
# TLDR: changes content of page based on sidebar navigation
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])

#determines which content page to display based on menu selection
def render_page_content(pathname):
    if pathname == "/":
        return [html.H3("Dashboard", className="display-3"),
            html.P("Your Test Results")]
    elif pathname == "/history":
        return [html.H4("History", className="display-3"), 
            html.P("This page displays past readings.")]
    elif pathname == "/recs":
        return [html.H5("Recommendations", className="display-3"), 
            html.P("This page gives the user tips on how to help increase pool quality.")]
    elif pathname == "/about":
        return [html.H6("About", className="display-3"),
        html.P("This page explains some background on the technology and any other relevant information.")]
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888)