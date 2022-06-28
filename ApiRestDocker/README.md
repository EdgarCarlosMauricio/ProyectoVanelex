
# Para instalar la app
1. lo clonan
2. npm i
3. docker compose build
4. docker compose up -d
- Si se reqiere entrar al contenedor docker ps para buscar el nombre
5. docker exec -it appbase64 sh
- Si se desea borrarlo
6. docker compose down

# Para Interactuar con la API basta con colocar 
- GET
- http://IP:5000/api/files
- http://IP:5000/api/files/id
- POST
- http://IP:5000/api/files
- DELETE
- http://IP:5000/api/files/id
- PUT
- http://IP:5000/api/files/id

# CRUDMongoNodeDocker

## CRUD para recibir datos de un PDF asociado a un numero de siniestro

```
_id: 62ad50608f453635bdae0bfd
input1: "523221"
input2: "6546"
input3: "6546"
input4: "6546"
input5: "6546"
input6: "6546"
input7: "6546"
input8: "6546"
input9: "6546"
input10: "6546"

```

# Datos en .env de variables de entorno si se corre en local 

- PORT=3000 
- BD_CNN=mongodb://localhost:27017/files

## npm run dev