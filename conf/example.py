#!/usr/bin/env python3
from datetime import datetime

# 提交人员基本信息
from personal import institution, author, contact
date = '提交日期', datetime.now().strftime('%Y 年 %-m 月 %-d 日')

# CVE https://cveform.mitre.org/

email = 'TextBoxEmail', contact[1]

# [...document.getElementById('DropDownListVulnerabilityType').children].map(x => x.innerText).slice(1)
__vulntypes = ['Buffer Overflow', 'Cross Site Request Forgery (CSRF)', 'Cross Site Scripting (XSS)', 'Directory Traversal', 'Incorrect Access Control',
'Insecure Permissions', 'Integer Overflow', 'Missing SSL Certificate Validation', 'SQL Injection', 'XML External Entity (XXE)', 'Other or Unknown']
vulntype = 'DropDownListVulnerabilityType', __vulntypes[10]  # selectElem.value = 'vulntype'

vendor = 'TextBoxVendor', 'Please ensure vendor or product is not covered by another CNA'
product = 'TextBoxProdCodeBase', 'Product Name'
versions = 'TextBoxVersions', '8.4.2'

# [...document.querySelectorAll('[name*=CheckBoxListImpact]')].map(x => x.value)
__impacts = ['Code Execution', 'Information Disclosure', 'Denial of Service', 'Other', 'Escalation of Privileges']
impact = 'CheckBoxListImpact', __impacts[4]  # TODO: click multiple checkboxs

affected_components = 'TextBoxAffectedComponents', 'affected source code file, affected function, affected executable, etc.'
attack_vectors = 'TextBoxAttackVectors', '''What are the methods of exploitation?
Example: to exploit vulnerability, someone must open a crafted JPEG file.'''

# http://cveproject.github.io/docs/content/key-details-phrasing.pdf
desc = 'TextBoxOwnDescription', f'''{vulntype[1]} in {affected_components[1]} in \
{vendor[1]} {product[1]} {versions[1]} allows attacker to {impact[1]} via {attack_vectors[1]}.'''
discoverer = 'TextBoxDiscoverer', 'individual(s) or organization(s)'
references = 'TextBoxReferences', '''Please include one reference/URL per line including protocol and domain name, e.g.,
www.link.com
https://link.org
'''


# 漏洞基本信息
vul_name = '漏洞名称', 'APP存在XX漏洞'  # http://www.cnnvd.org.cn/web/wz/bzxqById.tag?id=4&mkid=4
affected_entity = '受影响实体版本号', f'{product} {versions}'
vul_type = '漏洞类型', '缓冲区错误（CWE-119）'  # http://www.cnnvd.org.cn/web/wz/bzxqById.tag?id=3&mkid=3
vul_level = '危害等级', '中危'  #  http://www.cnnvd.org.cn/web/wz/bzxqById.tag?id=2&mkid=2
vul_desc = '漏洞简介', """
[实体描述]
[漏洞描述]
[影响描述]
[实体下载地址]"""

# 漏洞验证
vul_loc = '漏洞定位', '[漏洞定位]'
vul_trigger = '漏洞触发条件', '[触发条件]'
vul_verify = '漏洞验证过程', '[漏洞验证过程应该包括完整的复现步骤及结果]'
