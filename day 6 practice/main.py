import cloud_tool

servers = [
    ["web-01", 81, 15, True],
    ["web-02", 16, 87, True],
    ["web-03", 45, 48, False],
    ["web-04",45,]
]

for server in servers:
    cloud_tool.server_check(server[0],server[1],server[2],server[3])