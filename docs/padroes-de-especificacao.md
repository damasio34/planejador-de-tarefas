# Padrões de Especificação de Tarefas

## 1. Princípios
Uma especificação deve ser clara, objetiva, rastreável, testável e
suficiente para orientar a implementação sem impor decisões desnecessárias.

### Clareza
Descrever o problema, o resultado esperado e o contexto relevante.
Evitar expressões subjetivas, como "melhorar bastante" ou "deixar adequado".

### Rastreabilidade
Relacionar a tarefa à demanda, incidente, requisito ou componente de origem,
quando essas informações estiverem disponíveis.

### Testabilidade
Cada critério de aceite deve descrever um resultado que possa ser observado
e validado, manualmente ou por automação.

### Delimitação
Explicitar escopo e exclusões relevantes para evitar expansão não planejada.

### Fundamentação técnica
Explicar por que a mudança é necessária e quais componentes ou contratos
podem ser afetados. Não prescrever uma solução sem necessidade ou evidência.

## 2. Classificação

- **Feature:** entrega de capacidade funcional nova.
- **Bug:** comportamento que diverge de um comportamento esperado conhecido.
- **Task:** atividade técnica, operacional ou documental com resultado definido.
- **Sub-Task:** unidade de trabalho subordinada a uma tarefa maior.

A classificação deve refletir a finalidade real da demanda e as convenções
do projeto Jira utilizado.

## 3. Contexto técnico
Identificar apenas as áreas aplicáveis:
- Frontend: interface, estado, acessibilidade e interação.
- Backend: regras de negócio, serviços, validações e processamento.
- API: contratos, códigos de resposta, autenticação e compatibilidade.
- Dados: esquema, integridade, migração e consistência.
- QA: cenários, regressão, automação e evidências.
- DevOps: pipelines, infraestrutura, configuração e observabilidade.
- Documentação: contratos, procedimentos e instruções de operação.

Tecnologias e componentes específicos devem ser confirmados no projeto.

## 4. Estrutura da descrição
A descrição deve responder, quando aplicável:
- Qual é o problema ou a necessidade?
- Quem ou qual componente é afetado?
- Qual resultado deve ser alcançado?
- Quais regras e restrições são relevantes?
- Quais elementos estão fora do escopo?

## 5. Critérios de aceite
Preferir cenários Gherkin quando houver comportamento condicional,
fluxos alternativos ou necessidade de explicitar pré-condições.

Estrutura:
- Dado (Given): contexto ou pré-condição.
- Quando (When): ação ou evento.
- Então (Then): resultado observável.

Exemplo:
Dado que o usuário possui uma sessão autenticada
Quando solicita um recurso permitido para seu perfil
Então o sistema retorna o resultado esperado conforme o contrato da API

O exemplo é ilustrativo. Os detalhes reais devem refletir os requisitos
e os contratos efetivos do sistema.

Critérios devem cobrir, quando relevantes:
- fluxo principal;
- entradas inválidas e limites;
- autorização e autenticação;
- erros e indisponibilidade;
- persistência e consistência;
- compatibilidade e regressão;
- observabilidade e auditoria.

## 6. Passo a passo
Propor etapas em ordem lógica, por exemplo:
1. Inspecionar o comportamento atual e os componentes afetados.
2. Confirmar regras de negócio e contratos.
3. Definir a abordagem técnica compatível com a arquitetura existente.
4. Implementar a alteração.
5. Criar ou atualizar testes.
6. Executar validações disponíveis.
7. Atualizar documentação e evidências.
8. Revisar regressões e critérios de aceite.

Adaptar as etapas ao tipo e ao tamanho da tarefa. Não apresentar comandos
ou procedimentos específicos sem conhecer as ferramentas do projeto.

## 7. Dependências e riscos
Registrar:
- equipes ou tarefas predecessoras;
- alterações de contrato;
- migrações ou dados necessários;
- permissões e configurações;
- impactos de compatibilidade;
- riscos de segurança, desempenho e regressão;
- decisões pendentes que bloqueiem a implementação.

Não inventar dependências. Usar "a confirmar" quando necessário.

## 8. Definição de pronto para execução
Uma tarefa está suficientemente especificada quando possui objetivo claro,
escopo delimitado, critérios testáveis, contexto relevante e dependências
conhecidas ou explicitamente registradas.

A prontidão para execução não substitui revisão técnica nem aprovação do time.

## 9. Esclarecimento, prévia e aprovação para gravação

Quando o problema, o resultado esperado ou o escopo estiver ambíguo de modo
que altere a solução, perguntar e aguardar esclarecimento antes de redigir a
tarefa. Uma premissa explicitada não substitui resposta para dúvida essencial.
Lacunas não bloqueadoras podem ser registradas como “A confirmar”.

Antes de redigir, confirmar se o passo a passo deve conter todas as etapas em
detalhe ou somente os principais marcos, salvo se essa preferência já estiver
clara.

Exibir a especificação integral no chat como prévia ainda não salva e pedir
aprovação explícita antes de criar ou atualizar qualquer arquivo em `tarefas/`.
Se houver alterações solicitadas, apresentar nova prévia e pedir nova
aprovação. Após aprovada, salvar exatamente a versão aprovada, sem acrescentar
requisitos.

Usar um arquivo Markdown por tarefa em `tarefas/`, com nome
`AAAA-MM-DD-titulo-em-kebab-case.md`. Nunca sobrescrever uma especificação
existente; escolher um nome livre com sufixo numérico se houver colisão.

## 10. Granularidade do passo a passo

O nível de detalhe dos passos deve seguir a preferência confirmada pela pessoa
solicitante. Se preferir etapas completas, descreva em ordem as etapas de
análise, decisão, implementação e validação que sejam sustentadas pelas
informações disponíveis. Se preferir marcos principais, mantenha passos
concisos sem omitir dependências ou decisões bloqueadoras. Não invente
comandos, diretórios ou procedimentos específicos sem evidência no projeto.
