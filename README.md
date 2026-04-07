# MVP Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes - Fullstack

Aplicação fullstack para predição de risco de Burnout em indivíduos da geração Z.

## Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- Scikit-learn
- Pickle
- Notebook

## Modo de instalação e execução

1. Clone este repositório para o seu ambiente local.

2. Certifique-se de ter o Python instalado na sua máquina. Recomendamos a versão 3.14 ou superior.

3. Instale as dependências do projeto executando o seguinte comando no terminal:
```
pip install -r requirements.txt
```

4. Inicie o servidor Flask executando o seguinte comando no terminal:
```
python3 app/main.py
```

5. Acesse a aplicação em http://localhost:5000 no seu navegador.

## Rotas do projeto

- /: Redireciona para /front/index.html.
- /docs: Redireciona para /openapi.
- /api/individuos: Rotas relacionadas a indivíduos, incluindo:
- GET /api/individuos: Retorna uma lista de indivíduos.
- GET /api/individuos/id: Retorna um indivíduo específico com base no id.
- POST /api/individuos: Cria um novo indivíduo.
- DELETE /api/individuos/id: Deleta um indivíduo específico com base no id.