import os
import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import random
from pathlib import Path
import sys


comendo = False
comendo_index = 0

root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.config(bg="pink")
root.wm_attributes("-transparentcolor", "pink")

balao_win = tk.Toplevel(root)
balao_win.overrideredirect(True)
balao_win.wm_attributes("-topmost", True)
balao_win.config(bg="pink")
balao_win.wm_attributes("-transparentcolor", "pink")


balao_canvas_w, balao_canvas_h = 120, 90
balao_canvas = tk.Canvas(
   balao_win, width=balao_canvas_w, height=balao_canvas_h,
   bg="pink", highlightthickness=0
)
balao_canvas.pack()
balao_win.withdraw()


def resource_path(relative_path):
    """Retorna o caminho absoluto para recursos, funciona em dev e no PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', Path(__file__).parent)
    return Path(base_path) / relative_path



def load_frames(folder, scale=1.0, keep_ratio=True):
    frames = []
    folder_str = str(folder)
    if not os.path.exists(folder_str):
        print(f"Erro: pasta não encontrada: {folder_str}")
        return frames
    for f in sorted(os.listdir(folder_str)):
        if f.lower().endswith(".png"):
            img = Image.open(os.path.join(folder_str, f))
            if keep_ratio:
                w, h = img.size
                img = img.resize((int(w * scale), int(h * scale)))
            else:
                img = img.resize((20, 20))
            frames.append(img)
    return frames


base_path = resource_path("")
base_path_str = str(base_path)

path_walk = os.path.join(base_path_str, "desenhos", "Movimentos básicos", "andando", "esquerda")
path_idle = os.path.join(base_path_str, "desenhos", "Movimentos básicos", "parado")
path_heart = os.path.join(base_path_str, "desenhos", "icones botoes", "coracao")
path_ninho = os.path.join(base_path_str, "desenhos", "icones botoes", "ninho", "sprite_0.png")
path_dormir = os.path.join(base_path_str, "desenhos", "Movimentos básicos", "dormindo")
path_sono = os.path.join(path_dormir, "sono")
path_lamp_apagada = os.path.join(base_path_str, "desenhos", "icones botoes", "luz", "apagada")
path_lamp_acesa = os.path.join(base_path_str, "desenhos", "icones botoes", "luz", "acesa")
path_bateria = os.path.join(base_path_str, "desenhos", "icones botoes", "bateria")
path_balao = os.path.join(base_path_str, "desenhos", "icones botoes", "balao", "balao0.png")
path_milho = os.path.join(base_path_str, "desenhos", "icones botoes", "milho", "milho.png")
path_comendo = os.path.join(base_path_str, "desenhos", "Movimentos básicos", "comendo")
path_sabao = os.path.join(base_path_str, "desenhos", "icones botoes", "sabao", "sabonete1.png")
path_bolha = os.path.join(base_path_str, "desenhos", "icones botoes", "sabao", "bolha.png")



walk_right_raw = load_frames(path_walk, 0.4)
walk_left_raw = [ImageOps.mirror(img) for img in walk_right_raw]
idle_raw = load_frames(path_idle, 0.4)
heart_raw = load_frames(path_heart, 0.2)
dormir_raw = load_frames(path_dormir, 0.4)
sono_raw = load_frames(path_sono, 0.4)
bateria_raw = load_frames(path_bateria, scale=0.15)
balao_img = ImageTk.PhotoImage(Image.open(path_balao).resize((80, 60)))
milho_img = ImageTk.PhotoImage(Image.open(path_milho).resize((50, 50)))
comendo_raw = load_frames(path_comendo, 0.4)
sabao_img = ImageTk.PhotoImage(Image.open(path_sabao).resize((50, 50)))
bolha_img = ImageTk.PhotoImage(Image.open(path_bolha).resize((32, 32)))


comendo_frames = [ImageTk.PhotoImage(img) for img in comendo_raw]
walk_right = [ImageTk.PhotoImage(img) for img in walk_right_raw]
walk_left = [ImageTk.PhotoImage(img) for img in walk_left_raw]
idle_frames = [ImageTk.PhotoImage(img) for img in idle_raw]
heart_frames = [ImageTk.PhotoImage(img) for img in heart_raw]
dormir_frames = [ImageTk.PhotoImage(img) for img in dormir_raw]
sono_frames = [ImageTk.PhotoImage(img) for img in sono_raw]
bateria_imgs = [ImageTk.PhotoImage(img) for img in bateria_raw]


lamp_apagada_img = ImageTk.PhotoImage(
   Image.open(os.path.join(path_lamp_apagada, "apagada0.png")).resize((80, 80))
)
lamp_acesa_imgs = [
   ImageTk.PhotoImage(Image.open(os.path.join(path_lamp_acesa, f"acesa_{i}.png")).resize((80, 80)))
   for i in range(2)
]


ninho_img = ImageTk.PhotoImage(Image.open(path_ninho).resize((150, 150)))


sprite_w = idle_frames[0].width()
sprite_h = idle_frames[0].height()


balao_img_id = balao_canvas.create_image(
   balao_canvas_w // 2, balao_canvas_h // 2,
   anchor='center', image=balao_img, state='hidden'
)
balao_text_id = balao_canvas.create_text(
   balao_canvas_w // 2, balao_canvas_h // 2 - 5,
   text="", font=("Arial", 14, "bold"),
   fill="black", state='hidden'
)

icone_path = resource_path("desenhos/icone.png")
icone_img = Image.open(str(icone_path))
icone_img.save(str(resource_path("desenhos/icone.ico")), sizes=[(256,256), (128,128), (64,64), (32,32), (16,16)])



canvas = tk.Canvas(root, width=sprite_w + 50, height=sprite_h + 300, bg="pink", highlightthickness=0)
canvas.pack()


sprite = canvas.create_image(0, 10, anchor='nw', image=idle_frames[0])


heart = canvas.create_image(
   sprite_w // 2, sprite_h // 2 - 40, anchor='center', image=heart_frames[0]
)
canvas.itemconfigure(heart, state='hidden')







aba_lateral = tk.Toplevel(root)
aba_lateral.overrideredirect(True)
aba_lateral.wm_attributes("-topmost", True)
aba_lateral.config(bg="pink")
aba_lateral.wm_attributes("-transparentcolor", "pink")


tijolo_canvas_w = 200
tijolo_canvas_h = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()


aba_lateral.geometry(f"{tijolo_canvas_w}x{tijolo_canvas_h}+{screen_w - tijolo_canvas_w}+480")


canvas_lateral = tk.Canvas(
   aba_lateral, width=tijolo_canvas_w, height=tijolo_canvas_h, bg="pink", highlightthickness=0
)
canvas_lateral.pack()



ninho_x = tijolo_canvas_w // 2
ninho_y = 180
ninho = canvas_lateral.create_image(ninho_x, ninho_y, anchor="center", image=ninho_img)


lamp_x = tijolo_canvas_w // 2
lamp_y = 30
lamp_img_id = canvas_lateral.create_image(lamp_x, lamp_y, anchor="center", image=lamp_apagada_img)


bateria_img_id = canvas_lateral.create_image(-5, 5, anchor="nw", image=bateria_imgs[0])



lampada_acesa = False
lamp_anim_index = 0
lamp_anim_id = None


def toggle_lamp(event=None):
   global lampada_acesa, lamp_anim_id
   lampada_acesa = not lampada_acesa
   if lampada_acesa:
       animar_lampada()
   else:
       if lamp_anim_id:
           canvas_lateral.after_cancel(lamp_anim_id)
       canvas_lateral.itemconfig(lamp_img_id, image=lamp_apagada_img)


def animar_lampada():
   global lamp_anim_index, lamp_anim_id
   if lampada_acesa:
       lamp_anim_index = (lamp_anim_index + 1) % len(lamp_acesa_imgs)
       canvas_lateral.itemconfig(lamp_img_id, image=lamp_acesa_imgs[lamp_anim_index])
       lamp_anim_id = canvas_lateral.after(500, animar_lampada)


canvas_lateral.tag_bind(lamp_img_id, "<Button-1>", toggle_lamp)




def on_click_milho(event):
   global comendo, comendo_index, state, frames
   if not comendo and not dormindo and not indo_dormir:
       comendo = True
       comendo_index = 0
       state = "comendo"
       frames = comendo_frames
       show_balao()


def sprite_screen_pos():
   """Posição absoluta do sprite (canto superior esquerdo) na tela."""
   sx, sy = canvas.coords(sprite)
   return root.winfo_x() + int(sx), root.winfo_y() + int(sy)


def posicionar_balao():
   """Posiciona a janela do balão acima da cabeça da galinha."""
   global balao_offset_y
   sx, sy = sprite_screen_pos()
   bx = sx + sprite_w // 2 - balao_canvas_w // 2
   by = sy + 30 + balao_offset_y - balao_canvas_h
   balao_win.geometry(f"{balao_canvas_w}x{balao_canvas_h}+{int(bx)}+{int(by)}")


def show_balao():
   global balao_visible, balao_timer, balao_cooldown, balao_offset_y
   balao_visible = True
   balao_timer = 0
   balao_cooldown = 0
   balao_offset_y = 0

   pool = insetos_emojis if (comendo or state == "comendo") else balao_emojis
   chosen = random.choice(pool)

   balao_canvas.itemconfigure(balao_text_id, text=chosen)
   balao_canvas.itemconfigure(balao_img_id, state='normal')
   balao_canvas.itemconfigure(balao_text_id, state='normal')
   balao_win.deiconify()
   posicionar_balao()


def hide_balao():
   global balao_visible, balao_next_interval
   balao_visible = False
   balao_canvas.itemconfigure(balao_img_id, state='hidden')
   balao_canvas.itemconfigure(balao_text_id, state='hidden')
   balao_win.withdraw()
   balao_next_interval = random.randint(9000, 16000)


janela_botao = tk.Toplevel(root)
janela_botao.overrideredirect(True)
janela_botao.wm_attributes("-topmost", True)
janela_botao.config(bg="pink")
janela_botao.wm_attributes("-transparentcolor", "pink")


botao_w = 25
botao_h = 40
janela_botao.geometry(f"{botao_w}x{botao_h}+{screen_w - tijolo_canvas_w - botao_w}+570")


aba_lateral_aberta = True
canvas_lateral.create_rectangle(0, 0, tijolo_canvas_w, tijolo_canvas_h, outline="red")



x, y = 300, 570
frame_index = 0
speed = 8
frame_delay = 180
direction = "right"
state = "idle"
frames = idle_frames
state_timer = 0
state_delay = random.randint(2000, 4000)


heart_visible = False
heart_timer = 0
heart_frame_index = 0


indo_dormir = False
dormindo = False
dormir_index = 0
sono_index = 0
z_labels = []
z_timer = 0
z_interval = 2000
MAX_ZS = 3


nivel_bateria = 0
tempo_ultimo_gasto = 0
tempo_ultimo_recarga = 0
intervalo_gasto = 300000
intervalo_recarga = 5000


milho_x = 150
milho_y = 5
milho_id = canvas_lateral.create_image(milho_x, milho_y, anchor="nw", image=milho_img)


sabao_x = milho_x
sabao_y = milho_y + 60
sabao_pos_lateral = (sabao_x, sabao_y)
sabao_id = canvas_lateral.create_image(sabao_x, sabao_y, anchor="nw", image=sabao_img)
SABAO_TAG = "sabao_tag"
canvas_lateral.addtag_withtag(SABAO_TAG, sabao_id)
canvas_lateral.addtag_withtag(SABAO_TAG, sabao_id)
print("sabao_id =", sabao_id, type(sabao_id))


soap_win = tk.Toplevel(root)
soap_win.overrideredirect(True)
soap_win.wm_attributes("-topmost", True)
soap_win.config(bg="pink")
soap_win.wm_attributes("-transparentcolor", "pink")
soap_canvas = tk.Canvas(soap_win, width=50, height=50, bg="pink", highlightthickness=0)
soap_canvas.pack()
soap_canvas_img_id = soap_canvas.create_image(25, 25, image=sabao_img)
soap_win.withdraw()

comidas_contadas = 0

soap_offset = (0, 0)
dragging_sabao = False
bubble_last_time = 0
bubble_interval = 1000
bubble_counter = 0
bubble_ids = []
soap_return_anim = None
sabao_rest_screen = (0, 0)


canvas_lateral.tag_bind(milho_id, "<Button-1>", on_click_milho)


balao_visible = False
balao_timer = 0
balao_duration = 2500
balao_cooldown = 0
balao_next_interval = 0
balao_offset_y = 0
balao_emojis = [
   ":)", ":D", ":P", ";)", ":(", ":O", ":|", ":/", ":3", ":]",
   ":(", ":'(", ":')", ":*", ":$", ">:(", ">.<", "O:)", ">:)", ":-)",
    "(^_^)", "(^.^)", "(>_<)", "(=_=)", "(T_T)", "(°ロ°)", "(^o^)", "(o_O)", "(¬_¬)",
   "(◕‿◕)", "(♥_♥)", "(✿◠‿◠)", "(≧▽≦)",  "(~_^)", "(¬‿¬)", "(¬‿¬ )",
   "(•_•)", "⌐■-■", "(⌐■_■)", "(^_−)☆", "(っ˘з˘⌣", "(｡◕‿◕｡)", "（＾_＾）",
   "(⌒‿⌒)", "(>ω<)", "(>^.^<)", "◕ヮ◕", "☆彡", "(✧ω✧)", "(✿╹◡╹)", "╹◡╹"
]
insetos_emojis = ["🐛", "🪲", "🐜", "🪳", "🦟", "🕷️", "🦗", "🪰", "🪱", "🐞"]


def animar_aba(destino, passo):
   atual_x = aba_lateral.winfo_x()
   if (passo > 0 and atual_x < destino) or (passo < 0 and atual_x > destino):
       novo_x = atual_x + passo
       aba_lateral.geometry(f"{tijolo_canvas_w}x{tijolo_canvas_h}+{novo_x}+480")
       janela_botao.geometry(f"{botao_w}x{botao_h}+{novo_x - botao_w}+570")


       if dormindo:
           galinha_x = novo_x + ninho_x - sprite_w // 2
           root.geometry(f"+{int(galinha_x)}+{y}")


       aba_lateral.after(10, lambda: animar_aba(destino, passo))
   else:
       aba_lateral.geometry(f"{tijolo_canvas_w}x{tijolo_canvas_h}+{destino}+480")
       janela_botao.geometry(f"{botao_w}x{botao_h}+{destino - botao_w}+570")

       if dormindo:
           galinha_x = destino + ninho_x - sprite_w // 2
           root.geometry(f"+{int(galinha_x)}+{y}")
           if not aba_lateral_aberta:
               root.withdraw()


def sabao_rest_screen_pos():
   ax, ay = aba_lateral.winfo_x(), aba_lateral.winfo_y()
   sx = ax + sabao_pos_lateral[0]
   sy = ay + sabao_pos_lateral[1]
   return sx, sy


def start_drag_sabao(event):
   global dragging_sabao, soap_offset, sabao_rest_screen
   dragging_sabao = True
   sabao_rest_screen = sabao_rest_screen_pos()

   soap_win.geometry(f"50x50+{sabao_rest_screen[0]}+{sabao_rest_screen[1]}")
   soap_win.deiconify()

   soap_x = soap_win.winfo_x()
   soap_y = soap_win.winfo_y()

   soap_offset = (event.x_root - soap_x, event.y_root - soap_y)

   follow_mouse_with_soap()


def follow_mouse_with_soap():
   global dragging_sabao, bubble_counter


   if not dragging_sabao:
       return


   mx = root.winfo_pointerx()
   my = root.winfo_pointery()


   nx = mx - soap_offset[0]
   ny = my - soap_offset[1]
   soap_win.geometry(f"50x50+{int(nx)}+{int(ny)}")

   check_bubble(nx, ny)

   root.after(16, follow_mouse_with_soap)


def end_drag_sabao(event):
   global dragging_sabao
   dragging_sabao = False
   smooth_return_to_rest()


def smooth_return_to_rest(duration=250):
   """Anima o retorno do sabonete até sua posição de descanso."""
   global soap_return_anim
   start_x = soap_win.winfo_x()
   start_y = soap_win.winfo_y()
   end_x, end_y = sabao_rest_screen
   steps = max(1, duration // 16)
   dx = (end_x - start_x) / steps
   dy = (end_y - start_y) / steps


   def step(i=0):
       if i < steps:
           soap_win.geometry(f"50x50+{int(start_x + dx*i)}+{int(start_y + dy*i)}")
           soap_return_anim = root.after(16, lambda: step(i+1))
       else:
           soap_win.geometry(f"50x50+{end_x}+{end_y}")
           soap_win.withdraw()


   step()


def sprite_bbox_screen():
   """Retorna bbox (x1,y1,x2,y2) do sprite em coordenadas de tela."""
   sx, sy = canvas.coords(sprite)
   x1 = root.winfo_x() + int(sx)
   y1 = root.winfo_y() + int(sy)
   x2 = x1 + sprite_w
   y2 = y1 + sprite_h
   return x1, y1, x2, y2


def check_bubble(soap_x, soap_y):
   cx = soap_x + 25
   cy = soap_y + 25


   x1, y1, x2, y2 = sprite_bbox_screen()
   inside = (x1 <= cx <= x2) and (y1 <= cy <= y2)


   if inside:
       spawn_bubble()


def spawn_bubble():
   sx, sy = canvas.coords(sprite)
   bx = sx + sprite_w // 2 + random.randint(-20, 20)
   by = sy + 80 + random.randint(-10, 10)

   bid = canvas.create_image(bx, by, image=bolha_img)

   canvas.after(1000, lambda i=bid: canvas.delete(i))


def toggle_aba_lateral():
   global aba_lateral_aberta
   if aba_lateral_aberta:
       destino_x = screen_w
       animar_aba(destino_x, 20)
       aba_lateral_aberta = False
   else:
       destino_x = screen_w - tijolo_canvas_w
       aba_lateral.deiconify()
       if dormindo:
           root.deiconify()
       animar_aba(destino_x, -20)
       aba_lateral_aberta = True


def atualizar_bateria_visual():
   canvas_lateral.itemconfig(bateria_img_id, image=bateria_imgs[nivel_bateria])


def criar_z():
   sprite_pos = canvas.coords(sprite)
   base_x = sprite_pos[0] + sprite_w // 2 + random.randint(-10, 10)
   base_y = sprite_pos[1] + sprite_h // 2 - 60
   z = canvas.create_text(base_x, base_y, text="Z", font=("Arial", 20, "bold"),
                          fill="#0000ff", anchor="center")
   z_labels.append({"id": z, "y": base_y, "alpha": 1.0})


def atualizar_zs():
   remover = []
   for z in z_labels:
       z["y"] -= 0.5
       z["alpha"] -= 0.10
       if z["alpha"] <= 0:
           remover.append(z)
           continue
       azul = int(50 + z["alpha"] * (255 - 50))
       azul = max(0, min(255, azul))
       cor = f"#0000{azul:02x}"
       canvas.coords(z["id"], canvas.coords(z["id"])[0], z["y"])
       canvas.itemconfig(z["id"], fill=cor)
   for z in remover:
       canvas.delete(z["id"])
       z_labels.remove(z)


def show_heart():
   global heart_visible, heart_timer, heart_frame_index
   heart_visible = True
   heart_timer = 0
   heart_frame_index = 0
   canvas.itemconfigure(heart, state='normal')
   canvas.after(2000, lambda: canvas.itemconfigure(heart, state='hidden'))


def on_click(event):
   show_heart()


def on_click_ninho(event):
   global indo_dormir, dormindo, state, frames, frame_index
   global tempo_ultimo_gasto, tempo_ultimo_recarga
   if not indo_dormir and not dormindo:
       indo_dormir = True
       state = "walking"
   elif dormindo:
       dormindo = False
       tempo_ultimo_gasto = 0
       tempo_ultimo_recarga = 0
       state = "idle"
       frames = idle_frames
       frame_index = 0
       root.deiconify()
   for z in z_labels:
       canvas.delete(z["id"])
   z_labels.clear()

def update():
   global frame_index, x, y, direction, state, frames
   global state_timer, state_delay
   global heart_visible, heart_timer, heart_frame_index
   global indo_dormir, dormindo, dormir_index, sono_index
   global z_timer, z_labels
   global tempo_ultimo_gasto, tempo_ultimo_recarga, nivel_bateria
   global balao_visible, balao_timer, balao_duration, balao_cooldown, balao_next_interval, balao_offset_y
   global screen_w, tijolo_canvas_w, ninho_x, sprite_w
   global frame_delay, speed, aba_lateral_aberta
   global comendo, comendo_index


   if comendo:
       if comendo_index < len(comendo_frames):
           canvas.itemconfig(sprite, image=comendo_frames[comendo_index])
           comendo_index += 1
           root.after(frame_delay, update)
           return
       else:
           comendo = False
           state = "idle"
           frames = idle_frames
           comendo_index = 0
           hide_balao()

   if balao_visible:
       balao_offset_y -= 1
       posicionar_balao()
       balao_timer += frame_delay
       if balao_timer >= balao_duration:
           hide_balao()
   else:
       if (not indo_dormir) and (not dormindo):
           balao_cooldown += frame_delay
           if balao_cooldown >= balao_next_interval:
               show_balao()


   if indo_dormir and not dormindo:
       destino = screen_w - tijolo_canvas_w + ninho_x - sprite_w // 2
       if abs(x - destino) > speed:
           direction = "right" if x < destino else "left"
           x += speed if direction == "right" else -speed
           frames = walk_right if direction == "right" else walk_left
           state = "walking"
       else:
           x = destino
           root.geometry(f"+{x}+{y}")
           indo_dormir = False
           dormindo = True


           if not aba_lateral_aberta:
               root.withdraw()
               if balao_visible:
                   hide_balao()
           else:
               root.deiconify()


           dormir_index = 0
           frame_index = 0
           state = "dormir"
           frames = dormir_frames


   if dormindo:
       if state == "dormir":
           if dormir_index < len(dormir_frames):
               canvas.itemconfig(sprite, image=dormir_frames[dormir_index])
               dormir_index += 1
           else:
               state = "sono"
               sono_index = 0
       elif state == "sono":
           canvas.itemconfig(sprite, image=sono_frames[sono_index])
           sono_index = (sono_index + 1) % len(sono_frames)

           z_timer += frame_delay
           if z_timer >= z_interval:
               criar_z()
               z_timer = 0
           atualizar_zs()

           tempo_ultimo_recarga += frame_delay
           if tempo_ultimo_recarga >= intervalo_recarga:
               if nivel_bateria > 0:
                   nivel_bateria -= 1
                   atualizar_bateria_visual()
               tempo_ultimo_recarga = 0


       root.geometry(f"+{x}+{y}")
       root.after(frame_delay, update)
       return

   frame_index = (frame_index + 1) % len(frames)
   canvas.itemconfig(sprite, image=frames[frame_index])


   if state == "walking":
       x += speed if direction == "right" else -speed
       x = max(0, min(x, root.winfo_screenwidth() - sprite_w))
       if x == 0:
           direction = "right"
           frames = walk_right
       elif x == root.winfo_screenwidth() - sprite_w:
           direction = "left"
           frames = walk_left


   root.geometry(f"+{x}+{y}")

   state_timer += frame_delay
   if state_timer >= state_delay and not indo_dormir:
       state_timer = 0
       state_delay = random.randint(2000, 4000)
       if state == "idle":
           state = "walking"
           direction = random.choice(["left", "right"])
           frames = walk_right if direction == "right" else walk_left
       else:
           state = "idle"
           frames = idle_frames
       frame_index = 0

   heart_timer += frame_delay
   if heart_visible:
       heart_frame_index = (heart_frame_index + 1) % len(heart_frames)
       canvas.itemconfig(heart, image=heart_frames[heart_frame_index])
       canvas.coords(heart, sprite_w // 2, sprite_h // 2 - 40)

   tempo_ultimo_gasto += frame_delay
   if tempo_ultimo_gasto >= intervalo_gasto:
       if nivel_bateria < 5:
           nivel_bateria += 1
           atualizar_bateria_visual()
           if nivel_bateria == 5 and not indo_dormir:
               indo_dormir = True
               state = "walking"
       tempo_ultimo_gasto = 0


   root.after(frame_delay, update)

botao_toggle = tk.Button(
   janela_botao,
   text="🐔",
   command=toggle_aba_lateral,
   bg="#ffd8a8",
   fg="black",
   font=("Arial", 18),
   relief="flat",
   bd=0,
   highlightthickness=0,
   activebackground="#ffc078"
)
botao_toggle.pack(expand=True, fill='both')

canvas.tag_bind(sprite, "<Button-1>", on_click)

canvas_lateral.tag_bind(ninho, "<Button-1>", on_click_ninho)
canvas_lateral.tag_bind(milho_id, "<Button-1>", on_click_milho)

SABAO_TAG = "sabao_tag"
canvas_lateral.tag_bind(SABAO_TAG, "<Button-1>", start_drag_sabao)
canvas_lateral.tag_bind(SABAO_TAG, "<ButtonRelease-1>", end_drag_sabao)
print(""""─────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────
─────────────────────────── A  ──────────────────────────────
────────────────────────── AAA ──────────────────────────────
───────────────────────── AA A  ─────────────────────────────
──────────────────────── AA ─ A  ────────────────────────────
──────────────────────── A ── AA ────────────────────────────
─────────────────────── A ──── AA ───────────────────────────
────────────────────── A ────── A ───────────────────────────
───────────────────── AA ───────AA ──────────────────────────
──────────────────── AA ──────── A ──────────────────────────
─────────────────── AA ──────────AA ─────────────────────────
─────── A ───────── A ─────────── A  ────────────────────────
──────── AA ────── A ───────────── A ────────────────────────
────────── AA ─── AA────────────── AA ───────────────────────
──────────── AAA AA ──────────────  A ───────────────────────
─────────────── AAA ─────────────── AA ──────────────────────
────────────── AA──AA ────────────── AA ─────────────────────
───────────── AA ─── AA ───────────── A ─────────────────────
────────────  A ────── AAA─────────── AA ─────────EEEEEEE ───
──────────── A ─────────  AA────────── A ─────── EE ─── EE ──
───────────AA───────────── AAA───────── A ───── E ────── E ──
───────── AA  ─────────────  AAA ────── AA ──── E ────── E───
──────── AA─────────────────── AAA  ──── AA ─── EEEEEEEEEE───
─────── AA  ───────────────────── AA ──── A ─── E ───────────
────── AA──────────────────────────AAA────AA ── E ───────────
───── AA──────────────────────────────AA── A ───E ────── E───
──── AA ────────────────────────────────AAA A ───EE ──── E───
─── AAA───────────────────────────────────AAAA ── EEEEEEEE───""")

update()
root.mainloop()
