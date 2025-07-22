# Teste Técnico de Analista de BI/Dados

Este repositório contém as soluções para o Teste Técnico de Analista de BI/Dados. O projeto está dividido em quatro partes, cada uma abordando diferentes competências em análise de dados, SQL, visualização e integração com APIs.

## Parte 1: Preparação de Dados e Visualização no Google Looker Studio

- **Descrição:**
  - Preparação e limpeza dos dados fornecidos.
  - Criação de um dashboard interativo no Google Looker Studio para análise de performance de campanhas de marketing.
- **Onde encontrar:**
  - Link para o dashboard: _https://lookerstudio.google.com/s/vcpkaKoB_G4_
  - Arquivo de dados original: `Isadora Perdigao - [HP] PLANILHA TESTE TÉCNICO` do Google Sheets

## Parte 2: Análise SQL e Banco de Dados

- **Descrição:**
  - Criação de um banco de dados SQLite local a partir do Excel.
  - Scripts para importação dos dados e análise SQL.
- **Onde encontrar:**
  - Scripts Python: `db_setup_and_import.py`, `sql_analysis_queries.py`
  - Banco de dados gerado: `marketing_data.db` (não incluso no repositório, gere usando o script)

## Parte 3: Capacidade Analítica e Recomendações

- **Descrição:**
  - Análise dos dados e elaboração de insights e recomendações para o negócio.
- **Onde encontrar:**
  - Documento de análise: `part_3_capacidade_analitica/insights_e_recomendacoes.md`

## Parte 4: Integração com API Pública (OpenWeatherMap)

- **Descrição:**
  - Script Python para coletar previsões meteorológicas diárias para Belo Horizonte (7 dias) usando a API OpenWeatherMap.
  - Exportação dos dados para um arquivo CSV.
- **Onde encontrar:**
  - Scripts e arquivos: `part_4_integracoes_python/api_data_fetcher.py`, `part_4_integracoes_python/requirements.txt`, `part_4_integracoes_python/clima_tempo_data.csv`

### Como rodar o script da Parte 4:

1. Obtenha uma chave de API gratuita em https://openweathermap.org/.
2. Defina a variável de ambiente `OPENWEATHERMAP_API_KEY`:
   - **Windows PowerShell:**
     ```powershell
     $env:OPENWEATHERMAP_API_KEY="SUA_CHAVE_AQUI"
     ```
   - **Linux/macOS:**
     ```bash
     export OPENWEATHERMAP_API_KEY="SUA_CHAVE_AQUI"
     ```
3. Instale as dependências:
   ```bash
   cd part_4_integracoes_python
   pip install -r requirements.txt
   ```
4. Execute o script:
   ```bash
   python api_data_fetcher.py
   ```

## Como Usar/Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Navegue até a parte desejada e siga as instruções específicas de cada pasta/script.
3. Para gerar o banco de dados e importar os dados:
   ```bash
   python db_setup_and_import.py
   ```
4. Para executar análises SQL:
   ```bash
   python sql_analysis_queries.py
   ```
5. Para rodar a integração com API, siga as instruções da Parte 4 acima.

## Considerações Finais

- Os arquivos `.db` (banco de dados SQLite) não são versionados neste repositório. Gere-os localmente usando os scripts fornecidos.
- Os arquivos `.csv` gerados pelos scripts (como `clima_tempo_data.csv`) são entregáveis e estão incluídos.
- Não compartilhe sua chave de API publicamente.
- Para dúvidas ou sugestões, entre em contato.
