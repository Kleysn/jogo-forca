# Jogo da Forca

O objetivo desse progama é conseguir raspar informações de quatro paginas web. Todas essas paginas contem informações de A a Z de quatro categoria: Animais, Objetos, Paises e Frutas. Foi utilizado um biblioteca do python que possibilida a pesquisa de Tags HTML. Dessa forma foi possível buscar pela Tag ul e li na pagina, essas tags em especificos são utilizadas para listar informações.

Apos a raspagem de dados, foi armazenado dentro de uma lista todas as tags li ques estão dentro das lu. Essa etapa consisti em preparar os dados ára serem tratados. Os dados foram armazenados como string na lista, no entanto eles vieram com as nomeclaturas das tags HTML o que futuramente atraparia na hora de escolher uma plavra de forma aleatoria para iniciar o jogo. Então, foi criando uma função para manter so os nomes de forma limpa dentro da lista. Esse passo foi feito para todas as quatro paginas e cada montante de informações ficou armazenado em uma lista distinta, pois mais a frente do jogo facilitaria a escolha de uma categoria para o ususario escolher.

OBS: A ideia do jogo é basica. Mas o principal objetivo aqui foi praticar a busca de informações em um determinada pagina WEB, prepafrar e tratar os dados para serem usados pelo usuario.
