# IP Banner and Log Server

Este é um código Python que cria banners de serviço e arquivos de log, abre portas específicas e aguarda conexões nessas portas. Quando uma conexão é estabelecida, o código envia o conteúdo dos arquivos de texto correspondentes e registra informações de conexão nos arquivos de log.

## Funcionamento

1. O código cria banners de serviço e arquivos de log para as portas especificadas.
2. É exibida a mensagem "Opening ports" e aguarda por 5 segundos.
3. A chamada subprocess `subprocess.call("clear", shell=True)` é utilizada para limpar a tela.
4. É exibida a mensagem "Ports open!" e uma listagem das portas abertas usando `subprocess.call("netstat -nlpt", shell=True)`.
5. Em um loop infinito, o código aguarda conexões em cada porta especificada.
6. Quando uma conexão é estabelecida em uma porta, o código registra as informações de endereço e horário da conexão no arquivo de log correspondente.
7. O conteúdo do arquivo de texto correspondente à porta é enviado ao cliente.
8. A conexão é encerrada.

## Uso

1. Antes de executar o código, verifique se os arquivos de texto `20.txt`, `21.txt`, `22.txt` e `53.txt` estão presentes com os conteúdos desejados.
2. Execute o código Python.

   ```bash
   python arquivo.py
   ```

3. O código iniciará o servidor de banners e logs, abrindo as portas especificadas.
4. O console exibirá a mensagem "Ports open!" e uma listagem das portas abertas.
5. O servidor aguardará por conexões nas portas especificadas.
6. Quando uma conexão for estabelecida, o conteúdo do arquivo de texto correspondente será enviado ao cliente e as informações de conexão serão registradas nos arquivos de log correspondentes.
7. O servidor continuará aguardando por novas conexões indefinidamente.

## Observação

Este código é fornecido como um exemplo básico e deve ser utilizado com responsabilidade. É importante observar que o código está abrindo portas e aceitando conexões, o que pode apresentar riscos de segurança se usado de forma inadequada ou sem as devidas precauções.

Certifique-se de configurar corretamente os arquivos de texto com os banners desejados e monitore cuidadosamente o uso desse código para evitar qualquer atividade maliciosa.