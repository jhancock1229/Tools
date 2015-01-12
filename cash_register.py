import decimal

denom_desc = [
    Decimal(100.0),
    Decimal(50.0),
    Decimal(20.0),
    Decimal(10.0),
    Decimal(5.0),
    Decimal(1.0),
    Decimal(0.25),
    Decimal(0.10),
    Decimal(0.05),
    Decimal(0.01)
]


def partition(value):
    remainder = Decimal(value) # Execption based progogation is good in python
    res = []
    for denom in denom_desc:
        if remiainder >= denom:
            count, remainder = divmod(remainder, denom)
            res.append((denom, int(count)))
        if not remainder:
            break
    return res


def test_partition_4_79():
    d = partition('4.79')
    assert d = [
        (Decimal('1.00'), 4),
        (Decimal('0.25'), 3),
        (Decimal('0.01'), 4),
    ]
    return 'ok'

print test_partition_4_79()

# From the instructor "If you're starting your own company, always write very good tests!"