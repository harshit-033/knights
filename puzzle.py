from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Additional symbols for utterances in Puzzle 3
ASaidKnight = Symbol("A said I am a knight")
ASaidKnave = Symbol("A said I am a knave")

# Helper to enforce each character is either a knight or a knave but not both
def exclusive(symbol_knight, symbol_knave):
    return And(
        Or(symbol_knight, symbol_knave),
        Not(And(symbol_knight, symbol_knave))
    )

# Puzzle 0
# A says "I am both a knight and a knave."
statement0 = And(AKnight, AKnave)
knowledge0 = And(
    exclusive(AKnight, AKnave),
    Implication(AKnight, statement0),
    Implication(AKnave, Not(statement0))
)

# Puzzle 1
# A says "We are both knaves." (A and B are knaves)
statement1 = And(AKnave, BKnave)
knowledge1 = And(
    exclusive(AKnight, AKnave),
    exclusive(BKnight, BKnave),
    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

# Puzzle 2
# A says "We are the same kind." (both knights or both knaves)
statement2_a = Biconditional(AKnight, BKnight)
# B says "We are of different kinds."
statement2_b = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    exclusive(AKnight, AKnave),
    exclusive(BKnight, BKnave),
    Implication(AKnight, statement2_a),
    Implication(AKnave, Not(statement2_a)),
    Implication(BKnight, statement2_b),
    Implication(BKnave, Not(statement2_b))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave." (unknown which)
utterance_exclusive = And(
    Or(ASaidKnight, ASaidKnave),
    Not(And(ASaidKnight, ASaidKnave))
)
# Link A's identity to what they could say (knights tell truth, knaves lie)
# In either case, the only consistent utterance is "I am a knight"
knowledge3 = And(
    exclusive(AKnight, AKnave),
    exclusive(BKnight, BKnave),
    exclusive(CKnight, CKnave),
    utterance_exclusive,
    # A's utterance constraints
    Implication(AKnight, ASaidKnight),
    Implication(AKnave, ASaidKnight),
    # B's statements
    Implication(BKnight, ASaidKnave),   # B says "A said I am a knave"
    Implication(BKnave, Not(ASaidKnave)),
    Implication(BKnight, CKnave),       # B says "C is a knave"
    Implication(BKnave, Not(CKnave)),
    # C's statement
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
