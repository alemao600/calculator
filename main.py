from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from num2words import num2words

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(12)

        MDLabel:
            text: "Conversor de Moedas"
            halign: "center"
            font_style: "H5"

        MDTextField:
            id: entrada_reais
            hint_text: "Valor em R$"
            input_filter: "float"
            helper_text: "Use vírgula ou ponto"
            helper_text_mode: "on_focus"

        MDLabel:
            id: resultado_label
            text: ""
            halign: "center"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(8)

            MDRaisedButton:
                text: "Converter"
                md_bg_color: app.theme_cls.success_color
                on_release: app.converter()

            MDRaisedButton:
                text: "Mostrar/Ocultar Histórico"
                on_release: app.toggle_historico()

            MDRaisedButton:
                text: "Mostrar/Ocultar Conversão"
                on_release: app.toggle_conversao()

            MDFlatButton:
                text: "Alternar Tema"
                on_release: app.alternar_tema()

        # Caixa da taxa (inicia oculta)
        MDBoxLayout:
            id: taxa_box
            orientation: "vertical"
            adaptive_height: True
            size_hint_y: None
            height: 0
            opacity: 0
            disabled: True
            spacing: dp(8)

            MDLabel:
                text: "Taxa de conversão (ex: 1950)"
                theme_text_color: "Secondary"

            MDTextField:
                id: entrada_taxa
                text: "1950"
                input_filter: "float"

        # Caixa do histórico (inicia oculta)
        MDBoxLayout:
            id: historico_box
            orientation: "vertical"
            adaptive_height: True
            size_hint_y: None
            height: 0
            opacity: 0
            disabled: True
            spacing: dp(8)

            MDLabel:
                text: "Histórico"
                theme_text_color: "Secondary"

            ScrollView:
                size_hint_y: None
                height: dp(150)
                MDList:
                    id: historico_list
'''


class ConversorApp(MDApp):
    def build(self):
        self.title = "Calculadora de Moedas"
        self.theme_cls.theme_style = "Dark"
        self.historico = []
        return Builder.load_string(KV)

    def formatar_resultado(self, valor: float) -> str:
        inteiro = int(valor)
        decimal = round((valor - inteiro) * 100)
        extenso_inteiro = num2words(inteiro, lang='pt_BR')
        if decimal > 0:
            extenso_decimal = num2words(decimal, lang='pt_BR')
            extenso_completo = f"{extenso_inteiro} e {extenso_decimal}"
        else:
            extenso_completo = extenso_inteiro
        valor_formatado = f"{valor:,.2f}".replace(",", ".")
        return f"{valor_formatado} moedas ({extenso_completo})"

    def converter(self):
        try:
            reais_str = self.root.ids.entrada_reais.text.strip().replace(",", ".")
            reais = float(reais_str)
            taxa = float(self.root.ids.entrada_taxa.text.strip().replace(",", "."))
            resultado = reais * taxa
            texto_resultado = self.formatar_resultado(resultado)
            self.root.ids.resultado_label.text = texto_resultado

            self.historico.append(f"R$ {reais:.2f} → {texto_resultado}")
            self.atualizar_historico()
        except ValueError:
            from kivymd.toast import toast
            toast("Digite um número válido.")

    def atualizar_historico(self):
        from kivymd.uix.list import OneLineListItem
        lista = self.root.ids.historico_list
        lista.clear_widgets()
        for item in self.historico[-10:]:
            lista.add_widget(OneLineListItem(text=item))

    def _toggle_box(self, box):
        # Mostra/oculta usando altura e opacidade
        if box.height == 0:
            box.disabled = False
            box.opacity = 1
            box.height = box.minimum_height
        else:
            box.disabled = True
            box.opacity = 0
            box.height = 0

    def toggle_historico(self):
        self._toggle_box(self.root.ids.historico_box)

    def toggle_conversao(self):
        self._toggle_box(self.root.ids.taxa_box)

    def alternar_tema(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )


if __name__ == "__main__":
    ConversorApp().run() 