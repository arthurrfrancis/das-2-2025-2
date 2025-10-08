## das-2-2025-2

# Aula 30/07

- Apresentação do curso da AWS sobre arquitetura cloud

- AWS well architected: https://aws.amazon.com/pt/architecture/well-architected/
  Documento que traz boas práticas de arquitetura, vai ser mencionado durante o curso

- Papéis do arquiteto de nuvem:
  - Planejar: Analisar soluções para as necessidades e requisitos
  - Pesquisar: Fazer provas de conceito
  - Construir: Gerenciar a adoção do modelo

- Pilares do AWS Well Architected:
  1. Operational excellence: Run and monitor systems that deliver business value, Continually improve supporting processes and procedures, View the entire workload as code
  2. Security: Implement a strong identity foundation, Mantain traceability, Implement risk assessment and mitigation strategies
  3. Reliability: Recover quickly, Dynamically meet compute demand, Mitigate disruptions
  4. Performance Effiency: Choose and maintain efficient resources, Democratize advanced technologies, Employ mechanical Sympathy
  5. Cost optimization: Measure effiency, Eliminate unneeded expense, Adopt the right consumption model, Consider using managed services
  6. Sustainability: Establish sustainability goals, Maximize utilization, Choose efficient hardware and software, Reduce downstream impact

- Implementando escalabilidade
- Automatizando o ambiente

# Aula 06/08 
(escrevi um monte e o navegador crashou sem salvar)

- Regiões e AZs das infraestruturas

- Princípios do pilar de segurança

- Princípio do privilégio mínimo

- Protegendo com server encription

- Autenticação e autorização

# Aula 13/08

- Determining permissions at the time of request

- IAM policy document structure
    - Version
    - Statement
    - Effect
    - Principal
    - Action
    - Resource
    - Condition

# Aula 20/08

- Amazon S3
  - A bucket is a container for objects
  - Benefits
      - Durability
      - Availability
      - High Performance
   
- How costumers use Amazon S3
  - Spikes in demand
  - Static site
  - Financial analysis
  - Disaster recovery

- Object storage classes
- Block storage
- File Share
- Object Store
- S3 resumo geral

# Aula 27/08

- Considerations when choosing a Region
  - Data privacy laws and regulatory compliance
    - Entender e aderir às leis de proteção de dados (como GDPR, LGPD, HIPAA) e requisitos regulatórios específicos da indústria (como PCI DSS) do local onde os dados serão armazenados.
  - Proximity of users to data
    - Escolher uma Região próxima aos usuários finais para minimizar a latência e melhorar a experiência do usuário.
  - Availability service and feature
    - Verificar se a Região oferece todos os serviços e recursos da AWS necessários para a aplicação ou infraestrutura.
  - Cost-effectiveness
    - Avaliar o custo dos serviços e recursos na Região, pois os preços podem variar entre diferentes Regiões.

- Amazon S3 Inventory
  - Use Amazon S3 inventory to help manage your storage
    - Uma ferramenta que fornece listas de objetos no S3 para análise de negócios, conformidade e necessidades de segurança. Ajuda a gerenciar o armazenamento ao fornecer relatórios diários ou semanais do status dos objetos.

# Aula 03/09

- AWS runtime compute choices
  - VMs (Virtual Machines - Máquinas Virtuais)
    - Ex: Amazon EC2. Oferece controle total sobre o sistema operacional, software e recursos. Ideal para migração de workloads existentes (lift-and-shift).
  - Containers
    - Ex: Amazon ECS, EKS. Empacotamento leve de software, incluindo código, bibliotecas e dependências, para rodar de forma consistente em qualquer ambiente.
  - VPS (Virtual Private Server - Servidor Virtual Privado)
    - Ex: Amazon Lightsail. Uma máquina virtual de propósito geral com planos de preço simples e fácil gerenciamento, ideal para workloads mais simples, websites e aplicações de desenvolvimento/teste.
  - Platform as a Service (PaaS)
    - Ex: AWS Elastic Beanstalk. Permite que você implante e escale aplicações sem se preocupar com a infraestrutura subjacente.
  - Serverless
    - Ex: AWS Lambda. Execução de código sem provisionar ou gerenciar servidores. Você paga apenas pelo tempo de computação consumido.
- Amazon Machine Image (AMI)
  - Um template que contém a configuração de software (sistema operacional, servidor de aplicações e aplicações) necessária para iniciar sua instância EC2.

# Aula 10/09

- https://aws.amazon.com/pt/ec2/instance-types/
  - Tipos de Instâncias EC2: Categorias de configurações de hardware otimizadas para diferentes workloads (ex: propósito geral, otimizadas para computação, otimizadas para memória).

- Instance store (Armazenamento de Instância)
  - Armazenamento temporário e de bloco físico anexado diretamente à instância EC2. Os dados persistem apenas durante o ciclo de vida da instância.
- Amazon EBS (Elastic Block Store)
  - Armazenamento de bloco persistente que pode ser anexado a uma única instância EC2. Ideal para bancos de dados ou volumes de boot do sistema operacional.
- Amazon Elastic File System (EFS)
  - Serviço de armazenamento de arquivos escalável, elástico e *gerenciado* para uso com instâncias EC2 e outros serviços AWS, acessível por múltiplas instâncias simultaneamente.

- Subindo EC2 Windows
  - O processo de provisionar e configurar uma instância EC2 que executa o sistema operacional Windows Server.

# Aula 17/09

- Retrieving instance metadata (Recuperando metadados da instância)
  - Acesso a informações sobre a instância EC2 em execução (ex: tipo de instância, ID, endereços IP), utilizando o Instance Metadata Service.
- AMI deployment models (Modelos de implantação de AMI)
  - Estratégias para criar e gerenciar AMIs para implantação de aplicações (ex: AMI de Ouro - "Golden AMI", customização em tempo de execução).
- Amazon VPC (Virtual Private Cloud)
  - Uma rede virtual isolada na AWS onde você pode lançar seus recursos AWS.
- Network address translation (NAT) gateway
  - Um serviço gerenciado que permite que instâncias em uma sub-rede privada iniciem conexões de saída para a internet (ou outros serviços AWS), mas impede conexões de entrada não solicitadas.
- Amazon Route 53
  - Um serviço web de Sistema de Nomes de Domínio (DNS) altamente disponível e escalável.

# Aula 24/09

- Arquitetura de Rede AWS
  - Visão geral de como a rede é estruturada na AWS, incluindo Regiões, Zonas de Disponibilidade, e a infraestrutura de rede global.
- Virtual Private Cloud (VPC)
  - Detalhes adicionais sobre como configurar e usar sua rede virtual isolada, incluindo sub-redes, tabelas de rotas e gateways.

# Aula 01/10

- Peering
  - Conexão de rede que permite o roteamento do tráfego entre duas VPCs usando endereços IP privados, mesmo que pertençam a contas AWS diferentes ou Regiões diferentes.
- VPC connectivity with AWS PrivateLink architecture
  - Tecnologia para criar endpoints de VPC que permitem o acesso privado e seguro a serviços hospedados na AWS sem que o tráfego precise atravessar a internet.
- AWS site-to-site VPN
  - Conexão criptografada (túnel VPN) que permite estender sua rede on-premise para sua VPC na AWS de forma segura através da internet pública.
- Creating a site-to-site VPN connection
  - O processo de configuração do lado da AWS (Gateway de Cliente, Gateway de VPN) e do lado on-premise para estabelecer a conexão VPN.
- AWS Direct Connect
  - Serviço que estabelece uma conexão de rede dedicada de sua instalação on-premise para a AWS. Oferece maior largura de banda e menor latência.
- Extend an on-premise network to AWS by using direct connect
  - Como o Direct Connect é utilizado para criar uma rede híbrida, fazendo com que a AWS pareça uma extensão de seu próprio datacenter.

# Aula 08/10

- Identity federation
- AWS IAM Identity Center
- AWS Security Token Service
- Amazon Cognito
- AWS WAF
