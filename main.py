from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from login import pegar_id_autenticado
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

import requests

class Gerenciador(ScreenManager):
    pass

class PopErrorConection(Popup):
    """Caso a função de login falhe em se conectar com o servidor do sigaa"""
    pass
    
class PopSenhaErrada(Popup):
    pass

class DoLogin(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    usuario_input = ObjectProperty()
    senha_input = ObjectProperty()
    
    def logar_se(self):
        #pego a entrada o user
        usuario = str(self.usuario_input.text)
        senha = str(self.senha_input.text)
        
        try:
            
            self.login = pegar_id_autenticado( usuario, senha)
            self.session_id = self.login[0]
            self.resposta = self.login[1]
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            PopError().open()

            print('erro de connection')
            
        if self.resposta.text.find('Usuário e/ou senha inválidos') >= 0:
            PopSenhaErrada().open()
            print('Usuário e/ou senha inválidos')
    
    
        
        
    
class Sigaa(App):
    def build(self):
        return Gerenciador()
    pass

Sigaa().run()
