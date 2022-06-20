#!/usr/bin/env python3
import argparse
import os
import shutil
import sys
from docx import Document


def setup_folder(conf: dict[str, str]) -> str:
    dst = conf['漏洞名称']
    src = 'template/generic/'
    shutil.copytree(src, dst)
    docpath = dst + f'/{dst}.docx'
    shutil.move(dst + '/name.docx', docpath)
    shutil.move(dst + '/attachment.zip', dst + f'/{dst}.zip')
    with open(dst + '/email.txt', 'w') as f:
        f.write(conf['联系方式'])
    return docpath


def read_conf(confname: str, only_tuple=True) -> dict:
    sys.path.append('conf')
    confmod = __import__(confname)
    keynames = [item for item in dir(confmod) if not item.startswith("__")]
    dic = {key: getattr(confmod, key) for key in keynames}
    if only_tuple:
        dic = {v[0]: v[1] for v in dic.values() if isinstance(v, tuple)}
    return dic


def modify_doc(docpath: str, conf: dict[str, str]) -> str:
    doc = Document(docpath)
    table = doc.tables[0]
    for row in table.rows:
        key = row.cells[0].text
        if key in conf:
            row.cells[1].text = conf.pop(key)
    doc.save(docpath)
    return os.path.dirname(docpath)


def gen_cve_js(conf: dict[str, str], savedir=None) -> str:
    cmds = []
    VALUE_BY_ID = 'document.querySelector("[id*={key}]").value = {value};'
    CHECK_BY_VALUE = 'document.querySelector("[type=checkbox][value={value}]").click();'
    for key, value in conf.items():
        if key.startswith('TextBox') or key.startswith('DropDownList'):
            cmds.append(VALUE_BY_ID.format(key=key, value=repr(value)))
        elif key.startswith('CheckBoxList'):
            cmds.append(CHECK_BY_VALUE.format(value=repr(value)))
    cmdstr = '\n'.join(cmds)
    if savedir:
        savepath = os.path.join(savedir, 'cve.js')
        with open(savepath, 'w') as f:
            f.write(cmdstr)
    return cmdstr


def gen_cnvd_js(conf: dict[str, str], savedir=None) -> str:
    cmds = []
    VALUE_BY_ID = 'document.getElementById("{key}").value = {value};'
    for key, value in conf.items():
        if key.endswith('1'):
            cmds.append(VALUE_BY_ID.format(key=key, value=repr(value)))
    cmdstr = '\n'.join(cmds)
    if savedir:
        savepath = os.path.join(savedir, 'cnvd.js')
        with open(savepath, 'w') as f:
            f.write(cmdstr)
    return cmdstr


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CNVD helper')
    parser.add_argument('--conf', '-c', type=str,
                        default='example', help='配置文件名称')
    args = parser.parse_args()
    conf = read_conf(args.conf)
    docpath = setup_folder(conf)
    folder = modify_doc(docpath, conf)
    cve_js = gen_cve_js(conf, savedir=folder)
    print(cve_js)
    cnvd_js = gen_cnvd_js(conf, savedir=folder)
    print(cnvd_js)
