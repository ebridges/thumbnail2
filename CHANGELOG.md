# Change Log

## v1.1.0 (2020-07-17)

### Fix

- **release**: ensure all history is available for generating the changelog

### Feat

- Test automated release.

## v1.0.1 (2020-07-16)

### Fix

- **ci**: scope execution of release to master branch
- **ci**: insert correct repository name
- **ci**: nothing further to commit or tag, as it gets done by cz
- **ci**: ensure that build artifacts are not included in commit
- **ci**: ensure that commits and tags are made and pushed.
- **ci**: ensure commitizen is available for bumping, but removed afterward.
- **ci**: reduce scope of builds to only targetted platform.
- **ci**: install poetry before trying to use it.
- **config**: update cz configuration so that it updates version.txt and pyproject.toml

### Feat

- **ci**: add configuration to build release on push

## v1.0.0 (2020-05-09)
