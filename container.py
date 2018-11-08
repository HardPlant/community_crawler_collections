import docker
import atexit

class Docker_Container(object):
    """docstring for Redis."""
    def __init__(self, name):
        super(Docker_Container, self).__init__()
        self.client = docker.from_env()
        self.container = self.client.containers.run(name, detach="True")
        atexit.register(self.terminate)
    
    def terminate(self):
        self.container.stop()
        self.container.wait()
        self.container.remove()
