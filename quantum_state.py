import os
from typing import Optional, Any

import openai

def extract_code(msg: str) -> Optional[str]:
    if "```" not in msg:
        return None
    code_st = False
    code = ""
    for line in msg.splitlines():
        if code_st:
            if line.strip().startswith("```"):
                break
            code += line + "\n"
        else:
            if line.strip().startswith("```"):
                code_st = True
    return code


class QuantumState:
    def __init__(self, model: str, system_message: str):
        self.model = model
        self.system_message = system_message
        self.client = openai.OpenAI(
            base_url=os.getenv("OPENAI_URL"),
            api_key=os.getenv("OPENAI_KEY"),
        )

    def llm_generate(self, user_input: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": user_input},
            ],
            # max_tokens=256,
            max_tokens=2048,
            top_p=0.8,
            n=1,
        )
        response = response.choices[0].message.content
        return response

    def observe(self, user_input: str) -> Optional[str]:
        msg = self.llm_generate(user_input)
        # print(f"llm msg:\n {msg}")
        return extract_code(msg)

    def wave_function(self, x):
        try:
            # signature = inspect.signature(QuantumState.wave_function)
            # signature_str = str(signature)
            signature_str = "def custom_func(x): "
            code = self.observe(f"""
            Now we have a python function signature: `{signature_str}`.
            The input variable type is `{type(x)}`, and the output variable type is `{type(x)}`.
            You can implement any Python function with your custom logic.
            I will not tell you implement what process logic, you determine it.
            We will only provide you the signature of this function, help me impl the function body.
            """)
            if code is None:
                return None

            # print("executing:\n" + code)

            namespace = {}
            exec(code, namespace)
            ret = namespace["custom_func"](x)
            return ret
        except Exception as e:
            print(f"exec error: {e}")
            return x
