# Chapter 5: 보안 가이드라인

**키워드**: 인증, 권한, 토큰, 암호화, XSS, SQL Injection, 보안

## 5.1 입력 검증
- 모든 사용자 입력은 서버 측에서 검증
- SQL Injection 방지: 파라미터 바인딩 필수
- XSS 방지: 출력 시 이스케이프 처리

## 5.2 인증 보안
- 비밀번호: bcrypt/argon2 해싱 (평문 저장 절대 금지)
- JWT: 시크릿 키를 환경 변수로 관리
- 세션: HttpOnly + Secure + SameSite 쿠키

## 5.3 민감 정보 관리
- API 키, 비밀번호 등은 `.env`에만 저장
- `.env`는 `.gitignore`에 반드시 포함
- 로그에 민감 정보 출력 금지

## 5.4 의존성 보안
- 정기적으로 `npm audit` / `pip audit` 실행
- 알려진 취약점이 있는 패키지 즉시 업데이트
- 사용하지 않는 의존성 제거
