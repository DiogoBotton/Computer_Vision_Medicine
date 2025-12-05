# Computer_Vision_Medicine

## FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Classificação de Anomalias em Radiografias de Tórax com CNN

Projeto de Classificação Multi-Rótulo usando Transfer Learning (InceptionV3 + CBAM) no dataset CheXpert.

## 👨‍🎓 Integrantes:

- <a href="https://www.linkedin.com/in/bryanjfagundes/">Bryan Fagundes</a>
- <a href="https://br.linkedin.com/in/brenner-fagundes">Brenner Fagundes</a>
- <a href="https://www.linkedin.com/in/diogo-botton-46ba49197/">Diogo Botton</a>
- <a href="https://www.linkedin.com/in/hyankacoelho/">Hyanka Coelho</a>
- <a href="https://www.linkedin.com/in/julianahungaro/">Juliana Hungaro Fidelis</a>

## 👩‍🏫 Professores:

### Tutor(a)

- <a href="https://www.linkedin.com/in/leonardoorabona?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Leonardo Ruiz Orabona</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>

## 📜 Descrição

Este projeto desenvolve um modelo baseado em Redes Neurais Convolucionais (CNNs) para identificar **14 anomalias** em radiografias de tórax utilizando o dataset **CheXpert-v1.0-small**.

A tarefa é uma **classificação multi-rótulo**, onde uma mesma imagem pode conter várias patologias simultaneamente. O pipeline inclui:

- Pré-processamento e padronização das imagens  
- Filtragem por projeção (Frontal/PA)  
- Deduplicação por paciente para evitar viés  
- Tratamento de incertezas com a estratégia **U-Zero**  
- Criação do modelo com **InceptionV3 + módulo de atenção CBAM**  
- Avaliação com métricas adequadas a dados desbalanceados (PR AUC, ROC AUC, F1)  
- Deploy via Docker + FastAPI  
- Protótipo de interface para inferência

# 🧠 Resumo Técnico

- **Tipo:** Classificação multi-rótulo (14 classes)  
- **Dataset:** CheXpert-v1.0-small  
- **Modelo:** InceptionV3 + CBAM  
- **Técnicas:** Transfer Learning, Attention Module, Early Stopping  
- **Métricas:** PR AUC, ROC AUC, F1 Score  
- **Deploy:** Docker + FastAPI  
- **Notebook principal:** `chexpert_cnn.ipynb`

  
## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: Aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>scripts</b>: Aqui está um arquivo de implementação (deploy), no caso, o docker-compose.yml que realiza o deploy da API juntamente com o modelo.

- <b>src</b>: Todo o código fonte criado.

## 🔧 Como executar o código

Para executar a API com o modelo gerado atráves do notebook `chexpert_cnn.ipynb` e o frontend para integração com a API e visualização dos resultados, é necessário ter o Docker instalado em sua máquina. Com ele instalado, basta com alguma CLI (por exemplo, o prompt do windows) navegar até a pasta `scripts` e digitar:

```bash
    docker-compose up -d --build
```

Ao rodar o comando, a API estará disponível com a documentação do Swagger e pronta para ser acessada através da url: `http://localhost/docs`. O frontend estará disponível através da url: `http://localhost:8080`.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
