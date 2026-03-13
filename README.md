# 🍕 Pizza Price Prediction – Machine Learning Example

## [🇺🇸] English

This repository contains a simple Machine Learning project built with Python to demonstrate how a **Linear Regression model** can be used to predict pizza prices based on their diameter.

The project also includes a small **interactive web application** built with Streamlit where users can input a pizza diameter and receive an estimated price.

The goal of this repository is educational: to demonstrate a minimal but complete workflow including:

* Dataset loading
* Data visualization
* Model training
* Prediction
* Interactive web interface

---

# Using Poetry (Recommended)

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

# Dataset

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

# Machine Learning Model

This project uses:

* **Linear Regression**
* Library: scikit-learn

The model learns a linear relationship between:

```
Pizza Diameter → Pizza Price
```

---

# Testing the Model

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

# Application Screenshot

Add a screenshot of the application here.

```

```

---

# Technologies Used

Main libraries used in this project:

* Python
* pandas
* scikit-learn
* streamlit
* matplotlib

---

# [🇧🇷] Português

Este repositório contém um projeto simples de **Machine Learning em Python** que demonstra como utilizar **Regressão Linear** para prever o preço de pizzas com base no diâmetro.

O projeto também inclui uma pequena **aplicação web interativa com Streamlit**, onde o usuário pode inserir o diâmetro da pizza e receber uma estimativa de preço.

O objetivo deste repositório é educacional, demonstrando um fluxo completo e simples que inclui:

* Carregamento de dados
* Visualização
* Treinamento de modelo
* Previsão
* Interface interativa

---

# Usando Poetry

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

# Screenshot da Aplicação

Adicione aqui um print da aplicação rodando.

```

```

---

# Tecnologias Utilizadas

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
