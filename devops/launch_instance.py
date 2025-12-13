import boto3
import json
import time
from utils.logger import logging
from datetime import datetime, timezone

INSTANCE_TYPE = "t4g.nano"
PRODUCT_DESCRIPTION = "Linux/UNIX"

ec2_global = boto3.client("ec2", region_name="us-east-1")
regions = [
    r["RegionName"] for r in ec2_global.describe_regions(AllRegions=True)["Regions"]
]

lowest = None

for region in regions:
    try:
        ec2 = boto3.client("ec2", region_name=region)
        resp = ec2.describe_spot_price_history(
            InstanceTypes=[INSTANCE_TYPE],
            ProductDescriptions=[PRODUCT_DESCRIPTION],
            StartTime=datetime.now(timezone.utc),
            MaxResults=10,
        )

        for h in resp.get("SpotPriceHistory", []):
            price = float(h["SpotPrice"])
            if lowest is None or price < lowest["price_usd_per_hour"]:
                lowest = {
                    "instance_type": INSTANCE_TYPE,
                    "price_usd_per_hour": price,
                    "region": region,
                    "availability_zone": h["AvailabilityZone"],
                    "product": PRODUCT_DESCRIPTION,
                    "ipv6": True,
                    "elastic_ip": False,
                    "nat_gateway": False,
                    "timestamp": h["Timestamp"].isoformat(),
                }
    except Exception:
        continue

logging.info(json.dumps(lowest, indent=2))

region = lowest["region"]
az = lowest["availability_zone"]
instance_type = lowest["instance_type"]

ec2 = boto3.client("ec2", region_name=region)
ssm = boto3.client("ssm", region_name=region)

ami = ssm.get_parameter(
    Name="/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-arm64"
)["Parameter"]["Value"]

response = ec2.run_instances(
    ImageId=ami,
    InstanceType=instance_type,
    Placement={"AvailabilityZone": az},
    MinCount=1,
    MaxCount=1,
)

instance_id = response["Instances"][0]["InstanceId"]
logging.info(f"Instance lancée : {instance_id}")


time.sleep(10)

ec2.stop_instances(InstanceIds=[instance_id])
logging.info(f"Instance arrêtée : {instance_id}")
