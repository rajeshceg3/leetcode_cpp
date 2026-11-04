# Grid paths

## Sub-features

Count3x7=28,1x1=1,1x8=1; minimum sums7for3x3,5single cell,6single row.

## How to get to it (user POV)

Call the class in `Unique Paths.cpp and Minimum Path Sum.cpp` in a C++ judge-style driver. This repository contains snippets, not an installed CLI.

## Driving it with Python and g++

Run `python3 .cursor/skills/verify-algorithms/helpers/drive.py`. It wraps the real snippet in a temporary translation unit and executes assertions for this contract. A nonzero compiler/binary status fails the run and is retained in JSON.

## Gotchas

Minimum sum mutates its input. Empty grids and count overflow are not claimed. Standard headers and node structs are explicit local judge scaffolding. No external judge acceptance is claimed.
