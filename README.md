# thread
Smallest library that every project needs!

It just... Runs your function in new thread with decorator!

```bash
pip install thread
```

# Use
```python
from thread import threaded

@threaded
def func():
    print("Printed from new thread!")
func()
```

