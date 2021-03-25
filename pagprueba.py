import time
import cv2
from flask import Flask, render_template, Response
#servidor flask llamando archvo .html
app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/temperatura')
def pag3():
    return render_template ('index2.html')


@app.route('/monitoreo')
def pag2():
    return render_template ('camaras.html')

#LLAMAR A CAMARA POR MEDIANTE OPENCV
def gen():
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
      # CAPTURA frame POR frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
            frame = cv2.imencode('1.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            #time.sleep(0.1)
        else: 
            break
 # LLAMADO VIDEO A PAGINA   
               
""" LAMADO DE HOST Y PUERTO """
#if __name__ == '__main__':
#   app.run(debug=True) 
def gen1():
   
    cap1 = cv2.VideoCapture('rtsp://192.168.0.11:554/')
    # Read until video is completed
    while(cap1.isOpened()):
      # Capture frame-by-frame
        ret, img1 = cap1.read()
        if ret == True:
            img1 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5) 
            frame1 = cv2.imencode('1.jpg', img1)[1].tobytes()
            yield (b'--frame1\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n')
            #time.sleep(0.1)
        else: 
            break

def gen2():
    cap2 = cv2.VideoCapture('rtsp://192.168.0.12:554/')
    # Read until video is completed
    while(cap2.isOpened()):
      # Capture frame-by-frame
        ret, img2 = cap2.read()
        if ret == True:
            img2 = cv2.resize(img2, (0,0), fx=0.5, fy=0.5) 
            frame2 = cv2.imencode('1.jpg', img2)[1].tobytes()
            yield (b'--frame2\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n')
            #time.sleep(0.1)
        else: 
            break


#camara2
@app.route('/video_feed')
def video_feed():
 #Ruta de transmisión de video. Pon esto en el atributo src de una etiqueta img.
    return Response(gen(),
              mimetype='multipart/x-mixed-replace; boundary=frame')
              

#CAMARAS 2
@app.route('/video_feed1')
def video_feed1():
    return Response(gen1(),
                    mimetype='multipart/x-mixed-replace; boundary=frame1')

#camara3  
@app.route('/video_feed2')
def video_feed2():
    return Response(gen2(),
                    mimetype='multipart/x-mixed-replace; boundary=frame2')

app.run(host='127.0.0.1',debug=True,port=9999)


