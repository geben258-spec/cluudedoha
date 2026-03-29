#!/usr/bin/env node
/**
 * 자동 품질 검사 Hook
 *
 * Claude Code의 PostToolUse Hook으로 동작.
 * 파일 수정(Edit/Write) 후 자동으로 체크리스트를 확인하고
 * TODO.md 업데이트를 리마인드합니다.
 */

const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..');
const DOCS_DIR = path.join(PROJECT_ROOT, 'docs');

try {
  const input = JSON.parse(fs.readFileSync('/dev/stdin', 'utf8'));
  const toolName = input.tool_name || '';

  // Edit 또는 Write 후에만 동작
  if (!['Edit', 'Write', 'MultiEdit'].includes(toolName)) {
    process.exit(0);
  }

  const filePath = input.tool_input?.file_path || input.tool_input?.path || '';

  // docs/ 폴더 자체 수정은 무시 (무한 루프 방지)
  if (filePath.includes('/docs/') || filePath.includes('\\docs\\')) {
    process.exit(0);
  }

  const warnings = [];

  // 1. PLAN.md 존재 확인
  const planPath = path.join(DOCS_DIR, 'PLAN.md');
  if (fs.existsSync(planPath)) {
    const plan = fs.readFileSync(planPath, 'utf8');
    if (plan.includes('(프로젝트명)')) {
      warnings.push('⚠️ PLAN.md가 아직 템플릿 상태입니다. /plan을 먼저 실행하세요.');
    }
  } else {
    warnings.push('⚠️ PLAN.md가 없습니다! 계획 없이 코딩 중입니다.');
  }

  // 2. TODO.md 업데이트 리마인드
  const todoPath = path.join(DOCS_DIR, 'TODO.md');
  if (fs.existsSync(todoPath)) {
    const todo = fs.readFileSync(todoPath, 'utf8');
    const pending = (todo.match(/\[ \]/g) || []).length;
    const done = (todo.match(/\[x\]/g) || []).length;
    if (pending > 0) {
      warnings.push(`📋 TODO: ✅${done} 완료 / ⬜${pending} 대기 — 완료된 항목이 있으면 체크하세요.`);
    }
  }

  if (warnings.length > 0) {
    console.error(warnings.join('\n'));
  }

  process.exit(0);
} catch (e) {
  process.exit(0);
}
