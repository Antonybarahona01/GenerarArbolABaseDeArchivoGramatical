import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    no_terminales = []
    terminales = []
    producciones = {}
    simbolo_inicial = None

    for linea in lineas:
        if linea.startswith("N:"):
            no_terminales = linea.replace("N:", "").strip().split(", ")
        elif linea.startswith("T:"):
            terminales = linea.replace("T:", "").strip().split(", ")
        elif linea.startswith("S:"):
            simbolo_inicial = linea.replace("S:", "").strip()
        elif linea.startswith("P:"):
            continue
        elif '->' in linea:
            izquierda, derecha = linea.split('->')
            izquierda = izquierda.strip()
            derecha = [x.strip().split() for x in derecha.split('|')]  # Cada lado se convierte en una lista de símbolos
            producciones[izquierda] = derecha
    return no_terminales, terminales, simbolo_inicial, producciones

def leer_cadena(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        cadena = archivo.read().strip()
    return cadena

def construir_arbol(gramatica, simbolo_inicial, cadena):
    G = nx.DiGraph()  # Usamos un grafo dirigido
    nodos_a_procesar = [(simbolo_inicial, None, cadena)]  # Lista de nodos a expandir, junto con su nodo padre y la cadena restante
    visitados = set()  # Para evitar ciclos

    while nodos_a_procesar:
        simbolo, padre, resto_cadena = nodos_a_procesar.pop(0)

        # Evita procesar nodos ya visitados
        if simbolo in visitados:
            continue
        visitados.add(simbolo)

        # Agrega el nodo al grafo
        G.add_node(simbolo)

        # Si tiene un padre, crea la arista (padre -> hijo)
        if padre is not None:
            G.add_edge(padre, simbolo)
        
        # Expande los hijos si el símbolo tiene reglas
        if simbolo in gramatica:
            for produccion in gramatica[simbolo]:
                if produccion == ["ε"]:  # Ignora producciones vacías
                    continue
                # Concatenar los símbolos de la producción con el resto de la cadena
                nuevo_resto_cadena = resto_cadena
                for hijo in reversed(produccion):
                    if hijo in gramatica or hijo in resto_cadena.split():  # Agrega solo si es un símbolo conocido
                        nodos_a_procesar.append((hijo, simbolo, nuevo_resto_cadena))

    return G

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)

    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)

    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
    
    return pos

def dibujar_arbol(G, simbolo_inicial):
    plt.figure(figsize=(10, 7))
    pos = hierarchy_pos(G, simbolo_inicial)  # Disposición jerárquica
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_weight="bold", arrows=True)
    plt.show()

# Archivos
nombre_archivo_gramatica = "gramatica.txt"
nombre_archivo_cadena = "cadena.txt"

# Leer la gramática y la cadena
no_terminales, terminales, simbolo_inicial, producciones = leer_gramatica(nombre_archivo_gramatica)
cadena = leer_cadena(nombre_archivo_cadena)

# Construir el árbol a partir de la gramática y la cadena
arbol = construir_arbol(producciones, simbolo_inicial, cadena)

# Dibujar el árbol con disposición de arriba hacia abajo
dibujar_arbol(arbol, simbolo_inicial)
