
plot_good = [(0,0,'Encerramento','Quatro anos se passaram e a cidade progrediu muito, e logo','você se tornou o herói da cidade, todos pretendem','seguir o seu exemplo e tornar o mundo um lugar melhor e mais limpo.'),
(0,0,'Encerramento','Final Bom','','','Fim.')]
plot_bad = [(0,1,'Encerramento','Quatro anos se passaram e a cidade não progrediu em nada','você ficou muito mal visto pelos Vastayas que o culpam por suas decisões','e alguns até questionam sua integridade'),
(0,1,'Encerramento','Final Ruim','','','Fim.')]
plot_neutral = [(0,0,'Encerramento','Quatro anos se passaram e a cidade progrediu, porém muitas de suas ações foram questionáveis','e os Vastayas percebendo isso acreditam que seja melhor procurar outra pessoa.'),
(0,0,'Encerramento','Final Neutro','','','Fim.')]


question_diag = [('Comprar carros agora está proibido!','Vamos implementar um novo sistema de transporte público sustentável!','Vamos construir ciclovias, e conscientizar as pessoas!','Carros da Ford não poluem comprem eles!'),
('Vamos gerar energia através da combustão de nossos inimigos!','Vamos gerar energia através de placas solares!','Vamos gerar energia através de usinas Eólicas!','Vamos gerar energia através de usinas Termoelétricas!'),
('Vamos melhorar o contrato de trabalho das pessoas!','Então vamos fechar todas as empresas!','Isso não é um problema.','Vamos aumentar a jornada de trabalho, para que não tenham mais tempo parar reclamar!'),
('Se estiverem nos pagando tudo bem.','Essas empresas sustentam essa cidade, esqueça isso!','Isso é um absurdo, fechem essas empresas de imediato!','De agora em diante as empresas teram que fazer um descarte de dejetos consciente!'),
('Caso queriam retirar a madeira terão que plantar própriamente para isso!','Não iremos mais usar madeira, está proibida a retirada de madeira de qualquer lugar!','Queimem todas as florestas! Assim não poderão desmatar.','Demitam todos!')]

text_base = [(1,3,'Instrução aos Comandos','► Z, Espaço ou Botão esquerdo do mouse sobre', ' a caixa de texto inferior: Avançam o diálogo.','► Esc e Enter:','Abrem o menu de opções.'),
(0,3,'Introdução','Em um planeta distante chamado Aniland','viviam um povo muito peculiar estes se','chamavam Vastayas um povo feliz e animado'),
(0,3,'Introdução','Os Vastayas se orgulhavam de viver em harmonia com a natureza','E por muitos anos isso continuou assim...'),
(0,2,'Introdução','Até o dia em que a corrida pela evolução e crescimento da civilização se tornou uma realidade problemática,','tomando conta dos Vastayas, e fazendo estes esquecerem o que já sabiam deste sempre','a importância de se viver em paz e harmonia com a natureza.'),
(0,2,'Introdução','Os Vastayas estavam preocupados com essa realidade então','decidiram começar uma nova era onde tudo voltaria a ser como antes','para isso deveriam escolher alguém para os guiar'),
(0,0,'Introdução','E aqui está ele Glusternio o Vastaya escolhido pelo povo para governar','sobre a promessa de mudar esse cenário, e visando alcançar o sonho','de uma vida onde o progresso e a harmonia com a natureza andem de mãos dadas.'),
(0,0,'Introdução','Seu dever como representante dos Vastayas é governar visando salvar a natureza,','para isso você deve entender das necessidades ecológicas de uma sociedade,','e evitar iniciativas baseadas em mentiras, já que estas causam uma perda de tempo e recurso,', 'que poderiam ser utilizadas em uma iniciativa com real impacto ecológico.'),
(2,0,'Proibir quer as pessoas comprem carros','Implementar sistemas de transporte público eficientes','Construir ciclovias, e concientizar as pessoas sobre sua importância','Anunciar que carros da Ford não poluem o meio ambiente','Os Vastayas estão com um grave problema de','locomoção, devido a poluição e congestionamento','e você se vê obrigado a tomar uma atitude e como',' seu primeiro ato você irá...'),
(0,0,'Glusternio','*'),
(2,0,'Combustão dos nossos inimigos','Fazendas de placas solares','Usinas Eólicas','Usinas Termoelétricas','Os Vastayas querem migrar suas usinas para um','tipo que tenha um funcionamento mais sustentável,',' e você ficou encarregado de decidir a mais','adequada entre as citadas por eles.'),
(0,0,'Glusternio','*'),
(2,0,'Exigir que as empresas tenham uma jornada de trabalho menor e melhores salários','Fechar todas as empresas para as pessoas pararem de trabalhar','Ignorar o problema','Exigir que as empresas tenham uma jornada de trabalho maior e manter o salário','Os Vastayas estão trabalhando muito e ganhando', 'pouco dinheiro, o que no geral diminui a','produtividade e deixa o povo descontente. Qual','atitude você irá tomar para resolver este problema?'),
(0,0,'Glusternio','*'),
(2,1,'Exigir uma multa para poluírem livremente o rio','Deixar como está porque as empresas estão gerando lucro','Fechar as empresas sem contestações','Exigir que as empresas façam um descarte consciente','As fábricas da cidade estão poluindo o rio.','o que um dia foi um símbolo do vínculo da cidade', 'com a natureza, agora está perecendo.','Como você irá intervir?'),
(0,1,'Glusternio','*'),
(2,1,'Criar lei obrigando o reflorestamento','Proibir retirada de madeira por completo','Queimar todas as florestas','Demitir todos envolvidos','As empresas estão desmatando as florestas em', 'torno da cidade em busca de matéria prima.','O que você vai fazer a respeito?'),
(0,1,'Glusternio','*'),]

'''
caso não queria escrever por uma linha, mas queira escrever em outra mais abaixo, coloque um "" ou '' para cada linha que queria pular
até 7 linhas de texto por etapa de diálogo. 9 caso seja pergunta contando as opções
0 = 0 para texto na caixa de diálogo padrão, 1 para texto na caixa de diálogo do centro como nas instruções por exemplo, 2 para seleção de dialogos (do 0~3 são as opções, e do 5~9 são do texto base)
1 = background, 0 = Dia, 1 = Noite, 2 = Cidade  
2 = nome da pessoa que está falando, se for na caixa de diálogo do centro é um título 
3 = primeira linha
4 = segunda linha 
5 = ...
'''
