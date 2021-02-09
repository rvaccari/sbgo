# SBGO - Seu Barriga Gerador de Ofertas

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Crie o banco de dados. (Necessário postgres instalado, caso Docker, criar as bases: `sbgo` e `sbgo_test`)
7. Execute os testes.


```console
git clone git@github.com:rvaccari/sbgo.git
cd sbgo/project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
cp contrib/env.docker-sample .env
make pre-install
make test
```

## Docker

1. Clone o repositório.
2. Configure a instância com o .env.
3. Execute os testes.
4. Execute a aplicação
5. Pare a aplicação.

```console
git clone git@github.com:rvaccari/sbgo.git
cd sbgo/project
cp contrib/env-sample .env
cp contrib/env.docker-sample .env
make docker-test
make docker-up
make docker-down
```

## Documentação

A documentação está disponível nas urls

- http://0.0.0.0:8005/swagger/
- http://0.0.0.0:8005/redoc/
