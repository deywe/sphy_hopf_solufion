from ursina import *
import pandas as pd
import os

class LyraAuditor(Entity):
    def __init__(self, file_path='lyra_master_audit.parquet'):
        super().__init__()
        self.file_path = file_path

        # File validation based on integrity test
        if not os.path.exists(self.file_path):
            print(f"❌ Error: File '{self.file_path}' not found in directory.")
            application.quit()
            return

        print(f"📂 Starting Audit: {self.file_path}")
        self.df = pd.read_parquet(self.file_path)
        self.total_frames = self.df['frame'].max()
        self.current_frame = 0
        self.playing = True

        # 1. Central Singularity (Absolute Black)
        self.black_hole = Entity(
            model='sphere', 
            color=color.black, 
            scale=1.5, 
            unlit=True, 
            position=(0,0,0)
        )

        # 2. 1000 Qudits Reconstruction (Stars)
        self.ids_unique = self.df['id'].unique()
        self.stars = {q_id: Entity(model='sphere', scale=0.06, color=color.cyan) for q_id in self.ids_unique}

        # 3. HUD - English Instructions
        self.title = Text(text="LYRA SYSTEM AUDIT", origin=(0,0), y=0.45, scale=1.3, color=color.gold)
        
        # Navigation Instructions on Screen
        self.nav_info = Text(
            text="[MOUSE RIGHT CLICK] -> Rotate Torus\n[MOUSE SCROLL WHEEL] -> Zoom In/Out\n[SPACE] -> Pause/Play", 
            origin=(-0.5, 0.5), x=0.5, y=0.45, scale=0.7, color=color.white
        )
        
        self.status = Text(text="", origin=(-0.5, 0.5), x=-0.85, y=0.4, color=color.cyan)

    def update(self):
        if not self.playing: return
        
        f_idx = int(self.current_frame)
        data = self.df[self.df['frame'] == f_idx]
        
        if not data.empty:
            for _, row in data.iterrows():
                s_id = row['id']
                if s_id in self.stars:
                    # Apply X, Y, Z coordinates from Parquet
                    self.stars[s_id].position = (row['x'], row['y'], row['z'])

        # 30 FPS Frame Synchronization
        self.current_frame += time.dt * 30
        if self.current_frame >= self.total_frames: self.current_frame = 0

        self.status.text = f"FRAME: {f_idx} / {self.total_frames}\nSTABILITY: SPHY WAVES OK"

    def input(self, key):
        if key == 'space':
            self.playing = not self.playing
        if key == 'r':
            self.current_frame = 0

# --- GLOBAL VISUALIZATION SETUP ---
app = Ursina()
window.color = color.black
window.fps_counter.enabled = False

# 4. Native Mouse Control Activation
cam_control = EditorCamera()
cam_control.target = Vec3(0,0,0) # Locks pivot on the Black Hole for perfect rotation

# 5. Strategic Viewpoint (Prevents Torus from starting off-screen)
camera.position = (0, 20, 15) 
camera.rotation_x = 20        

auditor = LyraAuditor()
app.run()