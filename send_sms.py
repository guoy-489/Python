from twilio.rest import Client

account_sid = 'AC31a59783249b0c6037e679ebaa9e4a9f'
auth_token = 'cdbfba269008cb186f5ac0cc94b078f6'
to_phone_number = input("Enter Phone Number to Send Message To, No - or (): +1")
message_to_send = input("Which Message Would You Like To Send? ")
client = Client(account_sid, auth_token)

message = client.messages.create(body= message_to_send, from_='+19388888126', to = to_phone_number)
print(message)