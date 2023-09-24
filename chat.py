from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "TheBloke/Xwin-LM-13B-V0.1-GPTQ",
    use_fast=True
)
model = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Xwin-LM-13B-V0.1-GPTQ",
    device_map="auto",
    trust_remote_code=False,
    revision="main"
)

# プロンプトの準備
prompt = """
### Instruction:
- You are my friend
- You are not AI
- You speak Japanese
- User's name is "kmizu"
- You are expert Java and C programmer.  You know everything about these languages
- You talk very casually with user
- You must not talk formally with user. For example, you must not use "です", "ます".

If you unserstand, say only 「はい」.

### ASSISTANT:
はい

### USER: 
以下のC言語プログラムをJavaに翻訳して欲しい。ただし、CのポインタはJavaでは参照に該当することに注意してね。と、Javaでは変数への参照を取得する機能（Cでの&a）はないから、xとyの型も変える必要があることにも注意してね。

void s(int *a, int * b) {
  int t = *a;
  *a = *b;
  *b = t;
}

int main(void) {
  int x = 100, y = 200;
  s(&x, &y);
  printf("x = %d, y = %d\n", x, y);
  return 0;
}

### ASSISTANT:
"""

# 推論の実行
with torch.no_grad():
    token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
    output_ids = model.generate(
        token_ids.to(model.device),
        temperature=0.01,
        do_sample=True,
        top_p=1,
        top_k=40,
        max_new_tokens=1000,
    )
output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1) :], skip_special_tokens=True)
print(output)
