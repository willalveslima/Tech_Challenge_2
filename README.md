# Tech Challenge Fase 2 - Machine Learning Engineering

## Pipeline Batch Bovespa

Este projeto faz parte do Tech Challenge da fase 2 da pós-graduação em Machine Learning Engineering. O objetivo é construir um pipeline batch para ingestão e processamento de dados da Bovespa.

### Requisitos

1. **Scrap de dados**: Coletar dados do site da B3 referentes ao pregão D-1.
2. **Ingestão no S3**: Os dados brutos devem ser ingeridos no S3 em formato Parquet com partição diária.
3. **Acionamento de Lambda**: O bucket deve acionar uma Lambda, que por sua vez irá chamar o job de ETL no Glue.
4. **Lambda**: A Lambda pode ser desenvolvida em qualquer linguagem, e deve apenas iniciar o job Glue.
5. **Job Glue**: O job Glue deve ser feito no modo visual e conter as seguintes transformações obrigatórias:
    - Agrupamento numérico, sumarização, contagem ou soma.
    - Renomear duas colunas existentes além das de agrupamento.
    - Realizar um cálculo com campos de data, como duração, comparação ou diferença entre datas.
6. **Dados refinados**: Os dados refinados no job Glue devem ser salvos no formato Parquet em uma pasta chamada `refined`, particionados por data e pelo nome ou abreviação da ação do pregão.
7. **Catalogação no Glue**: O job Glue deve automaticamente catalogar os dados no Glue Catalog e criar uma tabela no banco de dados default do Glue Catalog.
8. **Disponibilidade no Athena**: Os dados devem estar disponíveis e legíveis no Athena.
9. **Notebook no Athena (Opcional)**: É opcional construir um notebook no Athena para montar uma visualização gráfica dos dados ingeridos.

### Estrutura do Projeto

- **Scraping**: Scripts para coleta de dados do site da B3.
- **Ingestão**: Scripts para ingestão dos dados no S3.
- **Lambda**: Código da função Lambda para iniciar o job Glue.
- **ETL no Glue**: Configuração e transformações do job Glue.
- **Refinamento**: Scripts para salvar os dados refinados no S3.
- **Catalogação**: Configuração do Glue Catalog.
- **Athena**: Consultas e notebooks para visualização dos dados.

### Como Executar

1. Configurar as credenciais AWS.
2. Executar o script de scraping para coletar os dados.
3. Ingerir os dados no S3.
4. Configurar a Lambda para iniciar o job Glue.
5. Configurar e executar o job Glue.
6. Verificar os dados refinados no S3 e no Glue Catalog.
7. Consultar os dados no Athena.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
