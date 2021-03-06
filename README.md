# Crypto New Listing
### Receive exchange announcements from WebSocket immediately and without delay 

(Get Binance announcement on time)

***We have designed a web socket so that users can receive and process exchange announcements without delay***

### Join to [Telegram Channel](https://t.me/coinixy).



### WebSocket Endpoint
```
ws://coinixy.com:8080/ws
```
After connecting to WebSocket, you should wait for new announcements from exchanges

### Exchanges currently supported:

- ##### Binance

Wait for other exchanges

### Message for successful connection to WebSocket:
```
{'status': 'ok'}
```

### WebSocket Response Message Type
```
{
   "id": "b76eb4e952a94959afb5964c32ddbb7a", 
   "url": "https://www.binance.com/en/support/announcement/b76eb4e952a94959afb5964c32ddbb7a", 
   "title": "Binance Will List Lido DAO (LDO)", 
   "serverTime": 1652079437647, 
   "exchange": "Binance"
}
```

### Python example
#### For example, you can run Python code and process incoming messages according to the [Json](https://github.com/coinixy/CryptoNewListing#websocket-response-message-type) instance.
```
pip install websocket-client
```
```
python coinixyws.py
```
Receive new announcement event:
```
def on_message(ws, message):
    # Message example
    # message='{
    # "id": "b76eb4e952a94959afb5964c32ddbb7a", 
    # "url": "https://www.binance.com/en/support/announcement/b76eb4e952a94959afb5964c32ddbb7a", 
    # "title": "Binance Will List Lido DAO (LDO)", 
    # "serverTime": 1652079437647, 
    # "exchange": "Binance"
    #}'
    try:
        data = json.loads(message)
        print(data)
    except Exception as ex:
        print(ex.__str__())
 ```
