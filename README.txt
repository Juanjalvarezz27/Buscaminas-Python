PROYECTO BUSCAMINAS - PYTHON POO FREELANCE

DESCRIPCIÓN:
Este es un juego clásico de Buscaminas implementado en Python usando el paradigma de Programación Orientada a Objetos (POO). El juego se ejecuta en consola y permite seleccionar distintos niveles de dificultad.

REQUISITOS:
- Python 3.7 o superior instalado
- Editor como Visual Studio Code (opcional)
- Consola/terminal para ejecutar el juego

INSTRUCCIONES DE USO:
1. Clona o copia todo el proyecto en una carpeta local.
2. Asegúrate de tener el archivo `records.json` en la misma carpeta que el código.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta el archivo principal con:
   python main.py
5. El juego se ejecutará por consola, y te permitirá:
   - Ingresar tu nombre
   - Seleccionar la dificultad
   - Revelar o marcar casillas escribiendo comandos

FUNCIONALIDADES:
✔ Juego completo de Buscaminas en consola  
✔ Interfaz por texto clara y amigable  
✔ 4 niveles de dificultad (Fácil, Medio, Difícil, Imposible)  
✔ Número de minas calculado automáticamente según dificultad  
✔ Expansión automática de casillas vacías  
✔ Marcado de casillas como bandera (`!`) o duda (`?`)  
✔ Control de errores: coordenadas inválidas o casillas ya reveladas  
✔ Limpieza de consola al actualizar el tablero  
✔ Registro de los 3 mejores tiempos en un archivo JSON  
✔ Comentarios claros para facilitar comprensión y mantenimiento del código  

ARCHIVOS CLAVE:
- `main.py`: punto de entrada al programa
- `juego.py`: controla el flujo general del juego
- `tablero.py`: maneja el tablero y su lógica
- `casillas.py`: define las casillas (mina o vacía)
- `jugador.py`: maneja la interacción con el jugador
- `config_loader.py`: lee y guarda los récords
- `records.json`: archivo donde se guardan los mejores tiempos

AUTORÍA:
- Desarrollado por: [Juan Jose Sarmiento Alvarez]

