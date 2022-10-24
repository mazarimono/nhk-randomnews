from dash import Dash, html, dcc 
import requests


app = Dash('__name__')
server = app.server

r= requests.get('https://nhk-hackathon.herokuapp.com/random_news')

app.layout = html.Div([
    html.H3(r.json()['news_title']),
    html.A(r.json()['news_url'], href=r.json()['news_url'])
])

if __name__ == "__main__":
    app.run_server(debug=True)