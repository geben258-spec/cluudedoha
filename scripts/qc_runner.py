#!/usr/bin/env python3
"""
품질 검사 자동 실행기
- 파일 변경 감지 시 자동으로 검사 수행
"""

import subprocess
from pathlib import Path
from datetime import datetime


class QCRunner:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.docs_dir = project_root / "docs"

    def check_git_diff(self) -> list[str]:
        """변경된 파일 목록 반환"""
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only"],
                capture_output=True, text=True,
                cwd=self.project_root
            )
            files = [f for f in result.stdout.strip().split("\n") if f]
            return files
        except Exception:
            return []

    def check_todo_updated(self) -> bool:
        """TODO.md가 최신 상태인지 확인"""
        todo_path = self.docs_dir / "TODO.md"
        if not todo_path.exists():
            return False
        content = todo_path.read_text(encoding="utf-8")
        return "[ ]" in content or "[x]" in content

    def check_plan_exists(self) -> bool:
        """PLAN.md가 작성되어 있는지 확인"""
        plan_path = self.docs_dir / "PLAN.md"
        if not plan_path.exists():
            return False
        content = plan_path.read_text(encoding="utf-8")
        return len(content) > 200  # 템플릿 이상의 내용이 있는지

    def generate_report(self, changed_files: list[str]) -> str:
        """QC 보고서 생성"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        report = f"# QC 보고서\n\n"
        report += f"**검사 시간**: {now}\n\n"

        # 변경 파일 목록
        report += "## 변경된 파일\n"
        if changed_files:
            for f in changed_files:
                report += f"- `{f}`\n"
        else:
            report += "- (변경 없음)\n"

        # 체크리스트
        report += "\n## 검사 항목\n"
        checks = [
            ("PLAN.md 작성 여부", self.check_plan_exists()),
            ("TODO.md 업데이트 여부", self.check_todo_updated()),
        ]
        for name, passed in checks:
            status = "✅" if passed else "❌"
            report += f"- {status} {name}\n"

        return report

    def run_all(self):
        """전체 QC 실행"""
        print("🔍 품질 검사 실행 중...\n")

        changed = self.check_git_diff()
        report = self.generate_report(changed)
        print(report)

        # REVIEW.md에 저장
        review_path = self.docs_dir / "REVIEW.md"
        review_path.write_text(report, encoding="utf-8")
        print(f"\n📄 보고서 저장: {review_path}")


if __name__ == "__main__":
    runner = QCRunner(Path(__file__).parent.parent)
    runner.run_all()
