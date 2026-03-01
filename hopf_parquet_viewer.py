from ursina import *
import pandas as pd
import math

app = Ursina()
window.color = color.black
window.title = "SPHY Player v2.0 - Estrelas Reais"
EditorCamera()

# --- CARREGAMENTO DOS DADOS ---
print("Carregando dataset... por favor, aguarde.")
try:
    df = pd.read_csv("sphy_galaxy_dataset.csv")
    TOTAL_FRAMES = int(df['frame'].max() + 1)
    NUM_ESTRELAS = int(df['star_id'].max() + 1)
    TAMANHO_PADRAO = df['size'].iloc[0]
except FileNotFoundError:
    print("Erro: Arquivo 'sphy_galaxy_dataset.csv' não encontrado!")
    application.quit()

# --- INICIALIZAÇÃO DOS CORPOS ---
# Criamos esferas reais. Isso evita o bug do "lilás" da GPU.
estrelas = []
for i in range(NUM_ESTRELAS):
    e = Entity(
        model='sphere', 
        color=color.white, 
        scale=TAMANHO_PADRAO # Agora usamos o tamanho real do dataset
    )
    estrelas.append(e)

# O Buraco Negro Central
bh = Entity(model='sphere', color=color.black, scale=0.8)
aura = Entity(model='sphere', color=color.cyan, scale=0.82, alpha=0.1)

# --- CONTROLE DE REPRODUÇÃO ---
class PlayerControl:
    def __init__(self):
        self.current_frame = 0
        self.playing = True
        self.speed = 1.0
        
    def update_frame(self):
        if not self.playing:
            return
            
        # Filtra os dados do frame atual de forma eficiente
        frame_idx = int(self.current_frame)
        f_data = df[df['frame'] == frame_idx]
        
        # Se por algum motivo o frame estiver vazio (ex: erro no CSV), pula
        if f_data.empty:
            return

        # Extraímos os valores como matrizes numpy para velocidade máxima
        posicoes = f_data[['x', 'y', 'z']].values
        cores = f_data[['r', 'g', 'b']].values
        
        # Atualizamos cada entidade individualmente
        for i in range(len(estrelas)):
            if i < len(posicoes):
                estrelas[i].position = (posicoes[i][0], posicoes[i][1], posicoes[i][2])
                estrelas[i].color = color.rgb(cores[i][0], cores[i][1], cores[i][2])
        
        # Avança o frame com base na velocidade
        self.current_frame += self.speed
        if self.current_frame >= TOTAL_FRAMES:
            self.current_frame = 0

player = PlayerControl()

# --- INTERFACE E COMANDOS ---
info = Text(
    text="[Espaco]: Pausar | [R]: Reiniciar | [+/-]: Velocidade", 
    position=(-0.85, 0.45), scale=0.8, color=color.azure
)
frame_counter = Text(text="Frame: 0", position=(-0.85, 0.40), scale=0.8)

def input(key):
    if key == 'space':
        player.playing = not player.playing
    if key == 'r':
        player.current_frame = 0
    if key == '+':
        player.speed += 0.2
    if key == '-':
        player.speed = max(0.1, player.speed - 0.2)

def update():
    player.update_frame()
    frame_counter.text = f"Frame: {int(player.current_frame)} / {TOTAL_FRAMES-1}"
    
    # Pulso estético da aura e do buraco negro
    s = 0.82 + (math.sin(time.time() * 2) * 0.03)
    aura.scale = s
    bh.scale = s * 0.95

app.run()
