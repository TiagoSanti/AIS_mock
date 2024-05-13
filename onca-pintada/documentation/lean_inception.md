# Lean Inception Relâmpago

## Introdução

Este documento registra a metodologia _Lean Inception Relâmpago_[^1] utilizada na descoberta do nosso produto, etapa crucial para compreender e explorar as necessidades dos usuários, o contexto do problema e as oportunidades de mercado antes de iniciar a fase de desenvolvimento propriamente dita. 

Neste processo, realizamos 2 sessões de 3 horas para discutir, gerar e definir a visão do produto, os objetivos do projeto, as personas e o feature mapping, com todos os membros da nossa equipe, no qual buscamos coletar informações valiosas para tomar decisões informadas sobre o que construir e como construir.

A metodologia se baseia na [Lean Inception](https://www.caroli.org/lean-inception/).

Algumas atividades foram adaptadas utilizando artefatos do Lean Inception padrão retirados [deste template](https://miro.com/miroverse/lean-inception-workshop/).

[^1]: Descrição do autor da Lean Inception Relâmpago: https://www.caroli.org/inception-relampago-template-de-agenda-e-documentos-colaborativos/


## Definição

Uma Lean Inception Relâmpago é uma abordagem ágil e colaborativa para iniciar um projeto ou iniciar a fase de descoberta de um novo produto ou iniciativa. Ela se baseia nos princípios do Lean Startup e do Design Thinking para acelerar o processo de alinhamento da equipe e definição da visão do produto.

A Lean Inception Relâmpago geralmente é realizada em um curto período de tempo, que pode variar de alguns dias a uma semana. Durante esse período, a equipe multidisciplinar, que inclui membros de diferentes áreas, como desenvolvimento, design, negócios e usuários finais, trabalha em conjunto para alcançar os seguintes objetivos:

- Compreender o problema: A equipe busca um entendimento claro do problema que está sendo enfrentado e das necessidades dos usuários. Isso envolve a realização de pesquisas, entrevistas e discussões para coletar informações relevantes.

- Definir a visão do produto: Com base na compreensão do problema, a equipe trabalha para estabelecer a visão compartilhada do produto. Isso inclui a definição de metas, objetivos e resultados esperados, além de identificar os principais benefícios e valor que o produto deve fornecer.

- Priorizar e mapear funcionalidades: A equipe colabora para identificar as funcionalidades essenciais do produto que ajudarão a alcançar a visão estabelecida. Essas funcionalidades são priorizadas com base no valor para o usuário e no esforço necessário para implementá-las.

- Definir o MVP (Minimum Viable Product): O MVP é a versão mínima do produto que será desenvolvida para validar as hipóteses e fornecer valor aos usuários. Durante a Lean Inception Relâmpago, a equipe trabalha para definir as funcionalidades-chave que serão incluídas no MVP.

- Identificar riscos e restrições: A equipe também analisa e identifica os principais riscos e restrições que podem afetar o projeto ou produto, para que possam ser abordados adequadamente ao longo do desenvolvimento.

A abordagem Lean Inception Relâmpago enfatiza a colaboração intensiva da equipe, a iteração rápida e a busca por um entendimento comum. Ela ajuda a economizar tempo e esforço, ao permitir que a equipe alinhe rapidamente suas ideias e crie uma visão compartilhada do produto, reduzindo assim os riscos e incertezas iniciais.


## Glossário de termos

#### Visão

O entendimento da necessidade do produto guiará as atividades da inception. Os conceitos apresentados inicialmente são apenas uma visão, e a ideia será refinada durante a inception.

#### Objetivos

Cada membro da equipe deve compartilhar o que entende sobre os objetivos do projeto, e isto deve ser discutido para que o time alcance um consenso sobre o que é realmente importante.

#### Personas

Para efetivamente identificar as funcionalidades de um sistema, consideramos importante ter em mente os usuários e seus objetivos. A maneira que normalmente utilizamos para representar estes usuários é através de personas.

Uma persona representa um usuário do sistema, descrevendo não só o seu papel, mas também suas necessidades específicas. Isto cria uma representação realística de usuários, auxiliando o time a descrever funcionalidades do ponto de vista de quem interagirá com o produto final.

#### Features

Feature é um agrupamento de funcionalidades afins. Tal agrupamento nos ajuda com a compreensão sobre o requisito como um todo, bem como das suas partes menores e complementares. O entendimento de feature vai variar de time para time. O importante é que tal agrupamento faça sentido para aquela equipe.

#### Feature Mapping

A partir de um conjunto de features precisamos elaborar um plano de execução. Para isto, adicionamos dados de capacidade da equipe, sequenciamento lógico, prioridade e tempo. O feature mapping é uma representação visual deste plano.


## Visão do produto

Nossa visão do produto foi construída a  partir dos seguintes campos:

- Para [cliente final]: o perfil dos clientes finais ou usuários que serão beneficiados pelo seu produto. Quem são eles? Quais são suas necessidades específicas?
- Cujo [problema que precisa ser resolvido]: o problema ou desafio que os clientes finais enfrentam e que o nosso produto se propõe a resolver.
- O [nome do produto]: o nome ou título do produto. Buscando um nome que seja memorável e reflita a essência do que estamos oferecendo.
- É um [categoria do produto]: a categoria ou classificação do produto.
- Que [benefício chave, razão para adquirí-lo]: o benefício principal que os clientes finais obterão ao adquirir o produto. Quais são os pontos fortes e únicos que tornam nosso produto atraente e valioso para os clientes?
- Diferentemente da [alternativa da concorrência]: as alternativas existentes no mercado que tentam abordar o mesmo problema que do nosso produto e como o nosso produto se diferencia e se destaca em relação a essas alternativas. Quais são as vantagens competitivas do nosso produto?
- O nosso produto [diferença chave]: a diferença chave ou o valor único que o produto oferece em comparação com as alternativas existentes. Uma funcionalidade exclusiva, uma abordagem inovadora, uma melhor relação custo-benefício, entre outros aspectos distintivos.

A visão do produto, ao preencher esses elementos, fornece uma descrição concisa e clara do que o produto representa, quem são os clientes que desejamos atingir, quais problemas pretendemos resolver e como nosso produto se diferencia no mercado, o que ajuda a orientar o desenvolvimento, o marketing e a estratégia geral do produto. 

Para uma análise mais ampla da visão do produto, realizamos uma dinâmica individual em que cada membro da equipe compartilhou sua próprias expectativas de entrega da plataforma:

<img src="https://github.com/4Banks/documentation/blob/main/images/visao_do_produto.jpeg" alt="Descrição da imagem" width="500" height="800">

Em seguida, realizamos uma discussão em grupo e definimos a seguinte visão de produto:

|                   |                                            |
| :---------------: | ------------------------------------------ |
|       Para        | Cientistas de dados do time de análise e detecção de fraude de instituições financeiras                          |
|       Cujo(a)     | Transações bancárias de cartão de crédito necessitam de insights sobre os seus dados para mitigar fraudes     |
|         O         | 4Banks                       |
|       É um(a)     | Plataforma de análise de dados                   |
|        Que        | Fornece insights, de alto e baixo nível detalhando a metodologia usada para facilitar a tomada de decisões |
| Diferentemente de | Produtos internos utilizados nos sistemas bancários atualmente, outros produtos do pantanal.dev            |
|  O nosso produto  | É uma plataforma intuitiva que aceita diversos datasets e fornece análises exaustivas gráficas e aprofundadas baseadas na necessidade do cliente                        |

#### É/Não é, Faz/Não faz

Além disso, realizamos a mesma dinâmica individual e em grupo para definirmos o que a nossa plataforma entrega e não entrega ao usuário final:

<img src="https://github.com/4Banks/documentation/blob/main/images/e_naoe_faz_naofaz.jpeg" alt="e_naoe_faz_naofaz" width="600" height="600">


## Objetivos


<img src="https://github.com/4Banks/documentation/blob/main/images/objetivos.jpeg" alt="e_naoe_faz_naofaz" width="800" height="500">

| Objetivo maior                               | Milestones       | 
| --------------------                         | -------------- | 
| `Importar os dados do usuário`               | `(Front) Entrada do dataset` |          
|                                              | `Validar o dataset` |                 
|                                              |                  |          
| `Tratar os dados fornecidos`                 | `Remover valores do dataset (Pré-processamento)` |      
|                                              | `Transformação dos dados (PCA, T-SNE, UMAP e VAE)` |  
|                                              | `Balancear as classes (Amostragem)` |  
|                                              | `Armazenar os dados na cloud` |  
|                                              |                  |  
| `Análise dos dados`                          | `Personalização das técnicas de análise` |          
|                                              | `Treinamento e análise dos modelos de IA` |                 
|                                              |                  |    
| `Apresentar o resultado obtido`              | `Apresentar os insights obtidos` |      
|                                              | `Apresentar resultado das análises e taxas dos modelos` |  
|                                              | `Exportar relatório` |  
|                                              |                  | 

## Personas

| Persona             | Perfil                 | Comportamento           | Necessidades                |
| ------------------- | --------------------   | ----------------------- | --------------------------- |
| `Juliana Hosoume`   | `Cientistas de dados`  | `[o que a persona faz]` | `[o que a persona precisa]` |

## Features

> 1. Importar dataset
> 2. Tratamento do dataset
> 3. Análise dos dados
> 4. Visualizar o resultado

## Referências úteis

- [FunRestrospectives](https://www.funretrospectives.com/)
