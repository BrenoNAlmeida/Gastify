# CAMADAS DE APLICAÇÃO DO PROJETO GASTIFY_API




## Camada de Apresentação (Presentation Layer)
Esta camada lida com a interação com o usuário e a apresentação dos dados, embora, em uma API, isso geralmente envolva a definição de endpoints e a serialização/deserialização de dados.

**Arquivos Relevantes**:

-   **`gastify_api/views.py`**:

    -   Define os endpoints da API e lida com as requisições HTTP 	(GET, POST, PUT, DELETE).
   - **`gastify_api/serializers.py`**:
       -  Define os serializers que convertem instâncias de modelo em representações JSON e vice-versa.

## Camada de Aplicação (Application Layer)

Esta camada coordena a aplicação, definindo a lógica e as regras de negócio que não estão diretamente relacionadas à persistência dos dados.

-   **Arquivos Relevantes**:
    -   **`gastify_api/views.py`**:
        -   Além de ser parte da camada de apresentação, os ViewSets também podem conter lógica de aplicação, especialmente quando se trata de validação e manipulação de dados antes de chamar a camada de domínio.

## Camada de Modelo de Domínio (Domain Model Layer)
Esta camada contém as regras de negócio e a lógica que define o comportamento da aplicação.

**Arquivos Relevantes**:

-   **`gastify_api/models.py`**:
    -   Define os modelos de dados, que representam as entidades de domínio e encapsulam a lógica de negócios.

## Camada de Persistência (Persistence Layer)
Esta camada é responsável pela comunicação direta com o banco de dados.
**Arquivos Relevantes**:

-   **`gastify_api/models.py`**:
    
    -   Os próprios modelos Django fazem parte da camada de persistência, pois eles definem como os dados são armazenados no banco de dados.

## Camada de Dados (Data Layer)

Esta camada lida com a configuração do banco de dados e a integração com fontes de dados externas.

**Arquivos Relevantes**:

-   **`conf/settings.py`**:
    -   Contém as configurações do banco de dados, incluindo detalhes de conexão e configuração.

## Camada de Infraestrutura (Infrastructure Layer)

Esta camada inclui a configuração do ambiente, dependências externas e outras configurações necessárias para a execução da aplicação.

**Arquivos Relevantes**:

-   **`requirements.txt`**:
    
    -   Lista de dependências necessárias para a aplicação.
- **`conf/settings.py`**:

    - Configurações globais da aplicação, incluindo middleware, aplicações instaladas e configurações de segurança.

# 
# Dependências entre as Camadas do Projeto Gastify

-   **Camada de Apresentação (Presentation Layer)**
    
    -   **Dependências**:
        -   **Application Layer**: A camada de apresentação depende da camada de aplicação para obter dados processados e enviar comandos.
        -   **Domain Model**: Depende da camada de domínio para validar e mapear os dados de/para as entidades de domínio.
    -   **Arquivos**:
        -   `gastify_api/views.py`
        -   `gastify_api/serializers.py`
        
-   **Camada de Aplicação (Application Layer)**
    
    -   **Dependências**:
        -   **Domain Model**: Depende da camada de domínio para aplicar a lógica de negócio central.
        -   **Persistence**: Pode depender diretamente da camada de persistência para acessar dados.
    -   **Arquivos**:
        -   `gastify_api/views.py`
-   **Camada de Modelo de Domínio (Domain Model Layer)**
    
    -   **Dependências**:
        -   **Persistence**: Depende da camada de persistência para salvar e recuperar dados.
    -   **Arquivos**:
        -   `gastify_api/models.py`
        -   Possíveis serviços de domínio (e.g., `gastify_api/services.py`)
-   **Camada de Persistência (Persistence Layer)**
    
    -   **Dependências**:
        -   **Data**: Depende da camada de dados para configurações e interações com o banco de dados.
    -   **Arquivos**:
        -   `gastify_api/models.py`
        -   Custom managers e querysets
-   **Camada de Dados (Data Layer)**
    
    -   **Dependências**:
        -   **Infrastructure**: Depende da camada de infraestrutura para as configurações do ambiente e serviços externos.
    -   **Arquivos**:
        -   Configurações do banco de dados em `conf/settings.py`
-   **Camada de Infraestrutura (Infrastructure Layer)**
    
    -   **Dependências**:
        -   **Nenhuma Dependência**: A camada de infraestrutura fornece suporte transversal para todas as outras camadas, oferecendo serviços e configurações necessárias para a aplicação funcionar.
    -   **Arquivos**:
        -   `requirements.txt`
        -   Configurações em `conf/settings.py`
    
`![Camadas de Aplicação do Projeto Gastify](/docs/applications_layers.png)`
