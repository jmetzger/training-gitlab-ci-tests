# training-gitlab-ci-tests

Demo-Repository fuer die GitLab CI/CD Unit-Test-Uebung.

## Was ist hier drin?

- `calculator.py` — einfache Python-Funktionen (add, subtract, multiply, divide, is_even)
- `test_calculator.py` — pytest-Tests fuer alle Funktionen
- `.gitlab-ci.yml` — GitLab CI/CD Pipeline mit JUnit-Report-Artifact

## Pipeline

Die Pipeline fuehrt automatisch `pytest` aus und erzeugt einen JUnit-Report.
Das Ergebnis erscheint im **Merge Request Dashboard** unter "Test summary".

## Lokale Ausfuehrung

```
pip install -r requirements.txt
pytest test_calculator.py -v
```
