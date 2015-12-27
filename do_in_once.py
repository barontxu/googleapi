#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import os
import sys

def gen_input_txt(img_file, ofile):
  with open(ofile, 'w') as f:
    for img in os.listdir(img_file):
      f.write(os.path.join(os.path.abspath(img_file), img))
      f.write(' 5:20\n')

def gen_reqjson(input_txt):
  os.system("python generate.py -i " + input_txt + " -o req.json")

def gen_response():
  os.system("""curl -v -k -s -H "Content-Type: application/json" "https://vision.googleapis.com/v1alpha1/images:annotate?key=AIzaSyDViHE_kkBm6a7H1eEW_GeNTT5iD7yyse0" --data-binary @req.json -o response.json
""")

if __name__ == "__main__":
  if len(sys.argv) == 3:
    gen_input_txt(sys.argv[1], sys.argv[2])
    gen_reqjson('input.txt')
    gen_response()
  else:
    gen_reqjson(sys.argv[1])
    gen_response()