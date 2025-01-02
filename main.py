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

    result = wf.wave_function(x=1)
    print(result)
