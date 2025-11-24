# 🧠 Agente NL ↔ Lógica Proposicional (CPC)

## 📘 Descrição  
O **Agente NL ↔ Lógica Proposicional** é uma aplicação web capaz de traduzir frases escritas em **Linguagem Natural (NL)** para **Lógica Proposicional (Cálculo Proposicional Clássico – CPC)** e também converter expressões lógicas de volta para linguagem natural.

O usuário pode ainda definir os significados de **P, Q, R, S**, tornando o sistema flexível e personalizável.

---

## 🧑‍💻 Criado por  dd
- Felipe Gabriel Vieira Meira 
- Eduardo Pimenta

---

## 🎯 Objetivo do Sistema  
- Traduzir expressões da linguagem natural para lógica proposicional.  
- Traduzir lógica proposicional para linguagem natural.  
- Permitir que o usuário defina o significado das proposições básicas (P, Q, R, S).  
- Apresentar os conectivos formais de maneira simples e clara.

---

## 🧩 Requisitos Atendidos  
- Interface web simples  
- Tradução NL → Lógica  
- Tradução Lógica → NL  
- Suporte aos conectivos: ∧, ∨, ¬, →, ↔  
- Suporte à substituição dos significados de P, Q, R, S  
- Compatível com frases compostas e negações  

---

## 🛠 Tecnologias Utilizadas  
- **Python (Flask)**  
- **SymPy** (manipulação de conectivos lógicos)  
- **HTML/CSS**  
- Hospedagem possível: Render, Vercel, Replit ou Streamlit Cloud  

---

# 🏗 Arquitetura do Sistema

### 1. Interface Web  
Formulário HTML onde o usuário insere frases, expressões e significados.

### 2. Módulo NL → Lógica (nl.py)  
Transforma frases em símbolos formais (∧, ∨, ¬, →…).

### 3. Módulo Lógica → NL (logica.py)  
Transforma expressões simbólicas em frases explicadas.

### 4. Banco de Significados  
Armazena os valores de P, Q, R e S definidos pelo usuário.

### 5. Backend Flask (app.py)  
Faz a ponte entre a interface e os módulos de tradução.

### 6. Renderização Final  
Exibe o resultado na tela do usuário.

---

# 🧩 Código Base Utilizado (Resumo)

O arquivo `app.py` gerencia:

- o tipo de tradução desejada (NL ou lógica)  
- o texto de entrada  
- os significados de P, Q, R, S  
- a conversão através das funções:

```
nl_to_logic()
logic_to_nl()
substituir_proposicoes()
```

O Flask então retorna o texto traduzido.

---

# 🧠 Estratégia de Tradução

## 🔵 NL → Lógica  
Substituição direta baseada em palavras-chave:

| Linguagem Natural | Lógica |
|-------------------|--------|
| e | ∧ |
| ou | ∨ |
| não | ¬ |
| se (...) então | → |
| se e somente se | ↔ |

Exemplo:  
**“se P então não Q” → “P → ¬Q”**

---

## 🔴 Lógica → NL  
Conversão dos símbolos para texto:

| Símbolo | Linguagem Natural |
|---------|-------------------|
| ∧ | e |
| ∨ | ou |
| ¬ | não |
| → | então |
| ↔ | se e somente se |

Se o usuário definir:  
P = "Está chovendo"  
Q = "Vou sair"  

Expressão:  
**P → Q**  
Resultado:  
**“Está chovendo então Vou sair”**

---

# 📝 Exemplos de Tradução

## ✔ NL → Lógica
| Entrada | Saída |
|---------|-------|
| P e Q | P ∧ Q |
| não P ou Q | ¬P ∨ Q |
| se P então Q | P → Q |

## ✔ Lógica → NL
| Entrada | Saída |
|---------|--------|
| ¬P ∧ Q | não P e Q |
| P ↔ Q | P se e somente se Q |
| (P ∨ R) → Q | (P ou R) então Q |

---

# ⚠ Limitações
- Não interpreta frases ambíguas ou muito longas.  
- Não detecta automaticamente proposições em textos complexos.  
- Tradução baseada em substituições simples.  

---

# 🚀 Melhorias Futuras
- Implementar NLP com spaCy ou transformers.  
- Gerar árvores sintáticas.  
- Criar tabelas verdade automaticamente.  
- Interface com design moderno.  

---