#!/usr/bin/env python
def _ssh_run_remote_command(self, cmd):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.host,
                           username=self.config['ssh_user'],
                           password=self.config['ssh_password'])
        stdin, stdout, stderr = ssh_client.exec_command(uname -a)
        print(stdout)
        out = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        _ssh_run_remote_command("192.168.9.100, password")
        # if self.log_level:
        #     logger.info(out)
        # if error:
        #     raise Exception('There was an error pulling the runtime: {}'.format(error))
        # ssh_client.close()
        # return out