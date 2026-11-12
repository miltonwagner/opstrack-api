![CI Pipeline](https://github.com/miltonwagner/opstrack-api/actions/workflows/ci.yml/badge.svg)

# OpsTrack API

API simples de controle de chamados (tickets) de TI, desenvolvida como projeto contínuo da disciplina **Integração e Entrega Contínua (ISW-032)** — Fatec Indaiatuba, curso de Desenvolvimento de Software Multiplataforma.

O projeto nasceu na Semana 1 e evolui a cada aula ao longo do semestre, acompanhando os tópicos de versionamento, testes automatizados, CI/CD, containers e observabilidade.

## Tecnologias utilizadas

- Python 3.12
- Flask 3.1.3
- Gunicorn 26.2.0
- Git e GitHub
- GitHub Actions
- Docker
- Pytest e Flake8

## Requisitos

Para execução local:

- Python 3.x
- pip

Para execução em container:

- Docker instalado e em execução

## Configuração do ambiente

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows PowerShell
.\venv\Scripts\Activate.ps1

# Ativar no Linux/macOS
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt
```

## Executando a aplicação

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`.

Essa execução utiliza o servidor de desenvolvimento do Flask.

## Rotas disponíveis

| Rota | Método | Descrição |
|---|---|---|
| `/` | GET | Verificação simples de que o serviço está no ar |
| `/status` | GET | Endpoint dedicado de healthcheck |
| `/tickets` | GET | Retorna uma lista simulada de chamados de TI |
| `/version` | GET | Retorna a versão do sistema |
| `/usuarios` | GET | Retorna uma lista simulada de usuários |

## Rodando com Docker

A aplicação OpsTrack API pode ser executada em um container Docker, garantindo um ambiente padronizado e reproduzível.

### 1. Construir a imagem Docker

Na pasta raiz do projeto, execute:

```bash
docker build -t opstrack-api:0.1.0 .
```

Esse comando utiliza o Dockerfile para construir a imagem da aplicação.

### 2. Executar o container

```bash
docker run -d --name opstrack -p 8000:8000 opstrack-api:0.1.0
```

A aplicação estará disponível em:

http://localhost:8000

### 3. Verificar o funcionamento

```bash
docker ps
curl http://localhost:8000/status
```

Resposta esperada:

```json
{"status":"ok"}
```

### 4. Consultar os logs

```bash
docker logs opstrack
```

### 5. Verificar o healthcheck

```bash
docker inspect --format "{{.State.Health.Status}}" opstrack
```

Após o período inicial de verificação, o resultado esperado é:

```text
healthy
```

### 6. Verificar o usuário do container

```bash
docker exec opstrack whoami
```

Resultado esperado:

```text
appuser
```

O container utiliza um usuário sem privilégios administrativos, contribuindo para a segurança da aplicação.

### 7. Parar e remover o container

```bash
docker stop opstrack
docker rm opstrack
```

A imagem Docker permanece disponível para futuras execuções.

## Integração Contínua — GitHub Actions

O projeto utiliza GitHub Actions para automatizar verificações de qualidade e testes do código.

O workflow está definido no arquivo:

`.github/workflows/ci.yml`

A pipeline contempla verificações automatizadas e a integração da aplicação com Docker.

As execuções podem ser acompanhadas em:

https://github.com/miltonwagner/opstrack-api/actions

## Sobre o projeto

A OpsTrack API é o projeto-fio-condutor da disciplina: o mesmo repositório evolui semana após semana, incorporando padrões de commit (Conventional Commits), branching (GitHub Flow), testes automatizados, linters, pipelines de CI, containers Docker e práticas de entrega contínua.