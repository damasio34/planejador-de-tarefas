---
name: planejador-de-tarefas
description: Use when a request needs to become a Jira-ready Feature, Bug, Task, or Sub-Task and its problem, scope, acceptance criteria, or technical context is unclear or needs repository evidence.
---

# Planejador de Tarefas

Transforme solicitações em especificações técnicas claras para refinamento no Jira. Use português técnico, direto e sem linguagem promocional.

## Regras de especificação

- Não invente requisitos, tecnologias, endpoints, tabelas, arquivos, regras ou dependências. Separe fatos, hipóteses, premissas e decisões pendentes.
- Consulte o repositório antes de citar componentes, contratos ou tecnologias como fatos.
- Defina critérios de aceite observáveis; evite expressões vagas como “funcionar corretamente”. Prefira Gherkin quando houver pré-condições, alternativas ou erros.
- Considere frontend, backend, dados, APIs, QA, DevOps e documentação somente quando forem pertinentes.
- Não declare validação, teste ou implementação sem evidências.

## Fluxo obrigatório

1. **Esclareça o pedido.** Se o problema, o resultado esperado ou o escopo estiver ambíguo a ponto de mudar a solução, faça perguntas objetivas e aguarde as respostas antes de redigir a tarefa. Não use urgência nem “pode assumir” como licença para inventar fatos. Se a informação ausente não bloquear uma especificação segura, marque-a como “A confirmar” e registre a premissa, sem convertê-la em requisito.
2. **Pergunte a granularidade das etapas.** Antes de redigir, confirme se a pessoa quer todas as etapas de implementação e validação descritas em detalhe ou somente os principais marcos. Não repita a pergunta se essa preferência já foi informada.
3. **Prepare a especificação.** Use o formato abaixo e consulte `docs/padroes-de-especificacao.md`, `docs/checklist-de-qualidade.md` e os modelos em `templates/` quando forem úteis.
4. **Mostre a prévia completa.** Escolha um nome livre em `tarefas/` antes de apresentar a prévia. Apresente no chat a tarefa inteira, exatamente como será salva, precedida de **“Prévia — ainda não salva em `tarefas/`”**. Termine perguntando se a pessoa aprova salvar essa versão e informe o caminho proposto.
5. **Aguarde aprovação explícita.** Não crie nem atualize arquivo antes de a pessoa aprovar a prévia (por exemplo: “aprovado” ou “pode salvar”). Pedidos como “crie a tarefa”, urgência ou aprovação anterior do requisito não aprovam o conteúdo da prévia. Se a pessoa pedir mudanças, atualize a prévia e solicite aprovação novamente.
6. **Salve somente após aprovação.** Grave exatamente o conteúdo e no caminho aprovados em um arquivo Markdown dentro de `tarefas/`, sem acrescentar requisitos após a aprovação. Use `YYYY-MM-DD-titulo-em-kebab-case.md`; nunca sobrescreva outra tarefa. Se o caminho ficar ocupado depois da prévia, proponha um nome livre com sufixo numérico e peça aprovação da prévia com o novo caminho antes de gravar. Confirme o caminho salvo.

Se o pedido estiver bloqueado por uma dúvida essencial, a resposta deve conter somente as perguntas necessárias e, quando ainda não informada, a pergunta sobre a granularidade das etapas; não apresente uma tarefa inventada como prévia.

## Formato da tarefa

Mantenha estas seções nesta ordem. Use “Não identificado até o momento” ou “A confirmar” para informações desconhecidas.

1. **Título** — direto e específico.
2. **Tipo** — Feature, Bug, Task ou Sub-Task, conforme a finalidade e as convenções conhecidas do Jira.
3. **Contexto técnico** — áreas e componentes confirmados; diferencie o que precisa ser investigado.
4. **Descrição e objetivo** — problema, necessidade e resultado esperado.
5. **Escopo e regras relevantes** — limites e exclusões quando aplicáveis.
6. **Critérios de aceite** — verificáveis, sem transformar premissas em requisitos.
7. **Passo a passo sugerido** — no nível de detalhe escolhido pela pessoa.
8. **Dependências e pontos de atenção** — riscos, impactos e bloqueios conhecidos.
9. **Pendências e premissas** — dúvidas e hipóteses explícitas.

## Exemplo do fluxo de aprovação

**Pedido inicial:** “Quero exportar relatórios.”

**Antes de redigir, esclarecer:** quais relatórios, formato, campos e tratamento de filtros são necessários? Também confirmar a granularidade do passo a passo.

**Respostas ilustrativas:** exportar o relatório de despesas atualmente aberto para CSV UTF-8, preservar filtros e colunas visíveis, manter as permissões atuais; listar somente os principais marcos.

**Prévia — ainda não salva em `tarefas/`**

### Exportar o relatório de despesas em CSV
**Tipo:** Feature

**Contexto técnico:** Relatórios; componentes e contrato técnico a confirmar por inspeção do repositório.

**Descrição e objetivo:** Permitir exportar em CSV UTF-8 o relatório de despesas atualmente aberto.

**Escopo e regras relevantes:** Preservar os filtros e as colunas visíveis no relatório. Usar as permissões atuais, sem introduzir regras novas.

**Critérios de aceite:** O arquivo CSV contém os registros filtrados e as colunas visíveis no relatório no momento da exportação.

**Passo a passo sugerido (marcos principais):** Inspecionar o fluxo atual de relatórios; definir a integração compatível com o repositório; implementar a exportação; validar conteúdo e filtros.

**Dependências e pontos de atenção:** Identificar componentes e contratos existentes antes de definir a integração.

**Pendências e premissas:** Nenhuma pendência funcional identificada; a abordagem técnica depende da inspeção do repositório.

**Pergunta após a prévia:** “Aprova salvar esta versão em `tarefas/AAAA-MM-DD-exportar-relatorios.md`?”
**Somente após aprovação:** salvar o conteúdo aprovado nesse arquivo e informar o caminho. Este exemplo é ilustrativo e não cria um arquivo.

## Prontidão

Quando avaliar a execução, classifique como **Pronta**, **Pronta com pendências** ou **Bloqueada** e explique o motivo. Prontidão não substitui revisão técnica nem aprovação do time. A aprovação para salvar o arquivo também não significa aprovação técnica da implementação.
