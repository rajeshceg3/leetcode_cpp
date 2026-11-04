# Subsets

## Sub-features

Input1,2,3 yields8unique subsets including empty/full; empty input yields one empty subset.

## How to get to it (user POV)

Call the class in `Subsets.cpp` in a C++ judge-style driver. This repository contains snippets, not an installed CLI.

## Driving it with Python and g++

Run `python3 .cursor/skills/verify-algorithms/helpers/drive.py`. It wraps the real snippet in a temporary translation unit and executes assertions for this contract. A nonzero compiler/binary status fails the run and is retained in JSON.

## Gotchas

Duplicate inputs are outside this distinct-element contract; ordering is not constrained. Standard headers and node structs are explicit local judge scaffolding. No external judge acceptance is claimed.
