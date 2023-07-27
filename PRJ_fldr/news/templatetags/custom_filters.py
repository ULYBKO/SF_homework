from django import template


register = template.Library()
blacklist = ['You', 'many', 'We', 'How']
text = 'new1.title'

@register.filter()
def censor(sentence):
    text = sentence.split()
    for i, word in enumerate(text):
        if word in blacklist:
            text[i] = word[0] + '***'
    return ' '.join(text)