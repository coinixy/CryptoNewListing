import json
import websocket


def on_message(ws, message):
    try:
        data = json.loads(message)
        print(data)
    except Exception as ex:
        print(ex.__str__())

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == '__main__':
    while True:
        ws = websocket.WebSocketApp('ws://coinixy.com:8080/ws',
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.run_forever(ping_interval=30)
        ws.close()
