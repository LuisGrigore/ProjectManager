import unittest

if __name__ == '__main__':
    # Descubrir todas las pruebas en el paquete "tests"
    loader = unittest.TestLoader()
    suite = loader.discover('./test_project_manager')

    # Ejecutar las pruebas
    runner = unittest.TextTestRunner()
    runner.run(suite)
