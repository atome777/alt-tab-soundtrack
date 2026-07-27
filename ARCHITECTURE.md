# Alt+Tab Soundtrack — Instruções do Projeto

> Este documento define os padrões arquiteturais, convenções e boas práticas do projeto **Alt+Tab Soundtrack**. Toda nova implementação deve seguir estas diretrizes para manter a consistência do código, facilitar a manutenção e preservar a arquitetura existente.

---

# Objetivo do Projeto

O **Alt+Tab Soundtrack** automatiza a criação e publicação da série de posts no LinkedIn.

O fluxo principal da aplicação é:

1. Obter informações da música através do Spotify.
2. Gerar a arte HTML.
3. Capturar a imagem da arte.
4. Salvar os dados no banco SQLite.
5. Publicar automaticamente no LinkedIn utilizando Playwright.

Novas funcionalidades devem integrar-se a esse fluxo sem alterar sua arquitetura principal.

---

# Princípios Gerais

O projeto prioriza:

- Código simples e explícito.
- Alta legibilidade.
- Fácil manutenção.
- Separação de responsabilidades.
- Baixo acoplamento.
- Alta coesão.
- Reutilização de código.
- Tipagem completa.

Sempre prefira clareza em vez de reduzir quantidade de linhas.

---

# Arquitetura

O projeto é organizado por responsabilidade.

Cada diretório possui apenas uma função.

```
src/
│
├── assets/
├── configs/
├── cores/
├── data/
├── templates/
├── types/
├── ui/
└── utils/
```

Nunca misture responsabilidades entre diretórios.

---

# Organização das Camadas

## configs/

Contém apenas configurações da aplicação.

Exemplos:

- Banco de dados
- Playwright
- Logger
- Variáveis de ambiente
- Configurações gerais

Nunca colocar regras de negócio.

---

## cores/

Contém toda a lógica da aplicação.

Exemplos:

- Comunicação com Spotify
- Comunicação com LinkedIn
- Banco de dados
- Automações
- Serviços

Toda regra de negócio deve ficar nesta camada.

---

## ui/

Responsável exclusivamente pela interface gráfica.

A interface deve apenas:

- Exibir informações
- Receber eventos
- Chamar métodos da camada Core
- Atualizar componentes visuais

Nunca implementar regras de negócio diretamente na interface.

---

## utils/

Funções auxiliares reutilizáveis.

Exemplos:

- Helpers
- Enums
- Exceptions
- Manipulação de caminhos
- Funções utilitárias

---

## assets/

Arquivos estáticos.

Exemplos:

- CSS
- JavaScript
- Ícones
- Fontes
- Imagens

Nunca adicionar código Python.

---

## templates/

Modelos HTML utilizados para gerar a arte.

O HTML deve permanecer desacoplado do Python.

O Python apenas injeta os dados.

---

## data/

Arquivos gerados pela aplicação.

Exemplos:

- SQLite
- Logs
- Imagens exportadas

---

# Estrutura das Classes

Cada classe deve possuir apenas uma responsabilidade.

Evite classes grandes.

Caso uma classe comece a crescer excessivamente, divida-a.

---

# Métodos

Os métodos devem possuir nomes claros e objetivos.

Exemplo:

```python
create_html()

publish()

update_preview()

save_database()

get_spotify()
```

Evite nomes genéricos como:

```python
run()

execute()

process()

test()
```

---

# Tipagem

Todo código novo deve possuir type hints.

Utilizar sempre que possível:

- Self
- Path
- Optional
- TypedDict
- Enum

Exemplo:

```python
def update_preview(self: Self, image: Path) -> None:
```

Nunca remover tipagem existente.

---

# Assincronismo

O projeto utiliza asyncio.

Sempre utilizar async para operações envolvendo:

- Playwright
- Banco de dados
- Requisições HTTP
- Processos demorados

Nunca bloquear a interface gráfica.

---

# Interface

Utilizar CustomTkinter.

Fluxo esperado:

```
Botão

↓

Validação

↓

Método assíncrono

↓

Atualização da Interface
```

A interface nunca deve conter processamento pesado.

---

# Banco de Dados

Utilizar SQLite.

Toda comunicação deve passar por uma camada dedicada.

Nunca executar SQL diretamente na interface.

---

# Automação

Toda automação utilizando Playwright deve permanecer isolada.

Nunca misturar código de automação com componentes da interface.

---

# HTML

A geração da arte utiliza HTML.

Todo conteúdo visual deve permanecer no HTML/CSS.

O Python apenas substitui os dados necessários.

---

# CSS

Todo estilo deve permanecer no CSS.

Nunca gerar estilos dinamicamente via Python.

---

# JavaScript

JavaScript deve ser utilizado apenas para funcionalidades da página HTML.

Nunca implementar regras da aplicação em JavaScript.

---

# Organização dos Arquivos

Cada arquivo deve possuir apenas uma responsabilidade.

Quando um arquivo crescer demais, dividir em novos módulos.

---

# Tratamento de Erros

Nunca utilizar:

```python
except:
```

Sempre utilizar:

```python
except Exception as e:
```

Criar Exceptions específicas quando fizer sentido.

---

# Logs

Toda operação importante deve possuir registro.

Exemplos:

- Inicialização
- Finalização
- Publicação
- Erros
- Banco de dados

---

# Caminhos

Sempre utilizar:

```python
Path
```

ou

```python
get_app_path()
```

Nunca utilizar caminhos absolutos.

---

# Imports

Preferir:

```python
from pathlib import Path
```

ao invés de importar módulos completos sem necessidade.

Agrupar imports conforme o padrão do Python:

1. Biblioteca padrão
2. Bibliotecas externas
3. Módulos internos

---

# Convenções de Nome

## Classes

```text
PascalCase
```

Exemplo:

```
SpotifyService
LinkedInSite
DatabaseManager
```

---

## Métodos

```text
snake_case
```

Exemplo:

```
create_html()
save_database()
publish_post()
```

---

## Variáveis

```text
snake_case
```

---

## Constantes

```text
UPPER_CASE
```

---

# Reutilização

Antes de criar qualquer função ou classe:

- Verificar se já existe implementação semelhante.
- Reutilizar código sempre que possível.
- Evitar duplicação.

---

# Dependências

Adicionar novas bibliotecas somente quando realmente necessário.

Sempre preferir a biblioteca padrão do Python.

Evitar dependências desnecessárias.

---

# Interface Visual

Manter o padrão visual existente.

Características atuais:

- Tema escuro
- Interface minimalista
- Layout limpo
- Componentes alinhados
- Fonte JetBrains Mono quando aplicável

---

# Fluxo Padrão

Toda nova funcionalidade deve seguir:

```
UI

↓

Validação

↓

Core

↓

Persistência

↓

Atualização da Interface
```

Nunca inverter esta ordem.

---

# Padrões Observados no Projeto

O projeto já utiliza diversos padrões que devem ser mantidos.

## Uso consistente de Type Hints

Todo novo código deve ser tipado.

---

## Uso de Self

Métodos de classe devem utilizar:

```python
self: Self
```

sempre que possível.

---

## Uso de TypedDict

Estruturas de dados devem utilizar TypedDict quando apropriado.

---

## Uso de Enum

Valores fixos devem utilizar Enum.

Exemplos:

- BrowserEngine
- Tipos de publicação
- Status

---

## Herança

As automações seguem uma classe base.

Novas automações devem reutilizar essa estrutura.

Exemplo:

```
Site
 ├── Spotify
 ├── LinkedIn
 └── Outros Sites
```

---

## Separação de Responsabilidades

Nunca misturar:

- Interface
- Banco
- Automação
- Configuração
- Utilitários

Cada módulo possui apenas uma responsabilidade.

---

## Caminhos

Toda manipulação de arquivos deve utilizar funções centralizadas.

Evitar construir caminhos manualmente.

---

# O que Evitar

Não utilizar:

- Código duplicado
- Métodos gigantes
- Classes gigantes
- Imports desnecessários
- Caminhos absolutos
- SQL dentro da interface
- Lógica de negócio na UI
- Código bloqueante
- "except:" sem especificação
- Dependências desnecessárias

---

# Objetivo Final

Toda implementação deve priorizar:

- Legibilidade
- Simplicidade
- Organização
- Reutilização
- Escalabilidade
- Fácil manutenção

O código deve parecer escrito por uma única pessoa, mantendo consistência em nomenclatura, arquitetura e estilo ao longo de todo o projeto.