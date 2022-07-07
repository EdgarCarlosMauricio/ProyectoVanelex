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
    bandejasoat1 = graphene.String(required=False)
    bandejasoat2 = graphene.String(required=False)
    bandejasoat3 = graphene.String(required=False)
    bandejasoat4 = graphene.String(required=False)
    bandejasoat5 = graphene.String(required=False)
    bandejasoat6 = graphene.String(required=False)
    bandejasoat7 = graphene.String(required=False)
    bandejasoat8 = graphene.String(required=False)
    bandejasoat9 = graphene.String(required=False)
    bandejasoat10 = graphene.String(required=False)
    bandejasoat11 = graphene.String(required=False)
    bandejasoat12 = graphene.String(required=False)
    bandejasoat13 = graphene.String(required=False)
    bandejasoat14 = graphene.String(required=False)
    bandejasoat15 = graphene.String(required=False)
    bandejasoat16 = graphene.String(required=False)
    bandejasoat17 = graphene.String(required=False)
    bandejasoat18 = graphene.String(required=False)
    bandejasoat19 = graphene.String(required=False)
    bandejasoat20 = graphene.String(required=False)
    bandejasoat21 = graphene.String(required=False)
    bandejasoat22 = graphene.String(required=False)
    bandejasoat23 = graphene.String(required=False)
    bandejasoat24 = graphene.String(required=False)
    bandejasoat25 = graphene.String(required=False)
    bandejavida1 = graphene.String(required=False)
    bandejavida2 = graphene.String(required=False)
    bandejavida4 = graphene.String(required=False)
    bandejavida6 = graphene.String(required=False)
    bandejavida7 = graphene.String(required=False)
    bandejavida8 = graphene.String(required=False)
    bandejavida10 = graphene.String(required=False)
    bandejavida11 = graphene.String(required=False)
    bandejavida12 = graphene.String(required=False)
    bandejavida13 = graphene.String(required=False)
    bandejavida20 = graphene.String(required=False)
    bandejavida23 = graphene.String(required=False)
    bandejavida24 = graphene.String(required=False)
    bandejavida25 = graphene.String(required=False)
    bandejavida26 = graphene.String(required=False)
    bandejavida27 = graphene.String(required=False)
    bandejavida28 = graphene.String(required=False)
    bandejavida29 = graphene.String(required=False)
    bandejavida30 = graphene.String(required=False)
    bandejavida31 = graphene.String(required=False)
    bandejavida32 = graphene.String(required=False)
    bandejavida33 = graphene.String(required=False)
    bandejavida34 = graphene.String(required=False)
    bandejavida35 = graphene.String(required=False)
    bandejavida36 = graphene.String(required=False)
    rango0a3soat = graphene.String(required=False)
    rango4a6soat = graphene.String(required=False)
    rango7a10soat = graphene.String(required=False)
    rango11a15soat = graphene.String(required=False)
    rango16a25soat = graphene.String(required=False)
    rango26a30soat = graphene.String(required=False)
    rangomasde30soat = graphene.String(required=False)
    rango0a3vida = graphene.String(required=False)
    rango4a6vida = graphene.String(required=False)
    rango7a10vida = graphene.String(required=False)
    rango11a15vida = graphene.String(required=False)
    rango16a25vida = graphene.String(required=False)
    rango26a30vida = graphene.String(required=False)
    rangomasde30vida = graphene.String(required=False)


class AlertamientoInputx(graphene.InputObjectType):
    ids = graphene.String(required=True)
    data = graphene.InputField(DataInputAlertamiento)


class AlertamientoDeleteInput(graphene.InputObjectType):
    ids = graphene.String(required=True)

class CreateAlertamientoInput(graphene.InputObjectType):
    data = graphene.InputField(DataInputAlertamiento)

class CreateVacanteInputTotal(graphene.InputObjectType):
    nombres = graphene.String(required=True)
    apellidos = graphene.String(required=True)
    correo = graphene.String(required=True)
    telefono = graphene.String(required=True)
    url_linkedin = graphene.String(required=True)
    notas = graphene.String(required=True)

class CreateVacanteInput(graphene.InputObjectType):
    data = graphene.InputField(CreateVacanteInputTotal)

class VacanteInputTotal(graphene.InputObjectType):
    nombres = graphene.String(required=True)
    apellidos = graphene.String(required=True)
    correo = graphene.String(required=True)
    telefono = graphene.String(required=True)
    url_linkedin = graphene.String(required=True)
    notas = graphene.String(required=True)

class VacanteInputx(graphene.InputObjectType):
    ids = graphene.String(required=True)
    data = graphene.InputField(VacanteInputTotal)


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

class ReturnDeleteData(graphene.ObjectType):
    message = graphene.String()

# Datos A Devolver Mutacion Plan B Alertamiento
class ReturnData(graphene.ObjectType):
    ids = graphene.String()
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

class ReturnVacanteData(graphene.ObjectType):
    id_usuario = graphene.String()
    nombres = graphene.String()
    apellidos = graphene.String()
    correo = graphene.String()
    telefono = graphene.String()
    url_linkedin = graphene.String()
    notas = graphene.String()

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
        create_data = set_createinput(d.data)

        if create_data:
            ok = True
        else:
            ok = False

        return CreateAlertamiento(create_data=create_data[0], ok=ok)


def set_createinput(data):
   
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:3501/api/files/'
   
    gql = []
    
    try:

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
        x.update({'ids': x['_id']})
        gql.append(x)

    except (Exception, psycopg2.DatabaseError) as error:
         response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Alertamiento en API REST

# ------------------------------------------------------------------------
# PRINCIPIO Mutacion para BORRAR datos Alertamiento en API REST
class DeleteAlertamiento(graphene.Mutation):
    class Arguments:
        d = AlertamientoDeleteInput(required=True)

    ok = graphene.Boolean()
    data_delete = graphene.Field(lambda: ReturnDeleteData)

    def mutate(self, info, d):
        data_delete = set_delete_data(d.ids)

        if data_delete:
            ok = True
        else:
            ok = False
        
        return DeleteAlertamiento(data_delete=data_delete[0], ok=ok)

def set_delete_data(ids):
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:3501/api/files/'+ids
    gql = []

    try:
        response = requests.delete(url=url)
        gql.append(ReturnDeleteData(message=response.json().get("msg")))

    except (Exception, psycopg2.DatabaseError) as error:
         response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Alertamiento en API REST


# ------------------------------------------------------------------------
# PRINCIPIO Mutacion para crear datos Vacantes en API REST
class CreateVacante(graphene.Mutation):
    class Arguments:
        d = CreateVacanteInput(required=True)

    ok = graphene.Boolean()
    create_data = graphene.Field(lambda: ReturnVacanteData)

    def mutate(self, info, d):
       
        create_data = set_createvacante(d.data)

        if create_data:
            ok = True
        else:
            ok = False

        return CreateVacante(create_data=create_data[0], ok=ok)


def set_createvacante(data):
    
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:5001/api/app/users/add'
   
    gql = []

    try:

        response = requests.post(url, data=data)
        x = response.json()

        gql.append(ReturnVacanteData(id_usuario=x.get('_id'), nombres=x.get('nombres'), apellidos=x.get('apellidos'), correo=x.get('correo'), telefono=x.get('telefono'), url_linkedin=x.get('url_linkedin'), notas=x.get('notas')))


    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Vacantes en API REST

# ------------------------------------------------------------------------
# PRINCIPIO Mutacion para actualizar datos Vacantes en API REST
class UpdateVacante(graphene.Mutation):
    class Arguments:
        d = VacanteInputx(required=True)

    ok = graphene.Boolean()
    data_update = graphene.Field(lambda: ReturnVacanteData)

    def mutate(self, info, data):
        data_update = set_update_vacante(data.ids, data.data)

        if data_update:
            ok = True
        else:
            ok = False
        
        return UpdateVacante(data_update=data_update[0], ok=ok)

def set_update_vacante(ids, data):
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:5001/api/app/users/'+ids
    gql = []

    try:
         response = requests.put(url=url, data=data)
         x = response.json()

         gql.append(ReturnVacanteData(id_usuario=x.get('_id'), nombres=x.get('nombres'), apellidos=x.get('apellidos'), correo=x.get('correo'), telefono=x.get('telefono'), url_linkedin=x.get('url_linkedin'), notas=x.get('notas')))

    except (Exception, psycopg2.DatabaseError) as error:
         response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Vacantes en API REST


# PRINCIPIO Mutacion para actualizar datos Vacantes en API REST
class DeleteVacante(graphene.Mutation):
    class Arguments:
        d = VacanteInputx(required=True)

    ok = graphene.Boolean()
    data_update = graphene.Field(lambda: ReturnVacanteData)

    def mutate(self, info, data):
        data_update = set_delete_vacante(data.ids, data.data)

        if data_update:
            ok = True
        else:
            ok = False
        
        return DeleteVacante(data_update=data_update[0], ok=ok)

def set_delete_vacante(ids, data):
    pg_connect()
    global pg_conn, response_body
    url = 'http://172.30.0.37:5001/api/app/users/'+ids
    gql = []

    try:
         response = requests.delete(url=url, data=data)
         x = response.json()

         gql.append(ReturnVacanteData(message = response.json().get("Message")))

    except (Exception, psycopg2.DatabaseError) as error:
         response_body = "Notice: check set"
    
    return gql
# ------------------------------------------------------------------------
# FIN Mutacion para actualizar datos Vacantes en API REST