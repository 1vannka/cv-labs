import os
import shutil

out_dir= "uni_dataset"
for split in ['train', 'val']:
    os.makedirs(f"{out_dir}/{split}/images", exist_ok=True)
    os.makedirs(f"{out_dir}/{split}/labels", exist_ok=True)

print("часть svhn")
for split in ['train', 'val']:
    svhn_dir= f"archive/dataset/{split}"

    for filename in os.listdir(svhn_dir):
        base_name =filename.rsplit('.',1)[0]
        new_filename=f"svhn_{filename}"
        new_lbl_name= f"svhn_{base_name}.txt"
        img_path= os.path.join(svhn_dir,filename)
        lbl_path= os.path.join(svhn_dir,base_name +'.txt')

        shutil.copy(img_path, f"{out_dir}/{split}/images/{new_filename}")
        with open(lbl_path,'r') as a, open(f"{out_dir}/{split}/labels/{new_lbl_name}", 'w') as b:
            for line in a:
                parts= line.strip().split()
                if len(parts)>=5:
                    parts[0] = '0'
                    b.write(' '.join(parts) +'\n')

print("часть text")
for split in ['train', 'val']:
    coco_img_dir= f"coco_yolo_dataset/{split}/images"
    coco_lbl_dir= f"coco_yolo_dataset/{split}/labels"

    for filename in os.listdir(coco_img_dir):
        base_name =filename.rsplit('.',1)[0]
        new_filename=f"coco_{filename}"
        new_lbl_name= f"coco_{base_name}.txt"
        img_path= os.path.join(coco_img_dir,filename)
        lbl_path= os.path.join(coco_lbl_dir,base_name +'.txt')

        shutil.copy(img_path, f"{out_dir}/{split}/images/{new_filename}")
        with open(lbl_path,'r') as a, open(f"{out_dir}/{split}/labels/{new_lbl_name}", 'w') as b:
            for line in a:
                parts= line.strip().split()
                if len(parts)>=5:
                    parts[0] = '0'
                    b.write(' '.join(parts) +'\n')

yaml= f"train: {os.path.abspath(out_dir)}/train/images\nval: {os.path.abspath(out_dir)}/val/images\n\nnc: 1\nnames: ['text']"
with open(f"{out_dir}/data.yaml", 'w') as f:
    f.write(yaml)
