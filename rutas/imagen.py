from sys import path
from flask import Blueprint, request, send_from_directory
from os import getcwd
from responses import respons

routes_imangen = Blueprint("route_imagen", __name__)

PATH_IMAGEN = getcwd() + "/imagen/"

IMAGEN_MINE_TYPE = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'raw', 'psd'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGEN_MINE_TYPE

@routes_imangen.post("/upload")
def upload_file():
    try:
        imagen = request.files['imagen']
        if imagen and allowed_file(imagen.filename):
            imagen.save(PATH_IMAGEN + imagen.filename)
            return respons.response_json("success")
        else:
            return respons.response_json("invalid_imagen_type"), 400
    except FileNotFoundError:
        return respons.response_json("imagen_not_found"), 404
    
@routes_imangen.get("/imagen/<string:name_file>")
def get_file(name_file):
    return send_from_directory(PATH_IMAGEN, path = name_file, as_attachment = False)

@routes_imangen.get("/download/<string:name_file>")
def download_file(name_file):
    return send_from_directory(PATH_IMAGEN, path = name_file, as_attachment = True)