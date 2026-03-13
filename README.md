# 🍕 Pizza Price Prediction – Machine Learning Example

## 🇺🇸 English

This repository contains a simple Machine Learning project built with Python to demonstrate how a **Linear Regression model** can be used to predict pizza prices based on their diameter.

The project also includes a small **interactive web application** built with Streamlit where users can input a pizza diameter and receive an estimated price.

The goal of this repository is educational: to demonstrate a minimal but complete workflow including:

* Dataset loading
* Data visualization
* Model training
* Prediction
* Interactive web interface

---

# 📂 Project Structure

```
MLrepository
│
├── app.py                # Streamlit application
├── pizza.csv             # Dataset used for training
├── PizzaAnalysis.ipynb   # Notebook with data exploration
├── pyproject.toml        # Poetry configuration
├── requirements.txt      # Alternative dependency installation
└── README.md
```

---

# ⚙️ Environment Setup

This project supports **two installation methods**:

* Poetry (recommended)
* pip + requirements.txt

---

# Method 1 — Using Poetry (Recommended)

## 1. Install Poetry

If Poetry is not installed:

```bash
pip install poetry
```

Verify installation:

```bash
poetry --version
```

---

## 2. Install Dependencies

Inside the project folder:

```bash
poetry install
```

This will automatically:

* Create a virtual environment
* Install all project dependencies

---

## 3. Activate the Virtual Environment

Run:

```bash
poetry shell
```

---

## 4. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# Method 2 — Using pip

If you prefer using pip:

## 1. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run the Application

```bash
streamlit run app.py
```

---

# 📊 Dataset

The dataset used in this example is extremely simple:

| Diameter (cm) | Price (R$) |
| ------------- | ---------- |
| 20            | 50         |
| 22            | 55         |
| 24            | 60         |
| ...           | ...        |
| 40            | 100        |

The model learns the relationship between pizza diameter and price.

---

# 🧠 Machine Learning Model

This project uses:

* **Linear Regression**
* Library: scikit-learn

The model learns a linear relationship between:

```
Pizza Diameter → Pizza Price
```

---

# 🧪 Testing the Model

1. Run the Streamlit app
2. Enter a pizza diameter
3. Click **Predict Price**

The model will estimate the price.

Example:

```
Diameter: 30 cm
Estimated Price: R$ 75.00
```

---

# 📸 Application Screenshot

Add a screenshot of the application here.

```
[ PLACE APPLICATION SCREENSHOT HERE ]
```

Example location suggestion:

```
docs/app-preview.png
```

---

# 📚 Technologies Used

Main libraries used in this project:

* Python
* pandas
* scikit-learn
* streamlit
* matplotlib

---

# 🎯 Educational Purpose

This repository was created to practice and document basic Machine Learning concepts including:

* Regression models
* Data visualization
* Model training
* Interactive ML applications

---

# 🇧🇷 Português

Este repositório contém um projeto simples de **Machine Learning em Python** que demonstra como utilizar **Regressão Linear** para prever o preço de pizzas com base no diâmetro.

O projeto também inclui uma pequena **aplicação web interativa com Streamlit**, onde o usuário pode inserir o diâmetro da pizza e receber uma estimativa de preço.

O objetivo deste repositório é educacional, demonstrando um fluxo completo e simples que inclui:

* Carregamento de dados
* Visualização
* Treinamento de modelo
* Previsão
* Interface interativa

---

# 📂 Estrutura do Projeto

```
MLrepository
│
├── app.py
├── pizza.csv
├── PizzaAnalysis.ipynb
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# ⚙️ Configuração do Ambiente

Este projeto pode ser executado de duas formas:

* Usando **Poetry** (recomendado)
* Usando **pip + requirements.txt**

---

# Método 1 — Usando Poetry

## 1. Instalar Poetry

```bash
pip install poetry
```

Verifique se foi instalado:

```bash
poetry --version
```

---

## 2. Instalar Dependências

Dentro da pasta do projeto:

```bash
poetry install
```

O Poetry irá:

* Criar um ambiente virtual automaticamente
* Instalar todas as dependências do projeto

---

## 3. Ativar o Ambiente Virtual

```bash
poetry shell
```

---

## 4. Rodar a Aplicação

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador.

---

# Método 2 — Usando pip

## 1. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar ambiente:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 3. Executar aplicação

```bash
streamlit run app.py
```

---

# 📸 Screenshot da Aplicação

Adicione aqui um print da aplicação rodando.

```
[ COLOCAR PRINT DA APLICAÇÃO AQUI ]
```

Sugestão:

```
docs/app-preview.png
```

---

# 📚 Tecnologias Utilizadas

Principais bibliotecas usadas:

* Python
* pandas
* scikit-learn
* streamlit
* matplotlib

---

# 🎯 Objetivo Educacional

Este projeto foi criado para estudar conceitos básicos de Machine Learning, incluindo:

* Regressão
* Visualização de dados
* Treinamento de modelos
* Aplicações interativas com ML