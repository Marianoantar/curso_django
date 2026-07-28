from django.shortcuts import render

# Create your views here.

def lista_juegos(request):
    juegos = [
        {
            "nombre": "The Legend of Zelda: Breath of the Wild", 
            "plataforma": "Nintendo Switch", 
            "precio": 59.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Legend_of_Zelda_Breath_of_the_Wild_cover.png"
        },
        {
            "nombre": "God of War", 
            "plataforma": "PlayStation 4", 
            "precio": 39.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/a/a7/God_of_War_4_cover.jpg"
        },
        {
            "nombre": "Halo Infinite", 
            "plataforma": "Xbox Series X", 
            "precio": 59.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/1/14/Halo_Infinite.png"
        },
        {
            "nombre": "Cyberpunk 2077", 
            "plataforma": "PC", 
            "precio": 49.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/9/9f/Cyberpunk_2077_box_art.jpg"
        },
        {
            "nombre": "Minecraft", 
            "plataforma": "PC", 
            "precio": 29.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover_art.png"
        },
        {
            "nombre": "Super Mario Odyssey", 
            "plataforma": "Nintendo Switch", 
            "precio": 59.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/8/8d/Super_Mario_Odyssey.jpg"
        },
        {
            "nombre": "Red Dead Redemption 2", 
            "plataforma": "PlayStation 4", 
            "precio": 59.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg"
        },
        {
            "nombre": "Forza Horizon 5", 
            "plataforma": "Xbox Series X", 
            "precio": 59.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/8/86/Forza_Horizon_5_cover_art.jpg"
        },
        {
            "nombre": "The Witcher 3: Wild Hunt", 
            "plataforma": "PC", 
            "precio": 39.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg"
        },
        {
            "nombre": "Animal Crossing: New Horizons", 
            "plataforma": "Nintendo Switch", 
            "precio": 59.99,
            "imagen_url": "https://upload.wikimedia.org/wikipedia/en/1/10/Animal_Crossing_New_Horizons.png"
        },
    ]

    contexto_catalogo_juegos = {'lista_juegos': juegos}

    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)