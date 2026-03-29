#!/bin/bash
# 작업 완료 후 자동 QC 실행 스크립트
# 사용법: bash hooks/post-task.sh

echo "🔍 자동 품질 검사 시작..."

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# 1. 변경된 파일 확인
echo ""
echo "📁 변경된 파일:"
cd "$PROJECT_ROOT" && git diff --name-only 2>/dev/null
cd "$PROJECT_ROOT" && git diff --cached --name-only 2>/dev/null

# 2. TODO.md 업데이트 확인
if [ -f "$PROJECT_ROOT/docs/TODO.md" ]; then
    PENDING=$(grep -c "\[ \]" "$PROJECT_ROOT/docs/TODO.md" 2>/dev/null || echo 0)
    DONE=$(grep -c "\[x\]" "$PROJECT_ROOT/docs/TODO.md" 2>/dev/null || echo 0)
    echo ""
    echo "📋 TODO 상태: ✅ $DONE 완료 / ⬜ $PENDING 대기"
else
    echo ""
    echo "⚠️  docs/TODO.md가 없습니다!"
fi

# 3. PLAN.md 존재 확인
if [ ! -f "$PROJECT_ROOT/docs/PLAN.md" ]; then
    echo "⚠️  docs/PLAN.md가 없습니다! /plan을 먼저 실행하세요."
fi

# 4. Python QC 러너 실행 (있으면)
if [ -f "$PROJECT_ROOT/scripts/qc_runner.py" ]; then
    echo ""
    python "$PROJECT_ROOT/scripts/qc_runner.py"
fi

echo ""
echo "✅ 품질 검사 완료"
