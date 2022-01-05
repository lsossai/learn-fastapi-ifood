# learn-fastapi-ifood
Tutorial feito pras quartas de desenvolvimento

## Requisitos
* Python 3.6+
* Docker

Primeiro vamos instalar os requisitos no arquivo `requirements.txt`

>pip install -r requirements.txt

## Exemplo 1: Hello World
Execute o seguinte comando no terminal
> uvicorn hello:app --reload

Se funcionou corretamente o terminal vai printar o seguinte:
```
INFO:     Will watch for changes in these directories: ['/home/lucas-sossai/dev-pessoal/learn-fastapi-ifood']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [43848] using statreload
INFO:     Started server process [43850]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Para verificar o funcionamento entre no endereço http://127.0.0.1:8000 e veja se a seguinte mensagem chegou: 
`{"detail":"Hello World!"}`

Você pode checar a docs automática pelo endpoint http://127.0.0.1:8000/docs

## Exemplo 2: Create User
Primeiro vamos dar deploy num postgres local para a API se comunicar. Execute o script `deploy_local_postgres.sh`
> sh deploy_local_postgres.sh

Através do DBeaver ou outro sistema de preferência verifique se o banco está no ar
* host: 127.0.0.1
* port: 5432
* user: postgres
* password: 1234

Agora vamos dar deploy na API com o seguinte comando: 
> uvicorn main:app --reload

Entre na docs http://127.0.0.1:8000/docs e teste a criação de usuário, depois verifique se foi salvo no banco Postgres.
