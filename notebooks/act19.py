import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# DATAFRAMES PARA GRAFICAR
df = pd.read_csv('../data/DataVentas.csv')

df20=df[df['Year']==2020]
df21=df[df['Year']==2021]
df22=df[df['Year']==2022]
####
df20zn=df20[df20['Zona']=='Norte']
df21zn=df21[df21['Zona']=='Norte']
df22zn=df22[df22['Zona']=='Norte']

df20znS=df20zn.groupby('Sucursal').sum()['Venta'].reset_index()
df21znS=df21zn.groupby('Sucursal').sum()['Venta'].reset_index()
df22znS=df22zn.groupby('Sucursal').sum()['Venta'].reset_index()
####
df20zc=df20[df20['Zona']=='Centro']
df21zc=df21[df21['Zona']=='Centro']
df22zc=df22[df22['Zona']=='Centro']

df20zcS=df20zc.groupby('Sucursal').sum()['Venta'].reset_index()
df21zcS=df21zc.groupby('Sucursal').sum()['Venta'].reset_index()
df22zcS=df22zc.groupby('Sucursal').sum()['Venta'].reset_index()
####
df20zg=df20[df20['Zona']=='Golfo']
df21zg=df21[df21['Zona']=='Golfo']
df22zg=df22[df22['Zona']=='Golfo']

df20zgS=df20zg.groupby('Sucursal').sum()['Venta'].reset_index()
df21zgS=df21zg.groupby('Sucursal').sum()['Venta'].reset_index()
df22zgS=df22zg.groupby('Sucursal').sum()['Venta'].reset_index()
####
df20zs=df20[df20['Zona']=='Sur']
df21zs=df21[df21['Zona']=='Sur']
df22zs=df22[df22['Zona']=='Sur']

df20zsS=df20zs.groupby('Sucursal').sum()['Venta'].reset_index()
df21zsS=df21zs.groupby('Sucursal').sum()['Venta'].reset_index()
df22zsS=df22zs.groupby('Sucursal').sum()['Venta'].reset_index()
####

### GRAFICA EXTERNA A CALLBACK
def grafica1 (dfAux1):
    gAux1=px.sunburst(data_frame=dfAux1,
                      path=['Sucursal', 'Mes'],
                      values='Venta', color='Venta')
    gAux1.update_traces(marker=dict(line=dict(color='purple',width=1)))
    gAux1.update_layout(title="Zona y sucursal",
                        font=dict(family="Courier New, monospace",
                                  size=14, color="RebeccaPurple"
                                  ),height=700
                        )
    return gAux1

def grafica2 (dfAux2):
    gAux2=px.bar(data_frame=dfAux2, x='Mes', y='Venta', color='Mes')
    gAux2.update_layout(title="Sucursal por Mes",
                        xaxis_title="Mes",
                        yaxis_title='Ventas',
                        font=dict(family="Courier New, monospace",
                                  size=14,
                                  color="RebeccaPurple"
                                  ),height=350
                        )
    return gAux2

def grafica3 (dfAux3):
    gAux3=px.line(data_frame=dfAux3, x='Mes', y='Venta',
                  markers=True)
    gAux3.update_traces(line=dict(dash="dot", width=4, color="red"),
                        marker=dict(color="darkblue", size=6, opacity=0.8),
                        )
    gAux3.update_layout(title="Sucursal por mes",
                        font=dict(family="Courier New, monospace",
                                  size=14, color="RebeccaPurple"
                                  ),height=350
                        )
    return gAux3

# CREAR APLICACIÓN
# app = dash.Dash(__name__)
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# CREAR CONTENEDOR PRINCIPAL
app.layout = dbc.Container([

    # Renglón1 encabezado
    dbc.Row(
        dbc.Col(html.H2("TABLERO DE VISUALIZACIÓN DE VENTAS ANUALES",
                        className='text-center mb-0'),
                width={'size':12, 'offset':0, 'order':1},
                ),className='bg-light py-3 mb-4',
    ),
    # Renglón1

    # Renglón 2 Visualizar gráficos
dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            dbc.Label("Año", className='fw-bold mb-1 '),
                            dcc.Dropdown(id='slct_Year',
                                            options=[{'label': x, 'value': x}
                                                    for x in sorted(df['Year'].unique())
                                                    ],
                                            value=2020,
                                            multi=False,
                                            className='mb-3',
                                            style={'text-align': 'left', 'color': 'black'}
                                            ),

                            dbc.Label("Zona", className='fw-bold mb-1 '),
                            dcc.Dropdown(id='slct_Zona',
                                            options=[{'label': x, 'value': x}
                                                    for x in sorted(df['Zona'].unique())
                                                    ],
                                            value='Norte',
                                            multi=False,
                                            style={'text-align': 'left', 'color': 'black'}
                                            ),
                        ]
                    ),
                    className='shadow-sm border-start border-4',
                ),
                width={'size': 2, 'offset': 0, 'order': 1},
            ),

            dbc.Col(dcc.Graph(id='glsb'),
                    width={'size': 5, 'offset': 0, 'order': 2},
                    ),

            dbc.Col(
                [
                    dbc.Row(
                        dbc.Col(
                            [
                                dcc.Dropdown(id='Drop1Suc', multi=False, value='Matamoros',
                                             options=[{'label': x, 'value': x}
                                                      for x in sorted(df['Sucursal'].unique())
                                                      ],
                                             className='mb-2',
                                             ),
                                dcc.Graph(id='g2bar'),
                            ], width={'size': 12, 'offset': 0},
                        ),
                    ),
                    dbc.Row(
                        dbc.Col(
                            [
                                dcc.Dropdown(id='Drop2Suc', multi=False, value='Matamoros',
                                             options=[{'label': x, 'value': x}
                                                      for x in sorted(df['Sucursal'].unique())
                                                      ],
                                             className='mb-2',
                                             ),
                                dcc.Graph(id='g3line'),
                            ], width={'size': 12, 'offset': 0},
                        )
                    ),
                ], width={'size': 5, 'offset': 0, 'order': 3},
            )
        ], className='g-3'
    )
], fluid=True)
# cierra layout

# FLUID: elimina los margenes laterales

# FUNCIÓN DE CALLBACK

@app.callback(
    [Output(component_id = 'glsb', component_property='figure'),
     Output(component_id = 'g2bar', component_property='figure'),
     Output(component_id = 'g3line', component_property='figure'),
    ],
    [Input(component_id ='slct_Year', component_property='value'),
     Input(component_id ='slct_Zona', component_property='value'),
     Input(component_id ='Drop1Suc', component_property='value'),
     Input(component_id ='Drop2Suc', component_property='value'),
    ]
)

def graficos(SYear, SZona, SSuc1, SSuc2):
    if (SZona == 'Norte'):
        if (SYear == 2020):
            if (SSuc1 =='Matamoros'):dff1=df20zn[df20zn['Sucursal']=='Matamoros']
            elif (SSuc1 =='Reynosa'):dff1=df20zn[df20zn['Sucursal']=='Reynosa']
            elif (SSuc1 =='Nuevo Laredo'):dff1=df20zn[df20zn['Sucursal']=='Nuevo Laredo']

            if (SSuc2=='Matamoros'):dff2=df20zn[df20zn['Sucursal']=='Matamoros']
            elif (SSuc2=='Reynosa'):dff2=df20zn[df20zn['Sucursal']=='Reynosa']
            elif (SSuc2=='Nuevo Laredo'):dff2=df20zn[df20zn['Sucursal']=='Nuevo Laredo']

            g1=grafica1(df20zn)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2021):
            if (SSuc1 =='Matamoros'):dff1=df21zn[df21zn['Sucursal']=='Matamoros']
            elif (SSuc1 =='Reynosa'):dff1=df21zn[df21zn['Sucursal']=='Reynosa']
            elif (SSuc1 =='Nuevo Laredo'):dff1=df21zn[df21zn['Sucursal']=='Nuevo Laredo']

            if (SSuc2=='Matamoros'):dff2=df21zn[df21zn['Sucursal']=='Matamoros']
            elif (SSuc2=='Reynosa'):dff2=df21zn[df21zn['Sucursal']=='Reynosa']
            elif (SSuc2=='Nuevo Laredo'):dff2=df21zn[df21zn['Sucursal']=='Nuevo Laredo']

            g1=grafica1(df21zn)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2022):
            if (SSuc1 =='Matamoros'):dff1=df22zn[df22zn['Sucursal']=='Matamoros']
            elif (SSuc1 =='Reynosa'):dff1=df22zn[df22zn['Sucursal']=='Reynosa']
            elif (SSuc1 =='Nuevo Laredo'):dff1=df22zn[df22zn['Sucursal']=='Nuevo Laredo']

            if (SSuc2=='Matamoros'):dff2=df22zn[df22zn['Sucursal']=='Matamoros']
            elif (SSuc2=='Reynosa'):dff2=df22zn[df22zn['Sucursal']=='Reynosa']
            elif (SSuc2=='Nuevo Laredo'):dff2=df22zn[df22zn['Sucursal']=='Nuevo Laredo']

            g1=grafica1(df22zn)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

    ###
    if (SZona == 'Centro'):
        if (SYear == 2020):
            if (SSuc1 =='Mante'):dff1=df20zc[df20zc['Sucursal']=='Mante']
            elif (SSuc1 =='Victoria'):dff1=df20zc[df20zc['Sucursal']=='Victoria']

            if (SSuc2=='Mante'):dff2=df20zc[df20zc['Sucursal']=='Mante']
            elif (SSuc2=='Victoria'):dff2=df20zc[df20zc['Sucursal']=='Victoria']

            g1=grafica1(df20zc)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2021):
            if (SSuc1 =='Mante'):dff1=df21zc[df21zc['Sucursal']=='Mante']
            elif (SSuc1 =='Victoria'):dff1=df21zc[df21zc['Sucursal']=='Victoria']

            if (SSuc2=='Mante'):dff2=df21zc[df21zc['Sucursal']=='Mante']
            elif (SSuc2=='Victoria'):dff2=df21zc[df21zc['Sucursal']=='Victoria']

            g1=grafica1(df21zc)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2022):
            if (SSuc1 =='Mante'):dff1=df22zc[df22zc['Sucursal']=='Mante']
            elif (SSuc1 =='Victoria'):dff1=df22zc[df22zc['Sucursal']=='Victoria']

            if (SSuc2=='Mante'):dff2=df22zc[df22zc['Sucursal']=='Mante']
            elif (SSuc2=='Victoria'):dff2=df22zc[df22zc['Sucursal']=='Victoria']

            g1=grafica1(df22zc)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

    ###
    if (SZona == 'Golfo'):
        if (SYear == 2020):
            if (SSuc1 =='Madero'):dff1=df20zg[df20zg['Sucursal']=='Madero']
            elif (SSuc1 =='Tampico'):dff1=df20zg[df20zg['Sucursal']=='Tampico']
            elif (SSuc1 =='Altamira'):dff1=df20zg[df20zg['Sucursal']=='Altamira']
            elif (SSuc1 =='Tuxpan'):dff1=df20zg[df20zg['Sucursal']=='Tuxpan']
            elif (SSuc1 =='Poza Rica'):dff1=df20zg[df20zg['Sucursal']=='Poza Rica']

            if (SSuc2=='Madero'):dff2=df20zg[df20zg['Sucursal']=='Madero']
            elif (SSuc2=='Tampico'):dff2=df20zg[df20zg['Sucursal']=='Tampico']
            elif (SSuc2=='Altamira'):dff2=df20zg[df20zg['Sucursal']=='Altamira']
            elif (SSuc2=='Tuxpan'):dff2=df20zg[df20zg['Sucursal']=='Tuxpan']
            elif (SSuc2=='Poza Rica'):dff2=df20zg[df20zg['Sucursal']=='Poza Rica']

            g1=grafica1(df20zg)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2021):
            if (SSuc1 =='Madero'):dff1=df21zg[df21zg['Sucursal']=='Madero']
            elif (SSuc1 =='Tampico'):dff1=df21zg[df21zg['Sucursal']=='Tampico']
            elif (SSuc1 =='Altamira'):dff1=df21zg[df21zg['Sucursal']=='Altamira']
            elif (SSuc1 =='Tuxpan'):dff1=df21zg[df21zg['Sucursal']=='Tuxpan']
            elif (SSuc1 =='Poza Rica'):dff1=df21zg[df21zg['Sucursal']=='Poza Rica']

            if (SSuc2=='Madero'):dff2=df21zg[df21zg['Sucursal']=='Madero']
            elif (SSuc2=='Tampico'):dff2=df21zg[df21zg['Sucursal']=='Tampico']
            elif (SSuc2=='Altamira'):dff2=df21zg[df21zg['Sucursal']=='Altamira']
            elif (SSuc2=='Tuxpan'):dff2=df21zg[df21zg['Sucursal']=='Tuxpan']
            elif (SSuc2=='Poza Rica'):dff2=df21zg[df21zg['Sucursal']=='Poza Rica']

            g1=grafica1(df21zg)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2022):
            if (SSuc1 =='Madero'):dff1=df22zg[df22zg['Sucursal']=='Madero']
            elif (SSuc1 =='Tampico'):dff1=df22zg[df22zg['Sucursal']=='Tampico']
            elif (SSuc1 =='Altamira'):dff1=df22zg[df22zg['Sucursal']=='Altamira']
            elif (SSuc1 =='Tuxpan'):dff1=df22zg[df22zg['Sucursal']=='Tuxpan']
            elif (SSuc1 =='Poza Rica'):dff1=df22zg[df22zg['Sucursal']=='Poza Rica']

            if (SSuc2=='Madero'):dff2=df22zg[df22zg['Sucursal']=='Madero']
            elif (SSuc2=='Tampico'):dff2=df22zg[df22zg['Sucursal']=='Tampico']
            elif (SSuc2=='Altamira'):dff2=df22zg[df22zg['Sucursal']=='Altamira']
            elif (SSuc2=='Tuxpan'):dff2=df22zg[df22zg['Sucursal']=='Tuxpan']
            elif (SSuc2=='Poza Rica'):dff2=df22zg[df22zg['Sucursal']=='Poza Rica']

            g1=grafica1(df22zg)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

    ###
    if (SZona == 'Sur'):
        if (SYear == 2020):
            if (SSuc1 =='VeracruzPuerto'):dff1=df20zs[df20zs['Sucursal']=='VeracruzPuerto']
            elif (SSuc1 =='Coatzacoalcos'):dff1=df20zs[df20zs['Sucursal']=='Coatzacoalcos']
            elif (SSuc1 =='Minatitlan'):dff1=df20zs[df20zs['Sucursal']=='Minatitlan']
            elif (SSuc1 =='Jalapa'):dff1=df20zs[df20zs['Sucursal']=='Jalapa']

            if (SSuc2=='VeracruzPuerto'):dff2=df20zs[df20zs['Sucursal']=='VeracruzPuerto']
            elif (SSuc2=='Coatzacoalcos'):dff2=df20zs[df20zs['Sucursal']=='Coatzacoalcos']
            elif (SSuc2=='Minatitlan'):dff2=df20zs[df20zs['Sucursal']=='Minatitlan']
            elif (SSuc2=='Jalapa'):dff2=df20zs[df20zs['Sucursal']=='Jalapa']

            g1=grafica1(df20zs)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2021):
            if (SSuc1 =='VeracruzPuerto'):dff1=df21zs[df21zs['Sucursal']=='VeracruzPuerto']
            elif (SSuc1 =='Coatzacoalcos'):dff1=df21zs[df21zs['Sucursal']=='Coatzacoalcos']
            elif (SSuc1 =='Minatitlan'):dff1=df21zs[df21zs['Sucursal']=='Minatitlan']
            elif (SSuc1 =='Jalapa'):dff1=df21zs[df21zs['Sucursal']=='Jalapa']

            if (SSuc2=='VeracruzPuerto'):dff2=df21zs[df21zs['Sucursal']=='VeracruzPuerto']
            elif (SSuc2=='Coatzacoalcos'):dff2=df21zs[df21zs['Sucursal']=='Coatzacoalcos']
            elif (SSuc2=='Minatitlan'):dff2=df21zs[df21zs['Sucursal']=='Minatitlan']
            elif (SSuc2=='Jalapa'):dff2=df21zs[df21zs['Sucursal']=='Jalapa']

            g1=grafica1(df21zs)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

        if (SYear == 2022):
            if (SSuc1 =='VeracruzPuerto'):dff1=df22zs[df22zs['Sucursal']=='VeracruzPuerto']
            elif (SSuc1 =='Coatzacoalcos'):dff1=df22zs[df22zs['Sucursal']=='Coatzacoalcos']
            elif (SSuc1 =='Minatitlan'):dff1=df22zs[df22zs['Sucursal']=='Minatitlan']
            elif (SSuc1 =='Jalapa'):dff1=df22zs[df22zs['Sucursal']=='Jalapa']

            if (SSuc2=='VeracruzPuerto'):dff2=df22zs[df22zs['Sucursal']=='VeracruzPuerto']
            elif (SSuc2=='Coatzacoalcos'):dff2=df22zs[df22zs['Sucursal']=='Coatzacoalcos']
            elif (SSuc2=='Minatitlan'):dff2=df22zs[df22zs['Sucursal']=='Minatitlan']
            elif (SSuc2=='Jalapa'):dff2=df22zs[df22zs['Sucursal']=='Jalapa']

            g1=grafica1(df22zs)
            g2=grafica2(dff1)
            g3=grafica3(dff2)

    return g1,g2,g3

# inicializar el servidor
if __name__ == "__main__":
    app.run(debug=True, port=8050, jupyter_mode='inline')

#port = 8888
#port = 8050


# CONCLUSION 
# Entre 2020 y 2022 la empresa se fue recuperando poco a poco despues del golpe que sufrio en 2020 (posiblemente por la pandemia), y para 2022 ya estaba vendiendo bastante mas que al inicio, casi 90 millones de pesos mas. La zona Sur fue la que mas aporto durante todo el periodo, seguida de cerca por Golfo, mientras que Norte se mantuvo en un nivel medio. Centro fue la zona mas debil, aunque esto tiene sentido porque solo cuenta con dos sucursales (Mante y Victoria) contra las 4 o 5 que tienen las demas zonas. A nivel de sucursales, VeracruzPuerto se destaco como la de mejor desempeño, mientras que Mante quedo en el ultimo lugar. En general se ve una tendencia clara de recuperacion: un año dificil, seguido de dos años de crecimiento constante, con Sur y Golfo como las zonas que sostienen la mayor parte de las ventas.
