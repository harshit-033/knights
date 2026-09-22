# Knights and Knaves Logic Solver

## Overview

This project implements a small propositional-logic framework and uses it to solve Knights and Knaves puzzles.

In these puzzles, knights always tell the truth while knaves always lie. The program represents statements as logical sentences and determines which character identities are logically entailed by a knowledge base.

## Logic Framework

The project defines reusable sentence types including:

- Symbols
- Negation
- Conjunction
- Disjunction
- Implication
- Biconditional

Each sentence can:

- Be evaluated against a model.
- Return the symbols it contains.
- Produce a readable logical formula.
- Be compared and hashed as a logical object.

## Model Checking

The `model_check` function tests whether a knowledge base entails a query.

It recursively generates truth assignments for all symbols involved in the knowledge base and query. A query is considered entailed when every model that satisfies the knowledge base also satisfies the query.

## Included Puzzles

The `puzzle.py` file defines four logic puzzles involving characters A, B, and C. Each puzzle builds a knowledge base describing the characters' identities and statements.

The solver then checks which identity symbols are logically implied.

## Project Structure

| File | Purpose |
| --- | --- |
| `logic.py` | Defines the propositional-logic data structures and model-checking algorithm. |
| `puzzle.py` | Encodes the Knights and Knaves puzzles and evaluates their solutions. |

## Running

From the project directory:

```bash
python puzzle.py
```

The program prints the logical conclusions for each puzzle.

## Key Concepts

- Propositional logic
- Knowledge bases
- Logical entailment
- Truth assignments
- Model checking
- Recursive search
