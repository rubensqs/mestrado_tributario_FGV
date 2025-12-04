# mestrado_tributario_FGV
---
# Análise de Transações Individuais – PGFN (2024)

Este repositório contém os dados e scripts utilizados na análise das **transações individuais firmadas pela Procuradoria-Geral da Fazenda Nacional (PGFN) no ano de 2024**, conforme informações disponibilizadas na ferramenta oficial [Painel de Negociações da PGFN](https://www.gov.br/pgfn/pt-br/assuntos/divida-ativa-da-uniao/transparencia-fiscal-1/bem-vindo-ao-painel-dos-parcelamentos).

## 📊 Origem dos Dados
- Os dados foram **baixados diretamente da ferramenta da PGFN em 27 de novembro de 2025**.  
- Há um arquivo correspondente a cada estado da federação, conforme a apresentação do *Painel de Negociações*.  
- Foram utilizados **24 arquivos em formato CSV**, pois, nesta data, a plataforma informava não haver transações registradas para os estados do **Acre, Amapá e Roraima**.  

## 🔎 Filtros Aplicados
Na extração dos dados, foram selecionadas as seguintes opções disponíveis na plataforma:
- **Ano de concessão:** 2024  
- **Tipo de negociação:** Transação Individual (*Depende de Prévia Aprovação do PDA da Região*)  
- **UF do Devedor:** todos os estados da federação  

## 🛠️ Processamento
- O tratamento e análise dos dados foram realizados em **Python**, utilizando a biblioteca **pandas**.  
- Os scripts disponibilizados neste repositório permitem a reprodução integral das etapas de processamento e análise, garantindo transparência e verificabilidade.  

## 🎯 Finalidade
Este repositório foi criado para fins acadêmicos, como parte da dissertação apresentada à Escola de Direito de São Paulo da Fundação Getúlio Vargas, como requisito para obtenção de título de Mestre em Direito Tributário.  
A disponibilização pública tem como objetivo **permitir a verificação por pares** e assegurar a reprodutibilidade dos resultados apresentados.  

---

English version of the README:

---

# Analysis of Individual Transactions – PGFN (2024)

This repository contains the datasets and scripts used in the analysis of **individual transactions executed by the Office of the Attorney General of the National Treasury (PGFN) in 2024**, based on information made available through the official [PGFN Negotiations Dashboard](https://www.gov.br/pgfn/pt-br/assuntos/divida-ativa-da-uniao/transparencia-fiscal-1/bem-vindo-ao-painel-dos-parcelamentos).

## 📊 Data Source
- The data were **downloaded directly from the PGFN dashboard on November 27, 2025**.  
- Each file corresponds to one Brazilian state, following the structure presented in the *Negotiations Dashboard*.  
- A total of **24 CSV files** were used, since on that date the platform indicated that no transactions were registered for the states of **Acre, Amapá, and Roraima**.  

## 🔎 Filters Applied
The following filters were selected during data extraction:
- **Grant year:** 2024  
- **Type of negotiation:** Individual Transaction (*Subject to Prior Approval of the Regional PDA*)  
- **Debtor’s State (UF):** all states of the federation  

## 🛠️ Data Processing
- Data cleaning and analysis were performed using **Python** and the **pandas** library.  
- The scripts provided in this repository reproduce all processing steps, ensuring transparency and reproducibility.  

## 🎯 Purpose
This repository was created as part of a master’s dissertation, in compliance with ABNT academic standards.  
Its public availability aims to **enable peer verification** and guarantee the reproducibility of the results presented.  

---

Would you like me to also add a short section with instructions on how someone can run your scripts (e.g., Python version, required libraries, and a quick start example)? That would make the README even more practical for reviewers.
