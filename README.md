##   
Python `uuid` Module Overview

The `uuid` module in Python facilitates the generation and manipulation of Universally Unique Identifiers (UUIDs). UUIDs are 128-bit unique identifiers commonly used in distributed computing.

### Generating UUIDs

1.  **uuid1()**: Generates a UUID based on the current timestamp and hardware address.enter code here
    
    pythonCopy code
    
    `import uuid
    uuid1 = uuid.uuid1()` 
    
2.  **uuid4()**: Generates a random UUID.
    
    pythonCopy code
    
    `import uuid
    uuid4 = uuid.uuid4()` 
    

### UUID Properties and Methods

-   `hex`: Returns a hexadecimal string representation of the UUID.
-   `int`: Returns the UUID as a 128-bit integer.
-   `urn`: Returns the UUID as a URN (Uniform Resource Name).
-   `bytes`: Returns the UUID as a 16-byte string.
    
    pythonCopy code
    
    `import uuid
    uuid_obj = uuid.uuid4()
    print(uuid_obj.hex)
    print(uuid_obj.int)
    print(uuid_obj.urn)
    print(uuid_obj.bytes)` 
    

### Parsing UUIDs

Parse a UUID from a string using the `uuid.UUID` constructor.

pythonCopy code

`import uuid
uuid_str = "550e8400-e29b-41d4-a716-446655440000"
parsed_uuid = uuid.UUID(uuid_str)` 

These examples demonstrate the basic usage of the `uuid` module for UUID generation, properties access, and parsing in Python. Depending on your specific use case, choose the appropriate function or method.


![image](https://github.com/wathika-eng/AirBnB_clone/assets/71040609/4218289d-276f-48e8-a97c-e8e6a4974976)
