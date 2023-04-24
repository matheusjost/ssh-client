from paramiko import SSHClient
import paramiko
import socket

class SSH():
    def __init__(self, ip, port, user, pw):
        self.ip = ip
        self.port = port
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=ip, port=port, username=user, password=pw, allow_agent=False, timeout=3)

    def exec_cmd(self,cmd):
        try:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)
            if stderr.channel.recv_exit_status() != 0:
                return "CAIU NO ERRO", stderr.read().decode('ascii')
            else:
                return "CAIU NO OUTPUT", stdout.read().decode('ascii').strip("\n")
        except paramiko.AuthenticationException:
            return f'Não foi possível se autenticar no host {self.ip}'
        except paramiko.SSHException:
            return f'Não foi possível se conectar ao host {self.ip}'
        except TimeoutError:
            return f'Tempo limite esgotado ao tentar se conectar ao host {self.ip}'
        except Exception as e:
            return f'Ocorreu um erro ao tentar se conectar ao host {self.ip}: {e}'