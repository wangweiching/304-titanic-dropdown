######### Import your libraries #######
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly as py
import plotly.graph_objs as go


###### Define your variables #####
tabtitle = 'Avocados sold by region!'
sourceurl = 'https://www.kaggle.com/code/mohamedharris/visualizing-avocado-data-using-seaborn/notebook'
githublink = 'https://github.com/wangweiching/304-titanic-dropdown'

###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/chainhaus/pythoncourse/master/avocado.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
new_cols = {'4046' : 'Small Haas', '4225' : 'Large Haas', '4770' : 'XLarge Haas'}
df.rename(columns = new_cols, inplace = True)
for i in ['Total Volume', 'Small Haas', 'Large Haas','XLarge Haas', 'Total Bags']:
    df[i] = df[i].astype('int64')
variables_list=['Small Haas', 'Large Haas', 'XLarge Haas', 'Total Volume']

# print(df.info())
# print(df.head())

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a continuous variable for summary statistics:'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in variables_list],
        value=variables_list[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
])


######### Interactive callbacks go here #########
@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])
def display_value(continuous_var):
    grouped_mean=df.groupby(['type', 'region'])[continuous_var].mean()
    results=pd.DataFrame(grouped_mean)
    if continuous_var == 'Small Haas':
        mydata = go.Figure(data=[go.Pie(labels=results.loc['conventional'].index.tolist(), values=results.loc['conventional'][continuous_var].values.tolist())])
        mydata.update_traces(textposition="inside")
        mydata.update_layout(
            uniformtext_minsize=14, uniformtext_mode="hide", title="Conventional Avocado sold by region"
        )
    if continuous_var == 'Large Haas':
        mydata = go.Figure(data=[go.Pie(labels=results.loc['conventional'].index.tolist(), values=results.loc['conventional'][continuous_var].values.tolist())])
        mydata.update_traces(textposition="inside")
        mydata.update_layout(
            uniformtext_minsize=14, uniformtext_mode="hide", title="Conventional Avocado sold by region"
        )
    if continuous_var == 'XLarge Haas':
        mydata = go.Figure(data=[go.Pie(labels=results.loc['conventional'].index.tolist(), values=results.loc['conventional'][continuous_var].values.tolist())])
        mydata.update_traces(textposition="inside")
        mydata.update_layout(
            uniformtext_minsize=14, uniformtext_mode="hide", title="Conventional Avocado sold by region"
        )
    if continuous_var == 'Total Volume':
        mydata = go.Figure(data=[go.Pie(labels=results.loc['conventional'].index.tolist(),
                                        values=results.loc['conventional'][continuous_var].values.tolist())])
        mydata.update_traces(textposition="inside")
        mydata.update_layout(
            uniformtext_minsize=14, uniformtext_mode="hide", title="Conventional Avocado sold by region"
        )
    return mydata

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
