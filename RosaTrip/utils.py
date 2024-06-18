from django.core.mail import send_mail


# Método para enviar a notificação de novo cadastro de usuário.
def enviar_cadastro(cadastro):
    assunto = 'Confirmação de cadastro para novo usuário'
    mensagem = f"""
    Olá, um novo cadastro foi solicitado e aguarda aprovação:
    
    Nome de Usuário: {cadastro.username}
    Email: {cadastro.email}
    
    Acesse o painel administrativo para aprovar ou recusar o cadastro.
    """

    send_mail(
        assunto,
        mensagem,
        'qualteuemail@gmail.com', ['email.gerente@exemplo.com.br'])