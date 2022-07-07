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
    bandejasoat1 = graphene.String()
    bandejasoat2 = graphene.String()
    bandejasoat3 = graphene.String()
    bandejasoat4 = graphene.String()
    bandejasoat5 = graphene.String()
    bandejasoat6 = graphene.String()
    bandejasoat7 = graphene.String()
    bandejasoat8 = graphene.String()
    bandejasoat9 = graphene.String()
    bandejasoat10 = graphene.String()
    bandejasoat11 = graphene.String()
    bandejasoat12 = graphene.String()
    bandejasoat13 = graphene.String()
    bandejasoat14 = graphene.String()
    bandejasoat15 = graphene.String()
    bandejasoat16 = graphene.String()
    bandejasoat17 = graphene.String()
    bandejasoat18 = graphene.String()
    bandejasoat19 = graphene.String()
    bandejasoat20 = graphene.String()
    bandejasoat21 = graphene.String()
    bandejasoat22 = graphene.String()
    bandejasoat23 = graphene.String()
    bandejasoat24 = graphene.String()
    bandejasoat25 = graphene.String()
    bandejavida1 = graphene.String()
    bandejavida2 = graphene.String()
    bandejavida4 = graphene.String()
    bandejavida6 = graphene.String()
    bandejavida7 = graphene.String()
    bandejavida8 = graphene.String()
    bandejavida10 = graphene.String()
    bandejavida11 = graphene.String()
    bandejavida12 = graphene.String()
    bandejavida13 = graphene.String()
    bandejavida20 = graphene.String()
    bandejavida23 = graphene.String()
    bandejavida24 = graphene.String()
    bandejavida25 = graphene.String()
    bandejavida26 = graphene.String()
    bandejavida27 = graphene.String()
    bandejavida28 = graphene.String()
    bandejavida29 = graphene.String()
    bandejavida30 = graphene.String()
    bandejavida31 = graphene.String()
    bandejavida32 = graphene.String()
    bandejavida33 = graphene.String()
    bandejavida34 = graphene.String()
    bandejavida35 = graphene.String()
    bandejavida36 = graphene.String()
    rango0a3soat = graphene.String()
    rango4a6soat = graphene.String()
    rango7a10soat = graphene.String()
    rango11a15soat = graphene.String()
    rango16a25soat = graphene.String()
    rango26a30soat = graphene.String()
    rangomasde30soat = graphene.String()
    rango0a3vida = graphene.String()
    rango4a6vida = graphene.String()
    rango7a10vida = graphene.String()
    rango11a15vida = graphene.String()
    rango16a25vida = graphene.String()
    rango26a30vida = graphene.String()
    rangomasde30vida = graphene.String()
    createdAt = graphene.String()
    updatedAt = graphene.String()


    
class LoginFiltro(graphene.ObjectType):
   message = graphene.String()
   token = graphene.String()

class RecuperarFiltro(graphene.ObjectType):
   message = graphene.String()

class TotalUsuarios(graphene.ObjectType):
    total = graphene.String()

class DatosVacantes(graphene.ObjectType):
    id_usuario = graphene.ID()
    nombres = graphene.String()
    apellidos = graphene.String()
    correo = graphene.String()
    telefono = graphene.String()
    url_linkedin = graphene.String()
    notas = graphene.String()

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
        rta = response.json()
        
        for x in rta:
            # Obtenemos el valor de _id y lo insermops como ids ya que _id rompe graphql
            x.update({'ids': x['_id']})
            gql.append(x)

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
        
        # Obtenemos el valor de _id y lo insermops como ids ya que _id rompe graphql
        x.update({'ids': x['_id']})
        gql.append(x)

    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"

    return gql
# --------------------------------------------------------------------------------------------------

# Manejador graphql para API REST para Vacantes


def get_getallvacantes(pg_conn):
    global response_body

    gql = []
    url = 'http://172.30.0.37:5001/api/app/users/all'

    try:
        response = requests.get(url)
        x = response.json()
        
        for x in response.json():
            gql.append(DatosVacantes(id_usuario=x['_id'], nombres=x['nombres'], apellidos=x['apellidos'], correo=x['correo'], telefono=x['telefono'], url_linkedin=x['url_linkedin'], notas=x['notas']))

    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"

    return gql
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# Manejador graphql para API REST para vacantes de Alertamiento GET ONE 
def get_getonevacantes(pg_conn, id_usuario):
    global response_body

    gql = []
    url = 'http://172.30.0.37:5001/api/app/users/'+id_usuario

    try:
        response = requests.get(url)
        x = response.json()
        
        gql.append(DatosVacantes(id_usuario=x['_id'], nombres=x['nombres'], apellidos=x['apellidos'], correo=x['correo'], telefono=x['telefono'], url_linkedin=x['url_linkedin'], notas=x['notas']))

    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"

    return gql
# --------------------------------------------------------------------------------------------------