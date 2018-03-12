import requests
import getpass


def pegar_id_nao_autenticado():
    print("Gerando um novo id de sessão.")
    
    with requests.Session() as sessao:
    
        resposta = sessao.get("http://sigaa.ufpi.br/sigaa/verTelaLogin.do", timeout=10)
        
        b_session_id = resposta.text
        inicio = b_session_id.find("jsessionid=") + 11
        b_session_id = b_session_id[inicio:]
        fim = b_session_id.find('"')
        session_id  = b_session_id[:fim]
    
    print('id gerado')              
        
    return session_id
       
    

def login(session_id, usuario, senha):
    
    print('logando')
    
    cookies = {
        'JSESSIONID': session_id,
    }

    headers = {
        'Host': 'sigaa.ufpi.br',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://sigaa.ufpi.br/sigaa/verTelaLogin.do',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '96',
        'DNT': '1',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }

    params = (
        ('dispatch', 'logOn'),
    )


    data = 'width=1366&height=768&urlRedirect=&acao=&acessibilidade=&user.login=' + usuario + '&user.senha=' + senha
        
    response = requests.post('http://sigaa.ufpi.br/sigaa/logar.do;jsessionid='+session_id , headers=headers, params=params, cookies=cookies, data=data, verify=False, timeout=20)
    
    print("logado")


    return session_id, response
    
    
def pegar_id_autenticado(usuario, senha):
    session_id = pegar_id_nao_autenticado()
    return login(session_id, usuario, senha)



