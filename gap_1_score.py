import numpy as np 

MAX_SCORE = 40
P = 4

def get_gap_1_score(gaps, fps=False):
    """implementation of GAP_1_SCORE from https://confluence.atl.ring.com/display/CVIQ/GAP+Score
    gaps - list of all the gaps between frames

    GAP_1_SCORE requires only a list of all the gaps
    scaled GAP_1_SCORE and GAP_2_SCORE require the frame rate of the input video.
    """
    g = np.array(gaps)
    g1 = g[g <= 200]
    g2 = g[g > 200] 
    
    w = lambda x: (200 - x / P ) / (200 + x / P)

    s1, s2 = 0, 0

    if len(g1) != 0:
        w1 = w(g1)
        s1 = w1.sum() / g1.shape * g1.sum() / g.sum()
    if len(g2) != 0:
        w2 = (1 - (g2 - 200) / (g2 + 200) ) * (P - 1) / (P + 1)
        s2 = w2.sum() /  g2.shape * g2.sum() / g.sum()

    score = MAX_SCORE * (s1 + s2)

    if fps:
        scale = 1 / w(1000/fps)
        score = score[0] * scale

    print(f' {round(score, 2)}')
    return round(score, 2)

# # USAGE
# if __name__ == "__main__":
#     a = [50]*100   
#     get_gap_score(a, drops=[0]*100, fps=30)
