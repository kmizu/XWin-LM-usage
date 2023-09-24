python -m venv venv
source venv/bin/activate
pip install "transformers>=4.32.0" "optimum>=1.12.0"
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/
