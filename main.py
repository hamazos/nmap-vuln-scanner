import argparse
from scanner.core import NmapScanner
from scanner.report import generate_json_report


def main():
    parser = argparse.ArgumentParser(description="Network Vulnerability Scanner using Nmap")
    parser.add_argument("-t", "--target", required=True, help="Target IP or CIDR range")
    parser.add_argument("--ports", default="22-100", help="Port range to scan (default: 22-100)")
    parser.add_argument("-o", "--output", default="report.json", help="Output JSON file")

    args = parser.parse_args()

    scanner = NmapScanner()
    raw_data = scanner.scan_target(args.target, args.ports)
    generate_json_report(scanner.scanner.scan(), args.output)


if __name__ == "__main__":
    main()