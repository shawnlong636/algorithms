import unittest
import test  

def main():
    loader = unittest.TestLoader()
    suite = loader.discover('./test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    main()