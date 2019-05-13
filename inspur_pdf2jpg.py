"""
inspur_pdf2jpg.py
Created on Jul 30, 2018
Modified on Jan 03, 2019
@author: wang xinhu
"""
import os
import subprocess
import ast
import shutil
import platform


def convert_pdf2jpg_single(jarPath, inputpath, outputpath, pages, dpi):
    cmd = 'java -jar %s -i "%s" -o "%s" -p %s -d %s' % (jarPath, inputpath, outputpath, pages, dpi)
    outputpdfdir = os.path.join(outputpath, os.path.basename(inputpath))
    if os.path.exists(outputpdfdir):
        shutil.rmtree(outputpdfdir)

    system = platform.system()
    if system == "Linux":
        file_out = subprocess.Popen(
            'unset DISPLAY && java -jar %s -i "%s" -o "%s" -p %s -d %s' % (jarPath, inputpath, outputpath, pages, dpi),
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = file_out.stdout.readlines()
        output = line[0]
    else:
        file_out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = file_out.stdout.readlines()
        output = line[0]
    print(output)
    output = output.decode()
    print(output)
    # print(output)
    # output = output.split("#################################")[1].strip()
    #
    # output = ast.literal_eval(output)
    # outputpdfdir = output[inputpath]
    #
    # outputFiles = map(lambda x: os.path.join(outputpdfdir, x), os.listdir(outputpdfdir))
    # outputFiles = sorted(outputFiles, key=lambda x: os.path.basename(x).split("_")[0])

    result = {
        'cmd': cmd,
        'input_path': inputpath,
        'output_pdfpath': outputpdfdir,
        # 'output_jpgfiles': outputFiles
    }
    return [result]


def convert_pdf2jpg(inputpath, outputpath, pages="ALL", bulk=False, jobs=2, dpi=96):
    pages = pages.split(",")
    pages = map(lambda x: x.strip(), pages)
    pages = ",".join(pages)
    jarPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"inspur_pdf2jpg.jar")

    if not bulk:
        return convert_pdf2jpg_single(jarPath, inputpath, outputpath, pages=pages, dpi=dpi)


if __name__ == "__main__":
    inputpath = r"E:\xinhu\Project\gongchengyuan\scrapydManager\artcle_category\1.pdf"
    outputpath = r"E:\xinhu\Project\gongchengyuan\scrapydManager\artcle_category\pd"
    result = convert_pdf2jpg(inputpath, outputpath, pages="1,3", bulk=False, jobs=2, dpi=96)
    print(result)
