# Saunderson Parametric Sweep
def parametric_sweep(limit):
    best_diff = 1.0
    best_trio = (0,0,0)
    
    # We use the '19' and '11' as a baseline since they were load-bearing
    for u in range(1, limit):
        u2 = u*u
        for v in range(u + 1, limit):
            v2 = v*v
            uv_sum = u2 + v2
            for w in range(v + 1, limit):
                w2 = w*w
                
                # The 'Seventh Line' Identity
                g2 = uv_sum * (u2 + w2) * (v2 + w2)
                g = g2**0.5
                diff = abs(g - round(g))
                
                if diff < best_diff:
                    best_diff = diff
                    best_trio = (u, v, w)
                    if diff < 0.0001:
                        print(f"!!! CRITICAL PARAMETRIC HIT !!!")
                        print(f"u={u}, v={v}, w={w} | g_diff={diff:.12f}")
    
    return best_trio, best_diff

# Running the sweep for the 'Narrowed' space
parametric_sweep(128)