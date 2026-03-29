#!/usr/bin/env python3
"""
개발 자동화 오케스트레이터
- 매뉴얼 로더, 컨텍스트 매니저, QC 러너를 통합 관리
"""

import sys
import os
from pathlib import Path
from manual_loader import ManualLoader
from qc_runner import QCRunner

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
MANUALS_DIR = PROJECT_ROOT / "manuals"


def load_context() -> dict:
    """3대 문서를 로드하여 현재 컨텍스트 반환"""
    context = {}
    for doc in ["PLAN.md", "CONTEXT.md", "TODO.md"]:
        path = DOCS_DIR / doc
        if path.exists():
            context[doc] = path.read_text(encoding="utf-8")
        else:
            context[doc] = "(파일 없음)"
    return context


def show_status():
    """현재 프로젝트 상태 출력"""
    context = load_context()
    print("=" * 50)
    print("📋 현재 프로젝트 상태")
    print("=" * 50)

    # TODO.md에서 진행 상황 파싱
    todo = context.get("TODO.md", "")
    done = todo.count("[x]")
    pending = todo.count("[ ]")
    total = done + pending

    print(f"\n진행률: {done}/{total} 완료")
    print(f"  ✅ 완료: {done}")
    print(f"  ⬜ 대기: {pending}")

    # PLAN.md 요약
    plan = context.get("PLAN.md", "")
    if "현재 프로젝트" in plan:
        for line in plan.split("\n"):
            if line.startswith("- **"):
                print(f"  {line.strip()}")


def run_workflow(task_description: str):
    """전체 워크플로우 실행"""
    loader = ManualLoader(MANUALS_DIR)

    # 1. 관련 매뉴얼 로드
    print("\n📖 관련 매뉴얼 로드 중...")
    relevant = loader.find_relevant(task_description)
    for chapter in relevant:
        print(f"  → {chapter}")

    # 2. 컨텍스트 로드
    print("\n📄 컨텍스트 로드 중...")
    context = load_context()
    for doc, content in context.items():
        status = "✅ 로드됨" if "(파일 없음)" not in content else "⬜ 비어있음"
        print(f"  {doc}: {status}")

    # 3. QC 준비
    print("\n🔍 QC 시스템 대기 중...")
    print("  → 작업 완료 시 자동으로 품질 검사가 실행됩니다.")

    return relevant, context


def main():
    if len(sys.argv) < 2:
        print("사용법: python orchestrator.py [status|run|qc] [설명]")
        print("  status  - 현재 프로젝트 상태 확인")
        print("  run     - 워크플로우 실행")
        print("  qc      - 품질 검사 실행")
        sys.exit(1)

    command = sys.argv[1]

    if command == "status":
        show_status()
    elif command == "run":
        desc = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        run_workflow(desc)
    elif command == "qc":
        runner = QCRunner(PROJECT_ROOT)
        runner.run_all()
    else:
        print(f"알 수 없는 명령: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
