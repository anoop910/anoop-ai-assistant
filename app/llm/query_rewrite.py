
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class QueryRewriter:

    def __init__(self):

        MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float32,
            device_map="cpu"
        )

    def rewrite(self, system_prompt: str, user_prompt: str):
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=40,
            do_sample=False,
            temperature=0.0
        )

        result = self.tokenizer.decode(
            outputs[0][inputs.input_ids.shape[1]:],
            skip_special_tokens=True
        )

        return result.strip()


# ----------------------------
# Example
# ----------------------------

# if __name__ == "__main__":

#     rewriter = QueryRewriter()

#     conversation = [
#         "User: Tell me about ResumeIQ.",
#         "Assistant: ResumeIQ is an AI-powered resume screening application."
#     ]

#     question = "How does it work?"

#     print(rewriter.rewrite(conversation, question))