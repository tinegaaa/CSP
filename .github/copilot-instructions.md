### Quick context

This repository is a collection of small Python classroom exercises (CSP 2025) organized by lesson folders (for example `1.1.9 - Algorithms and Art`, `1.3.1 - Artistic Expression`, `2.2.7 - Command Line GUI`). Most files are short Python scripts that use the `turtle` module for graphics and simple CLI input for interaction.

Use this file to orient an AI coding agent to the repository's structure, common patterns, and how to run and modify code safely.

### Big picture


### How to run code (developer workflow)


  python3 "1.3.1 - Artistic Expression/131_EJ.py"



### Project-specific conventions and patterns

- Naming: folders use a numeric prefix (lesson/task) followed by a short title. Filenames follow `<lesson>_EJ.py` and `<lesson>_Mainhardt.py` patterns.
- Graphics assets: image files (for example `bg.gif`, `envv.gif`) may be placed at repo root and referred to by scripts via relative paths. Keep relative paths intact when moving files.
- Minimal imports: scripts commonly import only the Python stdlib (primarily `turtle`, `random`). Avoid adding new heavy dependencies unless required for a new exercise.

### Integration points & external dependencies

- External deps: none declared (no requirements.txt). Only standard Python library modules are used.
- Files may rely on local image assets (`bg.gif`, `envv.gif`). Confirm asset presence before changing paths.

### Typical edit scenarios (how AI agents should act)

- Small clarifying edits: fix typos, small logic bugs, or improve variable names in-place. Respect the simple script structure — don't convert into packages unless the user asks.
- Running changes: after edits, run the edited script to confirm the turtle window opens and the behavior matches expectations. Mention to the user when scripts block on GUI event loops.
- When adding files: place new exercise files next to their lesson folder and follow the naming convention.

### Examples from the repo

- `1.3.1 - Artistic Expression/131_EJ.py` — uses `turtle.Screen()`, `addshape`, and `mainloop()`; expect interactive graphics.
- `1.1.9 - Algorithms and Art/119_EJ.py` — demonstrates multiple small turtle subroutines and a text input loop for choosing behavior.

### Safety and limits for AI edits

- Do not attempt large-scale refactors across many lesson folders without explicit user instruction. These are independent student exercises.
- Avoid adding external dependencies or build tooling without the user's consent.

### When to ask the user

- If a change will move or rename assets (images) or convert many files into a package, ask first.
- If you need to run or test GUI scripts on a headless CI or remote environment, ask for guidance or a non-GUI mode.

If anything in this file is unclear or you'd like me to include additional examples or a different level of detail (for instance, instructions to run inside an IDE), tell me which areas to expand and I'll iterate.
