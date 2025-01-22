import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    #project_manager tests
    suite = loader.discover('./tests')
    runner.run(suite)
