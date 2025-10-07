# Redirector

Sistema web de redirecionamento de URLs usando **slugs** e QR Codes estáticos, desenvolvido em **Django** com **Tailwind CSS**.

---

## Objetivo

Este projeto foi criado como uma forma de estudo do Django e como um auxílio para o webapp que está sendo desenvolvido na matéria de **Projeto de Sistemas**, que está disponível neste [link](https://github.com/Iohanan-Cephas/projeto_de_sistemas-2025.2/).

---

## Funcionalidades

- Criar redirecionamentos com **slug único** e URL de destino.
- Gerar **QR Code estático** para cada redirecionamento.
- Visualizar **cliques** e **último acesso** de cada redirecionamento.
- Editar ou deletar redirecionamentos no painel.
- API REST (JSON) para listar, criar, atualizar e deletar redirecionamentos.

---

## Tecnologias

- Python 3.13
- Django 5.2
- Django REST Framework
- Tailwind CSS
- qrcode (Python library)
- Banco de dados: PostgreSQL, SQLite ou outro suportado
- QR Codes armazenados em `media/qrcodes/`

---