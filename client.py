import socketio

# Create a Socket.IO client instance
sio = socketio.Client()

# Define an event handler for the 'connect' event
@sio.event
def connect():
    print('Connected to server')

# Define an event handler for the 'response' event
@sio.event
def response(data):
    print('Received response:', data)

# Define an event handler for the 'disconnect' event
@sio.event
def disconnect():
    print('Disconnected from server')

if __name__ == '__main__':
    # Connect to the Socket.IO server
    sio.connect('http://localhost:8000')

    # Send a message to the server for example name of city
    user_input = input('city name : ')
    sio.emit('message', user_input)
    # Wait for events indefinitely
    sio.wait()

        