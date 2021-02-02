import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

pd.set_option('display.max_columns', 333)
pd.set_option('display.width', 333)

colors = {'backgound': '#111111',
          'text': '#7FDBFF'}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(r'C:\Users\UCA035\Desktop\pythonProject\StudentsPerformance2.csv')

# print(df[0:5], '\n' * 2,
#       df.describe(), '\n' * 2,
#       df.info())

df_fig_1 = df.groupby('gender', as_index=False)['math score'].sum()

fig = px.bar(df_fig_1, y='gender', x='math score')

fig.update_layout(plot_bgcolor=colors['backgound'],
                  paper_bgcolor=colors['backgound'],
                  font_color=colors['text'])

app.layout = \
    html.Div(
        style={'backgroundColor': colors['backgound']},
        children=[
            html.H1(children='Hello Dash',
                    style={'textAlign': 'center',
                           'color': colors['text']}),
            html.Div(children='Dash: A web application framework for Python.',
                     style={'textAlign': 'center',
                            'color': colors['text']}),
            dcc.Graph(id='example-graph-2',
                      figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)
