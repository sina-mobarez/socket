import socketio
from gevent import pywsgi
import requests
# from geventwebsocket.handler import WebSocketHandler



# Create a Socket.IO server instance
sio = socketio.Server()

# Define an event handler for the 'connect' event
@sio.on('connect')
def connect(sid, environ):
    print('Client connected:', sid)

# Define an event handler for the 'message' event
@sio.on('message')
def message(sid, data):

    # response = requests.get('api url to get wheather data')
    
    response = data
    sio.emit('response', {'message':f'{response} test it works' }, room=sid)

# Define an event handler for the 'disconnect' event
@sio.on('disconnect')
def disconnect(sid):
    print('Client disconnected:', sid)

if __name__ == '__main__':
    # Wrap the Socket.IO server with a WSGI application
    app = socketio.WSGIApp(sio)

    # Run the server on localhost:5000
    pywsgi.WSGIServer(('localhost', 8000), app).serve_forever()