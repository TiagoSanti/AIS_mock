# Branch Model: GitHub Flow

O GitHub Flow é um modelo de fluxo de trabalho (workflow) para o desenvolvimento de software utilizando o sistema de controle de versão Git e a plataforma GitHub. Os princípios-chave do GitHub Flow são:
- Branches: Cada nova funcionalidade, correção de bug ou tarefa é desenvolvida em uma branch separada. Essa prática permite que várias pessoas trabalhem em diferentes partes do projeto simultaneamente, sem interferir no trabalho umas das outras.
- Commits frequentes: Os desenvolvedores são encorajados a fazer commits frequentes em suas branches locais à medida que trabalham em uma funcionalidade ou correção. Isso ajuda a manter um histórico detalhado do progresso e permite que outros membros da equipe vejam as mudanças em andamento.
- Pull Requests: Quando um desenvolvedor conclui uma funcionalidade ou correção em sua branch, ele abre um Pull Request (PR) para mesclar suas alterações na branch principal do repositório. O PR é uma forma de iniciar uma discussão com outros membros da equipe, revisar o código e fornecer feedback antes de mesclar as alterações.
- Revisões de código: Os membros da equipe podem revisar o código enviado por meio dos Pull Requests. Eles podem fazer comentários, solicitar alterações ou aprovar o PR. A revisão de código é uma etapa importante para garantir a qualidade do código e compartilhar conhecimento entre os membros da equipe.

## Tomada de decisão

O GitHub Flow oferece várias vantagens como modelo de fluxo de trabalho para o desenvolvimento de software. Sua simplicidade torna fácil de entender e adotar, não exigindo ferramentas ou processos complexos. Além disso, sua flexibilidade permite que equipes trabalhem em paralelo, desenvolvendo funcionalidades independentes em suas branches separadas, facilitando a colaboração e evitando conflitos de código.

Uma das principais vantagens do GitHub Flow é a melhoria na colaboração entre os membros da equipe. Através do uso de Pull Requests, os desenvolvedores podem compartilhar seu trabalho, obter feedback e aprimorar a qualidade do código antes de mesclá-lo na branch principal. Isso não apenas identifica erros precocemente, mas também promove a consistência do código e o compartilhamento de conhecimento.

Além disso, o GitHub Flow fornece rastreabilidade e um histórico detalhado de cada funcionalidade ou correção desenvolvida em branches separadas. Isso facilita a visualização do progresso do trabalho, o acompanhamento de alterações e a possibilidade de reverter mudanças, se necessário.
Por fim, o GitHub Flow possibilita a implantação contínua das alterações assim que são concluídas e mescladas na branch principal. Essa abordagem acelera a entrega de novas funcionalidades e correções, resultando em um fluxo contínuo de valor para os usuários finais.


## Como usar
Para realizar qualquer alteração é necessário criar uma ramificação a partir da ramificação dev, mas é importante verificar se há uma ramificação aberta com o mesmo objetivo da sua atividade. Além disso, apenas as ramificações dev e "hotfix" podem ser implementadas diretamente na ramificação principal, para as outras necessidades é necessário seguir os seguintes passos:

1. Crie uma nova ramificação: para adicionar uma nova funcionalidade ao projeto, comece criando uma nova ramificação a partir da ramificação principal ("main"). Você pode nomear a ramificação de acordo com a funcionalidade que está sendo desenvolvida. Por exemplo, se você está adicionando o código do header da aplicação, você pode criar uma ramificação chamada "feature_header". 

2. Implemente as alterações: na sua nova ramificação, faça as alterações necessárias no código para realizar a sua atividade. Além disso, é importante realizar testes nas suas alterações para garantir que elas funcionem corretamente e não introduzam problemas no projeto. É recomendável realizar commits frequentes e descritivos, dividindo o trabalho em pequenas alterações lógicas. Lembre-se de usar o commit semântico, definido no documento guia de estilo de commits.

3. Abra um pull request: quando estiver pronto para enviar suas alterações para revisão e mesclá-las de volta à ramificação principal, abra um pull request. Um pull request é uma solicitação de revisão do código, na qual você pode discutir as alterações com outros membros da equipe, realizar revisões de código e resolver quaisquer problemas identificados. Além disso, caso haja dificuldade em dar continuar em uma atividade, o pull request pode ser utilizado para pedir ajuda de outros desenvolvedores do time, por exemplo, caso algum exercício peça para fazer uma recursiva e você não consegue fazer, abra um pull request e peça ajuda nesta parte.

4. Revisão do pull request: durante o processo de pull request, outros membros da equipe podem revisar suas alterações, fornecer comentários e sugestões. Você pode discutir as alterações e iterar sobre elas conforme necessário. 

5. Mescle o pull request: depois de receber aprovação e concluir todas as revisões e testes necessários, você pode mesclar o pull request na ramificação principal. Isso incorporará suas alterações à versão principal do projeto.

6. Aprovação da pull request: pelo menos duas pessoas da equipe deverá revisar a pull request aberta de outro membro para a mesclagem para a main.

7. Merge: quando a pull request tiver com duas aprovações ou mais, qualquer membro da equipe poderá dar o merge, inclusive aquele que abriu o pull request.

## Padronização da nomenclatura

A fim de manter uma nomenclatura consistente e organizada, comece o nome da ramificação com o tipo de atividade do objetivo da branch seguido de um descritor conciso da funcionalidade sendo desenvolvida. A padronização da nomenclatura ajudam a identificar rapidamente o propósito de cada ramificação, facilitando a colaboração e o entendimento do trabalho em andamento.

### Exemplos

- feature_header
- feature_exportar_relatorio
- feature_importar_dataset
- bug_correcao_da_validacao_do_tamanho_do_dataset
