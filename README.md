# WhatsClass

WhatsClass é uma plataforma para transmissão de aulas através do WhatsApp, oferecendo funcionalidades como encurtamento de URL, controle de entrada em grupos e conversação automatizada.

## Estrutura do Projeto

O projeto está organizado em microsserviços, cada um responsável por uma funcionalidade específica:

### 1. Microsserviço `conversation`

Serviço de conversação que permite a interação entre robôs baseados no serviço Twilio e o usuário.

**Funcionalidades:**
- Uso da conta Sandbox do Twilio para interação com o robô
- Os usuários podem se tornar beta-testers enviando a mensagem "join climb-knowledge" para o número +14155238886
- O robô está integrado no Twilio pelo endpoint https://api.whatsclass.com/conversation/response/v1
- Fornece respostas automatizadas com base nas mensagens do usuário

### 2. Microsserviço `entrance`

Serviço responsável pela administração de entrada de usuários em grupos e conversas.

**Funcionalidades:**
- Controle de tráfego e aplicação de regras para cada rota de campanha
- Configuração por conta de usuário, permitindo várias contas com suas próprias configurações
- Suporte a múltiplas campanhas por conta
- Estratégias de entrega que encaminham usuários ao ambiente para interação com o conteúdo
- Suporte a diferentes rotas de destino para a mesma URL de entrada
- Registro de eventos de redirecionamento para relatórios estatísticos
- URL de acesso: https://api.whatsclass.com/entrance/redirect/?account_id={ID_account}&campaign_id={ID_campaign}

### 3. Microsserviço `shortner`

Serviço de encurtamento de URLs que facilita o compartilhamento de links.

**Funcionalidades:**
- Criação de URLs encurtadas no formato https://in.whatsclass.com/r/{chave-unica}
- Redirecionamento de usuários da URL pública para a URL de destino

### 4. Microsserviço `marketing`

Serviço voltado para posicionamento digital e CDN para páginas de produto.

**Funcionalidades:**
- CDN para conteúdos públicos do projeto com foco em marketing
- Site básico inicial para o WhatsClass com descrição do serviço
- Função lambda que serve o site estático
- URLs de acesso: https://www.whatsclass.com/ e http://cdn.whatsclass.com/www/

### 5. Diretório `layers`

Camadas compartilhadas de código que podem ser utilizadas por todos os microsserviços, otimizando o reuso de bibliotecas.

## Como Executar

### Requisitos
- Python 3.8+
- AWS CLI configurado
- Conta na AWS
- Conta no Twilio (para o microsserviço de conversação)
- Docker (para construir as camadas)

### Configuração Inicial

1. **Configuração das Variáveis de Ambiente**

   O projeto utiliza um arquivo `.env` na raiz para armazenar informações sensíveis como credenciais e chaves de API. Crie este arquivo seguindo o modelo:

   ```
   # Credenciais Twilio
   TWILIO_ACCOUNT_SID=seu_account_sid
   TWILIO_AUTH_TOKEN=seu_auth_token

   # Configurações AWS
   AWS_ACCOUNT_ID=seu_account_id
   AWS_DEPLOYMENT_ROLE=seu_deployment_role

   # Buckets S3
   BUCKET_CONVERSATION=nome_do_bucket_conversation
   BUCKET_ENTRANCE=nome_do_bucket_entrance
   BUCKET_SHORTNER=nome_do_bucket_shortner
   BUCKET_MARKETING=nome_do_bucket_marketing

   # URLs
   DEFAULT_REDIRECT_URL=url_de_redirecionamento_padrao
   WHATSCLASS_LOGO_URL=url_do_logo
   ```

   Para usar as variáveis de ambiente nos microsserviços, instale o pacote `python-dotenv`:

   ```bash
   pip install python-dotenv
   ```

   E para integração com o Serverless Framework, instale o plugin:

   ```bash
   npm install --save-dev serverless-dotenv-plugin
   ```

2. **Configuração das Camadas (Layers)**

   Para configurar as camadas compartilhadas, execute no diretório `layers`:

   ```bash
   docker run -v "$PWD":/var/task "lambci/lambda:build-python3.8" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.8/site-packages/ --upgrade --use-feature=2020-resolver; exit"
   ```

3. **Deployment Serverless**

   Cada microsserviço utiliza o framework Serverless para deployment. Para realizar o deploy de um microsserviço:

   ```bash
   cd [microsserviço]
   serverless deploy
   ```

### Microsserviço Conversation

1. Para testar o microsserviço de conversação:
   - Envie "join climb-knowledge" para o número +14155238886 no WhatsApp
   - Após registrado como beta-tester, você pode enviar comandos como "oi", "menu" ou "piada"

### Microsserviço Entrance

1. Para utilizar o serviço de entrada em grupos:
   - Acesse a URL: https://api.whatsclass.com/entrance/redirect/?account_id={ID_account}&campaign_id={ID_campaign}
   - Substitua {ID_account} e {ID_campaign} pelos IDs apropriados

### Microsserviço Shortner

1. Para utilizar o encurtador de URLs:
   - As URLs encurtadas seguem o formato: https://in.whatsclass.com/r/{chave-unica}
   - Os redirecionamentos são configurados no arquivo data/redirects.csv

### Microsserviço Marketing

1. Para acessar o site de marketing:
   - Acesse https://www.whatsclass.com/
   - Para acessar via função lambda: http://cdn.whatsclass.com/www/

## Desenvolvimento Local

Para desenvolvimento local de cada microsserviço, você pode utilizar o plugin serverless-offline:

```bash
cd [microsserviço]
serverless offline
```

## Segurança

Para garantir a segurança das informações sensíveis:

1. **Nunca comite o arquivo `.env`** - Este arquivo já está incluído no `.gitignore`
2. **Use variáveis de ambiente** - Em vez de hardcoded no código
3. **Mantenha as credenciais seguras** - Compartilhe-as apenas por canais seguros
4. **Rotacione as chaves periodicamente** - Especialmente tokens de acesso e senhas

## Contato

Para mais informações sobre o WhatsClass, entre em contato via email: sales@whatsclass.com 