# Required for Docker
disable_mlock = true

storage "raft" {
  path    = "/vault/data"
  node_id = "node1"
}

listener "tcp" {
  address         = "0.0.0.0:8200"
  cluster_address = "0.0.0.0:8201"
  tls_disable     = true
}

# Required by Raft mode
api_addr     = "http://127.0.0.1:8200"
cluster_addr = "http://127.0.0.1:8201"

ui = true

telemetry {
  prometheus_retention_time = "30s"
  disable_hostname = true
}
