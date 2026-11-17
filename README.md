# 42 Python submissions

My numbered Python submissions from 42 Berlin, collected in one repository.
Each module retains its submitted exercise layout and source code.

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
commit IDs and SHA-256 checksums of every imported file.

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
