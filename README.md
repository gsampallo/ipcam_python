# ipcam_python

Captura un frame del video de la cámara IP, lo convierte a escala de grises y lo guarda en un archivo png.

El formato de la url normalmente es 'rtsp://'+host+':554/'+stream
Donde host es la ip de la camara, y stream esta compuesto por el usuario y la clave de la camara.
En mi caso funciono rtsp://192.168.1.10:554/user=admin&password=&channel=1&stream=0.sdp?

Para el caso que no funcion para la cámara que tengan, basta buscar un poco en la documentacion y van a encontrar cual es la url adecuada.

Fuente: http://www.dream-enterprise.com/_wp/python-3-and-opencv-with-an-ip-camera/

[![Video](https://img.youtube.com/vi/7-jZhobJjio/0.jpg)](https://www.youtube.com/watch?v=7-jZhobJjio)