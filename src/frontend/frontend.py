from cmath import nan
import dash
from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, dash_table, ctx
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import plotly.express as px
import plotly.graph_objects as go
import datetime as dt
import time
import pandas as pd 
import psycopg2
import psycopg2.extras
import sys
import os

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px',
    'fontWeight': 'bold',
}

tab_selected_style1 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#ff0018',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

tab_selected_style2 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#ffa52c',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

tab_selected_style3 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#ffff41',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

tab_selected_style4 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#008018',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

tab_selected_style5 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#0000f9',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

tab_selected_style6 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#86007d',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

tab_selected_style7 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#f6aab7',
    'color': 'white',
    'padding': '6px',
    'font-family':'Lucida Grande',
    'font-size': '15px'
}

header = {
    "font-family": "Lucida Grande",
    "font-size": "25px",
    'text-align':'center',
    "letter-spacing": "0.4px",
    "word-spacing": "2px",
    "color": "#ffffff",
    "font-weight": "700",
    "text-decoration": "none",
    "font-style": "normal",
    "font-variant": "small-caps",
    "text-transform": "none",
    'background': 'linear-gradient(to right, #FF0018 0%, #FFA52C 20%,#FFFF41 40%, #008018 60%, #0000F9 80%, #86007D 100%)'
}

searchBox = {
    'width': '99.3%',
    'margin-top':'10px',
    'background-color':'#dedede',
    'borderWidth': '1px',
    'borderStyle': 'solid',
    'borderRadius': '5px',
    'borderColor': '#dedede',
    'padding': '5px',
    'font-family':'Lucida Grande'
}

style_cell = {
    'text-align': 'left',
    'font-family': 'Lucida Grande',
    'font-size': '10px'
}

tbl_header_style = {
    'text-align': 'left',
    'font-family': 'Lucida Grande',
    'font-size': '12px',
    'font-weight': 'bold',
    'background-color': '#dedede',
}

data_saved_style = {
    'font-family':'Lucida Grande',
    'font-size':'14px',
    'text-align':'left',
}

saved_box_style = {
    'background-color':'#f5f5f5',
    'border-bottom':'2px solid #008018',
    'color':'#008018',
    'padding-top':'2px',
    'width':'50%',
    'padding-left':'10px',
    'height':'45px',
    'margin-top':'10px'
}

error_box_style = {
    'background-color':'#f5f5f5',
    'border-bottom':'2px solid #ff0018',
    'color':'#ff0018',
    'width':'50%',
    'padding-left':'10px',
    'margin-top':'10px'
}

button_style = {
    'background-color':'#F0F8FF',
    'border':'3px solid #FFFFFF',
    'padding':'10px',
    'width':'150px',
    'font-family':'Lucida Grande',
    'font-size':'10px',
    'color':'#00308F',
    'margin-top':'10px'
}
hostname = 'db'
#hostname = 'localhost'
database = 'rbike'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn= None
cur= None

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM customer')
    data = cur.fetchall()
    df_customer = pd.DataFrame(data=data, columns=['customer_id','first name','last name','sex', 'age', 'email'])
    #print(df_customer)

    cur.execute('SELECT * FROM bike')
    data = cur.fetchall()
    df_bike = pd.DataFrame(data=data, columns=['bike_id','brand','model', 'rent_fee_per_day','repair_status','order_id','repairshop_id','supplier_id'])
    #print(df_bike)

    cur.execute('SELECT * FROM order_in')
    data = cur.fetchall()
    df_order = pd.DataFrame(data=data, columns=['order_id','payment','customer_id','giftbox_id'])
    #print(df_order)

    cur.execute('SELECT * FROM employee')
    data = cur.fetchall()
    df_employee = pd.DataFrame(data=data,columns=['employee_id','first_name','last_name','sex', 'age','e-mail', 'income_per_year','department_id'])
    #print(df_employee)

    cur.execute('SELECT * FROM supplier')
    data = cur.fetchall()
    df_supplier = pd.DataFrame(data=data, columns=['supplier_id','supplier_name','contact_person','e-mail'])
    #print(df_supplier)

    cur.execute('SELECT * FROM repairshop')
    data = cur.fetchall()
    df_repair = pd.DataFrame(data=data, columns=['repair_shop_id','repairshop_name','contact_person','e-mail'])
    #print(df_repair)

    cur.execute('SELECT * FROM giftbox')
    data = cur.fetchall()
    df_gift = pd.DataFrame(data=data, columns=['giftbox_id','giftbox_name','giftbox_procurement_price','giftbox_amount'])
    #print(df_gift)

    #insert_script= 'INSERT INTO customer (first_name, last_name, sex, email) VALUES (%s,%s,%s,%s)'
    #insert_values= ('Mitchell', 'Pritchett','male', 'MVP@modern_family.com')
    #cur.execute(insert_script,insert_values)
    
    conn.commit()

except Exception as error:
    print('ERROR IN INITIAL DB PULL',error)

finally:
    if cur is not None:
        cur.close()
        conn.close()
################################################################################################################################################################################################
def connect():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return conn, cur

def disconnect(conn,cur):
    cur.close()
    conn.close()


def maybeMakeNumber(s):
    """Returns a string 's' into a integer if possible, a float if needed or
    returns it as is."""

    # handle None, "", 0
    if not s:
        return None  
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
        return s

#data = ["unkind", "data", "42", 98, "47.11", "of mixed", "types",'']

#converted = list(map(maybeMakeNumber, data))
#print(converted)


def make_ins_del_list(rows, df, unique_factor):
    df_new = pd.DataFrame(rows)
    df_comp1 = df.merge(df_new, how='outer', indicator=True)
    df_edited = df_comp1[df_comp1._merge != 'both']
    change_id_list_int = []
    change_column_list = []
    change_value_list = []
    #print(df_edited)
    if not df_edited.empty:
        l = list(df_edited[unique_factor])
        visited = set()
        dup = [x for x in l if x in visited or (visited.add(x) or False)]
        df_ins_del = df_edited.copy()
        for i in dup:
            df_ins_del = df_edited[df_edited[unique_factor] != i]  
        if dup != []: 
            for i in dup:
                df_value_change = df_edited[df_edited[unique_factor] == i]
        else:
            df_value_change = pd.DataFrame(columns=df_edited.columns)
        #print(df_value_change)
        #print(dup)
        #print(df_ins_del)
        if not df_value_change.empty:
            #print(df_value_change)
            change_id_list = list(df_value_change[unique_factor].unique())
            #print(change_id_list)
            for i in change_id_list:
                i = int(i)
                change_id_list_int.append(i)
            for i in change_id_list:
                df = df_value_change.copy()
                df = df.drop('_merge',1)
                df = df[df[unique_factor]==i]
                for j in df.columns:
                    if len(list(df[j].unique())) > 1:
                        change_column_list.append(j)
                for k in change_column_list:
                    df2 = df_value_change[df_value_change._merge=='right_only']
                    for g in list( df2[k].unique()):
                        g = str(g)
                        g = maybeMakeNumber(g)
                        change_value_list.append(g)
        df_ins = df_ins_del[df_ins_del._merge == 'right_only'].drop(unique_factor,1)
        df_del = df_ins_del[df_ins_del._merge == 'left_only']
        del_list = list(df_del[unique_factor])
        df_ins = df_ins.drop('_merge',1)
        ins_dict = df_ins.to_dict('split')
        ins_list = []
        for i in ins_dict['data']:
            #print(i)
            i = list(map(maybeMakeNumber, i))
            #print('after', i)
            t = tuple(i)
            #print('tuple', t)
            ins_list.append(t)
        return ins_list, del_list, change_id_list_int, change_column_list, change_value_list
    else:
        return [],[]

#################################################################################################################################################################################################
app = JupyterDash(__name__)
app.layout = html.Div(children=[
    html.H1(children=['RBike Database Management System'], style=header),
    html.Div(id='home', className='control_tabs',children=[
        dcc.Tabs(id='view_tabs',value='bikes', children=[
            dcc.Tab(
                label='Bikes',
                value='bikes',
                style=tab_style,
                selected_style= tab_selected_style1,
                children=[
                    html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_bike.to_dict('records'), [{"name": i, "id": i} for i in df_bike.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            filter_action='native',
                            id='bike_tbl'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_bike', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_bike', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_bike'),
                    dcc.Graph(id='bike_graph')
                ]
            ),
            dcc.Tab(
                label='Customers',
                value='customer',
                style=tab_style,
                selected_style= tab_selected_style2,
                children=[
                    html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_customer.to_dict('records'), [{"name": i, "id": i} for i in df_customer.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            filter_action = 'native',
                            id='customer_tbl'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_customer', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_customer', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_customer'),
                    dcc.Graph(id='customer_graph'),
                    dcc.Graph(id='customer_graph_2')
                ]
            ),
            dcc.Tab(
                label='Bookings',
                value='bookings',
                style=tab_style,
                selected_style=tab_selected_style3,
                children= [
                    html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_order.to_dict('records'), [{"name": i, "id": i} for i in df_order.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            filter_action='native',
                            id='order_tbl'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_order', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_order', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_order'),
                    dcc.Graph(id='order_graph')
                ]
            ),
            dcc.Tab(
                label='H.R.',
                value='hr',
                style=tab_style,
                selected_style=tab_selected_style4,
                children= [
                    html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_employee.to_dict('records'), [{"name": i, "id": i} for i in df_employee.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            id='employee_tbl',
                            filter_action = 'native'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_employee', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_employee', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_employee'),
                    dcc.Graph(id='employee_graph'),
                    dcc.Graph(id='employee_graph_2'),
                    dcc.Graph(id='employee_graph_3')
                ]
            ),
            dcc.Tab(
                label='Suppliers',
                value='suppliers',
                style=tab_style,
                selected_style=tab_selected_style5,
                children=[
                    html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_supplier.to_dict('records'), [{"name": i, "id": i} for i in df_supplier.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            id='supplier_tbl',
                            filter_action = 'native'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_supplier', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_supplier', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_supplier')
                ]
            ),
            dcc.Tab(
                label='Repair shops',
                value='repair_shops',
                style=tab_style,
                selected_style=tab_selected_style6,
                children=[
                     html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_repair.to_dict('records'), [{"name": i, "id": i} for i in df_repair.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            id='repair_tbl',
                            filter_action = 'native'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_repair', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_repair', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_repair')
                ]
            ),
            dcc.Tab(
                label='Gift Boxes',
                value='giftbox',
                style=tab_style,
                selected_style=tab_selected_style7,
                children=[
                    html.Div(style={'margin-top':'10px'},children=[
                        dash_table.DataTable(
                            df_gift.to_dict('records'), [{"name": i, "id": i} for i in df_gift.columns],
                            editable=True,
                            row_deletable=True,
                            style_cell=style_cell,
                            style_header=tbl_header_style,
                            style_as_list_view=True,
                            id='gift_tbl',
                            filter_action = 'native'
                        )
                    ]),
                    html.Button('Add row', id='edit_rows_button_gift', n_clicks=0, style=button_style),
                    html.Button('Save', id='save_to_postgres_gift', n_clicks=0, style=button_style),
                    html.Div([],'placeholder_gift')
                ]
            )
        ])
    ])
])

##########################################################################################################################
@app.callback(
    [Output('bike_graph','figure')],
    [Input('bike_tbl','data'),
    State('bike_tbl','columns')],
    prevent_initial_call=False
)
def make_bike_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['bike_id','brand','model', 'rent_fee_per_day','repair_status','order_id','repair_shop_id','supplier_id'])
    valueList = []
    for i in list(df.repair_status.unique()):
        s = (df.repair_status == i).sum()
        valueList.append(s)
    fig = go.Figure([go.Bar(x=list(df.repair_status.unique()), y=valueList)])
    fig.update_traces(opacity=0.6)
    fig.update_layout(title_text='Fleet repair status',xaxis_title="repair status",yaxis_title="count",)
    return [fig]

@app.callback(
    [Output('customer_graph','figure')],
    [Input('customer_tbl','data'),
    State('customer_tbl','columns')],
    prevent_initial_call=False
)
def make_cust_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['customer_id','first name','last name','sex', 'age', 'email'])
    valueList = []
    for i in list(df.sex.unique()):
        s = (df.sex == i).sum()
        valueList.append(s)
    fig = go.Figure([go.Bar(x=list(df.sex.unique()), y=valueList)])
    fig.update_traces(opacity=0.6)
    fig.update_layout(title_text='Customer gender distribution',xaxis_title="sex",yaxis_title="count",)
    return [fig]

@app.callback(
    [Output('customer_graph_2','figure')],
    [Input('customer_tbl','data'),
    State('customer_tbl','columns')],
    prevent_initial_call=False
)
def make_cust2_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['customer_id','first name','last name','sex', 'age', 'email'])
    
    fig = px.histogram(df, x='age',
    title='Customer age distribution',
    opacity=0.6)
    return [fig]

@app.callback(
    [Output('order_graph','figure')],
    [Input('order_tbl','data'),
    State('order_tbl','columns')],
    prevent_initial_call=False
)
def make_cust_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['order_id','payment','customer_id','giftbox_id'])
    valueList = []
    for i in list(df.payment.unique()):
        s = (df.payment == i).sum()
        valueList.append(s)
    fig = go.Figure([go.Bar(x=list(df.payment.unique()), y=valueList)])
    fig.update_traces(opacity=0.6)
    fig.update_layout(title_text='Payment method distribution',xaxis_title="payment",yaxis_title="count",)
    return [fig]

@app.callback(
    [Output('employee_graph','figure')],
    [Input('employee_tbl','data'),
    State('employee_tbl','columns')],
    prevent_initial_call=False
)
def make_cust_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['employee_id','first_name','last_name','sex', 'age','e-mail', 'income_per_year','department_id'])
    valueList = []
    for i in list(df.sex.unique()):
        s = (df.sex == i).sum()
        valueList.append(s)
    fig = go.Figure([go.Bar(x=list(df.sex.unique()), y=valueList)])
    fig.update_traces(opacity=0.6)
    fig.update_layout(title_text='Employee gender distribution',xaxis_title="sex",yaxis_title="count",)
    return [fig]

@app.callback(
    [Output('employee_graph_2','figure')],
    [Input('employee_tbl','data'),
    State('employee_tbl','columns')],
    prevent_initial_call=False
)
def make_cust2_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['employee_id','first_name','last_name','sex', 'age','e-mail', 'income_per_year','department_id'])
    
    fig = px.histogram(df, x='age',
    title='Employee age distribution',
    opacity=0.6)
    return [fig]

@app.callback(
    [Output('employee_graph_3','figure')],
    [Input('employee_tbl','data'),
    State('employee_tbl','columns')],
    prevent_initial_call=False
)
def make_cust2_graph(data, columns):
    df = pd.DataFrame(data = data, columns = ['employee_id','first_name','last_name','sex', 'age','e-mail', 'income_per_year','department_id'])
    df_male = df[df.sex=='male']
    df_female = df[df.sex=='female']
    fig = go.Figure([go.Bar(x=['male','female'], y=[df_male.income_per_year.mean(), df_female.income_per_year.mean()])])
    fig.update_traces(opacity=0.6)
    fig.update_layout(title_text='Gender Pay Gap',xaxis_title="sex",yaxis_title="average salary",)
    return [fig]






@app.callback(
    [Output('placeholder_bike','children'),
    Output('bike_tbl','data')],
    [Input('save_to_postgres_bike','n_clicks'),
    Input('edit_rows_button_bike','n_clicks')],
    [State('bike_tbl','data'),
    State('bike_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_bike':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM bike')
            data = cur.fetchall()
            df_bike = pd.DataFrame(data=data, columns=['bike_id','brand','model', 'rent_fee_per_day','repair_status','order_id','repairshop_id','supplier_id'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_bike,'bike_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO bike (brand, model, rent_fee_per_day, repair_status, order_ID, repairshop_ID, supplier_ID) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                    #print(ins_list)
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM bike WHERE bike_id = {i}')
                
                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE bike SET {change_column_list[c]} = '{change_value_list[c]}' WHERE bike_id = {i}")
                            else:
                                cur.execute(f"UPDATE bike SET {change_column_list[c]} = NULL WHERE bike_id = {i}")
                            c +=1
                            
                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM bike')
            data = cur.fetchall()
            df_bike = pd.DataFrame(data=data, columns=['bike_id','brand','model', 'rent_fee_per_day','repair_status','order_id','repairshop_id','supplier_id'])
            rows = df_bike.to_dict('records')

            return output_pos, rows


        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print('ERROR IN BIKE CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                cur.close()
                conn.close()

    elif button_clicked == 'edit_rows_button_bike':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows

    
@app.callback(
    [Output('placeholder_customer','children'),
    Output('customer_tbl','data')],
    [Input('save_to_postgres_customer','n_clicks'),
    Input('edit_rows_button_customer','n_clicks')],
    [State('customer_tbl','data'),
    State('customer_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_customer':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM customer')
            data = cur.fetchall()
            df_customer = pd.DataFrame(data=data, columns=['customer_id','first name','last name','sex', 'age', 'email'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_customer,'customer_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO customer (first_name, last_name, sex, age, email) VALUES (%s,%s,%s,%s,%s)'
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM customer WHERE customer_id = {i}')
                
                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE customer SET {change_column_list[c]} = '{change_value_list[c]}' WHERE customer_id = {i}")
                            else:
                                cur.execute(f"UPDATE customer SET {change_column_list[c]} = NULL WHERE customer_id = {i}")
                            c +=1

                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM customer')
            data = cur.fetchall()
            df_customer = pd.DataFrame(data=data, columns=['customer_id','first name','last name','sex', 'age', 'email'])
            rows = df_customer.to_dict('records')

            return output_pos, rows


        except Exception as error:
            print('ERROR IN CUSTOMER CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                cur.close()
                conn.close()


    elif button_clicked == 'edit_rows_button_customer':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows


@app.callback(
    [Output('placeholder_order','children'),
    Output('order_tbl','data')],
    [Input('save_to_postgres_order','n_clicks'),
    Input('edit_rows_button_order','n_clicks')],
    [State('order_tbl','data'),
    State('order_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_order':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM order_in')
            data = cur.fetchall()
            df_order = pd.DataFrame(data=data, columns=['order_id','payment','customer_id','giftbox_id'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_order,'order_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO order_in (payment, customer_ID, giftbox_ID) VALUES (%s,%s,%s)'
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM order_in WHERE order_id = {i}')
                
                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE order_in SET {change_column_list[c]} = '{change_value_list[c]}' WHERE order_id = {i}")
                            else:
                                cur.execute(f"UPDATE order_in SET {change_column_list[c]} = NULL WHERE order_id = {i}")
                            c +=1

                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM order_in')
            data = cur.fetchall()
            df_order = pd.DataFrame(data=data, columns=['order_id','payment','customer_id','giftbox_id'])
            rows = df_order.to_dict('records')

            return output_pos, rows


        except Exception as error:
            print('ERROR IN ORDER CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                disconnect(conn,cur)
                

    elif button_clicked == 'edit_rows_button_order':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows

@app.callback(
    [Output('placeholder_employee','children'),
    Output('employee_tbl','data')],
    [Input('save_to_postgres_employee','n_clicks'),
    Input('edit_rows_button_employee','n_clicks')],
    [State('employee_tbl','data'),
    State('employee_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_employee':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM employee')
            data = cur.fetchall()
            df_employee = pd.DataFrame(data=data, columns=['employee_id','first_name','last_name','sex', 'age','e-mail', 'income_per_year','department_id'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_employee,'employee_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO employee (first_name, last_name, sex, age, email, income_per_year, department_ID) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM employee WHERE employee_id = {i}')

                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE employee SET {change_column_list[c]} = '{change_value_list[c]}' WHERE employee_id = {i}")
                            else:
                                cur.execute(f"UPDATE employee SET {change_column_list[c]} = NULL WHERE employee_id = {i}")
                            c +=1

                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM employee')
            data = cur.fetchall()
            df_employee = pd.DataFrame(data=data, columns=['employee_id','first_name','last_name','sex', 'age','e-mail', 'income_per_year','department_id'])
            rows = df_employee.to_dict('records')

            return output_pos, rows


        except Exception as error:
            print('ERROR IN EMPLOYEE CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                cur.close()
                conn.close()
                

    elif button_clicked == 'edit_rows_button_employee':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows


@app.callback(
    [Output('placeholder_supplier','children'),
    Output('supplier_tbl','data')],
    [Input('save_to_postgres_supplier','n_clicks'),
    Input('edit_rows_button_supplier','n_clicks')],
    [State('supplier_tbl','data'),
    State('supplier_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_supplier':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM supplier')
            data = cur.fetchall()
            df_supplier = pd.DataFrame(data=data, columns=['supplier_id','supplier_name','contact_person','e-mail'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_supplier,'supplier_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO supplier (supplier_name, contact_person, email) VALUES (%s,%s,%s)'
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM supplier WHERE supplier_id = {i}')
                
                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE supplier SET {change_column_list[c]} = '{change_value_list[c]}' WHERE supplier_id = {i}")
                            else:
                                cur.execute(f"UPDATE supplier SET {change_column_list[c]} = NULL WHERE supplier_id = {i}")
                            c +=1

                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM supplier')
            data = cur.fetchall()
            df_supplier = pd.DataFrame(data=data, columns=['supplier_id','supplier_name','contact_person','e-mail'])
            rows = df_supplier.to_dict('records')

            return output_pos, rows


        except Exception as error:
            print('ERROR IN SUPPLIER CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                cur.close()
                conn.close()
                

    elif button_clicked == 'edit_rows_button_supplier':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows

@app.callback(
    [Output('placeholder_repair','children'),
    Output('repair_tbl','data')],
    [Input('save_to_postgres_repair','n_clicks'),
    Input('edit_rows_button_repair','n_clicks')],
    [State('repair_tbl','data'),
    State('repair_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_repair':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM repairshop')
            data = cur.fetchall()
            df_repair = pd.DataFrame(data=data, columns=['repair_shop_id','repairshop_name','contact_person','e-mail'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_repair,'repair_shop_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO repairshop (repairshop_name, contact_person, email) VALUES (%s,%s,%s)'
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM repairshop WHERE repairshop_id = {i}')
                
                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE repairshop SET {change_column_list[c]} = '{change_value_list[c]}' WHERE repairshop_id = {i}")
                            else:
                                cur.execute(f"UPDATE repairshop SET {change_column_list[c]} = NULL WHERE repairshop_id = {i}")
                            c +=1

                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM repairshop')
            data = cur.fetchall()
            df_repair = pd.DataFrame(data=data, columns=['repair_shop_id','repairshop_name','contact_person','e-mail'])
            rows = df_repair.to_dict('records')

            return output_pos, rows


        except Exception as error:
            print('ERROR IN REPAIRSHOP CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                cur.close()
                conn.close()
                

    elif button_clicked == 'edit_rows_button_repair':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows



@app.callback(
    [Output('placeholder_gift','children'),
    Output('gift_tbl','data')],
    [Input('save_to_postgres_gift','n_clicks'),
    Input('edit_rows_button_gift','n_clicks')],
    [State('gift_tbl','data'),
    State('gift_tbl','columns')],
    prevent_initial_call=True
)
def update_pg(n_clicks_save, n_clicks_add, rows, columns):
    button_clicked = ctx.triggered_id
    if button_clicked == 'save_to_postgres_gift':
        print('SAVE CLICKED\n')
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute('SELECT * FROM giftbox')
            data = cur.fetchall()
            df_gift = pd.DataFrame(data=data, columns=['giftbox_id','giftbox_name','giftbox_procurement_price','giftbox_amount'])
            #print(rows)
            if n_clicks_save > 0:
                ins_list, del_list, change_id_list, change_column_list, change_value_list = make_ins_del_list(rows,df_gift,'giftbox_id')
                print('INSERTS DETECTED:\t----------- ',ins_list)
                print('DELETS DETECTED:\t----------- ' ,del_list)
                print('EDITS DETECTED: \t----------- ', change_id_list)
                if ins_list != []:
                    print('inserting--------  ', ins_list)
                    insert_script= 'INSERT INTO giftbox (giftbox_name, giftbox_procurement_price, giftbox_amount) VALUES (%s,%s,%s)'
                    for i in ins_list:
                        cur.execute(insert_script,i)

                if del_list != []:
                    print('deleting--------  ', del_list)
                    for i in del_list:
                        cur.execute(f'DELETE FROM giftbox WHERE giftbox_id = {i}')
                
                if change_id_list != []:
                    print('updating id--------  ', change_id_list)
                    for i in change_id_list:
                        
                        print(change_column_list)
                        print(change_value_list)
                        c = 0
                        for j in range(len(change_column_list)):
                            if change_value_list[c] != 'None' and change_value_list[c] != 'nan':
                                cur.execute(f"UPDATE giftbox SET {change_column_list[c]} = '{change_value_list[c]}' WHERE giftbox_id = {i}")
                            else:
                                cur.execute(f"UPDATE giftbox SET {change_column_list[c]} = NULL WHERE giftbox_id = {i}")
                            c +=1

                conn.commit()

                output_pos = html.Div(style=saved_box_style,children=html.Plaintext( "\N{check mark} Data saved successfully.",style=data_saved_style))
            
            cur.execute('SELECT * FROM giftbox')
            data = cur.fetchall()
            df_gift = pd.DataFrame(data=data, columns=['giftbox_id','giftbox_name','giftbox_procurement_price','giftbox_amount'])
            rows = df_gift.to_dict('records')

            return output_pos, rows


        except Exception as error:
            print('ERROR IN GIFTBOX CALLBACK ',error)
            output_neg = html.Div(style=error_box_style,children=html.Plaintext( f"\N{cross mark} Sorry. Something went wrong.\n{error}",style=data_saved_style))
            return output_neg, rows
        finally:
            if cur is not None:
                cur.close()
                conn.close()
                

    elif button_clicked == 'edit_rows_button_gift':
        print('ADD CLICKED\n')
        if n_clicks_add > 0:
            rows.append({c['id']: '' for c in columns})
        return html.Div([]), rows
    
if __name__ == '__main__':
    app.run_server(debug=True, mode='external', host='0.0.0.0',port=8000)
