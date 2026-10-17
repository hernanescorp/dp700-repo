import json
import socket
import subprocess
from datetime import datetime, timezone

import psutil


def docker_query(arguments):
    result = subprocess.run(
        ["/usr/bin/sudo", "-n", "/usr/bin/docker", *arguments],
        capture_output=True,
        text=True,
        check=True,
        timeout=30,
    )

    return [
        json.loads(line)
        for line in result.stdout.splitlines()
        if line.strip()
    ]


def collect():
    containers = docker_query(["ps", "-a", "--format", "json"])
    stats = docker_query(["stats", "--no-stream", "--format", "json"])
    stats_by_name = {item["Name"]: item for item in stats}

    container_metrics = []

    for container in containers:
        name = container["Names"]
        usage = stats_by_name.get(name)

        container_metrics.append({
            "name": name,
            "state": container["State"],
            "status": container["Status"],
            "cpu_percent": (
                float(usage["CPUPerc"].rstrip("%"))
                if usage else None
            ),
            "memory_percent": (
                float(usage["MemPerc"].rstrip("%"))
                if usage else None
            ),
            "memory_usage": usage["MemUsage"] if usage else None,
            "network_io_total": usage["NetIO"] if usage else None,
            "block_io_total": usage["BlockIO"] if usage else None,
            "pids": int(usage["PIDs"]) if usage else None,
        })

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "schema_version": 1,
        "server": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "host": {
            "cpu_percent": cpu,
            "ram_percent": memory.percent,
            "ram_available_mb": round(memory.available / 1024**2, 2),
            "swap_used_mb": round(psutil.swap_memory().used / 1024**2, 2),
            "disk_used_percent": disk.percent,
            "disk_free_gb": round(disk.free / 1024**3, 2),
        },
        "containers": container_metrics,
    }


if __name__ == "__main__":
    try:
        print(json.dumps(collect(), indent=2))
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip()
        raise SystemExit(
            f"No se pudo consultar Docker: {detail}"
        ) from None
    except subprocess.TimeoutExpired:
        raise SystemExit(
            "Docker ha tardado más de 30 segundos en responder."
        ) from None
    except (ValueError, KeyError) as exc:
        raise SystemExit(
            f"Formato de respuesta inesperado: {exc}"
        ) from None