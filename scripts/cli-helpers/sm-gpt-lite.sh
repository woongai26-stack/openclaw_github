#!/bin/zsh
# Sets the default model to the cost-effective gpt-4o-mini

echo "🚀 기본 모델을 가성비 GPT(openai/gpt-4o-mini)로 변경합니다..."
openclaw config set agents.defaults.defaultModel openai/gpt-4o-mini
echo "✅ 모델 변경 완료. OpenClaw를 재시작합니다."
openclaw gateway restart --note="Set default model to gpt-4o-mini"
