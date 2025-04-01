# Academic Paper Scraper

Um scraper Python robusto para download automático de artigos acadêmicos de diversos publishers e repositórios. Desenvolvido especialmente para pesquisa em educação e psicologia cognitiva.

## Tópicos de Pesquisa

O scraper é otimizado para os seguintes tópicos:
- Superdotação (Giftedness)
- Aprendizagem Alternativa (Alternative Learning)
- Figuras Históricas (Historical Figures)
- Topologia Cerebral (Brain Topology)
- Tipos de Inteligência (Types of Intelligence)
- Métodos de Aprendizagem (Learning Methods)
- Interdisciplinaridade (Interdisciplinary)
- Dimensões Culturais (Cultural Dimensions)
- Metacognição (Metacognition)

## Publishers Suportados

### Principais Publishers
- PLOS ONE
  - Extração direta de PDFs
  - Suporte a metadados completos
  - Cache de resultados

- MDPI
  - Download via DOI
  - Extração de citações
  - Suporte a artigos Open Access

- Frontiers
  - Download direto de PDFs
  - Extração de referências
  - Suporte a supplementary materials

- BioMed Central
  - Acesso a texto completo
  - Extração de figuras
  - Metadados estruturados

- Nature
  - Acesso a abstracts
  - Download de PDFs (quando disponível)
  - Extração de dados de citação

### Publishers Secundários
- SciELO
- Taylor & Francis
- SAGE
- Wiley Online
- Cambridge Core

## Funcionalidades

### Download de Artigos
- Download automático de PDFs
- Verificação de acessibilidade
- Retry automático em caso de falha
- Suporte a proxy
- Rate limiting configurável
- Rotação de User-Agents

### Processamento de Dados
- Extração de metadados
- Parsing de referências
- Extração de texto do PDF
- Identificação de figuras
- Análise de citações

### Organização
- Estrutura de diretórios por tópico
- Nomeação padronizada de arquivos
- Metadados em JSON
- Cache de resultados
- Backup automático

## Requisitos

- Python 3.8+
- Dependências principais:
  ```
  requests>=2.31.0
  beautifulsoup4>=4.12.0
  selenium>=4.15.0
  PyPDF2>=3.0.0
  scholarly>=1.7.0
  ```

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Dagon67/scraping.git
cd scraping
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Busca Básica
```python
from scraper import PaperScraper

scraper = PaperScraper()
results = scraper.search("giftedness education")
scraper.download_papers(results, output_dir="downloads/giftedness")
```

### Busca Avançada
```python
scraper.search(
    query="metacognition in gifted students",
    year_range=(2018, 2023),
    publishers=["PLOS ONE", "Frontiers"],
    language="english",
    limit=50
)
```

### Download com Filtros
```python
scraper.download_papers(
    results,
    output_dir="downloads/metacognition",
    file_types=["pdf", "supplementary"],
    skip_existing=True,
    verify_integrity=True
)
```

## Estrutura do Projeto

```
scraping/
├── scraper.py          # Classe principal do scraper
├── publishers/         # Handlers específicos por publisher
│   ├── plos.py
│   ├── mdpi.py
│   └── frontiers.py
├── utils/             # Funções utilitárias
│   ├── download.py
│   ├── parser.py
│   └── metadata.py
├── config/           # Arquivos de configuração
│   ├── settings.py
│   └── proxies.py
├── tests/            # Testes unitários
├── downloads/        # Diretório de downloads
├── requirements.txt  # Dependências
└── README.md        # Documentação
```

## Configuração

### Configurações Gerais
```python
# config/settings.py
SETTINGS = {
    'max_retries': 3,
    'timeout': 30,
    'rate_limit': 2,  # requisições por segundo
    'cache_duration': 86400,  # 24 horas
    'verify_ssl': True
}
```

### Configuração de Proxy
```python
# config/proxies.py
PROXIES = {
    'http': 'http://proxy:port',
    'https': 'https://proxy:port'
}
```

## Tratamento de Erros

O scraper implementa tratamento robusto de erros:
- Retry automático com backoff exponencial
- Logging detalhado
- Verificação de integridade de arquivos
- Fallback para métodos alternativos de download
- Cache para evitar requisições repetidas

## Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Próximas Atualizações

- [ ] Suporte a novos publishers
- [ ] Interface web para busca
- [ ] Análise de texto completo
- [ ] Extração de referências cruzadas
- [ ] Integração com gestores bibliográficos
- [ ] Análise de redes de citação
- [ ] OCR para PDFs escaneados
- [ ] API REST

## Contato

 [@Dagon67](https://github.com/Dagon67)

Link do Projeto: [https://github.com/Dagon67/scraping](https://github.com/Dagon67/scraping)
