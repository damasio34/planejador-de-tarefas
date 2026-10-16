# Fluxo de criação, revisão e gravação

## 1. Esclarecer antes de especificar

Quando não estiver claro qual problema deve ser resolvido, qual resultado se
espera ou quais limites mudam a solução, faça perguntas objetivas e aguarde as
respostas antes de redigir a tarefa. Não invente detalhes para atender à
urgência nem trate uma hipótese como fato.

Quando uma lacuna não impedir uma especificação segura, registre-a como
pendência ou premissa e identifique-a explicitamente. Tecnologias, componentes,
contratos, integrações e dependências só podem ser afirmados com evidências no
repositório ou no contexto fornecido.

## 2. Confirmar o nível de detalhe

Antes de redigir, pergunte se o passo a passo deve descrever todas as etapas de
implementação e validação em detalhe ou somente os principais marcos. Não
repita a pergunta se a pessoa já informou a preferência. A especificação deve
respeitar a granularidade escolhida, sem inventar etapas técnicas específicas.

## 3. Apresentar uma prévia integral

Depois de esclarecer bloqueios, mostre a tarefa completa no chat, no formato
de `SKILL.md` e no modelo aplicável. Identifique o bloco com **“Prévia — ainda
não salva em `tarefas/`”** e informe o caminho proposto para o arquivo.

A prévia é exatamente o conteúdo a gravar. Peça aprovação explícita da versão
e do caminho. “Crie a tarefa”, urgência, aprovação do requisito ou respostas a
perguntas de esclarecimento não autorizam por si só a gravação da prévia.

Se forem solicitadas alterações, atualize a especificação inteira e apresente
uma nova prévia. Cada versão alterada precisa de nova aprovação explícita.
Confira se o caminho proposto está livre antes de pedir aprovação.

## 4. Gravar após aprovação

Somente após a pessoa aprovar a prévia, salve exatamente o conteúdo aprovado
como Markdown em `tarefas/`. Use o padrão
`AAAA-MM-DD-titulo-em-kebab-case.md`. Nunca sobrescreva outra tarefa. Se o
caminho ficar ocupado depois da prévia, proponha um nome livre com sufixo
numérico e peça aprovação da prévia com esse novo caminho antes de gravar.

Após gravar, confirme o caminho. Não declare que o arquivo foi criado sem
verificar a gravação. Especificações aprovadas anteriores permanecem na pasta.

## Exemplo ilustrativo

**Pedido inicial:** “Quero exportar relatórios.” Antes de redigir, pergunte quais relatórios, formato, campos e comportamento dos filtros são esperados, além da preferência de granularidade dos passos.

**Respostas ilustrativas:** exportar o relatório de despesas atualmente aberto em CSV UTF-8; preservar filtros e colunas visíveis; manter as permissões atuais; descrever somente os principais marcos.

**Prévia — ainda não salva em `tarefas/`**

### Exportar o relatório de despesas em CSV

- **Tipo:** Feature
- **Contexto técnico:** relatórios; componentes e contrato técnico a confirmar
  por inspeção do repositório.
- **Descrição e objetivo:** exportar em CSV UTF-8 o relatório de despesas
  atualmente aberto.
- **Escopo e regras relevantes:** preservar os filtros e colunas visíveis;
  usar as permissões atuais, sem introduzir regras novas.
- **Critérios de aceite:** o CSV contém os registros filtrados e as colunas
  visíveis no relatório no momento da exportação.
- **Passo a passo sugerido (marcos principais):** inspecionar o fluxo atual;
  definir integração compatível com o repositório; implementar; validar dados
  e filtros.
- **Dependências e pontos de atenção:** identificar componentes e contratos
  existentes antes de definir a integração.
- **Pendências e premissas:** nenhuma pendência funcional; a abordagem técnica
  depende da inspeção do repositório.

**Pergunta:** “Aprova salvar esta versão em
`tarefas/AAAA-MM-DD-exportar-relatorios.md`?”

Uma resposta explícita de aprovação autoriza gravar esse conteúdo. O exemplo é
apenas demonstrativo: nenhum arquivo deve ser criado a partir dele.
