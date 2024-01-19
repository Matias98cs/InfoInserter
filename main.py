from helpers.database import obtener_session
from helpers.models import ArticulosWeb, CategoriaWeb, Promocion, Ofertas
from helpers.config import endpoint_url
import requests
import json

session_db = obtener_session()

url_promociones = f'{endpoint_url}/api/v1/promocioneswebec'
response_promociones = requests.get(url_promociones)
promociones = json.loads(response_promociones.content)

url_ofertas = f'{endpoint_url}/api/v1/ofertaswebec?sucursal=1'
response_ofertas = requests.get(url_ofertas)
ofertas = json.loads(response_ofertas.content)

# url_articulosweb = f'{endpoint_url}/api/v1/articulosweb?sucursal=8'
url_articulosweb = f'{endpoint_url}/api/v1/articulosweb?sucursal=1'
response_articulosweb = requests.get(url_articulosweb)
articulosweb = json.loads(response_articulosweb.content)

url_categoriaweb = f'{endpoint_url}/api/v1/categoriasweb'
response_categoriaweb = requests.get(url_categoriaweb)
categoriaweb = json.loads(response_categoriaweb.content)

lista_errores_promociones = []
for item in promociones['registros']:
    try:
        promocion = Promocion.crear_y_obtener(session_db, **item)
        session_db.commit()
    except Exception as e:
        print(f"Error al cargar los datos {e}")
        session_db.rollback()
        lista_errores_promociones.append(item)

session_db.commit()
print('Datos de promociones cargados en DB')


lista_errores_ofertas = []
for item in ofertas['registros']:
    try:
        oferta = Ofertas.crear_y_obtener(session_db, **item)
        session_db.commit()
    except Exception as e:
        print(f"Error al cargar dos ofertas : {e}")
        session_db.rollback()
        lista_errores_ofertas.append(item)

session_db.commit()
print('Datos de ofertas cargados en DB')

lista_errores_articulosweb = []
for item in articulosweb['registros']:
    try:
        art_web = ArticulosWeb.crear_y_obtener(session_db, **item)
        session_db.commit()
    except Exception as e:
        print(f"Error al cargar los articulos web : {e}")
        session_db.rollback()
        lista_errores_articulosweb.append(item)

session_db.commit()
print('Datos de articulos web cargados en DB')


lista_errores_categoriaweb = []
for item in categoriaweb['registros']:
    try:
        cat_web = CategoriaWeb.crear_y_obtener(session_db, **item)
        session_db.commit()
    except Exception as e:
        print(f"Error al cargar los articulos web: {e}")
        session_db.rollback()
        lista_errores_categoriaweb.append(item)

session_db.commit()
print('Datos de categorias web cargados en DB')
