driver.py:

Este código utiliza as bibliotecas webdriver_manager e selenium para configurar e gerenciar uma instância do navegador Chrome. Ele segue os seguintes passos:

Importações: São feitas importações do ChromeDriverManager (para gerenciar a instalação do driver do Chrome) e do webdriver da biblioteca Selenium (para automação de navegadores).

Criação das Opções do Chrome: O código inicializa uma instância das opções de configuração do navegador Chrome através de webdriver.ChromeOptions(). Essas opções podem ser personalizadas conforme necessário (embora não estejam modificadas neste código).

Inicialização do WebDriver: O webdriver.Chrome() é inicializado utilizando o driver instalado automaticamente pelo ChromeDriverManager e as opções definidas. Esse WebDriver permite a automação de interações com o navegador.

Finalização do WebDriver: Após a inicialização, o código encerra a sessão do navegador com driver.quit().

Impressão do Caminho do Driver: Finalmente, o caminho do driver Chrome instalado é impresso com o comando print(driver_path).

Este código automatiza a instalação e inicialização do ChromeDriver, facilitando o processo de automação de testes ou navegação com o Selenium, sem a necessidade de instalação manual do driver do Chrome.

graph.py

Este código automatiza a geração de imagens PNG a partir de arquivos HTML contendo gráficos, utilizando o Selenium e o Pillow para capturar e processar essas imagens. Ele é especialmente útil para projetos que envolvem visualizações gráficas em HTML que precisam ser convertidas em imagens para outros usos.

Principais Funcionalidades:

Navegação automatizada com Selenium: O código usa o Selenium WebDriver para abrir arquivos HTML e renderizar gráficos presentes na página.
Modo headless: O navegador Chrome é executado em modo "headless", sem interface gráfica, para eficiência e automação.
Captura de imagens: Utiliza o método screenshot_as_png para capturar o gráfico renderizado e armazená-lo como PNG.
Redimensionamento e ajuste de gráficos: O código ajusta o tamanho dos gráficos via JavaScript, garantindo que sejam renderizados corretamente na tela.
Recorte automático de bordas: Utilizando a biblioteca Pillow, o código remove automaticamente as bordas brancas das imagens capturadas.
Organização de saída: As imagens são salvas em uma pasta png dentro do diretório principal, mantendo a estrutura de subpastas original.

Como Funciona:

Configuração do WebDriver: Define o caminho para o driver do Chrome e suas opções.
Mapeamento de resoluções: O código ajusta automaticamente a resolução da janela do navegador com base no nome da subpasta onde os arquivos HTML estão armazenados.
Processamento de arquivos: Itera sobre subpastas contendo arquivos HTML, abrindo cada arquivo, renderizando o gráfico e capturando-o como PNG.
Recorte da imagem: Após capturar o gráfico, a imagem é processada para remover bordas indesejadas, e então é salva no formato PNG.
