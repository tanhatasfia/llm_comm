import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("=== DEVICE CHECK ===")
print("torch.cuda.is_available():", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))
    print("CUDA capability:", torch.cuda.get_device_capability(0))
print("====================\n")

model_id  = "LLM4Binary/llm4decompile-1.3b-v1.5"
asm_path  = "input_func.s"
cache_dir = "/tmleclab/C00581680/hf_cache"   # <-- adjust if needed

os.makedirs(cache_dir, exist_ok=True)

# --------------------------------------------------------
# 1. TOKENIZER
# --------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

# --------------------------------------------------------
# 2. LOAD FULL MODEL (NO QLORA)
# --------------------------------------------------------
print(">>> about to load FULL model (no 4-bit)")

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,   # or torch.float16 / torch.float32 if you prefer
    device_map="auto",            # try GPU if usable, else CPU
    cache_dir=cache_dir,
)

print("### one param device:", next(model.parameters()).device)
model.eval()

# --------------------------------------------------------
# 3. READ ASSEMBLY
# --------------------------------------------------------
with open(asm_path, "r", encoding="utf-8") as f:
    asm_code = f.read().strip()

# --------------------------------------------------------
# 4. BUILD PROMPT
# --------------------------------------------------------
prompt = "# This is the assembly code:\n" + asm_code + "\n# What is the source code?\n"

print("===== PROMPT SENT TO MODEL =====")
print(prompt)
print("================================\n")

# --------------------------------------------------------
# 5. RUN MODEL (ON SAME DEVICE AS MODEL)
# --------------------------------------------------------
inputs = tokenizer(prompt, return_tensors="pt")
device = next(model.parameters()).device
inputs = {k: v.to(device) for k, v in inputs.items()}

print("### inputs on:", inputs['input_ids'].device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=1024,
        do_sample=False,
    )

generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
c_result = tokenizer.decode(generated_ids, skip_special_tokens=True)

# --------------------------------------------------------
# 6. PRINT RESULT
# --------------------------------------------------------
print("===== DECOMPILED C CODE =====")
print(c_result)
print("================================")
