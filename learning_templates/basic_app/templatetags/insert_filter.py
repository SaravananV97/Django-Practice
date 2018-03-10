from django import template

register = template.Library()

def replacer(s,word):
    return s.replace(word,"Hello")

register.filter("cut",replacer)
