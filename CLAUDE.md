# Dev Automation Orchestrator Agent

## Overview
이 프로젝트는 AI 에이전트가 길을 잃지 않게 만드는 **강제적 가이드라인 시스템**입니다.
AI에게 단순히 일을 시키는 것이 아니라, 매뉴얼/계획/품질검사를 통해 체계적으로 개발을 진행합니다.

## Project Structure
```
cluudedoha/
├── manuals/               # 프로젝트 규칙 매뉴얼
│   ├── index.md           # 전체 목차 (항상 먼저 읽음)
│   └── chapters/          # 기능별 상세 챕터
│       ├── architecture.md
│       ├── frontend.md
│       ├── backend.md
│       ├── database.md
│       └── security.md
├── docs/                  # 작업 기억 시스템 (3대 문서)
│   ├── PLAN.md            # 전체 설계도
│   ├── CONTEXT.md         # 기술적 결정 이유
│   └── TODO.md            # 현재 작업 상태
├── scripts/               # 자동화 스크립트
│   ├── orchestrator.py    # 메인 오케스트레이터
│   ├── manual_loader.py   # 매뉴얼 자동 로더
│   └── qc_runner.py       # 품질 검사 실행기
├── agents/                # 전문 에이전트 프롬프트
│   ├── planner.md         # 기획 에이전트
│   ├── coder.md           # 코딩 에이전트
│   ├── reviewer.md        # 코드 리뷰 에이전트
│   └── tester.md          # 테스트 에이전트
├── hooks/                 # Git/CLI 후킹
│   └── post-task.sh       # 작업 완료 후 자동 QC
└── .claude/commands/      # Claude Code 스킬
```

## Workflow
1. `/plan` → 계획 수립 (PLAN.md, CONTEXT.md, TODO.md 생성)
2. `/execute` → 계획대로 실행 (매뉴얼 자동 참조)
3. `/review` → 품질 검사 (셀프 체크 + 리뷰 보고서)
4. `/status` → 현재 진행 상태 확인

## Rules
- 코딩 전 반드시 PLAN.md 작성 및 승인
- 매뉴얼(manuals/) 규칙을 항상 준수
- 작업 완료 시 TODO.md 업데이트 필수
- REVIEW.md 보고서 없이 "완료" 보고 금지
