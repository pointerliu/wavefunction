import math

from quantum_state import QuantumState
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    wf = QuantumState(
        model="gpt-3.5-turbo",
        system_message="""
        From now on, you are an imaginative and creative programmer.
        """
    )

    t = 1
    for epoch in range(10):
        t = wf.wave_function(x=t)
        print(t)
