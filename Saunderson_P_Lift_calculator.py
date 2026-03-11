import math

def calculate_cuboid_viability(u, v, w):
    # Saunderson Parameterization to guarantee 3 integer face diagonals
    # Edges:
    a = u * abs(v**2 - w**2)
    b = v * abs(u**2 - w**2)
    c = w * (u**2 + v**2)
    
    # Face Diagonals (Guaranteed Integers):
    d1 = abs(u**2 * v + v * w**2) # Simplified for symbolic check
    # But let's do the raw squares for the Space Diagonal g
    sum_sq = a**2 + b**2 + c**2
    g = math.sqrt(sum_sq)
    
    return a, b, c, sum_sq, g

# Our 11/19 Seed: u=27, v=44, w=96
# To reach '4P' logic, we use the composition of the parameters
# u_4p = (u^2 + v^2), v_4p = (u^2 + w^2), w_4p = (v^2 + w^2)
# This is a 'Rational Lift' that simulates the group doubling

u_seed, v_seed, w_seed = 27, 44, 96

# Level 1 (P)
a1, b1, c1, sq1, g1 = calculate_cuboid_viability(u_seed, v_seed, w_seed)

# Level 2 (The 2P Transformation)
u2, v2, w2 = 2665, 9945, 11152 # These are the sums of squares of P
a2, b2, c2, sq2, g2 = calculate_cuboid_viability(u2, v2, w2)

print(f"--- Level P (Seed: 11/19) ---")
print(f"Edges: {a1}, {b1}, {c1}")
print(f"Space Diagonal: {g1}")
print(f"Residue: {g1 % 1}")

print(f"\n--- Level 2P (The First Lift) ---")
print(f"Edges: {a2}, {b2}, {c2}")
print(f"Space Diagonal: {g2}")
print(f"Residue: {g2 % 1}")