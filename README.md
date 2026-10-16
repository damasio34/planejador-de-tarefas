# Planejador de Tarefas — Documentação Técnica

## Objetivo
Padronizar a especificação, análise e preparação de tarefas para Jira,
mantendo clareza funcional, fundamentação técnica e critérios verificáveis.

## Escopo
- Features e melhorias.
- Bugs e correções.
- Tasks técnicas.
- Sub-tasks.
- Documentação, QA, infraestrutura e DevOps.

## Estrutura
- `AGENTS.md`: instruções para agentes de IA.
- `SKILL.md`: skill instalável para planejamento de tarefas.
- `docs/padroes-de-especificacao.md`: metodologia e fundamentação.
- `docs/checklist-de-qualidade.md`: validação antes da publicação.
- `templates/modelo-tarefa-jira.md`: modelo geral.
- `templates/modelo-feature.md`: modelo para funcionalidades.
- `templates/modelo-bug.md`: modelo para defeitos.
- `tarefas/`: especificações aprovadas, um arquivo Markdown por tarefa.
- `scripts/gerar_pacote.py`: gera o ZIP de distribuição.
- `docs/fluxo-de-criacao-de-tarefas.md`: esclarecimentos, prévia e aprovação antes de salvar.

## Gerar pacote

Execute `python3 scripts/gerar_pacote.py` na raiz do repositório. O arquivo
`planejador-tarefas-docs.zip` é gerado nesta pasta e ignorado pelo Git.
O pacote inclui os documentos, modelos e especificações aprovadas em `tarefas/`.

## Gerar uma tarefa

A skill esclarece dúvidas essenciais, pergunta o nível de detalhe do passo a
passo e apresenta a especificação completa para revisão. Só após aprovação
explícita salva o conteúdo aprovado em `tarefas/`; rascunhos não são gravados.
Consulte `docs/fluxo-de-criacao-de-tarefas.md` para o fluxo e o padrão dos nomes.

## OpenCode

A skill está definida em `SKILL.md`. No repositório, `.opencode/skills/planejador-de-tarefas/SKILL.md`
aponta para essa definição para habilitar a descoberta local pelo OpenCode.

## Fluxo recomendado
1. Identificar objetivo, problema e resultado esperado.
2. Levantar contexto técnico e informações ausentes.
3. Identificar tipo de tarefa e áreas envolvidas.
4. Documentar escopo, regras, restrições e dependências.
5. Definir critérios de aceite verificáveis.
6. Descrever uma sequência de implementação e validação.
7. Revisar a completude usando o checklist.
8. Adaptar o documento aos padrões efetivos do repositório e do Jira.

## Importante
Esta documentação define padrões de especificação, não a arquitetura
de uma aplicação específica. Tecnologias, comandos, diretórios, contratos,
convenções de branches e pipelines devem ser confirmados no repositório.
