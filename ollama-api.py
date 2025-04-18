from ollama import Client, chat
from sys import argv

if len(argv) < 4:
    print("Usage: python ollama-api.py <server_ip> <model> <user_message>")
    exit(1)

ip = argv[1] # IP of the server

client = Client(
  host=f'http://{ip}:11434/',
  headers={'x-some-header': 'some-value'}
)

user_message = ' '.join(argv[3:])
model = argv[2]

response = client.chat(model=model, messages=[
  {
    'role': 'user',
    'content': user_message,
  },
], stream=True)

for message in response:
    print(message.message.content, end='', flush=True)