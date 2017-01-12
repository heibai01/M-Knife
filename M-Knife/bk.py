#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow

log = None

def add_item(wf, title, subtitle):
    wf.add_item(title, subtitle, arg = title, valid = True)

def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`. Not so useful, as
    # the `wf` object created in `if __name__ ...` below is global.
    #
    # Your imports go here if you want to catch import errors (not a bad idea)
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    # import somemodule
    # import anothermodule
    # Get args from Workflow, already in normalized Unicode
    args = wf.args[0].split(' ')
    # Do stuff here ...

    # Add an item to Alfred feedback
    # add_item(wf, 'Test title', 'Test item subtitle')

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but Alfred won't be listening
    # any more...
    log.info(args)
    cmd = args[0]
    para = args[1]
    if(cmd == 'rand'):
        rand(wf, para)
    if(cmd == 'len'):
        add_item(wf, str(len(para)), u'字符串长度')
    if(cmd == 'lower'):
        add_item(wf, para.lower(), u'已转换的小写字母')
    if(cmd == 'upper'): 
        add_item(wf, para.upper(), u'已转换的大写字母')
    if(cmd == 'uuid'):
        uuidgen(wf, para)
    if(cmd == 'shiftuuid'):
        log.info('shiftuuid %s', para)
        print para.upper()
        
    wf.send_feedback()

def uuidgen(wf, para):
    import uuid
    add_item(wf, str(uuid.uuid1()), u'基于主机和当前时间')
    add_item(wf, str(uuid.uuid4()), u'随机UUID')

def rand(wf, size_str):
    import random, string
    size = int('8' if size_str == '' else size_str)
    log.info(size)
    if(size > 64 or size <= 0): size = 8
    def getRandom():
        intStr = ''
        count = 0
        while(count < 7):
            intStr += string.digits
            count += 1
        log.info(intStr)
        randomNum = ''.join(random.sample(intStr, size))
        return randomNum
    def getRandStr():
        # 小写大写字母共52个 + 数字10个 + 2个 共64个，即上限值
        str = string.ascii_letters + string.digits + 'a1'
        log.info(str)
        return ''.join(random.sample(str, size))
    def getRandMix():
        # 52+10+17=79个
        str = string.ascii_letters + string.digits + '[!@#$%^&*()-+=.,]'
        log.info(str)
        return ''.join(random.sample(str, size))
    add_item(wf, getRandom(), u'纯数字')
    add_item(wf, getRandStr(), u'大小写字母 + 数字')
    add_item(wf, getRandMix(), u'大小写字母 + 数字 + [!@#$%^&*()-+=.,"]')

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    log = wf.logger
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))

	