from dash import Dash, html, Input, Output
import requests


app = Dash("__name__")
server = app.server


app.layout = html.Div(
    [
        html.Div(
            [
                html.H3(id="selected_title"),
                html.A(id="selected_link"),
            ]
        ),
        html.Div(
            [html.Button(id="update_button", children="ニュース更新ボタン", n_clicks=1)],
            style={"padding": 30},
        ),
    ],
    style={"textAlign": "center"},
)


@app.callback(
    Output("selected_title", "children"),
    Output("selected_link", "href"),
    Output("selected_link", "children"),
    Input("update_button", "n_clicks"),
)
def update_news(n_clicks):
    if n_clicks > 0:
        r = requests.get("https://nhk-hackathon.herokuapp.com/random_news")
        news_title = r.json()["news_title"]
        news_url = r.json()["news_url"]
        return news_title, news_url, news_url
    else:
        pass


if __name__ == "__main__":
    app.run_server(debug=True)
