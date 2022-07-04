from itertools import chain
import config_sis
import os
import sys
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import re
import string
import graphene
from collections import namedtuple
import requests



# 1. Import Config
import sis_t_config

# 19042022
__version__ = "1.0"

# 0. Global
pg_conn = None
response_body = ""

# sys.stdout = open("/home/stgonzalez/prueba", "w")

# 0.1 PgSql

def pg_connect():
    global pg_conn, response_body
    try:
        pg_conn = config_sis.pgsis_analytics()
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check DB Conn"

# 1. Models

# 1.2 Input


# class TotalUsuarios(graphene.ObjectType):
#    total = graphene.String()
class UsuariosFiltro(graphene.ObjectType):
    id_usuario = graphene.ID()
    nombres = graphene.String()
    # nombresp = graphene.String()
    apellidos = graphene.String()
    # apellido_primer = graphene.String()
    # apellido_segundo = graphene.String()
    fecha_nacimiento = graphene.String()
    id_genero = graphene.String()
    telefono = graphene.String()
    correo = graphene.String()
    fecha_registro = graphene.String()
    estado = graphene.String()
    fecha_registro = graphene.String()
    # 
    id_tipo_acceso = graphene.String()
    contrasena = graphene.String()
    # grupos_id = graphene.String()
    # grupos_nombre = graphene.String()

# Clase Para API Plan B Alertamiento en API REST
class DatosAlertamiento(graphene.ObjectType):
    ids = graphene.ID()
    input1 = graphene.String()
    input2 = graphene.String()
    input3 = graphene.String()
    input4 = graphene.String()
    input5 = graphene.String()
    input6 = graphene.String()
    input7 = graphene.String()
    input8 = graphene.String()
    input9 = graphene.String()
    input10 = graphene.String()
    createdAt = graphene.String()
    updatedAt = graphene.String()
    
class LoginFiltro(graphene.ObjectType):
   message = graphene.String()
   token = graphene.String()

class RecuperarFiltro(graphene.ObjectType):
   message = graphene.String()

class TotalUsuarios(graphene.ObjectType):
    total = graphene.String()

# 2. Data

def get_login(pg_conn, email, contrasena):
    global response_body
    gql = []
    try:
        response = requests.post('http://172.30.0.37:4555/auth/login/', data={"correo":f'{email}', "contraseña":f'{contrasena}'})
        #response.raise_for_status()
        # if response.status_code >= 200:
        #     raise Exception(f'{response.json()}')
        gql.append(LoginFiltro(message=response.json().get('Message'), token=response.json().get('token')))
        #gql.append(LoginFiltro(message=response.content, token='Holaaa'))


    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"
        raise Exception('FALLÉEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')

    return gql


def get_recuperar(pg_conn, email):
    global response_body
    gql = []
    try:
        response = requests.post('http://172.30.0.37:4555/auth/forgot-password/', data={"correo":f'{email}'})
        #response.raise_for_status()
        # if response.status_code >= 200:
        #     raise Exception(f'{response.json()}')
        gql.append(RecuperarFiltro(message=response.json().get('Message')))
        #gql.append(LoginFiltro(message=response.content, token='Holaaa'))


    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"
        raise Exception('FALLÉEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')

    return gql


def get_usuarios(pg_conn, token):
    global response_body

    gql = []

    try:

        response = requests.get('http://172.30.0.37:4555/user-sis/users/', headers={"token":f'{token}'})

        for pg_row in response.json():
            nombres = pg_row.get("nombres")
            
            # print(nombrejson)

            gql.append(UsuariosFiltro(id_usuario=pg_row.get("id_usuario"), nombres=nombres, apellidos=pg_row.get("apellidos"), fecha_nacimiento=pg_row.get("fecha_nacimiento"), id_genero=pg_row.get("id_genero"), telefono=pg_row.get("telefono"), correo=pg_row.get("correo"), estado=pg_row.get("estado"), fecha_registro=pg_row.get("fecha_registro"), id_tipo_acceso=pg_row.get("id_tipo_acceso"), contrasena=pg_row.get("contraseña") ))


    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"
        gql = response
    return gql
    

def get_totalusuarios(pg_conn, tipo_filter, data_filter):
    global response_body

    gql = []
    
    try:
        
            # query = "SELECT id_usuario, nombres[1] AS nombre_primer, nombres[2] AS nombre_segundo, apellidos[1] AS apellido_primer, apellidos[2] AS apellido_segundo, fecha_nacimiento, id_genero, telefono, correo, fecha_registro, grupos_id, grupos_nombre FROM usuario_sis_grupo_vw WHERE '"+tp+"' LIKE '"+tipo_filter+"'"
            query = "SELECT count(*) AS total FROM usuario_sis_grupo_vw WHERE nombres[1] ilike ('%"+data_filter+"%') or nombres[2] ilike ('%"+data_filter+"%') or apellidos[1] ilike ('%"+data_filter+"%') or apellidos[2] ilike ('%"+data_filter+"%') or correo ilike ('%"+data_filter+"%') or grupos_nombre ilike ('%"+data_filter+"%')"
            # total = "SELECT count(*) AS n_total FROM usuario_sis_grupo_vw WHERE id_usuario != 1"
            cur = pg_conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query)
            pg_conn.commit()
            resultado = cur.fetchall()
            for y in resultado:
                gql.append(TotalUsuarios(total=y["total"]))
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"
        gql = TotalUsuarios(total=str(error))
    return gql

# --------------------------------------------------------------------------------------------------
# Manejador graphql para API REST para plan B de Alertamiento


def get_getallalertamiento(pg_conn):
    global response_body

    gql = []
    url = 'http://172.30.0.37:3501/api/files/'

    try:
        response = requests.get(url)
        x = response.json()
        
        for x in response.json():
            gql.append(DatosAlertamiento(ids=x['_id'], input1=x['input1'], input2=x['input2'], input3=x['input3'], input4=x['input4'], input5=x['input5'], input6=x['input6'], input7=x['input7'], input8=x['input8'], input9=x['input9'], input10=x['input10'], createdAt=x['createdAt'], updatedAt=x['updatedAt']))

    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"

    return gql
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# Manejador graphql para API REST para plan B de Alertamiento GET ONE 
def get_getonealertamiento(pg_conn, ids):
    global response_body

    gql = []
    url = 'http://172.30.0.37:3501/api/files/'+ids

    try:
        response = requests.get(url)
        x = response.json()
        
        gql.append(DatosAlertamiento(ids=x['_id'], input1=x['input1'], input2=x['input2'], input3=x['input3'], input4=x['input4'], input5=x['input5'], input6=x['input6'], input7=x['input7'], input8=x['input8'], input9=x['input9'], input10=x['input10'], createdAt=x['createdAt'], updatedAt=x['updatedAt']))

    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"

    return gql
# --------------------------------------------------------------------------------------------------