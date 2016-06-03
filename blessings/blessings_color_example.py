# http://readings.grelution.com/?p=370

from blessings import Terminal

if __name__ == "__main__":

    # create a new instance of Terminal class
    terminal = Terminal()

    print("Your terminal supports {0} different colors.\n".format(terminal.number_of_colors))

    indentation = 3 * terminal.move_right()

    print("Text with different background color:")
    for c in range(1, terminal.number_of_colors):
        formatted_text = terminal.color(c)("Sample text is displayed in different colors")
        print(indentation + formatted_text)

    print('\n')

    print("Text with different foreground color:")
    for c in range(1, terminal.number_of_colors):
        print(indentation + terminal.on_color(c)("Sample text is displayed in different colors"))

    print('\n')

    # custom formatting
    print(terminal.bold_italic_white_on_red('Freaky text entered.'))
    print(terminal.bold_underline_cyan_on_black('This is a bold cyan text on black.'))

    # moving the cursor can be handy when text
    # has to be displayed in different locations
    print(terminal.move_down() + 'This is one row down!')
    print(terminal.move_right() + 'This is one column to the right!')
