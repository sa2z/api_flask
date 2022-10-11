import os, json
from datetime import datetime, timedelta,timezone
from re import L
from flask import Flask, flash, jsonify, request, redirect, url_for, Response
import cv2

from module.ocr import OCR
from pathlib import Path
from main_config import setup_args

global args
args = setup_args()

p = Path.cwd()
files = p.glob('*') # p.glob('**/*')
p_src = p.parent.joinpath('src')

UPLOAD_FOLDER = p_src
ALLOWED_EXTENSIONS = set(['txt','json','jpg','jpeg','png','gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

@app.route('/')
def response_home():
    return 'response from home'

@app.route('/input', methods=['POST'])
def response_ocr():
    # process id from timestamp
    utc = datetime.utcnow()
    timezone_kst = timezone(timedelta(hours=9))
    kst = utc.astimezone(timezone_kst)
    pid = kst.strftime('%Y%m%d%H%M%S.%f')[:-4]
    
    # 전송이미지 저장
    data_rt = Path('/code/data')
    prj_path = data_rt.joinpath(args.prj_nm)
    os.makedirs(prj_path,exist_ok=True)
    fnm = "{}.jpg".format(pid)
    args.fp = str(prj_path.joinpath(fnm))
    fnm_edit = "{}_edit.jpg".format(pid)
    args.fp_edit = str(prj_path.joinpath(fnm_edit))

    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No selected image file')
            pass
            # return redirect(request.url)
        img = request.files['image']
        img.save(args.fp)
        img_fnm = img.filename
    img = cv2.imread(args.fp)
    ocr = OCR(img,args)
    res = ocr.process()

    ret = Response(json.dumps({
                                'seq':pid,
                                'img_fnm':img_fnm,
                                'result':res
                            }),status=201,mimetype='application/json')
    ret.headers['Access-Control-Allow-Origin'] = '*'
    return ret
# @app.route('/incomes')
# def get_incomes():
#     return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes = {}
    incomes['msg'] = request.get_json()
    return 'api_received', 204

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
