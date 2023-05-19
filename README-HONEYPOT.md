# Honeypot

Este é um código simples de um honeypot escrito em Python que recebe conexões de clientes em uma determinada porta TCP e registra informações sobre essas conexões em um arquivo de log.

## Funcionamento
1. O código cria um socket TCP para esperar por conexões de clientes.
2. Ao receber uma conexão, é iniciada uma thread separada para lidar com esse cliente.
3. A função `acao_cliente` é executada na nova thread, que realiza as seguintes etapas:
   - Registra a informação da conexão no arquivo de log.
   - Envia uma mensagem de boas-vindas ao cliente.
   - Entra em um loop para receber dados do cliente.
   - Registra os dados recebidos no arquivo de log.
   - Chama a função `analise_trafego` para realizar análise de tráfego com os dados recebidos.
   - Envia uma mensagem de agradecimento ao cliente.
   - Fecha a conexão com o cliente.
4. A função `analise_trafego` é uma função de espaço reservado para implementação personalizada de análise de tráfego. Você pode adicionar sua lógica de análise nessa função, como verificar padrões específicos, extrair informações relevantes, etc.
5. O código principal inicia o honeypot na porta 8080 chamando a função `honeypot`.

## Registro de Log
As informações das conexões recebidas são registradas em um arquivo de log chamado "honeypot_log.txt". O arquivo é aberto em modo de anexação (`"a"`) para que as informações sejam adicionadas ao final do arquivo a cada nova conexão recebida. O formato das informações registradas é o seguinte:

```
Conexão recebida de {IP}:{PORTA} em {DATA_HORA}
Dados recebidos de {IP}:{PORTA} em {DATA_HORA}:
{DADOS_RECEBIDOS}
```

Onde:
- `{IP}`: Endereço IP do cliente que se conectou.
- `{PORTA}`: Porta do cliente que se conectou.
- `{DATA_HORA}`: Data e hora da conexão ou recebimento dos dados.
- `{DADOS_RECEBIDOS}`: Dados recebidos do cliente.

## Análise de Tráfego
A função `analise_trafego` é um espaço reservado para realizar a análise de tráfego com os dados recebidos dos clientes. Atualmente, a função está vazia (`pass`), o que significa que não há implementação específica para análise. Você pode adicionar sua lógica personalizada nessa função para realizar análises mais avançadas de pacotes de rede, verificar padrões específicos nos dados recebidos, extrair informações relevantes ou qualquer outra lógica desejada.

## Uso
Para executar o honeypot, você pode simplesmente rodar o código. Ele será executado na porta 8080. Certifique-se de ter as permissões adequadas para abrir uma conexão nessa porta. O honeypot ficará aguardando conexões de clientes, registrando as informações relevantes em um arquivo de log e realizando uma análise de tráfego básica.

**Observação:** Este código é um exemplo básico e não implementa todas as funcionalidades necessárias para um honeypot completo e seguro. É importante ter cuidado ao executar um honeypot em um ambiente de

 produção, pois pode apresentar riscos de segurança.
