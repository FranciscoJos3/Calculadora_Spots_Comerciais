# Calculadora_Spots_Comerciais
Este programa deve receber textos para spots comerciais, em um formato que facilite a leitura do locutor, com todos os algarismos, caracteres especiais e espaços adequados.
O programa irá reescrever o texto, com números por extenso, ignorando pontuações, exceto o '.', que, se estiver entre dois digitos alfa-numéricos, será substituído pela palavra 'ponto':

Ex: 
  Input: Visite nosso site www.blabla.com.br.
  
  Output: Visite nosso site www ponto blabla ponto com ponto br

Ex2: 
  Input: Compre já sua caminhonete 1.8 4x4 com até 20 % de desconto em toda a linha. Vá até a loja mais próxima ou visite o instagram @loja.
  
  Output: Compre já sua caminhonete um ponto oito quatro por quatro com até vinte por centro de desconto em toda a linha Vá até a loja mais próxima ou visite o instagram arroba loja
  
Após reescrever, o programa irá contar os caracteres, e exibir uma mensagem final, com as sequintes informações:

Se o texto tiver até 80 caracteres, o spot terá até 5 segundos.
Se o texto tiver até 160 caracteres, o spot terá até 10 segundos.
Se o texto tiver até 240 caracteres, o spot terá até 15 segundos.
Se o texto tiver até 320 caracteres, o spot terá até 20 segundos.
Se o texto tiver até 400 caracteres, o spot terá até 25 segundos.
Se o texto tiver até 480 caracteres, o spot terá até 30 segundos.
Se o texto tiver até 560 caracteres, o spot terá até 35 segundos.
Se o texto tiver até 640 caracteres, o spot terá até 40 segundos.
Se o texto tiver até 720 caracteres, o spot terá até 45 segundos.
Se o texto tiver até 800 caracteres, o spot terá até 50 segundos.
Se o texto tiver até 880 caracteres, o spot terá até 55 segundos.
Se o texto tiver até 960 caracteres, o spot terá até 60 segundos.
Se o texto tiver até 1040 caracteres, o spot terá acima de 60 segundos.

Por fim, o programa pergunta se o usuario quer contar novamente, se Sim, retorna ao começo, se não, fecha o programa.
