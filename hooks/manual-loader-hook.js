#!/usr/bin/env node
/**
 * 매뉴얼 자동 로더 Hook
 *
 * Claude Code의 PreToolUse Hook으로 동작.
 * 사용자 입력에서 키워드를 감지하여 관련 매뉴얼 경로를
 * Claude의 컨텍스트에 주입합니다.
 */

const fs = require('fs');
const path = require('path');

const MANUALS_DIR = path.join(__dirname, '..', 'manuals', 'chapters');

const KEYWORD_MAP = {
  'architecture.md': ['구조', '설계', '폴더', '레이어', '모듈', 'architecture', 'structure', 'folder'],
  'frontend.md': ['UI', '컴포넌트', '스타일', 'React', '페이지', '화면', 'frontend', 'component', 'CSS'],
  'backend.md': ['API', '서버', '라우트', '인증', '엔드포인트', '미들웨어', 'backend', 'route', 'endpoint'],
  'database.md': ['DB', '모델', '스키마', '마이그레이션', '쿼리', '테이블', 'database', 'query', 'SQL'],
  'security.md': ['인증', '권한', '토큰', '암호화', 'XSS', '보안', 'security', 'auth', 'JWT'],
};

try {
  const input = JSON.parse(fs.readFileSync('/dev/stdin', 'utf8'));
  const toolInput = JSON.stringify(input.tool_input || {}).toLowerCase();

  const matchedChapters = [];

  for (const [chapter, keywords] of Object.entries(KEYWORD_MAP)) {
    for (const kw of keywords) {
      if (toolInput.includes(kw.toLowerCase())) {
        const chapterPath = path.join(MANUALS_DIR, chapter);
        if (fs.existsSync(chapterPath)) {
          matchedChapters.push(chapter);
        }
        break;
      }
    }
  }

  if (matchedChapters.length > 0) {
    // 매뉴얼 참조 알림을 stderr로 출력 (Claude가 읽음)
    const msg = `📖 관련 매뉴얼 감지: ${matchedChapters.join(', ')} — manuals/chapters/ 참조 권장`;
    console.error(msg);
  }

  // Hook 통과 (차단하지 않음)
  process.exit(0);
} catch (e) {
  // 에러 시에도 차단하지 않음
  process.exit(0);
}
