from prompt_toolkit import prompt
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token

def get_bottom_toolbar_tokens(cli):
    return [(Token.Toolbar, ' This is a toolbar. ')]

style = style_from_dict({
 
    Token.Toolbar: '#ffffff bg:#333333',
    })

text = prompt('> ', get_bottom_toolbar_tokens=get_bottom_toolbar_tokens, style=style)



print('You said: {}'.format(text))
