# Computer Vision Scraper

Um scraper Python que utiliza técnicas de visão computacional para extrair e processar informações de imagens e vídeos.

## Funcionalidades

- Detecção e reconhecimento de objetos em imagens
- Processamento de frames de vídeo
- Extração de texto de imagens (OCR)
- Análise de padrões visuais
- Tracking de objetos em vídeo
- Segmentação de imagens

## Tecnologias Utilizadas

- Python 3.8+
- OpenCV (cv2)
- TensorFlow/Keras
- Tesseract OCR
- NumPy
- Pillow (PIL)

## Requisitos

```txt
opencv-python>=4.8.0
tensorflow>=2.12.0
pytesseract>=0.3.10
numpy>=1.24.0
pillow>=10.0.0
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

4. Instale o Tesseract OCR:
- Windows: Baixe o instalador do [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux: `sudo apt install tesseract-ocr`
- Mac: `brew install tesseract`

## Uso

### Processamento de Imagem
```python
from scraper import ImageProcessor

# Inicializa o processador
processor = ImageProcessor()

# Detecta objetos em uma imagem
objects = processor.detect_objects('imagem.jpg')

# Extrai texto de uma imagem
text = processor.extract_text('documento.png')
```

### Processamento de Vídeo
```python
from scraper import VideoProcessor

# Inicializa o processador de vídeo
processor = VideoProcessor()

# Processa um vídeo frame por frame
processor.process_video('video.mp4', output='resultado.mp4')

# Tracking de objetos em tempo real
processor.track_objects('webcam', show_preview=True)
```

## Estrutura do Projeto

```
scraping/
├── scraper.py          # Classe principal
├── processors/         # Processadores específicos
│   ├── image.py       # Processamento de imagens
│   ├── video.py       # Processamento de vídeo
│   └── ocr.py         # Extração de texto
├── models/            # Modelos pré-treinados
├── utils/             # Funções utilitárias
│   ├── visualization.py
│   └── preprocessing.py
├── tests/             # Testes unitários
├── examples/          # Exemplos de uso
├── requirements.txt   # Dependências
└── README.md         # Documentação
```

## Recursos

### Processamento de Imagens
- Redimensionamento e recorte
- Filtros e transformações
- Detecção de bordas
- Segmentação
- Análise de cores
- Detecção de faces

### Processamento de Vídeo
- Extração de frames
- Tracking de movimento
- Análise de fluxo óptico
- Estabilização
- Detecção em tempo real

### OCR (Optical Character Recognition)
- Reconhecimento de texto em imagens
- Suporte a múltiplos idiomas
- Pré-processamento automático
- Correção de perspectiva
- Melhoria de contraste

## Configuração

### Configurações do OpenCV
```python
OPENCV_CONFIG = {
    'scale_factor': 1.1,
    'min_neighbors': 5,
    'min_size': (30, 30),
    'flags': cv2.CASCADE_SCALE_IMAGE
}
```

### Configurações do OCR
```python
OCR_CONFIG = {
    'lang': 'por+eng',
    'config': '--oem 3 --psm 6',
    'timeout': 30
}
```

## Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Próximas Atualizações

- [ ] Suporte a YOLO v5
- [ ] Integração com CUDA
- [ ] Interface gráfica
- [ ] Processamento em batch
- [ ] Novos modelos de detecção
- [ ] Melhorias no OCR
- [ ] Suporte a GPU
- [ ] API REST

## Contato

 [@Dagon67](https://github.com/Dagon67)

Link do Projeto: [https://github.com/Dagon67/scraping](https://github.com/Dagon67/scraping)
