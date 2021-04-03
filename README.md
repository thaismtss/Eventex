#EVENTEX

Sistema de eventos encomendado pela morena.

## Como desenvolver?

1.Clone o repositório

2.Crie uma virtualENv com Python 3.9

3.Ative a virtualenv.

4.Instale as dependências.

5.Configure a instância com o.env

6.Execute os tests.

```console
git clone git@github.com:thaismtss/eventex.git wttd
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

##Como fazer o deploy?

1.Crie uma instância no heroku.

2.Envie as configurações para o heroku.

3.Defina uma SECRET_KEY segura para a sua instância.

4.Defina DEBUG=False.

5.Configure o serviço de email.

6.Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY= `python contrib\secret_gen.py`
heroku config:set DEBUG=False
#configure email
git push heroku maste --force
```
