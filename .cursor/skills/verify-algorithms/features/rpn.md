# RPN calculator

## Sub-features

Evaluate2 1 + 3 * =9;4 13 5 / + =6;7 -3 / =-2.

## How to get to it (user POV)

Call the class in `Evaluate Reverse Polish Notation.cpp` in a C++ judge-style driver. This repository contains snippets, not an installed CLI.

## Driving it with Python and g++

Run `python3 .cursor/skills/verify-algorithms/helpers/drive.py`. It wraps the real snippet in a temporary translation unit and executes assertions for this contract. A nonzero compiler/binary status fails the run and is retained in JSON.

## Gotchas

Malformed tokens, divide-by-zero and integer overflow are untested judge-invalid inputs. Standard headers and node structs are explicit local judge scaffolding. No external judge acceptance is claimed.
