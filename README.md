# Data Science Project

This repository follows a standard, modular data science structure inspired by Cookiecutter Data Science.

## Structure
- data/ — data storage (raw, interim, processed, external)
- 
otebooks/ — exploratory notebooks
- src/ — source code package
  - src/data/ — data ingestion and processing
  - src/features/ — feature engineering
  - src/models/ — model training and inference
  - src/visualization/ — plotting and reporting
  - src/utils/ — shared utilities
- models/ — serialized models and artifacts
- eports/ — reports; eports/figures/ for generated plots
- configs/  configuration files (YAML/JSON)
- scripts/  CLI entry points or helper scripts
- 	ests/  unit/integration tests

## Setup
1. Create and activate environment (Conda recommended):
   `ash
   conda env create -f environment.yml
   conda activate data-science
   `
   Or with pip + venv:
   `ash
   python -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt
   `

2. Register the project for notebooks:
   `ash
   python -m ipykernel install --user --name "data-science" --display-name "Python (data-science)"
   `

3. Copy .env.example to .env and fill in secrets.

## Make commands
- Run a script: python -m src.data.make_dataset
- Train a model: python -m src.models.train_model

## Notes
- Large files should not be committed. See .gitignore.
- Use configs/ to keep parameters versioned and reproducible.
