"""Arma www/index.html (pagina completa, instalable) a partir de hocico.html."""
import pathlib, sys
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../hocico.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#3a461c">
<meta name="description" content="Hocico: ¿lo puede comer mi perro o mi gato? Cuidados, recordatorios y emergencias.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font-size:14px}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
# La libreria de QR va dentro de la app (funciona sin internet)
src = src.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>',
                  '<script src="qrcode.min.js"></script>')
tail = """
<script>
if ('serviceWorker' in navigator && location.protocol === 'https:') {
  navigator.serviceWorker.register('sw.js').catch(function(){});
}
</script>
</body>
</html>
"""
pathlib.Path("www/index.html").write_text(head + src + tail, encoding="utf-8")
print("www/index.html listo")
