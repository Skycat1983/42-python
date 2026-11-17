# 42 Python submissions

My numbered Python submissions from 42 Berlin, collected in one repository.
Each module retains its submitted exercise layout and executable code.
Selected files include additional requirement comments sourced from local PDFs.

## Modules

| Module | Commit date | Source commit | Files |
| --- | --- | --- | --- |
| [python00](python00/) | 2026-03-25 | `a75d9b3` | 9 |
| [python01](python01/) | 2026-03-30 | `ffbfca1` | 7 |
| [python02](python02/) | 2026-04-10 | `5db826b` | 5 |
| [python03](python03/) | 2026-06-03 | `929cb21` | 7 |
| [python04](python04/) | 2026-06-10 | `d9cf991` | 4 |
| [python05](python05/) | 2026-06-11 | `8cbd2a5` | 3 |
| [python06](python06/) | 2026-07-03 | `38a6167` | 24 |
| [python07](python07/) | 2026-07-06 | `16a72cf` | 12 |
| [python08](python08/) | 2026-07-20 | `bdcc932` | 7 |
| [python09](python09/) | 2026-07-24 | `5e5fc2c` | 3 |
| [python10](python10/) | 2026-07-31 | `f2937ce` | 5 |

## Snapshot provenance

Prepared on 2026-11-17. Each source commit was checked against the corresponding
school repository's remote HEAD on that date. Python 09 uses the newer
`python09_v2` submission, published here under `python09`.

This repository starts a new combined history. The original repositories retain
their existing histories. `submission-manifest.json` records the full source
commit IDs and original SHA-256 checksums (`sha256`) of every imported file.
Files with added comments also record `annotated_sha256` for the published copy.

Only committed submission files are included. Uncommitted notes, subject PDFs,
environments, and caches are omitted. The tracked macOS `.DS_Store` file in
Python 06 is also omitted. The example environment file in Python 08 contains
placeholder values and is included.

## Running exercises

Use Python 3 and run each exercise from its module or exercise directory as its
imports and file paths require. These are independent submissions, not one
installable application. Python 08 exercise 1 includes its own dependency files.

For example:

```sh
cd python00/ex0
python3 ft_hello_garden.py
```

All imported Python files passed syntax parsing during collection. This checks
syntax only; it does not establish runtime correctness or evaluation results.

## Requirement summaries

Added on 2026-11-17. Short comments in the Python files summarize the available
subjects, with version numbers and printed page references. Python 06 already
contained requirement comments; those were retained and supplemented.

| Module | Local source | Coverage |
| --- | --- | --- |
| Python 03 | Data Quest v3.0 | Exercises 0–6 |
| Python 05 | Code Nexus v3.0 | Exercises 0–2 |
| Python 06 | The Codex v2.0 | All four parts |
| Python 08 | The Matrix v3.0 | Exercises 0–2 |
| Python 10 | FuncMage v3.2 | Exercises 0–4 |

PDFs for Python 00, 01, 02, 04, 07, and 09 were not available during this pass;
no PDF-derived requirements were added to those modules. These summaries capture
core requirements, not the complete subjects or proof of compliance. All PDFs
and temporary full-text extractions stay outside this repository.

Python 06's module-wide rules require Python 3.10+, flake8, and type annotations
checked with mypy. Only project-local imports are allowed; modifying sys.path,
eval, and exec are forbidden. Some import/type errors are deliberate teaching
examples in that subject.

Validation: all 82 Python files parse; each annotated file has the same Python
abstract syntax tree as its original submission, confirming that these edits
only add comments. Original comments and learner questions are preserved.
This check does not execute the exercises or establish their correctness.
