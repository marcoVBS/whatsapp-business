# Integração Whatsapp Business

## Sobre
API REST desenvolvida com finalidade de testar integração com Whatsapp Business para armazenar localmente e fazer o envio de mensagens, também permitindo agendamento para envio posterior.

## Dependências
- Docker;
- Python;
- PostgreSQL;
- Redis;

## Iniciando e rodando o projeto
- Criar o arquivo `.env` a partir do `.env.example` e configurar as variáveis  access_token e phone_id;
- Após isso, rodar os comandos a seguir, respectivamente, na raiz do projeto.

```
// Inicia os containers
$ docker compose up -d

// Cria e ativa o ambiente virtual
$ python -m venv env
$ source env/bin/activate

// Instala as dependências
$ python -m pip install -r requirements.txt

// Roda as migrations
$ python manage.py migrate

// Cria usuário admin
$ python manage.py createsuperuser

// Inicia o servidor
$ python manage.py runserver

// Inicia o Celery (Rodar em outra aba do terminal)
$ python -m celery -A setup worker -B
```


## Endpoints

Endpoint | Method | Body | Descrição
-- | -- |-- |--
`api/users` | POST | `*username`, `*password`, `email` | Cadastro de usuários
`api/token` | POST | `*username`, `*password` | Autenticação e obtenção do access token
`api/token/refresh` | POST | `*refresh` | Refresh token
`api/messages`| GET | - | Buscar todas as mensagens (se admin retorna todas, caso não, retorna as do usuário)
`api/messages/:id` | GET | - | Buscar uma mensagem
`api/messages`| POST | `*recipient`, `*message`, `scheduled_date (data/hora de agendamento, para envio posteriormente)` | Criar uma mensagem nova
`api/messages/:id` | PUT | `recipient`, `message`, `scheduled_date`, `pending` | Alterar mensagem
`api/messages/:id` | DELETE | - | Remover mensagem