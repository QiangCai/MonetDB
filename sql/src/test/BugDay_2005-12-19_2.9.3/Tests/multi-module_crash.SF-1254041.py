import os, time

def main():
    srvcmd = '%s --dbname "%s" --dbinit "module(sql_server);module(mapi);module(monettime); mapi_start();"' % (os.getenv('MSERVER'),os.getenv('TSTDB'))
    srv = os.popen(srvcmd, 'w')
    time.sleep(10)                      # give server time to start
    cltcmd = os.getenv('MAPI_CLIENT')
    clt = os.popen(cltcmd, 'w')
    clt.close()
    srv.close()

main()
