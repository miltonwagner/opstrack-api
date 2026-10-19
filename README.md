# OpsTrack API

API REST em **Python/Flask** para gerenciamento de chamados (tickets), desenvolvida como projeto acadêmico da disciplina **Integração e Entrega Contínua (ISW-032)**, do curso de Desenvolvimento de Software Multiplataforma da Fatec.

O projeto demonstra, na prática, as etapas iniciais de uma esteira de entrega contínua: controle de versão, padronização de commits, análise estática (linter), hooks de pré-commit, **testes automatizados** e **medição de cobertura de código**.

## Sumário

- [Equipe](#equipe)
- [Tecnologias](#tecnologias)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Rotas da API](#rotas-da-api)
- [Instalação](#instalação)
- [Executando a API](#executando-a-api)
- [Rodando os testes](#rodando-os-testes)
- [Testes automatizados](#testes-automatizados)
- [Cobertura de código](#cobertura-de-código)
- [Qualidade de código: Flake8 e pre-commit](#qualidade-de-código-flake8-e-pre-commit)
- [Fluxo de trabalho com Git](#fluxo-de-trabalho-com-git)
- [Conventional Commits](#conventional-commits)
- [Esteira de entrega: onde estamos](#esteira-de-entrega-onde-estamos)
- [Status do projeto](#status-do-projeto)

---

## Equipe

| Integrante |
| ---------- |
| Adriel Rattes |
| Fernando Dias |
| Giuliano |
| Milton Wagner |
| Paulo Ricardo |
| Riquelme |

Repositório: <https://github.com/miltonwagner/opstrack-api>

---

## Tecnologias

| Ferramenta | Uso |
| ---------- | --- |
| Python | Linguagem do projeto |
| Flask | Framework web da API |
| pytest | Execução dos testes automatizados |
| pytest-cov | Medição de cobertura de código |
| Flake8 | Linter (análise estática) |
| pre-commit | Execução automática de verificações antes de cada commit |
| Git e GitHub | Controle de versão, branches e Pull Requests |
| Visual Studio Code | Editor de código |

---

## Estrutura do projeto

```text
opstrack-api/
├── app.py                    # Aplicação Flask e suas rotas
├── utils.py                  # Funções auxiliares
├── pytest.ini                # Configuração do pytest
├── requirements.txt          # Dependências de execução da API
├── requirements-dev.txt      # Dependências de desenvolvimento (testes e qualidade)
├── tests/
│   ├── conftest.py           # Fixtures compartilhadas (client)
│   └── test_api.py           # Testes das rotas da API
├── .flake8                   # Regras do linter
├── .pre-commit-config.yaml   # Hooks executados antes do commit
├── .gitignore                # Arquivos ignorados pelo Git
├── .github/                  # Template de Pull Request
├── LEIA-ME.txt
└── README.md
```

> **Dois arquivos de dependências:** o `requirements.txt` contém apenas o necessário para executar a API (e será usado futuramente na imagem Docker). O `requirements-dev.txt` inclui o `requirements.txt` e acrescenta as ferramentas de desenvolvimento (`pytest`, `pytest-cov`, `flake8`, `pre-commit`). Assim, as ferramentas de teste não vão para a imagem de produção.

---

## Rotas da API

| Método | Rota | Resposta |
| ------ | ---- | -------- |
| GET | `/` | Identificação do serviço e status `online` |
| GET | `/status` | `{"status": "ok"}` |
| GET | `/version` | Versão da API |
| GET | `/tickets` | Lista de chamados (`{"tickets": [...]}`) |
| GET | `/usuarios` | Lista de usuários (`{"usuarios": [...]}`) |
| GET | qualquer outra rota | `404 Not Found` |

### Exemplos de resposta

`GET /`

```json
{
  "servico": "OpsTrack API",
  "status": "online"
}
```

`GET /status`

```json
{
  "status": "ok"
}
```

`GET /tickets`

```json
{
  "tickets": [
    { "id": 1, "titulo": "Computador não liga", "status": "aberto" },
    { "id": 2, "titulo": "Erro no sistema", "status": "em andamento" }
  ]
}
```

> Cada ticket possui, no mínimo, os campos `id` e `titulo`, verificados pelos testes automatizados.

---

## Instalação

Pré-requisitos: **Python 3** e **Git** instalados.

### 1. Clonar o repositório

```powershell
git clone https://github.com/miltonwagner/opstrack-api.git
cd opstrack-api
```

### 2. Criar e ativar o ambiente virtual

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Mac e Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Confirme que o prompt mostra `(venv)` antes de continuar.

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements-dev.txt
```

### 4. Instalar o hook de pre-commit

```powershell
pre-commit install
```

Saída esperada: `pre-commit installed at .git\hooks\pre-commit`.

---

## Executando a API

Com o ambiente virtual ativo, na raiz do projeto:

```powershell
python app.py
```

A API ficará disponível em `http://127.0.0.1:5000`. Para conferir, acesse `/status` no navegador.

---

## Rodando os testes

Todos os comandos abaixo devem ser executados na **raiz do projeto**, com o ambiente virtual ativo.

### Executar a suíte completa

```powershell
pytest
```

O `pytest.ini` já define onde procurar os testes, então não é preciso informar a pasta.

### Executar com detalhes (um resultado por teste)

```powershell
pytest -v
```

### Medir a cobertura de código

```powershell
pytest --cov=app --cov-report=term-missing
```

### Executar o portão de cobertura

```powershell
pytest --cov=app --cov-fail-under=85
```

Se a cobertura total ficar abaixo da meta, o pytest termina com **código de saída diferente de zero**, mesmo que todos os testes tenham passado. É esse código de saída que barrará o commit (hook) e deixará a pipeline de CI vermelha.

### Gerar o relatório HTML de cobertura

```powershell
pytest --cov=app --cov-report=html
```

Abra `htmlcov/index.html` no navegador. As linhas em vermelho são as que nenhum teste executou.

### Como ler a saída do pytest

```text
platform win32 -- Python 3.12.4, pytest-9.1.1
rootdir: ...\opstrack-api
configfile: pytest.ini
collected 5 items

tests/test_api.py .....                                   [100%]
```

| Elemento | Significado |
| -------- | ----------- |
| `configfile: pytest.ini` | O pytest encontrou a configuração do projeto |
| `collected 5 items` | Quantidade de testes encontrados |
| `.` | Teste que passou |
| `F` | Teste que falhou |

Quando um teste falha, o bloco **FAILURES** mostra:

| Marca | Significado |
| ----- | ----------- |
| Título (`____ test_x ____`) | Qual teste falhou |
| `>` | A linha em que o teste parou |
| `E` | O motivo: valor esperado contra valor obtido (**comece a leitura por aqui**) |
| Rodapé (`arquivo:linha`) | Local para abrir no editor |

### Erros comuns

| Mensagem | Causa provável |
| -------- | -------------- |
| `ModuleNotFoundError: No module named "app"` | O `pytest.ini` não está na raiz ou está sem `pythonpath = .` |
| `assert 404 == 200` | A rota pedida no teste não existe. Confira o nome em `app.py` |
| `KeyError: "..."` | A chave procurada não existe no JSON da resposta |
| `assert None is not None` | O passo *Act* do teste não foi implementado |

---

## Testes automatizados

### O que é um teste automatizado

Um programa (o pytest) chama o seu programa (a API), compara o resultado com o esperado e responde **passou** ou **falhou**. Ao contrário do teste manual, roda em segundos e pode ser repetido a cada alteração. É um *health check* escrito uma vez.

### Pirâmide de testes

```text
          /\
         /  \        End-to-end: poucos, lentos, caros, frágeis
        /----\
       /      \      Integração: partes reais conversando (API e banco)
      /--------\
     /          \    Unitários: muitos, executam em milissegundos
    /------------\
```

O projeto está hoje na **base da pirâmide**: testes unitários de rota, usando o `client` do Flask, sem servidor, sem banco de dados e sem rede. Muitos testes rápidos e poucos testes lentos dão feedback imediato a um custo baixo.

### Linter não substitui teste

O Flake8 verifica **estilo**, não **comportamento**. Se a rota `/status` passar a devolver `"oks"` em vez de `"ok"`, o Flake8 continua aprovando o código, mas o pytest acusa a diferença imediatamente:

```text
E   assert 'oks' == 'ok'
E     - ok
E     + oks
```

### Anatomia de um teste (Arrange, Act, Assert)

```python
def test_status_retorna_ok(client):
    resposta = client.get('/status')                       # Act
    assert resposta.status_code == 200                     # Assert
    assert resposta.get_json()['status'] == 'ok'           # Assert
```

| Etapa | O que faz |
| ----- | --------- |
| **Arrange** | Prepara o cenário. Aqui, o `client` já vem pronto da fixture |
| **Act** | Executa a ação testada (`client.get(...)`) |
| **Assert** | Verifica o resultado. Se a condição for falsa, o teste falha na hora |

Convenções do pytest: arquivos `test_*.py` e funções cujo nome começa com `test_`.

### Fixture `client`

Definida em `tests/conftest.py`:

```python
import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
```

Quando um teste declara o parâmetro `client`, o pytest procura a fixture com esse nome no `conftest.py`, executa até o `yield`, entrega o cliente ao teste e, ao final, fecha o cliente. É um "navegador de mentira" que chama a API sem precisar de servidor no ar.

### Configuração do pytest (`pytest.ini`)

```ini
[pytest]
pythonpath = .
testpaths = tests
```

- `pythonpath = .` permite que o pytest enxergue o `app.py` na raiz do projeto.
- `testpaths = tests` define onde procurar os testes.

### Testes existentes

| Teste | Verifica |
| ----- | -------- |
| `test_raiz_informa_servico_online` | `GET /` retorna 200 com `servico` e `status` esperados |
| `test_status_retorna_ok` | `GET /status` retorna 200 e `status == "ok"` |
| `test_tickets_retorna_lista_com_id_e_titulo` | `GET /tickets` retorna 200 e tickets com `id` e `titulo` |
| `test_usuarios_retorna_dois_usuarios` | `GET /usuarios` retorna 200 com exatamente 2 usuários |
| `test_rota_inexistente_retorna_404` | Uma rota inexistente (`/nao-existe`) retorna 404 |

---

## Cobertura de código

**Cobertura = linhas executadas ÷ linhas executáveis × 100.**

Funciona como um checklist de inspeção: marca os cômodos visitados, mas não diz se estão em ordem. Mostra **onde ninguém está olhando**, não prova que o código está certo.

### Como ler o relatório

```text
Name     Stmts   Miss  Cover   Missing
app.py      24      4    83%   18, 38-39, 43
```

| Coluna | Significado |
| ------ | ----------- |
| `Stmts` | Linhas executáveis |
| `Miss` | Linhas que nenhum teste executou |
| `Cover` | (Stmts − Miss) ÷ Stmts |
| `Missing` | Quais linhas ficaram sem cobertura |

### Meta de cobertura da equipe

- **Meta:** 85% de cobertura total do `app.py`.
- **Justificativa:** o projeto é uma API pequena e de rotas simples. Uma meta de 85% exige que as rotas principais e seus caminhos de erro sejam exercitados, sem forçar testes artificiais para linhas que não fazem sentido testar (como a execução direta do servidor em `app.run`).
- **Aplicação:** o comando `pytest --cov=app --cov-fail-under=85` falha se a cobertura ficar abaixo da meta.

### Limites da métrica

- **Executada não é verificada.** Um teste sem `assert` aumenta a cobertura, mas não garante nada. Cobertura mede execução, não verificação.
- **Excluir linhas é uma decisão.** O comentário `# pragma: no cover` exclui uma linha da medição. Só deve ser usado quando a linha realmente não faz sentido testar (por exemplo, o bloco `if __name__ == "__main__"`), nunca como truque para atingir a meta, e a justificativa deve ser documentada.

---

## Qualidade de código: Flake8 e pre-commit

O **Flake8** analisa os arquivos Python e aponta problemas de formatação e padrões de escrita. As regras estão versionadas em `.flake8`, para que toda a equipe use a mesma configuração.

Executar manualmente:

```powershell
flake8
```

O **pre-commit** executa o Flake8 automaticamente antes de cada commit. A configuração está em `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
      - id: flake8
```

### Fluxo do hook

```text
git add  ->  git commit  ->  pre-commit  ->  Flake8
                                                |
                                  +-------------+-------------+
                                  |                           |
                              Sem erros                   Com erros
                                  |                           |
                          Commit permitido            Commit bloqueado
```

Cada integrante precisa instalar o hook localmente com `pre-commit install`, pois o arquivo `.git/hooks/pre-commit` é criado em cada máquina e não vai para o GitHub.

Verificar todos os arquivos manualmente:

```powershell
pre-commit run --all-files
```

---

## Fluxo de trabalho com Git

A branch `main` é **protegida**: push direto é recusado, e isso é esperado. O caminho é sempre:

```text
Branch  ->  Commit  ->  Push  ->  Pull Request  ->  Merge e pull
```

```powershell
git checkout -b feature/nome-da-alteracao   # 1. criar a branch
git add .
git commit -m "feat: descricao da alteracao" # 2. commitar
git push -u origin feature/nome-da-alteracao # 3. enviar ao GitHub
```

4. No GitHub, abrir o **Pull Request** preenchendo o template (descrição, tipo de alteração, como testar e checklist).
5. Após a revisão e o merge, atualizar a `main` local:

```powershell
git checkout main
git pull origin main
git ls-files          # conferir se os arquivos chegaram
```

### Se o push for rejeitado (non-fast-forward)

A branch remota tem commits que você não tem localmente. Faça o pull com rebase e envie novamente:

```powershell
git pull origin nome-da-branch --rebase
git push
```

Não use `git push --force` para contornar a rejeição.

### Desfazer uma alteração

Olhe antes de desfazer:

```powershell
git status
git diff app.py
git checkout app.py     # ou: git restore app.py
git status
```

| Situação | Comando |
| -------- | ------- |
| Salvo, sem `git add` | `git checkout app.py` ou `git restore app.py` |
| Já fez `git add` | `git restore --staged app.py` e depois `git checkout app.py` |
| Já fez commit | `git restore --source=HEAD~1 app.py` e um novo commit |

---

## Conventional Commits

Os commits seguem o padrão **Conventional Commits**, e cada commit representa **uma única mudança lógica**.

| Tipo | Utilização |
| ---- | ---------- |
| `feat` | Nova funcionalidade |
| `fix` | Correção de problema |
| `docs` | Alteração na documentação |
| `style` | Alteração de formatação |
| `refactor` | Mudança na estrutura do código sem alterar a funcionalidade |
| `chore` | Configuração ou manutenção |
| `test` | Criação ou alteração de testes |

Exemplos:

```text
feat: adiciona rota de status
test: adiciona testes da API
test: corrige rotas dos testes de usuarios e rota inexistente
chore: remove test_api.py duplicado da raiz
docs: atualiza README com testes e cobertura
```

---

## Esteira de entrega: onde estamos

```text
Hook local  ->  Testes  ->  CI no servidor  ->  Imagem Docker
  (Aula 05)    (Aula 06)      (Aula 07)         (Aulas 08 e 09)
```

O estágio de commit (lint e testes rápidos) roda primeiro e precisa responder em segundos (*fail fast*). O código de saída diferente de zero é o que barra o commit e o que deixará a pipeline vermelha. A pipeline da Aula 07 executará exatamente os comandos descritos na seção [Rodando os testes](#rodando-os-testes).

---

## Status do projeto

Projeto acadêmico da disciplina **Integração e Entrega Contínua (ISW-032)**.

**Marco 1:** suíte de testes verde e versionada na `main`, com meta de cobertura justificada, README com a seção "Rodando os testes" e tag `marco-1`.

**Status:** em desenvolvimento.
