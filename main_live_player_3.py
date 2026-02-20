from ursina import *
import pandas as pd
import os

# Importamos a IA de Fluidos para reconstruir o visual do centro
from harpia_core.kernel.simbiotic_fluid_ai import FluidVortexAI

class LyraAuditor(Entity):
    def __init__(self, file_path='lyra_master_audit.parquet'):
        super().__init__()
        self.file_path = file_path
        
        # 1. Carregamento dos Dados de Auditoria
        if not os.path.exists(self.file_path):
            print(f"❌ Erro: Arquivo {self.file_path} não encontrado.")
            application.quit()
            return

        print(f"📂 Iniciando Auditoria da Galáxia Lyra...")
        self.df = pd.read_parquet(self.file_path)
        self.total_frames = self.df['frame'].max()
        self.current_frame = 0
        self.playing = True
        
        # 2. Reconstrução do Centro (Buraco Negro + Fluidos)
        self.vortex_container = Entity()
        # O Buraco Negro (Esfera Co)
        self.buraco_negro = Entity(
            model='sphere', 
            color=color.black, 
            scale=1.5, 
            parent=self.vortex_container
        )
        # As bolinhas brilhando ao redor (IA de Fluidos)
        self.vortex_ai = FluidVortexAI(num_pontos=35)
        self.vortex_ai.spawn(parent_container=self.vortex_container)

        # 3. Reconstrução das Estrelas (Qudits)
        self.ids_unicos = self.df['id'].unique()
        self.estrelas = {}
        for q_id in self.ids_unicos:
            self.estrelas[q_id] = Entity(
                model='sphere',
                scale=0.05,
                color=color.cyan,
                add_to_builtin_render=True
            )

        # HUD de Auditoria Lyra
        self.title = Text(text="AUDITORIA DE SISTEMA: LYRA", origin=(0,0), y=0.45, scale=1.5, color=color.gold)
        self.info = Text(text="", origin=(-0.5, 0.5), x=-0.85, y=0.4, color=color.cyan)

    def update(self):
        if not self.playing:
            return

        # 4. Sincronização de Frame e Movimento
        f_idx = int(self.current_frame)
        data = self.df[self.df['frame'] == f_idx]
        
        if not data.empty:
            # Reproduz o movimento da sua câmera (Zoom/Giro)
            if 'cam_x' in data.columns:
                camera.x = data.iloc[0]['cam_x']
                camera.y = data.iloc[0]['cam_y']
                camera.z = data.iloc[0]['cam_z']
                camera.rotation_x = data.iloc[0]['cam_rot_x']
                camera.rotation_y = data.iloc[0]['cam_rot_y']

            # Posiciona cada estrela conforme o registro
            for _, row in data.iterrows():
                e_id = row['id']
                if e_id in self.estrelas:
                    self.estrelas[e_id].position = (row['x'], row['y'], row['z'])

        # Atualiza o movimento das bolinhas brilhando (Vortex)
        self.vortex_ai.update_vortex(time.time() * 1000, time.dt)

        # Controle de fluxo do Auditor
        self.current_frame += time.dt * 30
        if self.current_frame >= self.total_frames:
            self.current_frame = 0

        self.info.text = f"FRAME: {f_idx} / {self.total_frames}\nSINCRONIA: 100%\nCÂMERA: REGISTRADA"

    def input(self, key):
        if key == 'space':
            self.playing = not self.playing
        if key == 'r':
            self.current_frame = 0

# --- Inicialização ---
app = Ursina()
window.color = color.black
window.fps_counter.enabled = False

auditor = LyraAuditor()

app.run()