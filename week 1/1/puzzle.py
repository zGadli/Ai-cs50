from logic import Symbol, And, Or, Not, Implication, model_check

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(Or(AKnight, AKnave),
                 Implication(AKnight, And(AKnight, AKnave)),
                 Implication(AKnave, Not(And(AKnight, AKnave)))
                 )
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(Or(AKnight, AKnave), Or(Not(AKnight), Not(AKnave)),
                 Or(BKnight, BKnave), Or(Not(BKnight), Not(BKnave)),
                 Or(Not(AKnight), AKnave), Or(Not(AKnight), BKnave),
                 Or(Not(AKnave), Not(BKnave))
                 )

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(Or(AKnight, AKnave), Or(Not(AKnight), Not(AKnave)),
                 Or(BKnight, BKnave), Or(Not(BKnight), Not(BKnave)),
                 Or(Not(AKnave), BKnight),
                 Or(Not(AKnight), BKnight),
                 Or(Not(BKnave), AKnave),
                 Or(Not(BKnight), AKnave))

# Puzzle 3
# A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(Or(AKnight, AKnave), Or(Not(AKnight), Not(AKnave)),
                 Or(BKnight, BKnave), Or(Not(BKnight), Not(BKnave)),
                 Or(CKnight, CKnave), Or(Not(CKnight), Not(CKnave)),
                 # A says either "I am a knight." or "I am a knave.", but you don't know which.
                 Or(
                    # "I am a knight."
                    And(
                        Implication(AKnight, AKnight),
                        Implication(AKnave, Not(AKnight))
                    ),

                    # "I am a knave."
                    And(
                        Implication(AKnight, AKnave),
                        Implication(AKnave, Not(AKnave))
                    )
                ),

                Not(And(
                    # "I am a knight."
                    And(
                        Implication(AKnight, AKnight),
                        Implication(AKnave, Not(AKnight))
                    ),

                    # "I am a knave."
                    And(
                        Implication(AKnight, AKnave),
                        Implication(AKnave, Not(AKnave))
                    )
                )),

                # B says "A said 'I am a knave'."
                Implication(BKnight, And(
                    Implication(AKnight, AKnave),
                    Implication(AKnave, Not(AKnave))
                )),

                Implication(BKnave, Not(And(
                    Implication(AKnight, AKnave),
                    Implication(AKnave, Not(AKnave))
                ))),


                # B says "C is a knave."
                Implication(BKnight, CKnave),
                Implication(BKnave, Not(CKnave)),

                # C says "A is a knight."
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
