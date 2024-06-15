# Aplicativo Android com BeeWare e Toga

Este é um aplicativo Android desenvolvido em Python utilizando as bibliotecas BeeWare e Toga. O objetivo deste projeto é demonstrar como construir aplicativos móveis nativos usando ferramentas de código aberto, para o curso ADS do SENAI'SC

## Dependências

Para desenvolver e rodar este projeto, você precisará das seguintes ferramentas e bibliotecas:

- **Python**: A linguagem de programação utilizada.
- **BeeWare**: Um conjunto de ferramentas para construir aplicativos multiplataforma em Python.
- **Toga**: A biblioteca de UI do BeeWare para criar interfaces gráficas nativas.

Você pode instalar todas as dependências usando o seguinte comando:

```bash
pip install beeware
```

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/mur1lo/currency_converter.git
```

2. Navegue até o diretório do projeto:

```bash
cd currency_converter
```

3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

4. Certifique-se de que você tem todas as ferramentas necessárias para compilar para Android. Você pode seguir as instruções no [BeeWare Android tutorial](https://docs.beeware.org/en/latest/tutorial/tutorial-5/android.html).

## Como Rodar

Para rodar o aplicativo em um dispositivo Android, siga os passos abaixo:

1. Prepare o ambiente Android com as ferramentas do BeeWare:

```bash
briefcase create android
```

2. Compilar o projeto para Android:

```bash
briefcase build android
```

3. Instale e execute o aplicativo em um dispositivo Android conectado:

```bash
briefcase run android
```

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
meu_app/
│
├── src
|   ├── currency_converter
│     ├── __init__.py
│     ├── app.py
│     └── resources
│         └── icon.png
│
├── android
│   └── ...
│
├── LICENSE
├── README.md
└── requirements.txt
```

- `src/`: Contém o código fonte do aplicativo.
- `src/currency_converter/app.py`: O arquivo principal do aplicativo, onde a lógica principal é implementada.
- `src/currency_converte/resources/`: Contém recursos como ícones e imagens.
- `android/`: Contém arquivos específicos para a compilação Android.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Contribuição

Se você deseja contribuir com o projeto, por favor, siga os seguintes passos:

1. Fork o repositório.
2. Crie um novo branch com a sua feature (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona minha feature'`).
4. Faça push para o branch (`git push origin minha-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
