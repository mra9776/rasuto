class Host:
    def __init__(self, ip: str, port: int, protocol: str, is_active: bool) -> None:
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.is_active = is_active

    @staticmethod
    def from_dict(data: dict):
        print("from_dict has called")
        return Host(data['url'], data['port'], data['protocol'], data['is_active'])

    def __repr__(self) -> str:
        return f"{self.ip}:{self.port}"
    def to_dict(self):
        return {
            "ip": self.ip,
            "port": self.port,
            "protocol": self.protocol,
            "is_active": self.is_active
        }
