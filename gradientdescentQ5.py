import math

(u, v) = (1, 1)
i = 1
ite = 0
while i == 1:
    ite += 1
    dE_u = 2 * ((u * math.exp(v)) - (2 * v * math.exp(-u))) \
        * (math.exp(v) + (2 * v * math.exp(-u)))

    dE_v = 2 * ((u * math.exp(v)) - (2 * v * math.exp(-u))) \
        * ((u * math.exp(v)) - (2 * math.exp(-u)))

    u = u - (0.1 * dE_u)
    v = v - (0.1 * dE_v)

    E = ((u * math.exp(v)) - (2 * v * math.exp(-u)))**2

    if E < (10**(-14)):
        i = 0

print('(u, v) = ({res_u}, {res_v})'.format(res_u=u, res_v=v))
print('iteration = {k}'.format(k=ite))
print(E)
