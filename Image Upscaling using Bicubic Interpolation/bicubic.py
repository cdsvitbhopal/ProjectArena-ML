import cv2
import numpy as np
import sys
import os


try:
    if len(sys.argv) != 2:
        raise Exception("Usage: python bicubic.py path/to/1080p/image.png")
    
    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        raise Exception(f"Input file '{input_file}' does not exist.")
    
    input_dir = os.path.dirname(input_file)

    image = cv2.imread(input_file)

    height = image.shape[0]
    width = image.shape[1]

    b, g, r = cv2.split(image)

    r_upscale = np.zeros((int(height * 2), int(width * 2)))
    g_upscale = np.zeros((int(height * 2), int(width * 2)))
    b_upscale = np.zeros((int(height * 2), int(width * 2)))

    for i in range(0, r_upscale.shape[0], 2):
        for j in range(0, r_upscale.shape[1], 2):
            r_upscale[i, j] = r[int(i/2), int(j/2)]
            g_upscale[i, j] = g[int(i/2), int(j/2)]
            b_upscale[i, j] = b[int(i/2), int(j/2)]

    for i in range(0, r_upscale.shape[0], 2):
        for j in range(1, r_upscale.shape[1], 2):
            if j % 2 != 0:
                if j < 2 or j >= r_upscale.shape[1] - 3:
                    r_upscale[i, j] = r_upscale[i, j-1]
                    g_upscale[i, j] = g_upscale[i, j-1]
                    b_upscale[i, j] = b_upscale[i, j-1]                   

                else:
                    t = 0.5
                    tt = t**2
                    ttt = t**3

                    q1 = (-ttt + 2*tt - t) / 2
                    q2 = (3*ttt - 5*tt + 2) / 2
                    q3 = (-3*ttt + 4*t + t) / 2
                    q4 = (ttt - tt) / 2
                    
                    p1 = r_upscale[i, j-3]
                    p2 = r_upscale[i, j-1]
                    p3 = r_upscale[i, j+1]
                    p4 = r_upscale[i, j+3]

                    r_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

                    p1 = g_upscale[i, j-3]
                    p2 = g_upscale[i, j-1]
                    p3 = g_upscale[i, j+1]
                    p4 = g_upscale[i, j+3]

                    g_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

                    p1 = b_upscale[i, j-3]
                    p2 = b_upscale[i, j-1]
                    p3 = b_upscale[i, j+1]
                    p4 = b_upscale[i, j+3]

                    b_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

    for j in range(0, r_upscale.shape[1], 2):
        for i in range(1, r_upscale.shape[0], 2):
            if i % 2 != 0:
                if i < 2 or i >= r_upscale.shape[0] - 3:
                    r_upscale[i, j] = r_upscale[i-1, j]
                    g_upscale[i, j] = g_upscale[i-1, j]
                    b_upscale[i, j] = b_upscale[i-1, j]        

                else:
                    t = 0.5
                    tt = t**2
                    ttt = t**3

                    q1 = (-ttt + 2*tt - t) / 2
                    q2 = (3*ttt - 5*tt + 2) / 2
                    q3 = (-3*ttt + 4*t + t) / 2
                    q4 = (ttt - tt) / 2
                    
                    p1 = r_upscale[i-3, j]
                    p2 = r_upscale[i-1, j]
                    p3 = r_upscale[i+1, j]
                    p4 = r_upscale[i+3, j]

                    r_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

                    p1 = g_upscale[i-3, j]
                    p2 = g_upscale[i-1, j]
                    p3 = g_upscale[i+1, j]
                    p4 = g_upscale[i+3, j]

                    g_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

                    p1 = b_upscale[i-3, j]
                    p2 = b_upscale[i-1, j]
                    p3 = b_upscale[i+1, j]
                    p4 = b_upscale[i+3, j]

                    b_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

    for i in range(1, r_upscale.shape[0], 2):
        for j in range(1, r_upscale.shape[1], 2):
            if j<3 or j>r_upscale.shape[1]-5 or i<3 or i>r_upscale.shape[0]-5:
                r_upscale[i, j] = r_upscale[i-1, j]
                g_upscale[i, j] = g_upscale[i-1, j]
                b_upscale[i, j] = b_upscale[i-1, j]

            else:
                t = 0.5
                tt = t**2
                ttt = t**3

                q1 = (-ttt + 2*tt - t) / 2
                q2 = (3*ttt - 5*tt + 2) / 2
                q3 = (-3*ttt + 4*t + t) / 2
                q4 = (ttt - tt) / 2
                
                p1 = r_upscale[i-3, j]
                p2 = r_upscale[i-1, j]
                p3 = r_upscale[i+1, j]
                p4 = r_upscale[i+3, j]

                r_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

                p1 = g_upscale[i-3, j]
                p2 = g_upscale[i-1, j]
                p3 = g_upscale[i+1, j]
                p4 = g_upscale[i+3, j]

                g_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

                p1 = b_upscale[i-3, j]
                p2 = b_upscale[i-1, j]
                p3 = b_upscale[i+1, j]
                p4 = b_upscale[i+3, j]

                b_upscale[i, j] = round(p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4)

    frame_upscale = cv2.merge([b_upscale, g_upscale, r_upscale])

    input_dir = os.path.dirname(input_file)
    output_file = os.path.join(input_dir, os.path.splitext(os.path.basename(input_file))[0]+'_upscaled.jpg')
    cv2.imwrite(output_file, frame_upscale)

except Exception as e:
    print(e)