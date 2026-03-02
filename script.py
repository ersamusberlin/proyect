import subprocess
import configparser

# Leer la configuración desde el archivo config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Obtener los parámetros del archivo de configuración
command = config.get('gp', 'command')
action = config.get('gp', 'action')
reader = config.get('gp', 'reader')


# Función para ejecutar gp.exe con los parámetros obtenidos
def run_gp_command():
    try:
        # Construir el comando a ejecutar
        command_to_run = [command, action, "--reader", reader]

        # Ejecutar el comando utilizando subprocess
        result = subprocess.run(command_to_run, capture_output=True, text=True)

        # Mostrar la salida del comando
        print("Comando ejecutado:", " ".join(command_to_run))
        print("Salida del comando:", result.stdout)

        # Guardar la salida en un archivo
        with open('gp_output.txt', 'w') as f:
            f.write(result.stdout)

    except Exception as e:
        print("Error al ejecutar gp.exe:", e)


# Llamar a la función para ejecutar el comando
run_gp_command()