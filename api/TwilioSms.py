from twilio.rest import Client 
 
account_sid = 'AC148ca3bc3653099cdded7b6567832809' 
auth_token = '2316834c25b2d1a9ca90a0a1973e8609' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG3140c12d69753a58372ddeb25440140a', 
                              body='ahoy terminal',      
                              to='+8801872627888' 
                          ) 
 
print(message.sid)