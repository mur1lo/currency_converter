"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import requests
import currency


class CurrencyConverter(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Label
        self.label = toga.Label(
            "Selecione a moeda e insira o valor:",
            style=Pack(padding=(0, 5))
        )

        # Dropdown para selecionar a moeda
        self.currency_options = toga.Selection(
            items=currency.getCurrencies(),
            style=Pack(padding=(0, 5)),
            accessor="value"
        )
        
        # TextInput para inserir o valor
        self.value_input = toga.NumberInput(style=Pack(padding=(0, 5)))

        # Button para converter
        self.convert_button = toga.Button(
            "Converter",
            on_press=self.convert_currency,
            style=Pack(padding=(5, 5))
        )

        # Label para exibir o resultado
        self.result_label = toga.Label(
            "Resultado: ",
            style=Pack(padding=(0, 5))
        )

        # Adicionando os widgets à caixa principal
        main_box.add(self.label)
        main_box.add(self.currency_options)
        main_box.add(self.value_input)
        main_box.add(self.convert_button)
        main_box.add(self.result_label)

        # Definindo a caixa principal como a janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def convert_currency(self, widget):
        currency = self.currency_options.value.key
        value = self.value_input.value
        try:
            value = float(value)
            rate = self.get_exchange_rate(currency)
            result = value * rate
            self.result_label.text = f"Resultado: {result:.2f} BRL"
        except ValueError:
            self.result_label.text = "Por favor, insira um valor numérico."

    def get_exchange_rate(self, currency):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
        response = requests.get(api_url)
        data = response.json()
        return data["rates"]["BRL"]

def main():
    return CurrencyConverter('Currency Converter', 'Currency Converter')


if __name__ == '__main__':
    main().main_loop()
