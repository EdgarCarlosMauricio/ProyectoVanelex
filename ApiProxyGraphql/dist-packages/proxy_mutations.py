from email.message import Message
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
# Librerias para enviar emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Import Config
import sis_t_config
import requests
__version__ = "2.0.0"

# 0. Global
pg_conn = None
response_body = ""

# 0.1 PgSql


def pg_connect():
    global pg_conn, response_body

    try:
        pg_conn = config_sis.pgsis_analytics()
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check DB Conn"


# ---------------------------------------------------------------------------
# Inicio Clases Interfases De Parametros De Entrada
class UsuarioInputx(graphene.InputObjectType):
    id_usuario = graphene.String(required=True)
    nombre1 = graphene.String(required=True)
    nombre2 = graphene.String(required=True)
    apellido1 = graphene.String(required=True)
    apellido2 = graphene.String(required=True)
    fecha_nacimiento = graphene.String(required=True)
    id_genero = graphene.String(required=True)
    telefono = graphene.String(required=True)
    correo = graphene.String(required=True)
    fecha_registro = graphene.String(required=True)
    estado = graphene.String(required=True)
    contrasena = graphene.String(required=True)
    tipo_acceso = graphene.String(required=True)

class ResetInput(graphene.InputObjectType):
    token = graphene.String(required=True)
    contrasena = graphene.String(required=True)


class DataInputAlertamiento(graphene.InputObjectType):
    input1 = graphene.String(required=False)
    input2 = graphene.String(required=False)
    input3 = graphene.String(required=False)
    input4 = graphene.String(required=False)
    input5 = graphene.String(required=False)
    input6 = graphene.String(required=False)
    input7 = graphene.String(required=False)
    input8 = graphene.String(required=False)
    input9 = graphene.String(required=False)
    input10 = graphene.String(required=False)


class AlertamientoInputx(graphene.InputObjectType):
    ids = graphene.String(required=True)
    data = graphene.InputField(DataInputAlertamiento)


class CreateAlertamientoInputTotal(graphene.InputObjectType):
    input1 = graphene.String(required=True)
    input2 = graphene.String(required=True)
    input3 = graphene.String(required=True)
    input4 = graphene.String(required=True)
    input5 = graphene.String(required=True)
    input6 = graphene.String(required=True)
    input7 = graphene.String(required=True)
    input8 = graphene.String(required=True)
    input9 = graphene.String(required=True)
    input10 = graphene.String(required=True)
    

class CreateAlertamientoInput(graphene.InputObjectType):
    data = graphene.InputField(CreateAlertamientoInputTotal)

# Fin Clases Interfases De Parametros De Entrada
# ------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Inicio Clases Interfases De Respuesta

class UsuariosX(graphene.ObjectType):
    message = graphene.String()    
    id_usuario = graphene.String()
    nombre1 = graphene.String()
    nombre2 = graphene.String()
    apellido1 = graphene.String()
    apellido2 = graphene.String()
    fecha_nacimiento = graphene.String()
    id_genero = graphene.String()
    telefono = graphene.String()
    correo = graphene.String()
    fecha_registro = graphene.String()
    estado = graphene.String()
    contrasena = graphene.String()
    tipo_acceso = graphene.String()

class PasswordReset(graphene.ObjectType):
    message = graphene.String()

class ReturnCreateData(graphene.ObjectType):
    message = graphene.String()

# Datos A Devolver Mutacion Plan B Alertamiento
class ReturnData(graphene.ObjectType):
    ids = graphene.String()
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

# Fin Clases Interfases De Respuesta
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# PRINCIPIO ModifyUserNewx
class ModifyUserNewx(graphene.Mutation):
    class Arguments:
        userdata = UsuarioInputx(required=True)

    ok = graphene.Boolean()
    user_new = graphene.Field(lambda: UsuariosX)

    def mutate(self, info, userdata):
        user_new = set_usuario_sis( userdata.id_usuario, userdata.nombre1, userdata.nombre2, userdata.apellido1, userdata.apellido2, userdata.fecha_nacimiento, userdata.id_genero, userdata.telefono, userdata.correo, userdata.fecha_registro, userdata.estado, userdata.contrasena, userdata.tipo_acceso)

        
        if user_new[0].message == "User added":
            ok = True
        else:
            ok = False

        return ModifyUserNewx(user_new=user_new[0], ok=ok)


# 1.6 Funcion De Ejecucion De La Mutacion
def set_usuario_sis(id_usuario, nombre1, nombre2 , apellido1, apellido2, fecha_nacimiento, id_genero, telefono, correo, fecha_registro, estado, contrasena, tipo_acceso):
    pg_connect()
    global pg_conn, response_body

    gql = []
    url = 'http://172.30.0.37:4555/auth/register/'

    try:
        
        datosuser = {
            "nombres": [
                nombre1, nombre2
            ],
            "apellidos": [
                apellido1, apellido2
            ],
            "fecha_nacimiento": fecha_nacimiento,
            "id_genero": id_genero,
            "telefono": telefono,
            "fecha_registro": fecha_registro,
            "estado": estado,
            "correo": correo,
            "tipo_acceso": tipo_acceso,
            "contraseña": contrasena,
            "id_usuario": id_usuario
        }
        response = requests.post(url, data=datosuser)

        gql.append(UsuariosX(message=response.json().get('Message'), id_usuario=id_usuario, nombre1=nombre1, nombre2=nombre2, apellido1=apellido1, apellido2=apellido2, fecha_nacimiento=fecha_nacimiento, id_genero=id_genero, telefono=telefono, correo=correo, estado=estado, fecha_registro=fecha_registro, tipo_acceso=tipo_acceso, contrasena=contrasena ))
               
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check set"
    return gql
# ------------------------------------------------------------------------
# FIN ModifyUserNewx


# ------------------------------------------------------------------------
# PRINCIPIO ResetPassword
class ResetPassword(graphene.Mutation):
    class Arguments:
        user_data = ResetInput(required=True)

    ok = graphene.Boolean()
    user_new = graphene.Field(lambda: PasswordReset)

    def mutate(self, info, user_data):
        user_new = set_password(user_data.contrasena, user_data.token)

        if user_new:
            ok = True
        else:
            ok = False

        return ResetPassword(user_new=user_new[0], ok=ok)


def set_password(contrasena, token):
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:4555/auth/reset-password'
    gql = []

    try:
        datosuser = {
            "contraseña": contrasena,
        }

        response = requests.put(url, data=datosuser, params={"token":f'{token}'})
        gql.append(PasswordReset(message = response.json().get("Message")))
       
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check set"
    return gql
# ------------------------------------------------------------------------
# FIN ResetPassword




# ------------------------------------------------------------------------
# PRINCIPIO Mutacion para crear datos Alertamiento en API REST
class CreateAlertamiento(graphene.Mutation):
    class Arguments:
        d = CreateAlertamientoInput(required=True)

    ok = graphene.Boolean()
    create_data = graphene.Field(lambda: ReturnCreateData)

    def mutate(self, info, d):
        # create_data = set_createinput(d.input1, d.input2, d.input3, d.input4, d.input5, d.input6, d.input7, d.input8, d.input9, d.input10)
        create_data = set_createinput(d.data)

        if create_data:
            ok = True
        else:
            ok = False

        return CreateAlertamiento(create_data=create_data[0], ok=ok)


def set_createinput(data):
    # def set_createinput(input1, input2, input3, input4, input5, input6, input7, input8, input9, input10):
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:3501/api/files/'
   
    gql = []

    try:
        # datainputs = {
        #     "input1" : input1,
        #     "input2" : input2,
        #     "input3" : input3,
        #     "input4" : input4,
        #     "input5" : input5,
        #     "input6" : input6,
        #     "input7" : input7,
        #     "input8" : input8,
        #     "input9" : input9,
        #     "input10" : input10,
        # }
        
        response = requests.post(url, data=data)
        gql.append(ReturnCreateData(message=response.json().get("msg")))

    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Alertamiento en API REST

# ------------------------------------------------------------------------
# PRINCIPIO Mutacion para actualizar datos Alertamiento en API REST
class UpdateAlertamiento(graphene.Mutation):
    class Arguments:
        d = AlertamientoInputx(required=True)

    ok = graphene.Boolean()
    data_update = graphene.Field(lambda: ReturnData)

    def mutate(self, info, d):
        data_update = set_update_data(d.ids, d.data)

        if data_update:
            ok = True
        else:
            ok = False
        
        return UpdateAlertamiento(data_update=data_update[0], ok=ok)

def set_update_data(ids, d):
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:3501/api/files/'+ids
    gql = []

    try:
         response = requests.put(url=url, data=d)
         x = response.json()

         gql.append(ReturnData(ids=x.get('_id'), input1=x.get('input1'), input2=x.get('input2'), input3=x.get('input3'), input4=x.get('input4'), input5=x.get('input5'), input6=x.get('input6'), input7=x.get('input7'), input8=x.get('input8'), input9=x.get('input9'), input10=x.get('input10'), createdAt=x.get('createdAt'), updatedAt=x.get('updatedAt')))

    except (Exception, psycopg2.DatabaseError) as error:
         response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Alertamiento en API REST
