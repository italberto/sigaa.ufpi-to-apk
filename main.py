from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from login import pegar_id_autenticado
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

from extra_dados import *

import requests

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
    
    print(DoLogin.resposta.text)
    
    

    
    pass

class PopErrorConection(Popup):
    """Caso a função de login falhe em se conectar com o servidor do sigaa"""
    pass
    
class PopSenhaErrada(Popup):
    """Caso a senha ou usuários estejam errados"""
    pass

class DoLogin(Screen):

    usuario_input = ObjectProperty()
    senha_input = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(DoLogin, self).__init__(**kwargs)
    
    
    
    def logar_se(self):
        #pego a entrada o user
        usuario = str(self.usuario_input.text)
        senha = str(self.senha_input.text)
        
        try:
            
            self.login = pegar_id_autenticado( usuario, senha)
            self.session_id = self.login[0]
            self.resposta = self.login[1]
            
            #Caso usuário ou senha esteja errada ,um popup é chamado
            if self.resposta.text.find('Usuário e/ou senha inválidos') >= 0:
                PopSenhaErrada().open()
                print('Usuário e/ou senha inválidos')
                
                
                
                return False, None
            else:
                #caso a senha esteja correta chamamos a tela de menu
                self.parent.current = 'menu'
                ##############################################
                self.nome = pegar_nome(self.resposta.text)
                #############################################3
                return True, self.session_id

        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            PopErrorConection().open()

            print('erro de connection')
        
        
        
            
        
    
    
        
        
    
class Sigaa(App):
    def build(self):
        return Gerenciador()
    pass

Sigaa().run()
