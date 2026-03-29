#!/usr/bin/env python3
"""
매뉴얼 자동 로더
- 키워드 기반으로 관련 매뉴얼 챕터를 찾아 로드
"""

from pathlib import Path

# 챕터별 키워드 매핑
KEYWORD_MAP = {
    "architecture.md": ["구조", "설계", "폴더", "레이어", "모듈", "architecture", "structure"],
    "frontend.md": ["UI", "컴포넌트", "스타일", "React", "페이지", "화면", "frontend", "component"],
    "backend.md": ["API", "서버", "라우트", "인증", "엔드포인트", "미들웨어", "backend", "route"],
    "database.md": ["DB", "모델", "스키마", "마이그레이션", "쿼리", "테이블", "database", "query"],
    "security.md": ["인증", "권한", "토큰", "암호화", "XSS", "보안", "security", "auth"],
}


class ManualLoader:
    def __init__(self, manuals_dir: Path):
        self.manuals_dir = manuals_dir
        self.chapters_dir = manuals_dir / "chapters"

    def find_relevant(self, text: str) -> list[str]:
        """텍스트에서 키워드를 찾아 관련 챕터 경로 반환"""
        text_lower = text.lower()
        relevant = []

        for chapter, keywords in KEYWORD_MAP.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    chapter_path = self.chapters_dir / chapter
                    if chapter_path.exists() and str(chapter_path) not in relevant:
                        relevant.append(str(chapter_path))
                    break

        return relevant

    def load_chapter(self, chapter_path: str) -> str:
        """챕터 파일 내용 반환"""
        path = Path(chapter_path)
        if path.exists():
            return path.read_text(encoding="utf-8")
        return f"(챕터 파일 없음: {chapter_path})"

    def load_index(self) -> str:
        """목차 파일 반환"""
        index_path = self.manuals_dir / "index.md"
        if index_path.exists():
            return index_path.read_text(encoding="utf-8")
        return "(목차 파일 없음)"


if __name__ == "__main__":
    import sys
    loader = ManualLoader(Path(__file__).parent.parent / "manuals")

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        results = loader.find_relevant(query)
        if results:
            print(f"'{query}'와 관련된 매뉴얼:")
            for r in results:
                print(f"  → {r}")
        else:
            print(f"'{query}'와 관련된 매뉴얼이 없습니다.")
    else:
        print("사용법: python manual_loader.py [검색 키워드]")
