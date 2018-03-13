def pegar_nome(resposta):
        b_nome = resposta
        inicio = b_nome.find('<span class="nome"> <small><b>') + 30
        b_nome = b_nome[inicio:]
        fim = b_nome.find("</b>")
        nome  = b_nome[:fim]
        print (nome)
        return nome
