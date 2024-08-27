import datetime, shutil
import sys, os


def backup(src_dir, dst_dir):
    
    if not os.path.exists(src_dir):
        print(f"Error: Source directory provided as arguments'{src_dir}' doesn't exist!! ")
    if not os.path.exists(dst_dir):
        print(f"Error: Source directory provided as arguments'{dst_dir}' doesn't exist!! ")
    try:
        for file in os.listdir(src_dir):
            src_path = os.path.join(src_dir, file)
            dst_path = os.path.join(dst_dir, file)
            if os.path.exists(dst_path):
                ext = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
                dst_path = dst_path + "_" + ext
            shutil.copy(src_path, dst_path)

        print("Files are copied, refer files at destination directory: ")
        print(os.listdir(dst_dir))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        src_dir = sys.argv[1]
        dst_dir = sys.argv[2]
        backup(src_dir, dst_dir)
    else:
        print('''
              Please check the syntax and spaces for correct use:
              Usage:-
              python backup.py /path/to/source /path/to/destination
              ''')