# Bitbucket Resource Creation Plan

## Objetivo

Validar a automacao de criacao de projetos, repositorios e branches no Bitbucket Cloud antes de executar operacoes reais.

## Validacoes previstas

- Confirmar se o `BITBUCKET_WORKSPACE` esta correto.
- Confirmar se o `BITBUCKET_APP_PASSWORD` possui permissao de escrita em repositorios.
- Confirmar se o `BITBUCKET_APP_PASSWORD` possui permissao administrativa para projetos.
- Definir um nome de projeto de teste.
- Definir um nome de repositorio de teste.
- Definir uma branch de teste derivada de `master`.

## Sugestao de fluxo

1. Criar um projeto de QA temporario.
2. Criar um repositorio temporario vinculado ao projeto.
3. Criar uma branch temporaria no repositorio existente `python-automate`.
4. Registrar o resultado da API e eventuais erros.
5. Remover ou isolar recursos de teste se necessario.
