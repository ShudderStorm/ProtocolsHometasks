import subprocess


class TraceRoute:
    def __init__(self, destination):
        self.destination = destination
        self.ip_path = []

    def execute(self):
        try:
            trace_router = subprocess.run(
                ['tracert', self.destination],
                capture_output=True,
                text=True
            )

            return trace_router.stdout

        except Exception as ex:
            print(ex)
