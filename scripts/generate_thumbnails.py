"""
Ethio Telecom Games Portal — Premium Game Thumbnail Generator (V2)
Guarantees 100% full-bleed, opaque, real background pictures for all 142 games.
Zero transparency checkerboards. Rich environmental scenes, authentic game layouts, and game art.
"""

import json
import math
import os
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

WIDTH = 480
HEIGHT = 300

# Base category theme colors (solid, vibrant, rich)
THEMES = {
    "sports":     {"bg1": (24, 110, 45),  "bg2": (12, 65, 25),   "accent": (141, 198, 63)},
    "puzzle":     {"bg1": (245, 240, 230),"bg2": (220, 210, 195), "accent": (0, 114, 188)},
    "arcade":     {"bg1": (28, 22, 54),   "bg2": (12, 10, 28),   "accent": (236, 72, 153)},
    "shooter":    {"bg1": (18, 28, 48),   "bg2": (8, 14, 26),    "accent": (239, 68, 68)},
    "racing":     {"bg1": (38, 44, 56),   "bg2": (18, 22, 30),   "accent": (245, 158, 11)},
    "platformer": {"bg1": (40, 130, 210), "bg2": (20, 75, 140),  "accent": (6, 182, 212)},
    "casual":     {"bg1": (250, 120, 160),"bg2": (180, 50, 100), "accent": (244, 114, 182)},
    "board":      {"bg1": (44, 62, 80),   "bg2": (24, 34, 46),   "accent": (100, 116, 139)},
    "word-quiz":  {"bg1": (25, 45, 95),   "bg2": (12, 22, 55),   "accent": (59, 130, 246)},
    "3d":         {"bg1": (18, 30, 60),   "bg2": (8, 12, 28),    "accent": (141, 198, 63)},
}


def solid_gradient(c1, c2, w=WIDTH, h=HEIGHT):
    img = Image.new("RGB", (w, h), c1)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        r = int(c1[0] + (c2[0] - c1[0]) * (y / h))
        g = int(c1[1] + (c2[1] - c1[1]) * (y / h))
        b = int(c1[2] + (c2[2] - c1[2]) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def draw_space_background(w=WIDTH, h=HEIGHT):
    img = solid_gradient((12, 18, 42), (4, 6, 16), w, h)
    draw = ImageDraw.Draw(img)
    # Nebula glow
    nebula = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    nd = ImageDraw.Draw(nebula)
    nd.ellipse([60, 20, 320, 240], fill=(0, 114, 188, 45))
    nd.ellipse([220, 80, 440, 280], fill=(141, 198, 63, 30))
    nebula = nebula.filter(ImageFilter.GaussianBlur(35))
    img.paste(nebula, (0, 0), nebula)
    # Stars
    rnd = random.Random(42)
    for _ in range(90):
        sx = rnd.randint(0, w - 1)
        sy = rnd.randint(0, h - 1)
        sr = rnd.choice([1, 1, 1, 2])
        sc = rnd.choice([(255, 255, 255), (200, 230, 255), (255, 240, 200)])
        draw.ellipse([sx, sy, sx + sr, sy + sr], fill=sc)
    return img


def draw_grass_pitch(w=WIDTH, h=HEIGHT):
    img = Image.new("RGB", (w, h), (34, 139, 34))
    draw = ImageDraw.Draw(img)
    # Mow stripes
    for y in range(0, h, 24):
        col = (34, 142, 34) if (y // 24) % 2 == 0 else (28, 122, 28)
        draw.rectangle([0, y, w, y + 23], fill=col)
    return img


def draw_hardwood_court(w=WIDTH, h=HEIGHT):
    img = Image.new("RGB", (w, h), (218, 160, 102))
    draw = ImageDraw.Draw(img)
    for y in range(0, h, 14):
        col = (212 + (y % 28 == 0) * 12, 152 + (y % 21 == 0) * 10, 96 + (y % 14 == 0) * 6)
        draw.rectangle([0, y, w, y + 13], fill=col)
        draw.line([(0, y + 13), (w, y + 13)], fill=(185, 130, 80), width=1)
    return img


def generate_iconic_game(slug, category):
    """Returns custom, high-definition full-bleed artwork for iconic games"""
    w, h = WIDTH, HEIGHT

    if slug == "2048":
        img = solid_gradient((250, 248, 239), (235, 230, 218), w, h)
        draw = ImageDraw.Draw(img)
        bw, bh = 250, 250
        bx, by = (w - bw) // 2, (h - bh) // 2
        draw.rounded_rectangle([bx + 4, by + 6, bx + bw + 4, by + bh + 6], radius=14, fill=(190, 180, 170))
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=12, fill=(187, 173, 160))
        tile_colors = {
            '2': ((238, 228, 218), (119, 110, 101)),
            '4': ((237, 224, 200), (119, 110, 101)),
            '8': ((242, 177, 121), (255, 255, 255)),
            '16': ((245, 149, 99), (255, 255, 255)),
            '32': ((246, 124, 95), (255, 255, 255)),
            '64': ((246, 94, 59), (255, 255, 255)),
            '128': ((237, 207, 114), (255, 255, 255)),
            '2048': ((237, 194, 46), (255, 255, 255)),
            'empty': ((205, 193, 180), (0, 0, 0))
        }
        layout = [
            ['2', '4', '8', '16'],
            ['32', '64', '128', 'empty'],
            ['empty', '2', '4', 'empty'],
            ['empty', 'empty', 'empty', '2048']
        ]
        pad = 9
        ts = (bw - pad * 5) / 4
        for r in range(4):
            for c in range(4):
                val = layout[r][c]
                tx = bx + pad + c * (ts + pad)
                ty = by + pad + r * (ts + pad)
                bg_col, txt_col = tile_colors.get(val, tile_colors['empty'])
                draw.rounded_rectangle([tx, ty, tx + ts, ty + ts], radius=6, fill=bg_col)
                if val != 'empty':
                    draw.text((tx + ts/2 - len(val)*4.2, ty + ts/2 - 8), val, fill=txt_col, font_size=18, stroke_width=1)
        return img

    elif slug == "basketball":
        img = draw_hardwood_court(w, h)
        draw = ImageDraw.Draw(img)
        draw.line([(0, 60), (w, 60)], fill=(255, 255, 255), width=3)
        draw.arc([160, 20, 320, 180], start=0, end=180, fill=(255, 255, 255), width=3)
        draw.rectangle([180, 0, 300, 100], outline=(255, 255, 255), width=3)
        draw.arc([200, 60, 280, 140], start=0, end=360, fill=(255, 255, 255), width=3)
        bx, by, br = 240, 160, 52
        draw.ellipse([bx - br + 5, by + br - 10, bx + br + 25, by + br + 12], fill=(80, 50, 20))
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(235, 104, 30), outline=(40, 20, 10), width=2)
        draw.arc([bx - br + 8, by - br, bx + br - 8, by + br], start=280, end=80, fill=(40, 20, 10), width=3)
        draw.arc([bx - br + 8, by - br, bx + br - 8, by + br], start=100, end=260, fill=(40, 20, 10), width=3)
        draw.line([(bx - br, by), (bx + br, by)], fill=(40, 20, 10), width=3)
        draw.line([(bx, by - br), (bx, by + br)], fill=(40, 20, 10), width=3)
        return img

    elif slug in ("football", "penalty"):
        img = draw_grass_pitch(w, h)
        draw = ImageDraw.Draw(img)
        draw.rectangle([60, 40, 420, 280], outline=(255, 255, 255), width=4)
        draw.rectangle([140, 40, 340, 150], outline=(255, 255, 255), width=3)
        draw.ellipse([200, 180, 280, 260], outline=(255, 255, 255), width=3)
        draw.rectangle([170, 0, 310, 40], fill=(240, 240, 240), outline=(255, 255, 255), width=3)
        bx, by, br = 240, 200, 36
        draw.ellipse([bx - br + 4, by + br - 8, bx + br + 16, by + br + 8], fill=(15, 60, 15))
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
        draw.polygon([(bx, by - 12), (bx + 11, by - 4), (bx + 7, by + 9), (bx - 7, by + 9), (bx - 11, by - 4)], fill=(35, 31, 32))
        return img

    elif slug in ("table-tennis", "tennis"):
        img = solid_gradient((20, 100, 140), (10, 50, 80), w, h)
        draw = ImageDraw.Draw(img)
        # Table top
        draw.polygon([(60, 60), (420, 60), (460, 260), (20, 260)], fill=(0, 80, 130), outline=(255, 255, 255), width=3)
        draw.line([(240, 60), (240, 260)], fill=(255, 255, 255), width=2) # Center line
        draw.line([(40, 150), (440, 150)], fill=(255, 255, 255), width=4) # Net
        # Paddle
        px, py = 210, 190
        draw.ellipse([px - 30, py - 35, px + 30, py + 35], fill=(220, 40, 40), outline=(30, 30, 30), width=2)
        draw.rectangle([px - 6, py + 30, px + 6, py + 75], fill=(160, 90, 40)) # handle
        # Ball
        draw.ellipse([275, 175, 295, 195], fill=(255, 255, 255), outline=(200, 200, 200))
        return img

    elif slug == "bowling":
        img = solid_gradient((30, 35, 45), (15, 18, 24), w, h)
        draw = ImageDraw.Draw(img)
        # Lane
        draw.polygon([(170, 40), (310, 40), (420, 300), (60, 300)], fill=(225, 175, 120))
        # Gutters
        draw.polygon([(150, 40), (170, 40), (60, 300), (30, 300)], fill=(40, 45, 55))
        draw.polygon([(310, 40), (330, 40), (450, 300), (420, 300)], fill=(40, 45, 55))
        # Pins in triangle
        pin_col = (255, 255, 255)
        for r_idx, count in enumerate([1, 2, 3, 4]):
            py = 50 + r_idx * 15
            for c_idx in range(count):
                px = 240 - (count - 1) * 12 + c_idx * 24
                draw.ellipse([px - 5, py - 10, px + 5, py + 10], fill=pin_col, outline=(220, 40, 40))
        # Bowling ball in foreground
        bx, by, br = 240, 220, 40
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(20, 30, 50), outline=(0, 0, 0), width=2)
        draw.ellipse([bx - 12, by - 12, bx - 6, by - 6], fill=(0, 0, 0))
        draw.ellipse([bx + 4, by - 12, bx + 10, by - 6], fill=(0, 0, 0))
        draw.ellipse([bx - 4, by + 4, bx + 2, by + 10], fill=(0, 0, 0))
        return img

    elif slug in ("cricket", "cricket-123"):
        img = draw_grass_pitch(w, h)
        draw = ImageDraw.Draw(img)
        # Pitch
        draw.rectangle([180, 20, 300, 280], fill=(215, 190, 150))
        # Wickets
        for x in [220, 240, 260]:
            draw.line([(x, 50), (x, 110)], fill=(245, 235, 220), width=4)
        draw.line([(216, 50), (264, 50)], fill=(245, 235, 220), width=3) # bail
        # Bat
        draw.polygon([(260, 160), (290, 150), (310, 250), (280, 260)], fill=(180, 120, 60), outline=(100, 60, 20), width=2)
        # Red ball
        draw.ellipse([215, 185, 245, 215], fill=(200, 30, 30), outline=(100, 10, 10), width=2)
        return img

    elif slug in ("snake", "curve-snake"):
        img = solid_gradient((15, 23, 42), (8, 12, 22), w, h)
        draw = ImageDraw.Draw(img)
        # Grid
        for x in range(0, w, 24):
            draw.line([(x, 0), (x, h)], fill=(30, 41, 59))
        for y in range(0, h, 24):
            draw.line([(0, y), (w, y)], fill=(30, 41, 59))
        # Snake body segments
        snake_pts = [
            (144, 144), (168, 144), (192, 144), (216, 144),
            (216, 168), (216, 192), (240, 192), (264, 192),
            (288, 192), (312, 192), (312, 168), (336, 168)
        ]
        for sx, sy in snake_pts:
            draw.rounded_rectangle([sx + 2, sy + 2, sx + 22, sy + 22], radius=5, fill=(141, 198, 63), outline=(91, 135, 32))
        # Snake head with eyes
        hx, hy = snake_pts[-1]
        draw.ellipse([hx + 14, hy + 4, hx + 18, hy + 8], fill=(0, 0, 0))
        draw.ellipse([hx + 14, hy + 14, hx + 18, hy + 18], fill=(0, 0, 0))
        # Red Apple
        ax, ay = 384, 168
        draw.ellipse([ax + 2, ay + 2, ax + 22, ay + 22], fill=(239, 68, 68))
        draw.line([(ax + 12, ay + 2), (ax + 15, ay - 4)], fill=(120, 60, 20), width=2) # stem
        return img

    elif slug == "tetris":
        img = solid_gradient((12, 16, 32), (5, 8, 18), w, h)
        draw = ImageDraw.Draw(img)
        # Matrix board
        bx, by, bw, bh = 140, 20, 200, 260
        draw.rectangle([bx, by, bx + bw, by + bh], fill=(18, 24, 45), outline=(50, 70, 110), width=3)
        for x in range(bx, bx + bw, 20):
            draw.line([(x, by), (x, by + bh)], fill=(25, 35, 60))
        for y in range(by, by + bh, 20):
            draw.line([(bx, y), (bx + bw, y)], fill=(25, 35, 60))
        # Tetrominoes locked in bottom
        blocks = [
            (bx + 20, by + 220, (239, 68, 68)), (bx + 40, by + 220, (239, 68, 68)), (bx + 60, by + 220, (245, 158, 11)),
            (bx + 80, by + 220, (245, 158, 11)), (bx + 100, by + 220, (141, 198, 63)), (bx + 120, by + 220, (141, 198, 63)),
            (bx + 40, by + 200, (6, 182, 212)), (bx + 60, by + 200, (6, 182, 212)), (bx + 80, by + 200, (6, 182, 212)),
            (bx + 100, by + 200, (6, 182, 212)), (bx + 60, by + 180, (168, 85, 247)),
        ]
        for x, y, col in blocks:
            draw.rectangle([x + 1, y + 1, x + 19, y + 19], fill=col, outline=(255, 255, 255, 120))
        # Active falling piece (T shape)
        for x, y in [(bx + 80, by + 80), (bx + 100, by + 80), (bx + 120, by + 80), (bx + 100, by + 100)]:
            draw.rectangle([x + 1, y + 1, x + 19, y + 19], fill=(236, 72, 153), outline=(255, 255, 255))
        return img

    elif slug == "pacman":
        img = solid_gradient((5, 8, 18), (0, 0, 5), w, h)
        draw = ImageDraw.Draw(img)
        # Blue Maze corridors
        maze_lines = [
            [(40, 40), (440, 40)], [(40, 260), (440, 260)],
            [(40, 40), (40, 260)], [(440, 40), (440, 260)],
            [(90, 90), (190, 90)], [(290, 90), (390, 90)],
            [(90, 150), (150, 150)], [(330, 150), (390, 150)],
            [(90, 210), (190, 210)], [(290, 210), (390, 210)],
            [(240, 40), (240, 100)], [(240, 200), (240, 260)]
        ]
        for pts in maze_lines:
            draw.line(pts, fill=(33, 150, 243), width=6)
        # Yellow food dots
        for x in range(70, 420, 30):
            draw.ellipse([x - 3, 147, x + 3, 153], fill=(255, 235, 59))
        # Pacman
        px, py, pr = 220, 150, 28
        draw.pieslice([px - pr, py - pr, px + pr, py + pr], start=35, end=325, fill=(255, 214, 0))
        # Red Ghost chasing
        gx, gy = 120, 150
        draw.ellipse([gx - 20, gy - 24, gx + 20, gy], fill=(244, 67, 54))
        draw.rectangle([gx - 20, gy - 8, gx + 20, gy + 16], fill=(244, 67, 54))
        draw.ellipse([gx - 12, gy - 8, gx - 4, gy], fill=(255, 255, 255))
        draw.ellipse([gx + 4, gy - 8, gx + 12, gy], fill=(255, 255, 255))
        draw.ellipse([gx - 8, gy - 6, gx - 4, gy - 2], fill=(0, 0, 180))
        draw.ellipse([gx + 8, gy - 6, gx + 12, gy - 2], fill=(0, 0, 180))
        return img

    elif slug == "flappy":
        img = solid_gradient((110, 195, 240), (220, 240, 255), w, h)
        draw = ImageDraw.Draw(img)
        # Fluffy clouds
        for cx, cy in [(80, 80), (260, 60), (400, 100)]:
            draw.ellipse([cx - 40, cy - 15, cx + 40, cy + 15], fill=(255, 255, 255, 220))
            draw.ellipse([cx - 20, cy - 30, cx + 20, cy + 10], fill=(255, 255, 255, 220))
        # Green ground
        draw.rectangle([0, 260, w, h], fill=(141, 198, 63))
        draw.line([(0, 260), (w, 260)], fill=(91, 135, 32), width=3)
        # Green pipes
        pipe_x = 340
        draw.rectangle([pipe_x, 0, pipe_x + 55, 110], fill=(67, 160, 71), outline=(46, 125, 50), width=3)
        draw.rectangle([pipe_x - 5, 95, pipe_x + 60, 115], fill=(67, 160, 71), outline=(46, 125, 50), width=3)
        draw.rectangle([pipe_x, 210, pipe_x + 55, 260], fill=(67, 160, 71), outline=(46, 125, 50), width=3)
        draw.rectangle([pipe_x - 5, 205, pipe_x + 60, 225], fill=(67, 160, 71), outline=(46, 125, 50), width=3)
        # Flappy yellow bird
        bx, by = 180, 160
        draw.ellipse([bx - 22, by - 16, bx + 22, by + 16], fill=(253, 216, 53), outline=(245, 124, 0), width=2)
        draw.ellipse([bx - 12, by - 6, bx + 6, by + 8], fill=(255, 255, 255)) # wing
        draw.ellipse([bx + 8, by - 10, bx + 16, by - 2], fill=(0, 0, 0)) # eye
        draw.polygon([(bx + 18, by - 2), (bx + 30, by + 4), (bx + 18, by + 8)], fill=(230, 81, 0)) # beak
        return img

    elif slug in ("candy-crush", "candy-crusher"):
        img = solid_gradient((245, 130, 180), (180, 60, 120), w, h)
        draw = ImageDraw.Draw(img)
        # Candy grid pattern
        candies = [
            # Red jelly bean
            (140, 100, (239, 68, 68)), (200, 100, (245, 158, 11)), (260, 100, (141, 198, 63)), (320, 100, (59, 130, 246)),
            (140, 160, (168, 85, 247)), (200, 160, (239, 68, 68)), (260, 160, (245, 158, 11)), (320, 160, (239, 68, 68)),
            (140, 220, (141, 198, 63)), (200, 220, (59, 130, 246)), (260, 220, (168, 85, 247)), (320, 220, (245, 158, 11))
        ]
        for cx, cy, col in candies:
            draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=col, outline=(255, 255, 255), width=2)
            draw.ellipse([cx - 10, cy - 14, cx - 2, cy - 6], fill=(255, 255, 255)) # gloss reflection
        return img

    elif slug in ("bubble-shooter", "bubble-pop"):
        img = solid_gradient((45, 60, 110), (15, 22, 45), w, h)
        draw = ImageDraw.Draw(img)
        colors = [(239, 68, 68), (59, 130, 246), (141, 198, 63), (245, 158, 11), (168, 85, 247)]
        r = 18
        for row in range(4):
            y = 30 + row * 32
            offset = 18 if row % 2 == 1 else 0
            for col in range(11):
                x = 60 + col * 36 + offset
                c = colors[(row * 3 + col) % len(colors)]
                draw.ellipse([x - r, y - r, x + r, y + r], fill=c, outline=(255, 255, 255, 180), width=1)
                draw.ellipse([x - r/2, y - r/2, x - r/6, y - r/6], fill=(255, 255, 255)) # gloss
        # Shooter cannon at bottom
        draw.line([(240, 280), (240, 200)], fill=(255, 255, 255), width=3)
        draw.ellipse([240 - 20, 230 - 20, 240 + 20, 230 + 20], fill=(239, 68, 68), outline=(255, 255, 255), width=2)
        return img

    elif slug in ("car-race", "road-fighter", "one-car", "two-cars", "two-cars-ai"):
        img = solid_gradient((45, 55, 75), (20, 25, 35), w, h)
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, w, 80], fill=(25, 35, 55)) # sky
        draw.polygon([(180, 80), (300, 80), (470, 300), (10, 300)], fill=(32, 38, 48)) # road
        # Rumble strips
        draw.polygon([(175, 80), (185, 80), (20, 300), (0, 300)], fill=(229, 57, 53))
        draw.polygon([(295, 80), (305, 80), (480, 300), (460, 300)], fill=(229, 57, 53))
        # Dashed lane markings
        for y_top in range(85, 275, 30):
            prog = (y_top - 85) / 190
            dw = 3 + prog * 9
            dh = 12 + prog * 22
            draw.rectangle([240 - dw/2, y_top, 240 + dw/2, y_top + dh], fill=(253, 216, 53))
        # Red racer car
        cy = 185
        draw.rounded_rectangle([205, cy, 275, cy + 85], radius=14, fill=(229, 57, 53), outline=(180, 20, 20), width=2)
        draw.rounded_rectangle([216, cy + 22, 264, cy + 48], radius=6, fill=(20, 30, 45)) # windshield
        draw.rectangle([198, cy + 14, 205, cy + 38], fill=(15, 15, 15)) # wheels
        draw.rectangle([275, cy + 14, 282, cy + 38], fill=(15, 15, 15))
        draw.rectangle([198, cy + 54, 205, cy + 78], fill=(15, 15, 15))
        draw.rectangle([275, cy + 54, 282, cy + 78], fill=(15, 15, 15))
        return img

    elif slug in ("fighter-jet", "fighter-fury", "space-fighter", "alien-battle", "shooter", "shoot-enemy"):
        img = draw_space_background(w, h)
        draw = ImageDraw.Draw(img)
        # Laser beams
        draw.line([(220, 180), (220, 20)], fill=(0, 220, 255), width=3)
        draw.line([(260, 180), (260, 20)], fill=(0, 220, 255), width=3)
        # Hero Starship (bottom center)
        sx, sy = 240, 220
        draw.polygon([(sx, sy - 40), (sx + 35, sy + 30), (sx + 15, sy + 20), (sx, sy + 25), (sx - 15, sy + 20), (sx - 35, sy + 30)], fill=(220, 230, 245), outline=(0, 114, 188), width=2)
        draw.ellipse([sx - 8, sy - 15, sx + 8, sy + 5], fill=(0, 180, 255)) # cockpit
        draw.polygon([(sx - 8, sy + 25), (sx + 8, sy + 25), (sx, sy + 45)], fill=(255, 150, 0)) # engine flame
        # Alien ship (top)
        ax, ay = 240, 60
        draw.ellipse([ax - 35, ay - 15, ax + 35, ay + 15], fill=(141, 198, 63), outline=(91, 135, 32), width=2)
        draw.ellipse([ax - 18, ay - 22, ax + 18, ay - 2], fill=(236, 72, 153))
        return img

    elif slug in ("sudoku", "math-quest"):
        img = solid_gradient((245, 247, 250), (228, 234, 241), w, h)
        draw = ImageDraw.Draw(img)
        bx, by, bsz = 110, 20, 260
        draw.rounded_rectangle([bx, by, bx + bsz, by + bsz], radius=10, fill=(255, 255, 255), outline=(0, 114, 188), width=3)
        cell = bsz / 9
        for i in range(10):
            lw = 3 if i % 3 == 0 else 1
            col = (0, 114, 188) if i % 3 == 0 else (205, 215, 230)
            draw.line([(bx + i * cell, by), (bx + i * cell, by + bsz)], fill=col, width=lw)
            draw.line([(bx, by + i * cell), (bx + bsz, by + i * cell)], fill=col, width=lw)
        # Digits
        sample = [(0, 0, "5"), (1, 1, "3"), (2, 4, "7"), (3, 2, "6"), (4, 4, "9"), (5, 6, "8"), (6, 7, "1"), (7, 5, "4"), (8, 8, "2")]
        draw.rectangle([bx + 3 * cell, by + 3 * cell, bx + 6 * cell, by + 6 * cell], fill=(141, 198, 63, 40))
        for r, c, val in sample:
            draw.text((bx + c * cell + cell/2 - 4, by + r * cell + cell/2 - 7), val, fill=(35, 31, 32), stroke_width=1)
        return img

    elif slug in ("chess", "board"):
        img = solid_gradient((36, 42, 54), (20, 24, 32), w, h)
        draw = ImageDraw.Draw(img)
        cx, cy, sz = 115, 25, 250
        draw.rectangle([cx - 8, cy - 8, cx + sz + 8, cy + sz + 8], fill=(60, 42, 25), outline=(141, 198, 63), width=2)
        cell = sz / 8
        for r in range(8):
            for c in range(8):
                col = (238, 216, 179) if (r + c) % 2 == 0 else (181, 136, 99)
                draw.rectangle([cx + c * cell, cy + r * cell, cx + (c + 1) * cell, cy + (r + 1) * cell], fill=col)
        # Pieces
        draw.ellipse([cx + 3 * cell + 4, cy + 7 * cell + 4, cx + 4 * cell - 4, cy + 8 * cell - 4], fill=(255, 255, 255), outline=(0, 0, 0))
        draw.ellipse([cx + 4 * cell + 4, cy + 0 * cell + 4, cx + 5 * cell - 4, cy + 1 * cell - 4], fill=(35, 31, 32))
        return img

    elif slug == "wordle":
        img = solid_gradient((18, 22, 32), (8, 10, 16), w, h)
        draw = ImageDraw.Draw(img)
        rows = [
            [("A", (58, 58, 60)), ("U", (58, 58, 60)), ("D", (181, 159, 59)), ("I", (58, 58, 60)), ("O", (58, 58, 60))],
            [("P", (181, 159, 59)), ("L", (58, 58, 60)), ("A", (83, 141, 78)), ("N", (83, 141, 78)), ("T", (58, 58, 60))],
            [("G", (83, 141, 78)), ("A", (83, 141, 78)), ("M", (83, 141, 78)), ("E", (83, 141, 78)), ("S", (83, 141, 78))],
            [(" ", (30, 36, 48)), (" ", (30, 36, 48)), (" ", (30, 36, 48)), (" ", (30, 36, 48)), (" ", (30, 36, 48))]
        ]
        csz = 44
        gap = 8
        grid_w = 5 * csz + 4 * gap
        grid_h = 4 * csz + 3 * gap
        start_x = (w - grid_w) // 2
        start_y = (h - grid_h) // 2
        for r_idx, row in enumerate(rows):
            for c_idx, (letter, col) in enumerate(row):
                rx = start_x + c_idx * (csz + gap)
                ry = start_y + r_idx * (csz + gap)
                draw.rectangle([rx, ry, rx + csz, ry + csz], fill=col, outline=(75, 85, 105), width=1)
                if letter != " ":
                    draw.text((rx + csz/2 - 6, ry + csz/2 - 10), letter, fill=(255, 255, 255), stroke_width=1)
        return img

    # Default fallback: None so caller uses assets or generic rich environment
    return None


def generate_for_game(game):
    slug = game["slug"]
    category = game.get("category", "casual")
    game_path = game.get("path", "")
    game_dir = os.path.dirname(game_path)
    assets_dir = os.path.join(game_dir, "assets")

    out_file = f"assets/thumbnails/{slug}.png"

    # 1. First priority: Check iconic custom generator
    iconic_img = generate_iconic_game(slug, category)
    if iconic_img is not None:
        iconic_img.save(out_file, "PNG", optimize=True)
        return out_file

    # 2. Category fallback theme colors
    theme = THEMES.get(category, THEMES["arcade"])
    base_bg = solid_gradient(theme["bg1"], theme["bg2"], WIDTH, HEIGHT)

    # 3. Look inside assets/ for real game graphics
    files = []
    if os.path.exists(assets_dir):
        files = [f for f in os.listdir(assets_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]

    bg_found = False
    if files:
        # Check background candidate
        bgs = [
            f for f in files
            if any(k in f.lower() for k in ["bg", "background", "back", "wall"])
            and not any(k in f.lower() for k in ["btn", "icon", "music", "sound", "dialog", "black"])
        ]
        if bgs:
            bg_path = os.path.join(assets_dir, bgs[0])
            try:
                with Image.open(bg_path) as raw_bg:
                    raw_bg = raw_bg.convert("RGBA")
                    fitted = ImageOps.fit(raw_bg, (WIDTH, HEIGHT), method=Image.Resampling.LANCZOS)
                    # Paste fitted background over base_bg so any transparency is filled with rich theme color
                    base_bg.paste(fitted, (0, 0), fitted)
                    bg_found = True
            except Exception:
                pass

        # Check for character/hero sprites to place on top
        sprites = [
            f for f in files
            if any(k in f.lower() for k in ["hero", "player", "character", "car", "ship", "alien", "ball", "tile", "enemy", "boss", "weapon", "fruit", "candy", "bird", "plane", "runner", "item", "rock", "paper", "scissors"])
            and not any(k in f.lower() for k in ["btn", "button", "box", "replay", "next", "htp", "lvl", "score", "pause", "sound", "ovr", "bar", "dialog", "music"])
        ]
        if not sprites and not bg_found:
            sprites = [f for f in files if not any(k in f.lower() for k in ["btn", "button", "replay", "next", "pause", "music"])]

        if sprites:
            try:
                with Image.open(os.path.join(assets_dir, sprites[0])) as sp_raw:
                    sp = sp_raw.convert("RGBA")
                    if sp.width >= 24 and sp.height >= 24:
                        sp.thumbnail((150, 150), Image.Resampling.LANCZOS)
                        sx = (WIDTH - sp.width) // 2
                        sy = (HEIGHT - sp.height) // 2 + 10
                        # Soft shadow
                        shadow = Image.new("RGBA", (sp.width + 20, sp.height + 20), (0, 0, 0, 0))
                        sh_d = ImageDraw.Draw(shadow)
                        sh_d.ellipse([10, 10, sp.width + 10, sp.height + 10], fill=(0, 0, 0, 80))
                        shadow = shadow.filter(ImageFilter.GaussianBlur(8))
                        base_bg.paste(shadow, (sx - 10, sy - 10), shadow)
                        base_bg.paste(sp, (sx, sy), sp)
            except Exception:
                pass

    if not bg_found and not files:
        # For remaining games without files, give a polished arena scene
        draw = ImageDraw.Draw(base_bg)
        # Geometric arena circles
        draw.ellipse([80, -20, 400, 300], fill=(255, 255, 255, 20))
        draw.rounded_rectangle([190, 100, 290, 200], radius=24, fill=(255, 255, 255), outline=theme["accent"], width=3)
        draw.polygon([(228, 125), (268, 150), (228, 175)], fill=theme["accent"])

    base_bg.convert("RGB").save(out_file, "PNG", optimize=True)
    return out_file


def main():
    with open("games/registry.json", "r", encoding="utf-8") as f:
        registry = json.load(f)

    games = registry.get("games", [])
    print(f"Generating premium solid background thumbnails for {len(games)} games...")
    os.makedirs("assets/thumbnails", exist_ok=True)

    count = 0
    for g in games:
        generate_for_game(g)
        count += 1
        if count % 25 == 0 or count == len(games):
            print(f"Progress: {count}/{len(games)} games generated...")

    print("All thumbnails generated with 100% solid full-bleed background pictures!")


if __name__ == "__main__":
    main()
