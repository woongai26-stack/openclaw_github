#!/bin/zsh
# Sets the default model to the high-performance gpt-5.3-chat

echo "🚀 기본 모델을 고성능 GPT(openai/gpt-5.3-chat-latest)로 변경합니다..."
openclaw config set agents.defaults.defaultModel "openai/gpt-5.3-chat-latest"
echo "✅ 모델 변경 완료. OpenClaw를 재시작합니다."
openclaw gateway restart --note="Set default model to gpt-5.3-chat"
