from typing import Optional

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
    def __init__(self, model: str, system_message: str, user_input: str):
        self.model = model
        self.system_message = system_message
        self.user_input = user_input

    def llm_generate(self) -> str:
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": self.user_input},
            ],
            # max_tokens=256,
            max_tokens=2048,
            top_p=0.8,
            n=1,
        )
        return response.text

    def observe(self) -> Optional[str]:
        msg = self.llm_generate()
        return extract_code(msg)

    def wave_function(self, x: Any) -> Any:
        pass
