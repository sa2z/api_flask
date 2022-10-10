import argparse

def setup_args():

    parser = argparse.ArgumentParser(description='API function')
    parser.add_argument('--prj_nm', default='ocr')
    args = parser.parse_args() # vs code
    # args = parser.parse_args(args=[]) # jupyter notebook    

    return args