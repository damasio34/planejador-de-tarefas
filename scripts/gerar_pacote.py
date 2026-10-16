from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


PACKAGE_NAME = "planejador-tarefas-docs.zip"
PACKAGE_PATHS = ("AGENTS.md", "README.md", "SKILL.md", "docs", "tarefas", "templates")


def build_package(repo_root: Path, archive_path: Path | None = None) -> Path:
    """Create a flat ZIP containing the skill instructions and their references."""
    repo_root = Path(repo_root).resolve()
    archive_path = Path(archive_path) if archive_path else repo_root / PACKAGE_NAME

    files = []
    for relative_path in PACKAGE_PATHS:
        source = repo_root / relative_path
        if source.is_dir():
            files.extend(path for path in source.rglob("*") if path.is_file())
        elif source.is_file():
            files.append(source)

    with ZipFile(archive_path, "w", ZIP_DEFLATED) as archive:
        for path in sorted(files, key=lambda item: item.relative_to(repo_root).as_posix()):
            archive.write(path, path.relative_to(repo_root).as_posix())

    return archive_path


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    archive_path = build_package(repo_root)
    print(f"Tamanho do pacote: {archive_path.stat().st_size} bytes")
    print(f"Arquivo ZIP: {archive_path}")


if __name__ == "__main__":
    main()
