# 📊 Consulta de CNPJs em Lote

Este projeto permite consultar informações de múltiplos CNPJs utilizando a API pública da BrasilAPI, retornado o CNAE.

---

## 💡 Motivação

Este projeto surgiu a partir de uma necessidade prática.  

Durante uma análise de dados, foi necessário consultar uma grande quantidade de CNPJs manualmente, pois a base disponível possuía diversos registros com CNAEs inválidos ou inconsistentes, esse processo manual acabou sendo extremamente demorado e ineficiente.

Então, durante meus estudo de Python, assisti um curso em que o professor utilizava uma API para consultar CEPs automaticamente. A partir disso, pensei: se é possível consultar dados públicos de CEP, também deve ser possível consultar dados públicos de CNPJ.

Com isso, foi desenvolvido este script para automatizar o processo, tornando a coleta de dados mais rápida, confiável e escalável.

---

## 🚀 Funcionalidades

* Consulta individual ou em lote de CNPJs

* Entrada via:

  * Arquivo `.txt` (um CNPJ por linha)
  * Digitação manual

* Retorno com:

  * CNPJ
  * Razão Social
  * CNAE Fiscal

* Exportação automática para CSV

* Resumo de sucessos e erros

---

## 🧰 Tecnologias utilizadas

* Python 3.x
* Requests
* CSV (nativo)
* API: https://brasilapi.com.br/

---

## 🧾 Formas de entrada

### 🔹 Opção 1: Arquivo `.txt`

* Um CNPJ por linha
* Exemplo:

```
12345678000199
98765432000188
```

---

### 🔹 Opção 2: Entrada manual

* Separados por vírgula:

```
12345678000199, 98765432000188
```

* Ou digitando linha por linha

---

## 📁 Saída

O sistema gera automaticamente um arquivo CSV com o formato:

```
resultado_cnpjs_YYYYMMDD_HHMMSS.csv
```

---

## ⚠️ Observações

* A API pode limitar requisições em alta escala
* CNPJs inválidos retornarão erro no status
