import heapq
import tkinter as tk
from tkinter import messagebox


# =============================================================================
# FUNCIONES matematicas y algoritmos base
# =============================================================================

def manhattan(a, b):
    """
        a (tuple): Coordenadas de origen (fila, columna).
        b (tuple): Coordenadas de destino (fila, columna).
    Retorna:
        int: Distancia Manhattan absoluta |x1 - x2| + |y1 - y2|.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(start, goal, neighbors, cost=1):
    """
    Ejecuta el algoritmo clásico A* para encontrar la ruta óptima en un grafo.
    Utiliza una cola de prioridad (min-heap) para expandir primero los nodos
    con el menor costo estimado total f(n) = g(n) + h(n).
    Parámetros:
        start (tuple): Nodo de partida (fila, columna).
        goal (tuple): Nodo objetivo (fila, columna).
        neighbors (callable): Función generadora que recibe (r, c) y retorna
                              una lista de coordenadas vecinas transitables.
        cost (float, opcional): Costo de traslación entre nodos adyacentes.
    Retorna:
        list: Lista ordenada de tuplas (fila, columna) que conforman el camino,
              o None si no existe una ruta accesible.
    """
    open_heap = []
    heapq.heappush(open_heap, (manhattan(start, goal), 0, start))
    g_score = {start: 0}
    came_from = {}

    while open_heap:
        f, g, current = heapq.heappop(open_heap)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return list(reversed(path))

        for nxt in neighbors(current):
            new_g = g_score[current] + cost

            if nxt not in g_score or new_g < g_score[nxt]:
                g_score[nxt] = new_g
                came_from[nxt] = current
                h = manhattan(nxt, goal)
                heapq.heappush(open_heap, (new_g + h, new_g, nxt))

    return None


# =============================================================================
# INTERFAZ
# =============================================================================

class AStarGUI:
    """
    Controlador de la interfaz gráfica de usuario para el simulador A*.

    Gestiona el ciclo de vida de la ventana: captura de parámetros de entrada,
    validaciones numéricas, inicialización del lienzo matricial y orquestación
    de eventos de interacción del usuario.
    """

    # Definición de la paleta de colores del proyecto
    COLOR_PRIMARY = "#1d3557"    # Azul oscuro
    COLOR_SECONDARY = "#457b9d"  # Azul medio
    COLOR_ACCENT = "#a8dadc"     # Azul celeste
    COLOR_LIGHT = "#f1faee"      # Blanco crema
    COLOR_START = "#16db65"      # Verde inicio
    COLOR_GOAL = "#e01e37"       # Rojo meta

    def __init__(self, root):
        """
        Inicializa las propiedades del entorno gráfico y despliega el formulario.

        Parámetros:
            root (tk.Tk): Instancia principal de la ventana Tkinter.
        """
        self.root = root
        self.root.title("Simulador A* - Configuración")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLOR_LIGHT)

        # Dimensiones y costos iniciales por defecto
        self.rows = 12
        self.cols = 12
        self.cost_straight = 10.0
        self.cost_diag = 14.0

        # Variables reactivas para las entradas de texto
        self.rows_var = tk.StringVar(value="12")
        self.cols_var = tk.StringVar(value="12")
        self.cost_straight_var = tk.StringVar(value="10")
        self.cost_diag_var = tk.StringVar(value="14")

        # Control del estado del tablero
        self.phase = "SETUP_POINTS"  # 'SETUP_POINTS' -> siguiente paso será 'SETUP_OBSTACLES'
        self.start_pos = None
        self.goal_pos = None

        # Tamaño en píxeles de cada cuadro de la cuadrícula
        self.cell_size = 40

        # Mostrar formulario de configuración inicial
        self._build_config_form()

    def _build_config_form(self):
        """Construye los controles visuales (widgets) con textos claros e intuitivos."""
        self.config_frame = tk.Frame(self.root, padx=30, pady=25, bg=self.COLOR_LIGHT)
        self.config_frame.pack()

        # Título y descripción breve
        tk.Label(
            self.config_frame, 
            text="Parámetros del Tablero", 
            font=("Arial", 13, "bold"),
            bg=self.COLOR_LIGHT,
            fg=self.COLOR_PRIMARY
        ).grid(row=0, column=0, columnspan=2, pady=(0, 18))

        # Estilo común para etiquetas de texto
        lbl_style = {"bg": self.COLOR_LIGHT, "fg": self.COLOR_PRIMARY, "font": ("Arial", 9, "bold"), "anchor": "w"}
        entry_style = {"bg": "#ffffff", "fg": self.COLOR_PRIMARY, "relief": "solid", "bd": 1, "highlightthickness": 0}

        # Entradas de dimensiones
        tk.Label(self.config_frame, text="Filas:", **lbl_style).grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(self.config_frame, textvariable=self.rows_var, width=12, **entry_style).grid(row=1, column=1, pady=5)

        tk.Label(self.config_frame, text="Columnas:", **lbl_style).grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(self.config_frame, textvariable=self.cols_var, width=12, **entry_style).grid(row=2, column=1, pady=5)

        # Entradas de costos
        tk.Label(self.config_frame, text="Costo horizontal y vertical (↑ ↓ ← →):", **lbl_style).grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(self.config_frame, textvariable=self.cost_straight_var, width=12, **entry_style).grid(row=3, column=1, pady=5)

        tk.Label(self.config_frame, text="Costo diagonal (↗ ↘ ↙ ↖):", **lbl_style).grid(row=4, column=0, sticky="w", pady=5)
        tk.Entry(self.config_frame, textvariable=self.cost_diag_var, width=12, **entry_style).grid(row=4, column=1, pady=5)

        # Botón para generar la cuadrícula
        btn_generate = tk.Button(
            self.config_frame,
            text="Generar Cuadrícula",
            command=self._confirm_config,
            bg=self.COLOR_SECONDARY,
            fg=self.COLOR_LIGHT,
            activebackground=self.COLOR_PRIMARY,
            activeforeground=self.COLOR_LIGHT,
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=6,
            cursor="hand2"
        )
        btn_generate.grid(row=5, column=0, columnspan=2, pady=(18, 5))

    def _confirm_config(self):
        """Valida que los valores numéricos sean válidos y genera la cuadrícula."""
        try:
            m = int(self.rows_var.get().strip())
            n = int(self.cols_var.get().strip())
            c_str = float(self.cost_straight_var.get().strip())
            c_diag = float(self.cost_diag_var.get().strip())

            if m < 4 or m > 25 or n < 4 or n > 25:
                messagebox.showerror("Error", "Las filas y columnas deben estar entre 4 y 25.")
                return

            if c_str <= 0 or c_diag <= 0:
                messagebox.showerror("Error", "Los costos de movimiento deben ser mayores a 0.")
                return

            self.rows = m
            self.cols = n
            self.cost_straight = c_str
            self.cost_diag = c_diag

            # Destruir el formulario y dibujar la cuadrícula
            self.config_frame.destroy()
            self._build_grid_view()

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos en todos los campos.")

    def _build_grid_view(self):
        """Dibuja la cuadrícula y el panel lateral para seleccionar y confirmar Inicio y Meta."""
        self.root.title(f"A* - Tablero ({self.rows}x{self.cols})")

        container = tk.Frame(self.root, padx=15, pady=15, bg=self.COLOR_LIGHT)
        container.pack()

        # Canvas interactivo
        canvas_width = self.cols * self.cell_size
        canvas_height = self.rows * self.cell_size

        self.canvas = tk.Canvas(
            container,
            width=canvas_width,
            height=canvas_height,
            bg=self.COLOR_LIGHT,
            highlightthickness=2,
            highlightbackground=self.COLOR_PRIMARY
        )
        self.canvas.grid(row=0, column=0, padx=(0, 15))
        self.canvas.bind("<Button-1>", self._on_canvas_click)

        # Panel lateral de control
        side_panel = tk.Frame(container, bg=self.COLOR_LIGHT)
        side_panel.grid(row=0, column=1, sticky="n")

        self.lbl_instructions = tk.Label(
            side_panel,
            text="1er clic: Inicio (Verde)\n2do clic: Meta (Rojo)\n\nPuedes dar clic sobre ellos para reubicarlos.",
            bg=self.COLOR_LIGHT,
            fg=self.COLOR_PRIMARY,
            font=("Arial", 9, "bold"),
            justify="left",
            wraplength=200
        )
        self.lbl_instructions.pack(pady=(0, 15))

        # Botón para confirmar las posiciones elegidas
        self.btn_confirm_points = tk.Button(
            side_panel,
            text="Confirmar Inicio y Meta",
            command=self._confirm_points,
            bg=self.COLOR_SECONDARY,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2"
        )
        self.btn_confirm_points.pack(fill="x")

        self._draw_grid()

    def _draw_grid(self):
        """Redibuja las casillas de la matriz aplicando colores de Inicio y Meta si están definidos."""
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = self.COLOR_LIGHT
                if (r, c) == self.start_pos:
                    color = self.COLOR_START
                elif (r, c) == self.goal_pos:
                    color = self.COLOR_GOAL

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=self.COLOR_ACCENT,
                    width=1
                )

    def _on_canvas_click(self, event):
        """Maneja los clics para asignar y reubicar Inicio y Meta."""
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        cell = (row, col)

        if self.phase == "SETUP_POINTS":
            if self.start_pos is None:
                self.start_pos = cell
            elif self.goal_pos is None and cell != self.start_pos:
                self.goal_pos = cell
            elif cell == self.start_pos:
                self.start_pos = None
            elif cell == self.goal_pos:
                self.goal_pos = None
            else:
                self.goal_pos = cell

            self._draw_grid()

    def _confirm_points(self):
        """Valida que ambos puntos existan antes de avanzar."""
        if self.start_pos is None or self.goal_pos is None:
            messagebox.showwarning("Atención", "Debes seleccionar tanto el punto de Inicio como la Meta antes de continuar.")
            return

        self.btn_confirm_points.config(
            text="Puntos Confirmados ✔",
            state="disabled",
            bg=self.COLOR_PRIMARY
        )
        self.lbl_instructions.config(
            text=f"Inicio fijado en: {self.start_pos}\nMeta fijada en: {self.goal_pos}\n\n a chambear.png"
        )


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = AStarGUI(root)
    root.mainloop()