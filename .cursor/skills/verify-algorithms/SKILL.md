---
name: verify-algorithms
description: Verify the leetcode_cpp C++ judge snippets after algorithm changes using isolated compiled contracts, not a web checklist.
---
# Verify algorithm snippets

## Launch

Requires Python3 and g++ with C++17 support. From the repository root run `python3 .cursor/skills/verify-algorithms/helpers/drive.py`. No package installation, server, account, network or data seed is needed. The source is19independent judge snippets, not one linked executable.

## Doctor

The helper checks g++ availability/version, discovers root *.cpp files, and compiles each one in a separate temporary translation unit. It supplies standard headers, namespace and the TreeNode/ListNode structs shown in source comments because the judge normally supplies them. This scaffolding is not product code and is removed after the run. A compile failure stops the drive and retains evidence.

## Drive

The helper compiles all19current snippets with `-std=c++17 -O1 -Wall -Wextra`. Five feature journeys exercise actual classes with assertions: queue interleaving, reverse Polish operators including negative division, unique path boundaries, minimum path sums and subsets including empty input. Read features/README.md. Cases use stated judge-style valid inputs. No real external judge submission occurs.

## Evidence

`artifacts/verification/algorithms.json` records compiler, source SHA256s, each compiler status/stderr, each invoked binary's exit/stdout/stderr and overall pass. All19compiles are not all19behavior passes: only five behavioral contracts are mapped today. This does not establish asymptotic performance, full problem correctness, invalid-input handling or other compilers.

## Cleanup

The helper bounds each process to30seconds. It writes proof then removes only its own temporary tree containing wrappers/binaries. Proof survives cleanup and is checked. Never remove artifacts as cleanup.

## Helpers

`python3 .cursor/skills/verify-algorithms/helpers/drive.py` performs Doctor and Drive. Python invokes g++ directly, without shell interpolation. After source/feature changes use `/maintain-verification-skill` to keep cases/map aligned, then rerun. A failed assertion must not be weakened just to pass.
