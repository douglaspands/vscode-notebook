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
### Chrome + Chromedriver (Ubuntu)
É necessario fazer a instalação das seguintes dependencias do SO Linux (Ubuntu):
1) Instale o Google Chrome
```sh
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    sudo apt install ./google-chrome-stable_current_amd64.deb -y && \
    google-chrome --version
```
2) Instale o Chromedriver baseado na versão no Google-Chrome. Nesse momento a versão é a `108.0.5359.71`:
```sh
wget https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    sudo mv chromedriver /usr/bin/chromedriver && \
    sudo chown root:root /usr/bin/chromedriver && \
    sudo chmod +x /usr/bin/chromedriver
```
> - [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
