#!/bin/sh

echo "Fixing permissions for /vault/data ..."
mkdir -p /vault/data
chmod -R 777 /vault/data

echo "Permissions fixed. Starting Vault ..."
exec vault server -config=/vault/config/vault-config.hcl
