## **Top Commonly Raised Errors in Python (With Contexts)**

| Error                                 | What It Means                                        | When/Why You Should Raise It                                                                                                    | Example                                                                  |
| ------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `ValueError`                          | Argument has **correct type**, but **invalid value** | Raise when input **type is fine**, but the **content is not acceptable** (e.g., age < 0, empty name)                            | `if age < 0: raise ValueError("Age must be positive")`                   |
| `TypeError`                           | Operation received a **wrong type**                  | Raise when the **type of an argument is incorrect**, even if the value looks okay                                               | `if not isinstance(age, int): raise TypeError("Age must be an integer")` |
| `IndexError`                          | List or sequence index is **out of range**           | Raise if you're writing custom data structures (e.g., pagination or matrix access) and someone tries to access invalid position | `if index >= len(data): raise IndexError("Index out of bounds")`         |
| `KeyError`                            | Key not found in a dict                              | Raise when working with a custom mapping class or simulating dictionary behavior                                                | `if key not in my_dict: raise KeyError(f"Key {key} not found")`          |
| `AttributeError`                      | Attribute not found in object                        | Raise if you want to enforce interface/contract in dynamic behavior (like `getattr`)                                            | `raise AttributeError("Object must have 'save' method")`                 |
| `NotImplementedError`                 | Method is not yet implemented                        | Raise when you're defining **abstract methods** in base classes to force subclass implementation                                | `raise NotImplementedError("Subclasses must implement this")`            |
| `AssertionError`                      | An assertion failed                                  | Raise with `assert` when you want to **enforce conditions during development** or testing                                       | `assert x > 0, "x must be positive"`                                     |
| `RuntimeError`                        | Logical error that **doesn’t fit others**            | Raise when the program is in a **wrong or unstable state**, e.g., a resource was closed unexpectedly                            | `raise RuntimeError("Cannot call fetch before connecting")`              |
| `PermissionError`                     | Lacking permissions for an operation                 | Raise when user tries to do **unauthorized action**, e.g., writing to a restricted file                                         | `raise PermissionError("Write access denied")`                           |
| `ImportError` / `ModuleNotFoundError` | Module or object not found during import             | Raise in plugin loaders or dynamic imports where a **dependency is missing or wrong**                                           | `raise ImportError("Required module 'xyz' is not installed")`            |

---

### ✅ Use Case Example (Combined)

```python
def process_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("Expected a dictionary as input")

    if "name" not in data:
        raise KeyError("Missing required key: 'name'")

    name = data["name"]
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    if name.strip() == "":
        raise ValueError("Name cannot be empty")

    if len(name) > 50:
        raise ValueError("Name is too long")
```

---

### Summary Table (Cheat Sheet Style)

| Error                 | Best Use Case                             |
| --------------------- | ----------------------------------------- |
| `ValueError`          | Wrong value, correct type                 |
| `TypeError`           | Wrong type of argument                    |
| `KeyError`            | Missing dictionary key                    |
| `IndexError`          | Out-of-range access to list/sequence      |
| `AttributeError`      | Missing expected method/attribute         |
| `NotImplementedError` | Abstract base method or stub              |
| `AssertionError`      | Debug-only logic verification             |
| `RuntimeError`        | Invalid state not covered by other errors |
| `PermissionError`     | Unauthorized action attempted             |
| `ImportError`         | Missing required module or import failure |


