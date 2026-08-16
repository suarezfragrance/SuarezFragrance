from flask import Flask, render_template

app = Flask(__name__)

perfumes = {

    "rayhaan-aquatica": {
        "nombre": "Rayhaan Aquatica",
        "marca": "Rayhaan",
        "imagen": "rayhaan-aquatica.jpeg",
        "descripcion": "Fresco, acuático y perfecto para uso diario.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$90 MXN",
        "decant_10": "$160 MXN",
        "categoria": "arabe"
    },

    "rayhaan-elixir": {
        "nombre": "Rayhaan Elixir",
        "marca": "Rayhaan",
        "imagen": "rayhaan-elixir.jpeg",
        "descripcion": "Dulce, elegante y con gran presencia.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$80 MXN",
        "decant_10": "$140 MXN",
        "categoria": "arabe"
    },

    "honor-glory": {
        "nombre": "Badee Al Oud Honor & Glory",
        "marca": "Lattafa",
        "imagen": "honor-glory.jpeg",
        "descripcion": "Piña, vainilla y especias con un estilo dulce.",
       "precio": "Botella completa bajo pedido",
        "decant_5": "$60 MXN",
        "decant_10": "$110 MXN",
        "categoria": "arabe"
    },

    "spectre-wraith": {
        "nombre": "Spectre Wraith",
        "marca": "French Avenue",
        "imagen": "spectre-wraith.jpeg",
        "descripcion": "Dulce, misterioso y con un estilo diferente.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$80 MXN",
        "decant_10": "$140 MXN",
        "categoria": "arabe"
    },

    "khamrah-qahwa": {
        "nombre": "Khamrah Qahwa",
        "marca": "Lattafa",
        "imagen": "khamrah-qahwa.jpeg",
        "descripcion": "Fragancia dulce con café, especias y vainilla.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$70 MXN",
        "decant_10": "$120 MXN",
        "categoria": "arabe"
    },

    "afnan-9am-dive": {
    "nombre": "Afnan 9AM Dive",
    "marca": "Afnan",
    "imagen": "afnan-9am-dive.jpeg",
    "descripcion": "Una fragancia masculina fresca, acuática y cítrica, con un estilo limpio, moderno y versátil.",
    "precio": "Botella completa bajo pedido",
    "decant_5": "$55 MXN",
    "decant_10": "$100 MXN",
    "categoria": "arabe"
},

"lattafa-asad": {
    "nombre": "Lattafa Asad",
    "marca": "Lattafa",
    "imagen": "lattafa-asad.jpeg",
    "descripcion": "Una fragancia masculina cálida, especiada y ambarada, con un carácter intenso, dulce y elegante.",
    "precio": "Botella completa bajo pedido",
    "decant_5": "$60 MXN",
    "decant_10": "$110 MXN",
    "categoria": "arabe"
},

    "yara-tous": {
    "nombre": "Lattafa Yara Tous Women EDP",
    "marca": "Lattafa",
    "imagen": "yara-tous.jpeg",
    "descripcion": "Una fragancia femenina dulce, tropical y cremosa con un toque elegante y sofisticado.",
    "precio": "Botella completa bajo pedido",
    "decant_5": "$55 MXN",
    "decant_10": "$100 MXN",
    "categoria": "arabe"
    },

    "lattafa-eclaire": {
    "nombre": "Lattafa Eclaire EDP",
    "marca": "Lattafa",
    "imagen": "lattafa-eclaire.jpeg",
    "descripcion": "Una fragancia femenina dulce y cremosa con notas gourmand de vainilla, caramelo y leche, elegante y reconfortante.",
    "precio": "Botella completa bajo pedido",
    "decant_5": "$60 MXN",
    "decant_10": "$110 MXN",
    "categoria": "arabe"
},



   
    "eros-edp": {
        "nombre": "Versace Eros Eau de Parfum",
        "marca": "Versace",
        "imagen": "eros-edp.jpeg",
        "descripcion": "Dulce, fresco y con estilo juvenil.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$110 MXN",
        "decant_10": "$210 MXN",
        "categoria": "disenador"
    },

    "dylan-blue": {
        "nombre": "Versace Dylan Blue",
        "marca": "Versace",
        "imagen": "dylan-blue.jpeg",
        "descripcion": "Fresco, elegante y versátil.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$100 MXN",
        "decant_10": "$180 MXN",
        "categoria": "disenador"
    },

    "azzaro": {
        "nombre": "Azzaro The Most Wanted",
        "marca": "Azzaro",
        "imagen": "the-most-wanted.jpeg",
        "descripcion": "Fragancia dulce, intensa y masculina. Perfecta para noches y ocasiones especiales.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$100 MXN",
        "decant_10": "$180 MXN",
        "categoria": "disenador"
    },

    "montblanc-explorer": {
    "nombre": "Montblanc Explorer EDP",
    "marca": "Montblanc",
    "imagen": "montblanc-explorer.jpeg",
    "descripcion": "Una fragancia masculina fresca, amaderada y elegante, ideal para el uso diario y ocasiones especiales.",
    "precio": "Botella completa bajo pedido",
    "decant_5": "$80 MXN",
    "decant_10": "$150 MXN",
    "categoria": "diseñador"
},

"lacoste-l1212-noir": {
    "nombre": "Lacoste L.12.12 Noir",
    "marca": "Lacoste",
    "imagen": "lacoste-l1212-noir.jpeg",
    "descripcion": "Una fragancia masculina fresca, dulce y amaderada, con un estilo casual y elegante.",
    "precio": "Botella completa bajo pedido",
    "decant_5": "$80 MXN",
    "decant_10": "$150 MXN",
    "categoria": "diseñador"
},


    "swy-intensely": {
        "nombre": "Stronger With You Intensely",
        "marca": "Emporio Armani",
        "imagen": "swy-intensely.jpeg",
        "descripcion": "Dulce, cálido y elegante, ideal para noches frías.",
        "precio": "Botella completa bajo pedido",
        "decant_5": "$160 MXN",
        "decant_10": "$300 MXN",
        "categoria": "disenador"
    }


}

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", perfumes=perfumes)


@app.route("/producto/<nombre>")
def producto(nombre):

    perfume = perfumes.get(nombre)

    if perfume is None:
        return "Perfume no encontrado", 404


    mensaje = f"Hola, me interesa el perfume {perfume['nombre']}. ¿Sigue disponible?"


    return render_template(
        "producto.html",
        perfume=perfume,
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(debug=True)