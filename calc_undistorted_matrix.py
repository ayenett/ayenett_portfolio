import numpy as np

def get_css_matrix3d(src_pts, dst_pts):
    A = []
    for i in range(4):
        x, y = src_pts[i][0], src_pts[i][1]
        u, v = dst_pts[i][0], dst_pts[i][1]
        A.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
        A.append([0, 0, 0, x, y, 1, -v*x, -v*y])
    A = np.asarray(A)
    B = np.array([dst_pts[0][0], dst_pts[0][1], dst_pts[1][0], dst_pts[1][1], dst_pts[2][0], dst_pts[2][1], dst_pts[3][0], dst_pts[3][1]])
    
    h = np.linalg.solve(A, B)
    H = np.array([
        [h[0], h[1], 0, h[2]],
        [h[3], h[4], 0, h[5]],
        [0,    0,    1, 0   ],
        [h[6], h[7], 0, 1   ]
    ])
    
    css_matrix = []
    for col in range(4):
        for row in range(4):
            css_matrix.append(H[row][col])
    return css_matrix

tl = (196, 149)
tr = (627, 148)
br = (614, 456)
bl = (228, 537)

# Expand slightly to avoid black lines
tl = (tl[0] - 2, tl[1] - 2)
tr = (tr[0] + 2, tr[1] - 2)
br = (br[0] + 2, br[1] + 2)
bl = (bl[0] - 2, bl[1] + 2)

src_pts = [(0, 0), (1170, 0), (1170, 1000), (0, 1000)]
dst_pts = [tl, tr, br, bl]

matrix = get_css_matrix3d(src_pts, dst_pts)
matrix_str = ",".join(f"{x:.6f}" for x in matrix)
print(f"matrix3d({matrix_str})")
