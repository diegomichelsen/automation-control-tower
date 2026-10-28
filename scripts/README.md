# scripts/

Scripts utilitários executados manualmente ou por agendamento: importação de dados, cargas iniciais, manutenção.

Convenções:

- Nomes em inglês e em snake_case (ex.: `import_transactions.py`).
- Caminhos sempre relativos à raiz do projeto, nunca à sua pasta pessoal.
- Credenciais lidas do `.env`, nunca escritas no código.
