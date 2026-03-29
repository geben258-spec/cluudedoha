---
name: load-manual
description: 키워드에 맞는 매뉴얼 챕터를 로드합니다. 특정 가이드라인을 확인하거나 작업 전 규칙을 참조할 때 사용하세요.
---

# 매뉴얼 로드

키워드 기반으로 관련 매뉴얼 챕터를 찾아 읽습니다.

## Step 1: 목차 확인
`manuals/index.md`를 읽고 전체 챕터 목록 확인.

## Step 2: 키워드 매칭
사용자 요청에서 키워드를 추출하여 관련 챕터 선택:

| 키워드 | 챕터 |
|--------|------|
| 구조, 설계, 폴더, 레이어 | `chapters/architecture.md` |
| UI, 컴포넌트, 스타일, React | `chapters/frontend.md` |
| API, 서버, 라우트, 인증 | `chapters/backend.md` |
| DB, 모델, 스키마, 쿼리 | `chapters/database.md` |
| 보안, 토큰, 암호화, XSS | `chapters/security.md` |

## Step 3: 챕터 읽기 및 요약
관련 챕터를 읽고 사용자에게 핵심 규칙을 요약하여 전달.
여러 챕터가 관련되면 모두 로드.
