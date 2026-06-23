import os

def analizar_archivo(ruta_absoluta: str) -> bool:
    """
    Analiza un archivo en busca de firmas maliciosas.
    Devuelve True si detecta una amenaza (malware), False si está limpio.
    """
    # Método 1: Detección por extensión de archivo
    # Si el desarrollador sube un archivo con estas extensiones, lo bloqueamos.
    extensiones_bloqueadas = ['.malicioso', '.virus', '.ransomware']
    
    for ext in extensiones_bloqueadas:
        if ruta_absoluta.lower().endswith(ext):
            return True

    # Método 2: Detección por firma interna (Análisis heurístico básico)
    # Buscamos una cadena de texto específica que simula ser el código de un virus.
    firma_virus_prueba = "RUSTGUARD-TEST-SIGNATURE-12345"

    try:
        # Intentamos leer el archivo como texto plano
        with open(ruta_absoluta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            if firma_virus_prueba in contenido:
                return True
    except UnicodeDecodeError:
        # Si el archivo es un binario (ej. una imagen o un .exe) y no se puede leer como texto, 
        # pasamos de largo en esta prueba básica para evitar que el script falle.
        pass
    except Exception as e:
        print(f"No se pudo analizar el archivo {ruta_absoluta}: {e}")

    # Si pasa las pruebas, el archivo está limpio
    return False
