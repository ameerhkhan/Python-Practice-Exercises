#A simple example of what can be done with first class functions.

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return(wrap_text)

# Above types of definition of functions are also called closure functions.

print_h1 = html_tag('h1') #This equal print_h1 to the wrap_text function.
print_h1('First Headline') #giving this argument to wrap_text function so that it may execute.
print_h1('Another Headline') #same same

print_p = html_tag('p')
print_p('Test Paragraph')
