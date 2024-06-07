# У Игоря есть с1 бенгальских огней. Когда Игорь тратит один огонек, сначала он сверкает два часа, а затем тухнет.
# Игорь умный парень и из b1 потухших огоньков можно сделать 2 новых бенгальских огня, которые можно зажечь.
# Теперь Игорю интересно, сколько часов будет гореть огонек, если он будет действовать оптимальным образом.

def sparklers(c1: int, b1: int):
    if b1 <= 1:  # Igor can't make an sparkler from nothing, it's impossible.
        print(f"Sparklers can be burning for ever.")
        return

    burnt = c1  # Igor has burnt all his sparklers.
    amount = 0  # of created sparklers.
    while burnt >= b1:
        amount += burnt // b1 * 2
        burnt -= burnt // b1

    print(f"Sparklers can be burning for {(c1 + amount) * 2} hours.")


