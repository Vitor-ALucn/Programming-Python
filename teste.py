tab = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_tab(tab):
 
 print((f" {tab[0]}  | {tab[1]} | {tab[2]} ") * 1)
 print(f"+" + 3 * "-" + "+" + 3 * "-" + "+" + 3 * "-" + "+")
 print((f" {tab[3]}  | {tab[4]} | {tab[5]} ") * 1)
 print(f"+" + 3 * "-" + "+" + 3 * "-" + "+" + 3 * "-" + "+")
 print((f" {tab[6]}  | {tab[7]} | {tab[8]} ") * 1)
 
print_tab(tab)    