$(document).ready(function() {
    // Função para conectar ao banco de dados
    function conectarBancoDeDados() {
        $.ajax({
            type: 'GET',
            url: '/conectar_banco',
            success: lidarComRespostaBanco,
            error: lidarComErroBanco
        });
    }

    // Função para lidar com a resposta do banco de dados
    function lidarComRespostaBanco(response) {
        console.log(response); // Exemplo: exibe a resposta no console
    }

    // Função para lidar com erros ao conectar ao banco de dados
    function lidarComErroBanco(xhr, status, error) {
        console.error('Erro ao conectar ao banco de dados:', error);
    }

    // Função para enviar dados do formulário
    function enviarFormulario() {
        var formData = {
            'Titulo': $('#titulo').val(),
            'Ano_publicacao': $('#ano').val()
            // Adicione outros campos conforme necessário
        };

        $.ajax({
            type: 'POST',
            url: '/livro',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                $('#message').removeClass().addClass('success').text(response.message);
            },
            error: function(xhr, status, error) {
                $('#message').removeClass().addClass('error').text(xhr.responseJSON.error);
            }
        });
    }

    // Chama a função para conectar ao banco de dados quando o documento estiver pronto
    conectarBancoDeDados();

    // Evento de envio do formulário
    $('#livroForm').submit(function(event) {
        event.preventDefault();
        enviarFormulario();
    });
});
