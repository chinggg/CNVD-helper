#!/usr/bin/env python3
import argparse
import shutil
import sys
from docx import Document


def setup_folder(dst: str) -> str:
    src = 'template/generic/'
    shutil.copytree(src, dst)
    docpath = dst + f'/{dst}.docx'
    shutil.move(dst + '/name.docx', docpath)
    shutil.move(dst + '/attachment.zip', dst + f'/{dst}.zip')
    return docpath


def read_conf(confname: str, chinese=True) -> dict:
    sys.path.append('conf')
    confmod = __import__(confname)
    keynames = [item for item in dir(confmod) if not item.startswith("__")]
    dic = {key: getattr(confmod, key) for key in keynames}
    if chinese:
        dic = {v[0]: v[1] for v in dic.values()}
    return dic


def modify_doc(docpath: str, conf: dict) -> None:
    doc = Document(docpath)
    table = doc.tables[0]
    for row in table.rows:
        key = row.cells[0].text
        if key in conf:
            row.cells[1].text = conf[key]
    doc.save(docpath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CNVD helper')
    parser.add_argument('--conf', '-c', type=str,
                        default='example', help='配置文件路径')
    args = parser.parse_args()
    conf = read_conf(args.conf)
    docpath = setup_folder(conf['漏洞名称'])
    modify_doc(docpath, conf)
