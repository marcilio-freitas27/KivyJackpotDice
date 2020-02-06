from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from random import randint
from kivy.clock import Clock

Builder.load_string('''
<Primeiro>:
    orientation: 'vertical'
    #nome do jogo
    BoxLayout:
        pos_hint: {'center_x':0.5}
        size_hint: 0.3,0.7
        Label:
            font_size: 50
            text: 'Kivy Jackpot Dice'
    # imagens dos dados
    BoxLayout:
        pos_hint: {'center_x':0.5}
        size_hint: 0.3,0.5
        Image:
            id: um
            source:'dadoum.png'
        Image:
            id: dois
            source:'dadosdois.png'
        Image:
            id: tres
            source:'dadostres.png'
    # botões parar e iniciar
    BoxLayout:
        pos_hint: {'center_x':0.5}
        padding: 50
        spacing: 25
        size_hint: 0.5,0.5
        Button:
            id:inicia
            text:"Iniciar"
            on_release: root.iniciar(self)
        Button:
            id:para
            text:"Parar"
            on_release: root.parar(self)
    # tela de resultados
    BoxLayout:
        pos_hint: {'center_x':0.5}
        size_hint: 0.3,0.5
        Label:
            id: resultado
            font_size: 30
            text:"Vamos jogar!"

''')

class Primeiro(BoxLayout): 
    imagens = ['dadoum.png','dadosdois.png','dadostres.png','dadosquatro.png','dadoscinco.png','dadosseis.png']   
    # recebe a imagem escolhida quando inicia e quando para
    def callback(self, dt):
        self.ids.um.source = self.imagens[randint(0,5)]
        self.ids.dois.source = self.imagens[randint(0,5)]
        self.ids.tres.source = self.imagens[randint(0,5)]
    
    # dá inicio a troca de imagens ativando o contador 
    def iniciar(self, obj):
        # troca a imagem a cada 0.1 de tempo 
        Clock.schedule_interval(self.callback,0.1)
        # altera o valor da tela de resultados
        self.ids.resultado.text = "Lançados os dados..."

    # para a troca de imagens
    def parar(self,obj):
        Clock.unschedule(self.callback)
    
        #Condições de vitória

        # se 2 são iguais
        if self.ids.um.source == self.ids.dois.source and self.ids.um.source != self.ids.tres.source or \
            self.ids.um.source == self.ids.tres.source and self.ids.um.source != self.ids.dois.source or \
            self.ids.tres.source == self.ids.dois.source and self.ids.um.source != self.ids.dois.source :
                # altera o valor da tela de resultados
                self.ids.resultado.text = "Temos um vencedor!"

        # se 3 são iguais
        elif self.ids.um.source == self.ids.dois.source and \
            self.ids.um.source == self.ids.tres.source:
                self.ids.resultado.text = "Isso que é sorte!"

        # se nenhum é igual
        else:
            self.ids.resultado.text = "Não foi dessa vez."

class Iniciar(App):
    def build(self):
        return Primeiro()

if __name__ == "__main__":
    Iniciar().run()
