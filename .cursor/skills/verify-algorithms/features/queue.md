# Queue

## Sub-features

Push1,2, peek1, pop1, push3, pop2, pop3, then empty.

## How to get to it (user POV)

Call the class in `Implement Queue using Stacks.cpp` in a C++ judge-style driver. This repository contains snippets, not an installed CLI.

## Driving it with Python and g++

Run `python3 .cursor/skills/verify-algorithms/helpers/drive.py`. It wraps the real snippet in a temporary translation unit and executes assertions for this contract. A nonzero compiler/binary status fails the run and is retained in JSON.

## Gotchas

Empty pop/peek is outside this valid-input contract; no new behavior is invented. Standard headers and node structs are explicit local judge scaffolding. No external judge acceptance is claimed.
