import argparse
import os
import shutil
import tqdm

def organize_data(data_path, cam_number, frame_num = 0):
    raw_data_path = os.path.join(data_path, 'raw')
    organized_data_path = os.path.join(data_path, 'input')
    print("moving frames to organized directory...")
    for i in tqdm.tqdm(range(cam_number)):
        shutil.copy(
            os.path.join(raw_data_path, f"cam{i+1}.0000.jpeg"),
            os.path.join(organized_data_path, f"img{i+1:04}.jpg")
        )
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", type=str)
    parser.add_argument("cam_number", type=int)
    parser.add_argument("--frame_num", type=int, default=0)
    args = parser.parse_args()

    organize_data(args.data_path, args.cam_number, args.frame_num)