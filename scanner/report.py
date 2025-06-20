import json
from datetime import datetime


def generate_json_report(scan_data, output_file):
    report = {
        "scan_time": datetime.now().isoformat(),
        "hosts": []
    }

    for host in scan_data.get("scan", {}):
        host_info = {
            "ip": host,
            "status": scan_data["scan"][host].get("status", {}).get("state"),
            "open_ports": []
        }

        for proto in scan_data["scan"][host]:
            if proto in ["tcp", "udp"]:
                for port in scan_data["scan"][host][proto]:
                    port_data = scan_data["scan"][host][proto][port]
                    if port_data.get("state") == "open":
                        vulns = []
                        script_results = port_data.get("script", {})
                        for script_name, output in script_results.items():
                            vulns.append({
                                "script": script_name,
                                "output": output.strip()
                            })

                        host_info["open_ports"].append({
                            "port": port,
                            "protocol": proto,
                            "service": port_data.get("name"),
                            "product": port_data.get("product"),
                            "version": port_data.get("version"),
                            "vulnerabilities": vulns
                        })

        report["hosts"].append(host_info)

    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)

    print(f"[+] Report saved to: {output_file}")