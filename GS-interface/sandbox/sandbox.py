if tab == 'eps-vbatt':
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['vbatt'].sTs,
                        'y': eps.params['vbatt'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    elif tab == "eps-c-obc":
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['C_obc'].sTs,
                        'y': eps.params['C_obc'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])


eps_persistent_data = html.Table([
    html.Tr([
        html.Td([
            "Battery Mode"
        ]),
        html.Td([
            str(eps.params["battmode"].Vals[-1])
        ])
    ], style={'border': '1px solid black'}),
    html.Tr([
        html.Td([
            "wdt_i2c"
        ]),
        html.Td([
            str(eps.params["wdt_i2c"].Vals[-1])
        ])
    ],style={'border': '1 black'}),

])
 

 def render_context_info(tab):

    if tab == 'eps-vbatt' :
        return "EPS"
    elif tab == 'eps-c-obc':
        return "c-OBC"


Tab 
      children=[
                    dcc.Tabs(id="tabs-eps", value='eps-vbatt', children=[
        
                        dcc.Tab(label='vbatt', value='eps-vbatt'),
                        dcc.Tab(label='c-obc', value='eps-c-obc'),
    
                    ]),
                ]


#Hidden div inside the app that stores the intermediate value
html.Div(id='main-tab-selection', style={'display': 'none'}),
    
@app.callback(Output('main-tab-selection', 'children'),
              [Input("main-tabs", 'value')])
def update_main_tab_selection(main_tab):
    return main_tab



def eps_context_fig(eps,tab):
    if tab == 'eps-vbatt':
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['vbatt'].sTs,
                        'y': eps.params['vbatt'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    elif tab == "eps-c-obc":
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['C_obc'].sTs,
                        'y': eps.params['C_obc'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    elif tab == "eps-c-radio":
        return html.Div(className="figure",children=[
            dcc.Graph(
                id='context-plot',
                figure={
                    'data': [{
                        #x=eps.params['vbatt'].sTs, 
                        #y=eps.params['vbatt'].Vals,
                        'x': eps.params['C_radio'].sTs,
                        'y': eps.params['C_radio'].Vals,
                        'type': 'scatter'
                    }]
                }
            )
        ])
    

    import gsclasses.Eps
import gsclasses.Param

import dash
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objs as go

import time
import datetime

from contextFigGen import *



def eps_context_fig(eps,tab):
    return gen_context_fig(eps, tab[4:] )   
 

def eps_context_info(eps,tab,main_tab=""):
    return html.Table([
        html.Tr([
            html.Td([
                "Battery Mode"
            ]),
            html.Td([
                str(eps.params["battmode"].Vals[-1])
            ])
        ], style={'border': '1px solid black'}),
        html.Tr([
            html.Td([
                "wdt_i2c"
            ]),
            html.Td([
                #str(eps.params["wdt_i2c"].Vals[-1])
                main_tab
            ])
        ],style={'border': '1 black'}),

    ])
 
    