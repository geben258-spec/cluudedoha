# Chapter 2: 프론트엔드 가이드라인

**키워드**: UI, 컴포넌트, 스타일, React, 페이지, 화면

## 2.1 컴포넌트 규칙
- 컴포넌트는 재사용 가능하게 설계
- Props는 TypeScript 인터페이스로 정의
- 한 컴포넌트 파일은 200줄 이하 유지

## 2.2 상태 관리
- 로컬 상태: useState/useReducer
- 전역 상태: 상태 관리 라이브러리 사용
- 서버 상태: 데이터 페칭 라이브러리(SWR, React Query 등) 사용

## 2.3 스타일링
- 일관된 스타일링 방식 사용 (CSS Modules / Tailwind / Styled Components 중 택 1)
- 매직 넘버 대신 디자인 토큰 사용
- 반응형 디자인 필수 (모바일 우선)

## 2.4 접근성
- 시맨틱 HTML 태그 사용
- aria-label 적절히 배치
- 키보드 네비게이션 지원
