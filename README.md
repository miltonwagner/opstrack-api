![CI](https://github.com/linconperetto/aula-teste/actions/workflows/ci.yml/badge.svg)
# OpsTrack API

API simples de controle de chamados (tickets) de TI, desenvolvida como projeto contínuo da disciplina **Integração e Entrega Contínua (ISW-032)** — Fatec Indaiatuba, curso de Desenvolvimento de Software Multiplataforma.

O projeto nasceu na Semana 1 e evolui a cada aula ao longo do semestre, acompanhando os tópicos de versionamento, testes automatizados, CI/CD, containers e observabilidade.

## Requisitos

- Python 3.x
- pip

## Configuração do ambiente

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt
```

## Executando a aplicação

```bash
python app.py
```

A aplicação sobe em `http://localhost:5000`.

## Rotas disponíveis

| Rota | Método | Descrição |
|---|---|---|
| `/` | GET | Verificação simples de que o serviço está no ar. |
| `/status` | GET | Endpoint dedicado de health-check, separado da rota raiz para futura integração com ferramentas de monitoramento. |
| `/tickets` | GET | Retorna uma lista (por enquanto mockada) de chamados de TI. |
| `/version` | GET | Retorna a versão do sistema.

## Sobre o projeto

A OpsTrack API é o projeto-fio-condutor da disciplina: o mesmo repositório é evoluído semana após semana, incorporando padrões de commit (Conventional Commits), branching (GitHub Flow), testes automatizados, linters, pipelines de CI, containers Docker e, por fim, deploy contínuo.