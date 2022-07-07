# Crear Imagen Y subirla a DockerHub
docker login
docker build -t sisedgar/planb .
docker push sisedgar/planb

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
{
    "data": {
        "bandejasoat1": "25175",
        "bandejasoat2": "300",
        "bandejasoat3": "824",
        "bandejasoat4": "465",
        "bandejasoat5": "236",
        "bandejasoat6": "7463",
        "bandejasoat7": "236",
        "bandejasoat8": "1236",
        "bandejasoat9": "236",
        "bandejasoat10": "643",
        "bandejasoat11": "635",
        "bandejasoat12": "136",
        "bandejasoat13": "3999",
        "bandejasoat14": "665",
        "bandejasoat15": "555",
        "bandejasoat16": "689",
        "bandejasoat17": "111",
        "bandejasoat18": "696",
        "bandejasoat19": "3236",
        "bandejasoat20": "435",
        "bandejasoat21": "935",
        "bandejasoat22": "236",
        "bandejasoat23": "460",
        "bandejasoat24": "654",
        "bandejasoat25": "526",
        "bandejavida1": "444",
        "bandejavida2": "1236",
        "bandejavida4": "475",
        "bandejavida6": "746",
        "bandejavida7": "991",
        "bandejavida8": "212",
        "bandejavida10": "1262",
        "bandejavida11": "1006",
        "bandejavida12": "1116",
        "bandejavida13": "180",
        "bandejavida20": "144",
        "bandejavida23": "14408",
        "bandejavida24": "24785",
        "bandejavida25": "9856",
        "bandejavida26": "7854",
        "bandejavida27": "16",
        "bandejavida28": "36",
        "bandejavida29": "96",
        "bandejavida30": "222",
        "bandejavida31": "2558",
        "bandejavida32": "2569",
        "bandejavida33": "2936",
        "bandejavida34": "236",
        "bandejavida35": "574",
        "bandejavida36": "369",
        "rango0a3": "369",
        "rango4a6": "369",
        "rango7a10": "369",
        "rango11a15": "369",
        "rango16a25": "369",
        "rango26a30": "369",
        "rangomasde30": "369"
    }
}

```

# Datos en .env de variables de entorno si se corre en local 

- PORT=3000 
- BD_CNN=mongodb://localhost:27017/files

## npm run dev