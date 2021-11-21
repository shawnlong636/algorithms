import unittest
import sys
import logging
import test  

def main():
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger('graph').setLevel( logging.DEBUG )

    loader = unittest.TestLoader()
    suite = loader.discover('./test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()
    