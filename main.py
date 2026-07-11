import time
import yaml
from utils.logger import get_logger
from utils.formatter import build_json_payload

def load_config(filepath="config/settings.yml"):
    try:
        with open(filepath, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {filepath}")
        exit(1)

def main():
    logger = get_logger("InventorySync")
    logger.info("Initializing regional inventory sync service...")
    
    config = load_config()
    
    if not config.get('endpoints'):
        logger.warning("No endpoints configured. Exiting.")
        return

    for endpoint in config['endpoints']:
        logger.info(f"Targeting endpoint pipeline: {endpoint['name']}")
        
        # Simulating data packaging and transmission
        payload = build_json_payload(endpoint['name'], status="sync_ready")
        logger.debug(f"Generated payload size: {len(payload)} bytes")
        
        time.sleep(1.5) # Simulating network latency
        logger.info(f"Successfully processed queue for {endpoint['name']}")

if __name__ == "__main__":
    main()
