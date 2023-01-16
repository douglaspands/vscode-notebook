# vscode-notebook
Projeto de Jupyter Notebook configurado no VSCode.

## Como usar
### Requisitos
- Python >=3.9
- Poetry

### Instalar dependencias
```sh
poetry install
```

## Notebooks
- [Download de manga do MangaLivre](./notebooks/mangalivre.ipynb)
- [Download de video do Youtube](./notebooks/youtube.ipynb)

## Dependencias Importantes
### Dependencias do SO
É necessario ter o `Google-Chrome` instalado.

se necessario, a instalação do `Chrome` no `Ubuntu` de forma manual:
```sh
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    sudo apt install ./google-chrome-stable_current_amd64.deb -y && \
    google-chrome --version
```

### Dependencias do Python
Se tiver o `python-poetry`:
```sh
poetry install
```
