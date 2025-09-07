"""Model training script."""
from pathlib import Path

def train():
    models_dir = Path(__file__).resolve().parents[2] / 'models'
    models_dir.mkdir(parents=True, exist_ok=True)
    print(f"Models will be saved to: {models_dir}")

if __name__ == '__main__':
    train()
