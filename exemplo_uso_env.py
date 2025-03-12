# Exemplo de como usar as variáveis de ambiente em vez de credenciais hardcoded
import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Usar as variáveis de ambiente em vez de hardcoded
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Exemplo de envio de mensagem
def enviar_mensagem():
    # Introdução com emojis 
    msg = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='✌🏻 Seja muito bem vindo ao curso. Eu vou te acompanhar e trazer conteúdos para você aprender. 🙏🏻',      
        to='whatsapp:+5511975716615'
    ) 
    print(msg.sid)

# Exemplo de envio de imagem
def enviar_imagem():
    # Usar URL do logo do WhatsClass do arquivo .env
    logo_url = os.getenv('WHATSCLASS_LOGO_URL')
    msg = client.messages.create( 
        from_='whatsapp:+14155238886',  
        media_url=[logo_url],
        to='whatsapp:+5511975716615'
    ) 
    print(msg.sid)

# Exemplo de como modificar o arquivo main.py do microsserviço conversation
def exemplo_main_py():
    # No início do arquivo, adicionar:
    # from dotenv import load_dotenv
    # load_dotenv()
    
    # E substituir qualquer credencial hardcoded por:
    # account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    # auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    pass

# Exemplo de como modificar os arquivos serverless.yml
def exemplo_serverless_yml():
    """
    Nos arquivos serverless.yml, substituir:
    
    environment:
      AWS_CONFIG_FILE: ".aws/config"
      AWS_PROFILE: "default"
      BUCKET: "whatsclass-conversation"
    
    Por:
    
    environment:
      AWS_CONFIG_FILE: ".aws/config"
      AWS_PROFILE: "default"
      BUCKET: ${env:BUCKET_CONVERSATION}
    
    E substituir:
    
    deploymentRole: arn:aws:iam::492205185884:role/serverless
    
    Por:
    
    deploymentRole: ${env:AWS_DEPLOYMENT_ROLE}
    """
    pass

# Exemplo de como modificar o arquivo redirect.py do microsserviço shortner
def exemplo_redirect_py():
    """
    No arquivo redirect.py, substituir:
    
    redirect_url = 'https://go.whatsclass.education/r/not-found'
    
    Por:
    
    redirect_url = os.getenv('DEFAULT_REDIRECT_URL')
    """
    pass

# Nota importante
"""
Para usar as variáveis de ambiente em produção com o Serverless Framework:

1. Instalar o plugin serverless-dotenv-plugin:
   npm install --save-dev serverless-dotenv-plugin

2. Adicionar o plugin ao arquivo serverless.yml:
   plugins:
     - serverless-dotenv-plugin

3. Configurar o plugin no serverless.yml:
   custom:
     dotenv:
       include:
         - TWILIO_ACCOUNT_SID
         - TWILIO_AUTH_TOKEN
         - AWS_ACCOUNT_ID
         - AWS_DEPLOYMENT_ROLE
         - BUCKET_CONVERSATION
         - BUCKET_ENTRANCE
         - BUCKET_SHORTNER
         - BUCKET_MARKETING
         - DEFAULT_REDIRECT_URL
         - WHATSCLASS_LOGO_URL
""" 