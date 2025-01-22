# Visão Geral:
Este script (driver.py) utiliza as bibliotecas webdriver_manager e selenium para configurar e gerenciar uma instância do navegador Chrome.
Ele automatiza a instalação e inicialização do ChromeDriver, facilitando o processo de automação de testes ou navegação com o Selenium, sem a necessidade de instalação manual do driver do Chrome.
*** Não é necessário rodar todas as vezes, apenas quando o ChromeDriver estiver desatualizado.

Este script (graph.py) automatiza a geração de imagens PNG a partir de arquivos HTML contendo gráficos, utilizando o Selenium e o Pillow para capturar e processar essas imagens. Ele é especialmente útil para projetos que envolvem visualizações gráficas em HTML que precisam ser convertidas em imagens para outros usos.

# Funcionamento:
Navegação automatizada com Selenium: O código usa o Selenium WebDriver para abrir arquivos HTML e renderizar gráficos presentes na página.
Modo headless: O navegador Chrome é executado em modo "headless", sem interface gráfica, para eficiência e automação.
Captura de imagens: Utiliza o método screenshot_as_png para capturar o gráfico renderizado e armazená-lo como PNG.
Redimensionamento e ajuste de gráficos: O código ajusta o tamanho dos gráficos via JavaScript, garantindo que sejam renderizados corretamente na tela.
Recorte automático de bordas: Utilizando a biblioteca Pillow, o código remove automaticamente as bordas brancas das imagens capturadas.
Organização de saída: As imagens são salvas em uma pasta png dentro do diretório principal, mantendo a estrutura de subpastas original.
Configuração do WebDriver: Define o caminho para o driver do Chrome e suas opções.
Mapeamento de resoluções: O código ajusta automaticamente a resolução da janela do navegador com base no nome da subpasta onde os arquivos HTML estão armazenados.
Processamento de arquivos: Itera sobre subpastas contendo arquivos HTML, abrindo cada arquivo, renderizando o gráfico e capturando-o como PNG.
Recorte da imagem: Após capturar o gráfico, a imagem é processada para remover bordas indesejadas, e então é salva no formato PNG.

# Dependências:
selenium: biblioteca popular de automação de navegadores da web. Ela permite que você controle e interaja programaticamente com navegadores como Chrome, Firefox, Edge, e outros.
webdriver-manager: biblioteca Python que facilita o gerenciamento de drivers para navegadores ao usar o Selenium. Ele automatiza o processo de download, configuração e atualização dos WebDrivers necessários, como o chromedriver (para o Google Chrome), geckodriver (para o Firefox), msedgedriver (para o Microsoft Edge), entre outros.
Tradicionalmente, para usar Selenium, você precisa baixar manualmente o WebDriver correspondente à versão do navegador e configurar o caminho no sistema ou no código. O webdriver-manager elimina essa etapa, baixando e configurando automaticamente o driver apropriado para você.

# Como Usar:
driver.py: se precisar instalar ou configurar o chromedriver, execute o script com o seguinte comando: py driver.py ou python driver.py.
graph.py: execute o script com o seguinte comando: py graph.py ou python graph.py.
