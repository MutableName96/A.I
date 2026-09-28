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
    COLOR_OBSTACLE = "#1d3557"   # Color obstáculo
    COLOR_CURRENT = "#f4a261"    # Naranja suave: Nodo actual
    COLOR_PATH = "#e76f51"       # Trazo del camino final

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
        # 'SETUP_POINTS' -> 'SETUP_OBSTACLES' -> 'READY_TO_RUN' -> 'RUNNING' -> 'FINISHED'
        self.phase = "SETUP_POINTS"
        self.start_pos = None
        self.goal_pos = None
        self.obstacles = set()

        # Estructuras para el algoritmo interactivo
        self.open_set = []        # Min-heap: (f, counter, (r, c))
        self.open_members = set() # Rastreo rápido de celdas en lista abierta
        self.closed_set = set()   # Conjunto de visitados cerrados
        self.node_info = {}       # (r, c) -> {'g': float, 'h': float, 'f': float, 'parent': tuple}
        self.counter = 0          # Desempate de tuplas en heap
        self.animate_mode = True  # Bandera de animación
        self._search_job = None   # Temporizador de animación

        # Dimensiones visuales
        self.cell_size = 50
        self.offset = 24          # Espacio para los números de fila y columna

        # Mostrar formulario de configuración inicial
        self._build_config_form()

    def _build_config_form(self):
        """Construye los controles visuales (widgets) con textos claros e intuitivos."""
        self.root.title("Simulador A* - Configuración")
        
        # Desvincular teclas del tablero
        for key in ["<space>", "<Return>", "<r>", "<R>", "<c>", "<C>", "<e>", "<E>"]:
            self.root.unbind(key)

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

            if m < 4 or m > 20 or n < 4 or n > 20:
                messagebox.showerror("Error", "Para visualizar claramente f, g, h, las filas y columnas deben estar entre 4 y 20.")
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
            self._build_board_view()

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos en todos los campos.")

    def _build_board_view(self):
        """Dibuja la cuadrícula con coordenadas guía y el panel lateral para interacción."""
        self.root.title(f"A* - Tablero ({self.rows}x{self.cols})")

        self.board_container = tk.Frame(self.root, padx=15, pady=15, bg=self.COLOR_LIGHT)
        self.board_container.pack()

        # Canvas interactivo con margen superior e izquierdo para numeración de casillas
        canvas_width = self.cols * self.cell_size + self.offset
        canvas_height = self.rows * self.cell_size + self.offset

        self.canvas = tk.Canvas(
            self.board_container,
            width=canvas_width,
            height=canvas_height,
            bg=self.COLOR_LIGHT,
            highlightthickness=2,
            highlightbackground=self.COLOR_PRIMARY
        )
        self.canvas.grid(row=0, column=0, padx=(0, 15), sticky="n")
        self.canvas.bind("<Button-1>", self._on_canvas_click)

        # Panel lateral de control
        side_panel = tk.Frame(self.board_container, bg=self.COLOR_LIGHT)
        side_panel.grid(row=0, column=1, sticky="n")

        self.lbl_instructions = tk.Label(
            side_panel,
            text="1er clic: Inicio (Verde)\n2do clic: Meta (Rojo)\n\nPuedes dar clic sobre ellos para reubicarlos.",
            bg=self.COLOR_LIGHT,
            fg=self.COLOR_PRIMARY,
            font=("Arial", 9, "bold"),
            justify="left",
            wraplength=230
        )
        self.lbl_instructions.pack(pady=(0, 8))

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
            pady=4,
            cursor="hand2"
        )
        self.btn_confirm_points.pack(fill="x")

        # Botón para confirmar los obstáculos
        self.btn_confirm_obstacles = tk.Button(
            side_panel,
            text="Confirmar Obstáculos",
            command=self._confirm_obstacles,
            bg=self.COLOR_SECONDARY,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            state="disabled"
        )
        self.btn_confirm_obstacles.pack(fill="x", pady=(4, 8))

        # Sección de listas: Abierta y Cerrada (LC)
        tk.Label(
            side_panel, 
            text="Lista Abierta:", 
            bg=self.COLOR_LIGHT, 
            fg=self.COLOR_PRIMARY, 
            font=("Arial", 9, "bold")
        ).pack(anchor="w")

        self.lb_open = tk.Listbox(
            side_panel, 
            width=28, 
            height=3, 
            font=("Consolas", 8),
            bg="#ffffff",
            fg=self.COLOR_PRIMARY,
            highlightthickness=1,
            highlightbackground=self.COLOR_ACCENT
        )
        self.lb_open.pack(pady=(2, 4))

        tk.Label(
            side_panel, 
            text="Lista Cerrada (LC):", 
            bg=self.COLOR_LIGHT, 
            fg=self.COLOR_PRIMARY, 
            font=("Arial", 9, "bold")
        ).pack(anchor="w")

        self.lb_closed = tk.Listbox(
            side_panel, 
            width=28, 
            height=3, 
            font=("Consolas", 8),
            bg="#ffffff",
            fg=self.COLOR_PRIMARY,
            highlightthickness=1,
            highlightbackground=self.COLOR_ACCENT
        )
        self.lb_closed.pack(pady=(2, 6))

        # Botones de ejecución
        self.btn_run_step = tk.Button(
            side_panel,
            text="Animar [Espacio]",
            command=lambda: self._start_execution(animate=True),
            bg=self.COLOR_SECONDARY,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            state="disabled"
        )
        self.btn_run_step.pack(fill="x", pady=2)

        self.btn_run_direct = tk.Button(
            side_panel,
            text="Directo [Enter]",
            command=lambda: self._start_execution(animate=False),
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            state="disabled"
        )
        self.btn_run_direct.pack(fill="x", pady=2)

        # Botón 1: Reintentar escenario (mantiene obstáculos y puntos cargados)
        self.btn_retry_scenario = tk.Button(
            side_panel,
            text="Reintentar Escenario [E]",
            command=self._retry_scenario,
            bg=self.COLOR_SECONDARY,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            state="disabled"
        )
        self.btn_retry_scenario.pack(fill="x", pady=(6, 2))

        # Botón 2: Limpiar tablero completo
        self.btn_reset_board = tk.Button(
            side_panel,
            text="Limpiar Tablero [R]",
            command=self._reset_board,
            bg=self.COLOR_GOAL,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2"
        )
        self.btn_reset_board.pack(fill="x", pady=2)

        # Botón 3: Reconfigurar Dimensiones y Costos
        self.btn_reconfig = tk.Button(
            side_panel,
            text="Reconfigurar [C]",
            command=self._reconfigure,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_LIGHT,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2"
        )
        self.btn_reconfig.pack(fill="x", pady=2)

        # Enlace de atajos de teclado
        self.root.bind("<space>", lambda e: self._start_execution(animate=True))
        self.root.bind("<Return>", lambda e: self._start_execution(animate=False))
        self.root.bind("<e>", lambda e: self._retry_scenario())
        self.root.bind("<E>", lambda e: self._retry_scenario())
        self.root.bind("<r>", lambda e: self._reset_board())
        self.root.bind("<R>", lambda e: self._reset_board())
        self.root.bind("<c>", lambda e: self._reconfigure())
        self.root.bind("<C>", lambda e: self._reconfigure())

        self._draw_grid()

    def _retry_scenario(self):
        """Limpia los cálculos de la búsqueda pero conserva el Inicio, la Meta y los Obstáculos."""
        if self._search_job is not None:
            self.root.after_cancel(self._search_job)
            self._search_job = None

        self.phase = "READY_TO_RUN"
        self.open_set = []
        self.open_members = set()
        self.closed_set = set()
        self.node_info = {}
        self.counter = 0

        self.lb_open.delete(0, tk.END)
        self.lb_closed.delete(0, tk.END)

        self.btn_run_step.config(state="normal")
        self.btn_run_direct.config(state="normal")

        self.lbl_instructions.config(
            text="Escenario conservado.\n\nPulsa [Espacio] para animar o [Enter] para resolver directo."
        )

        self._draw_grid()

    def _reset_board(self):
        """Limpia todo el tablero actual manteniendo las dimensiones y costos configurados."""
        if self._search_job is not None:
            self.root.after_cancel(self._search_job)
            self._search_job = None

        self.phase = "SETUP_POINTS"
        self.start_pos = None
        self.goal_pos = None
        self.obstacles = set()
        self.open_set = []
        self.open_members = set()
        self.closed_set = set()
        self.node_info = {}
        self.counter = 0

        self.lb_open.delete(0, tk.END)
        self.lb_closed.delete(0, tk.END)

        self.btn_confirm_points.config(
            text="Confirmar Inicio y Meta",
            state="normal",
            bg=self.COLOR_SECONDARY
        )
        self.btn_confirm_obstacles.config(
            text="Confirmar Obstáculos",
            state="disabled",
            bg=self.COLOR_SECONDARY
        )
        self.btn_run_step.config(state="disabled")
        self.btn_run_direct.config(state="disabled")
        self.btn_retry_scenario.config(state="disabled")

        self.lbl_instructions.config(
            text="Tablero reiniciado.\n\n1er clic: Inicio (Verde)\n2do clic: Meta (Rojo)"
        )

        self._draw_grid()

    def _reconfigure(self):
        """Detiene cualquier búsqueda, destruye el tablero actual y regresa al formulario."""
        if self._search_job is not None:
            self.root.after_cancel(self._search_job)
            self._search_job = None

        self.board_container.destroy()
        self._build_config_form()

    def _draw_grid(self, current_eval=None):
        """Redibuja encabezados de filas/columnas, casillas, textos f/g/h y flechas directas."""
        self.canvas.delete("all")

        # Dibujar índices de columnas en la parte superior
        for c in range(self.cols):
            cx = self.offset + c * self.cell_size + self.cell_size // 2
            self.canvas.create_text(
                cx, self.offset // 2,
                text=str(c),
                font=("Arial", 9, "bold"),
                fill=self.COLOR_PRIMARY
            )

        # Dibujar índices de filas en la parte izquierda
        for r in range(self.rows):
            cy = self.offset + r * self.cell_size + self.cell_size // 2
            self.canvas.create_text(
                self.offset // 2, cy,
                text=str(r),
                font=("Arial", 9, "bold"),
                fill=self.COLOR_PRIMARY
            )

        # Dibujar casillas del tablero
        for r in range(self.rows):
            for c in range(self.cols):
                pos = (r, c)
                x1 = self.offset + c * self.cell_size
                y1 = self.offset + r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = self.COLOR_LIGHT
                if pos == self.start_pos:
                    color = self.COLOR_START
                elif pos == self.goal_pos:
                    color = self.COLOR_GOAL
                elif pos in self.obstacles:
                    color = self.COLOR_OBSTACLE
                elif pos == current_eval:
                    color = self.COLOR_CURRENT
                elif pos in self.closed_set:
                    color = "#bde0fe"
                elif pos in self.open_members:
                    color = self.COLOR_ACCENT

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="#d3d3d3",
                    width=1
                )

                # Si la celda tiene cálculos f, g, h y no es obstáculo, renderizarlos
                if pos in self.node_info and pos not in self.obstacles:
                    info = self.node_info[pos]
                    
                    self.canvas.create_text(
                        x1 + 4, y1 + 4,
                        text=f"f:{int(info['f'])}",
                        anchor="nw",
                        font=("Arial", 7, "bold"),
                        fill=self.COLOR_PRIMARY
                    )
                    self.canvas.create_text(
                        x1 + 4, y2 - 4,
                        text=f"g:{int(info['g'])}",
                        anchor="sw",
                        font=("Arial", 7),
                        fill=self.COLOR_PRIMARY
                    )
                    self.canvas.create_text(
                        x2 - 4, y2 - 4,
                        text=f"h:{int(info['h'])}",
                        anchor="se",
                        font=("Arial", 7),
                        fill=self.COLOR_PRIMARY
                    )

                    parent = info.get('parent')
                    if parent is not None:
                        self._draw_arrow_to_parent(pos, parent)

    def _draw_arrow_to_parent(self, current, parent):
        """Dibuja una flecha apuntando desde el centro del actual hacia el padre."""
        r, c = current
        pr, pc = parent
        
        cx = self.offset + c * self.cell_size + self.cell_size // 2
        cy = self.offset + r * self.cell_size + self.cell_size // 2
        
        px = self.offset + pc * self.cell_size + self.cell_size // 2
        py = self.offset + pr * self.cell_size + self.cell_size // 2

        dx = px - cx
        dy = py - cy
        dist = (dx**2 + dy**2) ** 0.5
        if dist > 0:
            arrow_len = self.cell_size * 0.28
            target_x = cx + (dx / dist) * arrow_len
            target_y = cy + (dy / dist) * arrow_len
            
            self.canvas.create_line(
                cx, cy, target_x, target_y,
                arrow=tk.LAST,
                arrowshape=(6, 8, 3),
                fill=self.COLOR_PRIMARY,
                width=2
            )

    def _on_canvas_click(self, event):
        """Mapea clics del usuario compensando el margen de las etiquetas de fila/columna."""
        if event.x < self.offset or event.y < self.offset:
            return

        col = (event.x - self.offset) // self.cell_size
        row = (event.y - self.offset) // self.cell_size

        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        cell = (row, col)

        # Fase 1: Selección de Inicio y Meta
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

        # Fase 2: Colocación de Obstáculos
        elif self.phase == "SETUP_OBSTACLES":
            if cell == self.start_pos or cell == self.goal_pos:
                return

            if cell in self.obstacles:
                self.obstacles.remove(cell)
            else:
                self.obstacles.add(cell)

            self._draw_grid()

    def _confirm_points(self):
        """Valida que ambos puntos existan y habilita el modo de obstáculos."""
        if self.start_pos is None or self.goal_pos is None:
            messagebox.showwarning("Atención", "Debes seleccionar tanto el punto de Inicio como la Meta antes de continuar.")
            return

        self.phase = "SETUP_OBSTACLES"

        self.btn_confirm_points.config(
            text="Puntos Confirmados ✔",
            state="disabled",
            bg=self.COLOR_PRIMARY
        )
        self.btn_confirm_obstacles.config(
            state="normal"
        )
        self.lbl_instructions.config(
            text=f"Inicio: {self.start_pos}\nMeta: {self.goal_pos}\n\nModo Obstáculos:\nHaz clic para colocar o remover muros.\nAl terminar, pulsa 'Confirmar Obstáculos'."
        )

    def _confirm_obstacles(self):
        """Fija los obstáculos y prepara los controles de ejecución del algoritmo."""
        self.phase = "READY_TO_RUN"
        self.btn_confirm_obstacles.config(
            text="Obstáculos Confirmados ✔",
            state="disabled",
            bg=self.COLOR_PRIMARY
        )
        self.btn_run_step.config(state="normal")
        self.btn_run_direct.config(state="normal")
        self.btn_retry_scenario.config(state="normal")

        self.lbl_instructions.config(
            text=f"Obstáculos fijados: {len(self.obstacles)}\n\nPulsa [Espacio] para animar o [Enter] para correr directo."
        )

    def _get_neighbors(self, pos):
        """Retorna los vecinos transitables en 8 direcciones con sus costos respectivos."""
        r, c = pos
        directions = [
            ((-1, 0), self.cost_straight),  # Arriba
            ((1, 0), self.cost_straight),   # Abajo
            ((0, -1), self.cost_straight),  # Izquierda
            ((0, 1), self.cost_straight),   # Derecha
            ((-1, -1), self.cost_diag),     # Diagonal Sup-Izq
            ((-1, 1), self.cost_diag),      # Diagonal Sup-Der
            ((1, -1), self.cost_diag),      # Diagonal Inf-Izq
            ((1, 1), self.cost_diag)        # Diagonal Inf-Der
        ]
        valid_neighbors = []
        for (dr, dc), cost in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if (nr, nc) not in self.obstacles:
                    valid_neighbors.append(((nr, nc), cost))
        return valid_neighbors

    def _start_execution(self, animate=True):
        """Prepara las estructuras iniciales antes de lanzar la búsqueda."""
        if self.phase != "READY_TO_RUN":
            return

        self.phase = "RUNNING"
        self.animate_mode = animate
        self.btn_run_step.config(state="disabled")
        self.btn_run_direct.config(state="disabled")
        self.btn_retry_scenario.config(state="normal")

        # Inicialización de la búsqueda A*
        self.open_set = []
        self.open_members = set()
        self.closed_set = set()
        self.node_info = {}
        self.counter = 0

        h_start = manhattan(self.start_pos, self.goal_pos)
        self.node_info[self.start_pos] = {
            'g': 0.0,
            'h': float(h_start),
            'f': float(h_start),
            'parent': None
        }

        heapq.heappush(self.open_set, (float(h_start), self.counter, self.start_pos))
        self.open_members.add(self.start_pos)

        # Actualizar vista de listas
        self.lb_open.delete(0, tk.END)
        self.lb_closed.delete(0, tk.END)
        self.lb_open.insert(tk.END, f"{self.start_pos} | f={h_start:.0f}")

        # Iniciar ciclo de búsqueda
        self._step_search()

    def _step_search(self):
        """Ejecuta un paso individual de la expansión de nodos de A*."""
        if not self.open_set:
            self.phase = "FINISHED"
            self.lbl_instructions.config(text="No existe un camino posible hasta la meta.\n\n[E] Reintentar | [R] Limpiar | [C] Configurar")
            messagebox.showinfo("Búsqueda finalizada", "No existe un camino transitable hacia la meta.")
            return

        # Extraer el nodo con menor f(n)
        f_val, _, current = heapq.heappop(self.open_set)
        if current in self.open_members:
            self.open_members.remove(current)

        # Si el nodo ya estaba en lista cerrada, continuar (defensa de heap)
        if current in self.closed_set:
            if self.animate_mode:
                self._search_job = self.root.after(10, self._step_search)
            else:
                self._step_search()
            return

        # Insertar en Lista Cerrada (LC)
        self.closed_set.add(current)
        self.lb_closed.insert(0, f"{current} | f={f_val:.0f}")

        # Redibujar resaltando el nodo que se está evaluando actualmente
        self._draw_grid(current_eval=current)

        # Condición de éxito: Llegamos a la meta
        if current == self.goal_pos:
            self.phase = "FINISHED"
            self._reconstruct_and_draw_path()
            self.lbl_instructions.config(text="¡Camino óptimo encontrado!\n\n[E] Reintentar escenario | [R] Limpiar tablero")
            return

        # Expansión de adyacencias en 8 direcciones
        for nxt, move_cost in self._get_neighbors(current):
            # REGLA DE NO-RECALCULACIÓN:
            # Si el nodo ya fue calculado/visitado previamente (está en node_info o en closed_set), se omite
            if nxt in self.closed_set or nxt in self.node_info:
                continue

            # Cálculo de nuevos valores
            new_g = self.node_info[current]['g'] + move_cost
            h = float(manhattan(nxt, self.goal_pos))
            f = new_g + h

            # Registro definitivo (sin recalculación)
            self.node_info[nxt] = {
                'g': new_g,
                'h': h,
                'f': f,
                'parent': current
            }

            self.counter += 1
            heapq.heappush(self.open_set, (f, self.counter, nxt))
            self.open_members.add(nxt)
            self.lb_open.insert(0, f"{nxt} | f={f:.0f}")

        # Programar siguiente paso (observable o inmediato)
        if self.animate_mode:
            self._search_job = self.root.after(120, self._step_search)
        else:
            self._step_search()

    def _reconstruct_and_draw_path(self):
        """Traza la línea continua y resalta los cuadros del camino final hallado."""
        curr = self.goal_pos
        path = []
        while curr is not None:
            path.append(curr)
            curr = self.node_info[curr]['parent']
        path.reverse()

        # Dibujar líneas del camino conectando los centros compensados
        for i in range(len(path) - 1):
            r1, c1 = path[i]
            r2, c2 = path[i + 1]
            x1 = self.offset + c1 * self.cell_size + self.cell_size // 2
            y1 = self.offset + r1 * self.cell_size + self.cell_size // 2
            x2 = self.offset + c2 * self.cell_size + self.cell_size // 2
            y2 = self.offset + r2 * self.cell_size + self.cell_size // 2

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill=self.COLOR_PATH,
                width=4,
                capstyle=tk.ROUND,
                joinstyle=tk.ROUND
            )


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = AStarGUI(root)
    root.mainloop()