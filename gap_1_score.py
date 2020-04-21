import numpy as np 

MAX_SCORE = 40
P = 4

def get_gap_1_score(gaps, fps=30):
    """implementation of GAP_1_SCORE from https://confluence.atl.ring.com/display/CVIQ/GAP+Score
    gaps - list of all the gaps between frames

    GAP_1_SCORE requires only a list of all the gaps
    """
    g = np.array(gaps)
    g1 = g[g <= 200]
    g2 = g[g > 200] 
    
    w = lambda x: (200 - x / P ) / (200 + x / P)

    s1, s2 = 0, 0

    if len(g1) != 0:
        w1 = w(g1)
        s1 = sum(w1) / len(g1) * sum(g1) / sum(g)
    if len(g2) != 0:
        w2 = (1 - (g2 - 200) / (g2 + 200) ) * (P - 1) / (P + 1)
        s2 = sum(w2) /  len(g2) * sum(g2) / sum(g)

    score = MAX_SCORE * (s1 + s2)

    if fps:
        scale = 1 / w(1000/fps)
        score = score * scale

    return round(score, 2)

# # USAGE
# if __name__ == "__main__":
#     a = [50]*100   
#     get_gap_score(a, drops=[0]*100, fps=30)
