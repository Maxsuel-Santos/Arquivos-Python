# Classe responsável por criar a Interface Gráfica e gerar o texto a ser pesquisado no Twitter

import PySimpleGUI as sg


class TwitterSearchInterface:

    def __init__(self):
        sg.theme('LightGray1')

        # Cria a Tela
        self.layout = [
            [sg.Text('Palavras-chave')],
            [sg.InputText(key='keywords')],
            [sg.Text('Conta')],
            [sg.InputText(key='from')],
            [sg.Text('Para usuários')],
            [sg.InputText(key='to')],
            [sg.Text('Mencionando usuários')],
            [sg.InputText(key='mentioning')],
            [sg.Text('Hashtags')],
            [sg.InputText(key='hashtags')],
            [sg.Text('Mínimo de Replies')],
            [sg.InputText(key='min_replie')],
            [sg.Text('Mínimo de Retweets')],
            [sg.InputText(key='min_retweet')],
            [sg.Text('Mínimo de Likes')],
            [sg.InputText(key='min_like')],
            [sg.Text('Língua')],
            [sg.Combo(['', 'pt', 'en', 'es', 'fr'], key='lang'),
             sg.Checkbox('Links', key='links', size=(10, 1)),
             sg.Checkbox('Replies', key='replies', size=(10, 1))],
            [sg.Text('De'),
             sg.Input(key='data1', size=(10, 1), disabled=True, disabled_readonly_background_color='#252531'), sg.CalendarButton('Selecione uma data', target='data1', format='%Y-%m-%d')],
            [sg.Text('Até'),
             sg.Input(key='data2', size=(10, 1), disabled=True, disabled_readonly_background_color='#252531'), sg.CalendarButton('Selecione uma data', target='data2', format='%Y-%m-%d')],

            [sg.Button('Buscar'), sg.Button('Cancelar')]


        ]

        self.window = sg.Window('Busca avançada do Twitter', self.layout)

    # Inicia a Tela
    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                break
            if event == 'Buscar':
                if self.all_fields_empty(values):
                    sg.popup('Por favor, preencha pelo menos um campo.')
                else:
                    generate_search = self.generate_search(values)
                    print(generate_search)

                    break

        self.window.close()
        return values

    # Verifica se todos os campos estão vazios
    def all_fields_empty(self, values):
        for value in values.values():
            if isinstance(value, str) and value.strip() != '':
                return False
        return True

    # Faz o tratamento dos dados dos campos
    def generate_search(self, values):
        params = ''

        txt_keywords = values['keywords'].strip()
        if txt_keywords != '':
            params += txt_keywords

        txt_hashtags = values['hashtags'].strip()
        if txt_hashtags != '':
            if txt_hashtags[0] == '#':
                params += ' ('+txt_hashtags + ')'
            else:
                params += ' (#'+txt_hashtags + ')'

        txt_from = values['from'].strip()
        if txt_from != '':
            params += ' (from:'+txt_from + ')'

        txt_to = values['to'].strip()
        if txt_to != '':
            params += ' (to:'+txt_to + ')'

        txt_mentioning = values['mentioning'].strip()
        if txt_mentioning != '':
            params += ' (@'+txt_mentioning + ')'

        txt_min_replie = values['min_replie'].strip()
        if txt_min_replie != '':
            params += ' min_replies:'+txt_min_replie

        txt_min_like = values['min_like'].strip()
        if txt_min_like != '':
            params += ' min_faves:'+txt_min_like

        txt_min_retweet = values['min_retweet'].strip()
        if txt_min_retweet != '':
            params += ' min_retweets:'+txt_min_retweet

        txt_lang = values['lang'].strip()
        if txt_lang != '':
            params += ' lang:'+txt_lang

        txt_until = values['data2'].strip()
        if txt_until != '':
            params += ' until:'+txt_until

        txt_since = values['data1'].strip()
        if txt_since != '':
            params += ' since:'+txt_since

        links = values['links']
        if links is False:
            params += ' -filter:links'

        replies = values['replies']
        if replies is False:
            params += ' -filter:replies'

        return params


# Cria uma instância da classe TwitterSearchInterface (somente para testes)
screen = TwitterSearchInterface()
search_params = screen.run()
print(search_params)
