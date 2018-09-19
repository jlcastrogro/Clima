import getopt


def options():
    print(
        """Opciones:
    --server (-s)   Dirección del servidor
    --user (-u)     Nombre de usuario
    --password (-p) Contraseña de usuario
    --help (-h)     Mostrar este menú
    """)


def attributes(args):
    try:
        opts, args = getopt.getopt(
            args, "s:u:p:h", ["server=", "user=", "password=", "help"])
    except getopt.GetoptError:
        print("Error en parámetros")
    for opt, arg in opts:
        if opt in ("-s", "--server"):
            server = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-h", "--help"):
            options()

    return (server, user, password, args)
