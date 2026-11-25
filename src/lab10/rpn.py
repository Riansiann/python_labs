from src.lab10.structures import stack_push, stack_pop
import operator


def rpn(expr: str) -> float:
    """
    Evaluate an expression in reverse Polish notation
    """
    st = []
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "//": operator.floordiv,
        "%": operator.mod
    }

    for token in expr.split():

        if token in operations:
            if len(st) >= 2:
                b = stack_pop(st)
                a = stack_pop(st)
                res = operations[token](a, b)
                stack_push(st, res)
            else:
                raise ValueError("not enough operands")

        else:
            try:
                token = float(token)
            except ValueError as e:
                raise ValueError("token must be float") from e

            stack_push(st, token)

    if len(st) != 1:
        raise ValueError("invalid RPN expression")

    return stack_pop(st)

            

if __name__ == "__main__":
    # tests
    assert rpn("3 4 +") == 7.0
    assert rpn("10 3 -") == 7.0
    assert rpn("10 3 //") == 3.0
    assert rpn("3 4 + 2 *") == 14.0

    # error tests
    for expr, error in [
        ("3 +", ValueError),
        ("3 4", ValueError),
        ("", ValueError),
        ("3 abc +", ValueError),
        ("3 0 /", ZeroDivisionError),
        ("3 0 //", ZeroDivisionError),
        ("3 0 %", ZeroDivisionError),
    ]:
        try:
            rpn(expr)
        except error:
            pass
        else:
            raise AssertionError(f"expected {error.__name__} for {expr!r}")

    print("\nall RPN tests passed!")



