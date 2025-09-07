"""Data ingestion and basic preprocessing CLI."""
import os
from pathlib import Path
from dotenv import load_dotenv


def main():
    load_dotenv()
    project_dir = Path(__file__).resolve().parents[2]
    raw_dir = project_dir / 'data' / 'raw'
    interim_dir = project_dir / 'data' / 'interim'
    interim_dir.mkdir(parents=True, exist_ok=True)
    print(f"Reading from: {raw_dir}")
    print(f"Writing to:   {interim_dir}")


if __name__ == '__main__':
    main()
