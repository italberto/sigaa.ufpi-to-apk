from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from login import pegar_id_autenticado
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass



class DoLogin(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    usuario_input = ObjectProperty()
    senha_input = ObjectProperty()
    
    def logar_se(self):
        usuario = str(self.usuario_input.text)
        senha = str(self.senha_input.text)
        self.resposta = pegar_id_autenticado( usuario, senha)
    
    
    
        
        
    
class Sigaa(App):
    def build(self):
        return Gerenciador()
    pass

Sigaa().run()
