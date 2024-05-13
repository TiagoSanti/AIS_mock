# <p align="center">Online Evidence Grabber<br/></p>

<p align="center">
  <img src="logo.png" height="175px" />
  <br/>
  <small>Logo ou screenshot da aplicação</small>
</p>

Este repositório armazena os artefatos da aplicação Online Evidence Grabber desenvolvida durante as atividades da disciplina de Prática de Desenvolvimento de Software I em 2024.1.

## Estrutura do documento

- [Online Evidence Grabber](#online-evidence-grabber)
  - [Estrutura do documento](#estrutura-do-documento)
  - [Descrição do Projeto](#descrição-do-projeto)
  - [Funcionalidades](#funcionalidades)
  - [Requisitos e Dependências](#requisitos-e-dependências)
  - [Building](#building)
  - [Autores](#autores)
  - [Licença](#licença)

## Descrição do Projeto

## Funcionalidades

## Requisitos e Dependências

Para a execução do código são necessárias as seguintes dependências:

- Python (versão 3.12.2)
- MongoDB (versão 7.0.8)

Para instalar as dependências de bibliotecas do Python, execute o comando abaixo:

```cmd
pip install -r requirements.txt
```

Então a aplicação pode ser executada com o comando:

```cmd
python -m src.main
```

Para executar a API, execute o comando:

```cmd
python -m uvicorn src.api:app --reload --port 8000
```

## Building

Para criar o executável da aplicação, siga os passos:

1. Instale o Python (versão 3.12.2)
2. Instale o PyInstaller usando pip com o comando:

    ```cmd
    pip install pyinstaller
    ```

3. Execute o comando abaixo a partir do diretório raiz do repositório:

   ```cmd
   pyinstaller --distpath ./dist --workpath ./build --specpath ./build -n "Online Evidence Grabber" --paths "./src" -w -y --clean --onefile ./src/main.py
   ```

 	Os detalhes dos parâmetros estão na [documentação do PyInstaller](https://pyinstaller.org/en/stable/usage.html#using-pyinstaller).

4. Após a execução, o executável estará localizado em ```dist/Online Evidence Grabber.exe```

## Autores

Este sistema foi desenvolvido pela seguinte equipe:

- [Gabriel Alexandre Dede Galassi Da Silva](https://github.com/GabrielDedeGalassi)
- [João Paulo Da Silva Dantas](https://github.com/jpdants)
- [João Pedro Figueiredo De Oliveira](https://github.com/joaoPedro-OliveiraFigueiredo)
- [Matheus Rodrigues Cavalcanti Goncalves](https://github.com/MatheusRCG)
- [Matheus Silva Oliveira](https://github.com/oliveiramatheus212)
- [Tiago Clarintino Santi](https://github.com/TiagoSanti)

Orientado pela professora [Maria Istela Cagnin Machado](https://github.com/beltrano-silva) e proposto por XXXX YYYY.

## Licença

Este sistema está disponível sob a licença [XXXX](https://opensource.org/licenses/).
