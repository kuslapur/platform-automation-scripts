server_name = "web-server-01"       # str
environment = "PROD"                # str
cpu_cores = 4                       # int
memory_gb = 16.0                    # float
application_status = "Running"      # str

is_production = environment.upper() == "PROD"  # bool

print("Server name:", server_name)
print("Environment:", environment)
print("CPU cores:", cpu_cores)
print("Memory (GB):", memory_gb)
print("Application status:", application_status)

if is_production:
    print("Server type: Production")
else:
    print("Server type: Non-production")