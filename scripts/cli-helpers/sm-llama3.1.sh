#!/bin/zsh
# Sets the default model to the local ollama llama3.1 model

echo "🚀 기본 모델을 로컬 LLM(ollama/llama3.1:latest)으로 변경합니다..."
openclaw config set agents.defaults.model ollama/llama3.1:latest
echo "✅ 모델 변경 완료. OpenClaw를 재시작합니다."
openclaw gateway restart --note="Set default model to local Llama3.1"
