import nmap
from utils.helpers import SCRIPTS, parse_nmap_output


class NmapScanner:
    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan_target(self, target, ports="22-100"):
        script_list = ",".join(SCRIPTS)
        args = f"-p {ports} -sV --script={script_list}"
        print(f"[+] Scanning {target} with ports {ports}")
        self.scanner.scan(hosts=target, arguments=args)
        return parse_nmap_output(self.scanner.scaninfo())