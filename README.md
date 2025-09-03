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
  - Proximity of users to data
  - Availability service and feature
  - Cost-effectiveness

- Amazon S3 Inventory
      - Use Amazon S3 inventory to help manage your storage

#  Aula 03/09

- AWS runtime compute choices
    - VMs
    - Containers
    - VPS
    - Platform as a Service (PaaS)
    - Serverless
