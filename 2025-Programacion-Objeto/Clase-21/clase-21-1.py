from html.parser import HTMLParser





salida=HTMLParser()
salida.feed("<html><head><title>Mi Primer pagina web</title></head><body><h1>Primer titulo</h1></body></html>")
print(salida)


