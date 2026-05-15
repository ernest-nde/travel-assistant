# Tests - Travel Assistant

## Exécuter les Tests

```bash
# Tous les tests
pytest

# Tests avec verbosité
pytest -v

# Tests avec couverture
pytest --cov=src

# Un fichier spécifique
pytest tests/test_config.py
```

## Structure

- `test_*.py` : Tests unitaires
- Chaque module dans `src/` aura son fichier de test correspondant
