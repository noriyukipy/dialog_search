set -eu

HOST=$1
INDEX=$2

# Remove index
curl -XDELETE http://${HOST}/${INDEX}
echo ""