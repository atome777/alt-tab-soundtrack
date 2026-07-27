# 🎧 Alt+Tab Soundtrack

Uma aplicação desktop desenvolvida em Python para automatizar a criação e publicação da série **Alt+Tab Soundtrack** no LinkedIn.

O projeto permite gerar imagens do post, organizar os dados das músicas e publicar automaticamente no LinkedIn, reduzindo um processo manual que levava vários minutos para apenas alguns cliques.

## ✨ Funcionalidades

- 🎵 Busca informações de músicas através do link do Spotify
- 🖼️ Geração automática da arte do post em HTML
- 👀 Pré-visualização da imagem antes da publicação
- 📅 Agendamento da data da postagem
- 🤖 Publicação automática no LinkedIn utilizando Playwright
- 💾 Armazenamento dos posts em SQLite
- 🎨 Interface gráfica desenvolvida com CustomTkinter
- ⚡ Operações assíncronas utilizando asyncio

---

## 📸 Fluxo

1. Informar o link da música no Spotify
2. Buscar automaticamente:
   - Nome da música
   - Artista
   - Capa do álbum
3. Preencher:
   - Situação relacionada à música
   - Curiosidade
4. Gerar a arte do post
5. Visualizar o resultado
6. Publicar automaticamente no LinkedIn

---

## 🛠️ Tecnologias

- Python 3.13+
- CustomTkinter
- Playwright
- aiosqlite
- Pillow
- asyncio

---

## 📂 Estrutura do projeto

```
src/
├── database/
├── services/
├── ui/
├── utils/
├── html/
├── output/
└── main.py
```

---

## 🚀 Instalação

Clone o projeto

```bash
git clone https://github.com/atome777/alt-tab-soundtrack.git
```

Entre na pasta

```bash
cd alt-tab-soundtrack
```

Instale as dependências Windows

```bash
install_requirements.bat
```

Instale as dependências Linux

```bash
install_requirements.sh
```

Ative o ambiente

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```


Execute o projeto

```bash
python src/main.py
```

---

## 📌 Roadmap

- [x] Interface gráfica
- [x] Integração com Spotify
- [x] Geração da imagem
- [x] Publicação automática no LinkedIn
- [x] Banco de dados SQLite
- [ ] Agendamento automático de publicações
- [ ] Histórico de postagens
- [ ] Exportação dos posts
- [ ] Suporte a múltiplas redes sociais

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

Caso tenha alguma sugestão ou encontre algum problema, abra uma *Issue* ou envie um *Pull Request*.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

---

## Autor

Desenvolvido por **atome**

Projeto criado para automatizar a série de posts **Alt+Tab Soundtrack** publicada no LinkedIn.