---
name: execute
description: PLAN.md의 계획대로 코딩을 실행합니다. TODO.md의 태스크를 순서대로 처리하고, 매뉴얼 규칙을 준수하며 구현합니다.
---

# 계획 실행

PLAN.md에 승인된 계획을 순서대로 실행합니다.

## Step 1: 현재 상태 확인
- `docs/TODO.md`를 읽고 다음 처리할 태스크 확인
- `docs/CONTEXT.md`를 읽고 기존 기술적 결정 확인
- `docs/PLAN.md`를 읽고 전체 설계 확인

## Step 2: 매뉴얼 로드
현재 태스크의 키워드에 따라 관련 매뉴얼 챕터를 읽기:
- API 관련 → `manuals/chapters/backend.md`
- UI 관련 → `manuals/chapters/frontend.md`
- DB 관련 → `manuals/chapters/database.md`
- 보안 관련 → `manuals/chapters/security.md`
- 구조 관련 → `manuals/chapters/architecture.md`

## Step 3: 코딩 실행
- 매뉴얼 규칙 준수
- PLAN.md에 없는 기능 추가 금지
- 한 태스크씩 순서대로 처리

## Step 4: 태스크 완료 처리
각 태스크 완료 시:
1. `docs/TODO.md`에서 해당 항목을 `[x]`로 변경
2. 새로운 기술적 결정이 있었다면 `docs/CONTEXT.md` 업데이트
3. 다음 태스크로 이동

## Step 5: 전체 완료 시
모든 태스크 완료 후 `/review` 스킬을 실행하여 품질 검사 진행.
