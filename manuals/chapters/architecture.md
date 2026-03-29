# Chapter 1: 아키텍처 가이드라인

**키워드**: 구조, 설계, 폴더, 레이어, 모듈

## 1.1 폴더 구조 원칙
- 기능(Feature) 기반 폴더 구성 우선
- 공통 유틸리티는 `shared/` 또는 `common/`에 배치
- 순환 의존성(Circular Dependency) 금지

## 1.2 레이어 분리
```
Presentation (UI/API) → Business Logic (Service) → Data Access (Repository)
```
- 상위 레이어는 하위 레이어만 호출 가능
- 하위 레이어는 상위 레이어를 알지 못함
- 레이어 간 데이터 전달은 DTO/모델 객체 사용

## 1.3 모듈 설계
- 한 모듈은 하나의 책임만 가짐 (Single Responsibility)
- 모듈 간 통신은 명시적 인터페이스를 통해서만
- 새 모듈 추가 시 반드시 PLAN.md에 기록

## 1.4 설정 관리
- 환경별 설정은 `.env` 파일로 관리
- 하드코딩된 설정값 금지
- 설정 스키마는 별도 파일로 문서화
