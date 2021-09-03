interest_rate = 1.0
credit = 1000
future_credit = 2 * credit
out = 1

# Fórmula para cálculo de Juros Compostos
# A = P(1 + r/n)^nt
# A = Valor Futuro
# P = Valor Presente
# r = taxa de juros anual nominal
# n = número de vezes que o juro é capitalizado por ano
# t = número de anos

if interest_rate == 0:
    out = 'NEVER'

while credit < future_credit:
    credit = credit * (1 + 1.0 / 1) ** (1 * out)
    print(credit)
    out += 1

print(out)
