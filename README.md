# calculator
Python package for calculator.

# docs
```bash
cd docs
make html

open build/html/index.html
```

# unit test
```bash
pytest

====================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.7.0, pytest-5.3.1, py-1.8.0, pluggy-0.13.1
rootdir: /Users/daniel/Projects/python/calculator
collected 2 items                                                                                                                                                                               

src/test/calculator_demo/test_op.py ..                                                                                                                                                    [100%]

======================================================================================= 2 passed in 0.07s =======================================================================================
```

# setup
1. Local install.
```bash
python setup.py sdist

pip install dist/calculator_demo-0.0.1.tar.gz
```

2. Test installed package.
```python
from calculator_demo.op import hello_world

hello_world()
# >>> Hello, World!
```