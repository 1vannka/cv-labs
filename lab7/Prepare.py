from facenet_pytorch import MTCNN
from PIL import Image
import os
from tqdm import tqdm
import torch
from config import *

os.makedirs(data_dir, exist_ok=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"{device}")

mtcnn = MTCNN(
    image_size=img_size,
    margin=10,
    keep_all=False,
    select_largest=True,
    post_process=False,
    device=device
)

all = [f for f in os.listdir(source) if f.endswith(('.jpg', '.png', '.jpeg'))]
imgs = all[:limit]
scs_cnt = 0

for img_name in tqdm(imgs):
    img_path= os.path.join(source, img_name)
    save_path= os.path.join(data_dir, img_name)

    if os.path.exists(save_path):
        scs_cnt+=1
        continue
    try:
        img= Image.open(img_path).convert('RGB')
        face =mtcnn(img)

        if face is not None:
            face_img= face.permute(1, 2, 0).byte().cpu().numpy()
            Image.fromarray(face_img).save(save_path)
            scs_cnt+= 1
    except Exception:
        pass