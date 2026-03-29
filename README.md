# 🤖 Dev Automation Orchestrator Agent (cluudedoha)

AI가 길을 잃지 않게 만드는 **강제적 가이드라인 시스템**.

## 핵심 개념

```
사용자 요청 → 매뉴얼 자동 로드 → 계획 수립 → 승인 → 코딩 → QC 자동 검사
```

| 시스템 | 역할 | 파일 |
|--------|------|------|
| **Manual Loader** | 키워드 기반 매뉴얼 자동 주입 | `hooks/manual-loader-hook.js` |
| **Context Manager** | 3대 문서로 기억력 보완 | `docs/PLAN.md, CONTEXT.md, TODO.md` |
| **Automatic QC** | 파일 수정 시 자동 품질 검사 | `hooks/qc-hook.js` |

## 사용법 (Claude Code 스킬)

```
/plan          → 코딩 전 계획 수립 + 3대 문서 생성
/execute       → 계획대로 실행 + 매뉴얼 준수
/review        → 100점 채점 품질 검사
/status        → 진행률 확인
/load-manual   → 매뉴얼 키워드 검색
```

## 전문 에이전트

| 에이전트 | 역할 | 파일 |
|----------|------|------|
| Planner | 요구사항 → 기술적 태스크 분해 | `agents/planner.md` |
| Coder | PLAN.md 기반 정확한 구현 | `agents/coder.md` |
| Reviewer | 100점 기준 코드 리뷰 + 보안 점검 | `agents/reviewer.md` |
| Tester | 엣지 케이스 포함 테스트 설계/실행 | `agents/tester.md` |

## 매뉴얼 (규칙집)

| 챕터 | 키워드 |
|------|--------|
| `architecture.md` | 구조, 설계, 폴더, 레이어 |
| `frontend.md` | UI, 컴포넌트, 스타일, React |
| `backend.md` | API, 서버, 라우트, 인증 |
| `database.md` | DB, 모델, 스키마, 마이그레이션 |
| `security.md` | 보안, 토큰, 암호화, XSS |

## 자동 트리거

- **PreToolUse**: 코드 작성/수정 전 관련 매뉴얼 자동 감지
- **PostToolUse**: 파일 수정 후 PLAN.md/TODO.md 상태 자동 체크

## Setup

1. Clone: `git clone https://github.com/geben258-spec/cluudedoha.git`
2. Claude Code에서 `cd cluudedoha`
3. `/plan`으로 시작
