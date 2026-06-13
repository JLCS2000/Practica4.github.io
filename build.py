import os

  os.makedirs("output", exist_ok=True)

  with open("output/index.html", "w") as f:
      f.write("""<!DOCTYPE html>
  <html>
  <head><title>Practica4</title></head>
  <body>
    <h1>Hello World!</h1>
    <p>Deployed automatically via CI/CD.</p>
  </body>
  </html>""")

  print("Build complete!")

