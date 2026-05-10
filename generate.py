import csv

HTML_TOP = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pruebas de CRM</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #333; }
    header { background-color: #1a73e8; color: white; padding: 20px 40px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
    header h1 { font-size: 1.8rem; font-weight: 600; }
    main { padding: 40px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; }
    .card { background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; }
    .card:hover { transform: translateY(-4px); box-shadow: 0 6px 16px rgba(0,0,0,0.12); }
    .card img { width: 100%; height: 180px; object-fit: cover; }
    .card-body { padding: 16px; }
    .card-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 8px; }
    .card-description { font-size: 0.9rem; color: #666; line-height: 1.5; margin-bottom: 12px; }
    .card-price { font-size: 1.2rem; font-weight: 700; color: #1a73e8; }
  </style>
</head>
<body>
  <header><h1>Pruebas de CRM</h1></header>
  <main><div class="grid">
"""

HTML_BOTTOM = """  </div></main>
</body>
</html>
"""

CARD = """    <div class="card">
      <img src="{foto}" alt="{titulo}">
      <div class="card-body">
        <div class="card-title">{titulo}</div>
        <div class="card-description">{descripcion}</div>
        <div class="card-price">{precio}</div>
      </div>
    </div>
"""

with open('productos.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    cards = ''.join(
        CARD.format(
            titulo=row['titulo'],
            descripcion=row['descripcion'],
            precio=row['precio'],
            foto=row['foto']
        )
        for row in reader
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_TOP + cards + HTML_BOTTOM)

print("index.html generado correctamente.")
