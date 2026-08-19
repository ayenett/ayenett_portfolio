import numpy as np
from PIL import Image

def find_corners_and_remove_green(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()
    width, height = img.size

    newData = []
    green_pixels = []
    
    for y in range(height):
        for x in range(width):
            idx = y * width + x
            item = datas[idx]
            # typical green screen colors: high G, lower R and B
            if item[1] > 90 and item[1] > item[0] * 1.2 and item[1] > item[2] * 1.2:
                newData.append((255, 255, 255, 0))
                green_pixels.append((x, y))
            else:
                newData.append(item)

    img.putdata(newData)
    img.save(out_path, "PNG")
    print(f"Saved transparent mockup to {out_path} ({width}x{height})")

    if not green_pixels:
        print("No green pixels found!")
        return None

    # Find extreme pixels
    tl = min(green_pixels, key=lambda p: p[0] + p[1])
    br = max(green_pixels, key=lambda p: p[0] + p[1])
    tr = max(green_pixels, key=lambda p: p[0] - p[1])
    bl = min(green_pixels, key=lambda p: p[0] - p[1])
    
    return tl, tr, br, bl, width, height

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

if __name__ == "__main__":
    corners = find_corners_and_remove_green('assets/nova_finance_mockup_new.png', 'assets/nova_finance_mockup_new_transparent.png')
    if corners:
        tl, tr, br, bl, w, h = corners
        print("Corners (TL, TR, BR, BL):", tl, tr, br, bl)
        
        # Expand slightly
        tl = (tl[0] - 10, tl[1] - 10)
        tr = (tr[0] + 10, tr[1] - 10)
        br = (br[0] + 10, br[1] + 10)
        bl = (bl[0] - 10, bl[1] + 10)

        vw, vh = 1920, 1048
        src_pts = [(0, 0), (vw, 0), (vw, vh), (0, vh)]
        dst_pts = [tl, tr, br, bl]
        
        matrix = get_css_matrix3d(src_pts, dst_pts)
        matrix_str = ",".join(f"{x:.6f}" for x in matrix)
        print("CSS matrix3d:")
        print(f"matrix3d({matrix_str})")
