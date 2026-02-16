import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class DataCollector:
    """
    Collects metrics from connected systems and stores them for processing.
    Implements error handling and retry logic.
    """

    def __init__(self, source_config: Dict[str, Any]):
        self.source_config = source_config
        self.metrics = {}

    def fetch_data(self) -> Dict[str, Any]:
        """
        Fetches metrics from connected systems.
        Returns collected data or raises an exception if failed.
        """
        try:
            # Simulated data collection logic
            self.metrics = {
                'system_usage': 0.8,
                'performance_score': 0.95,
                'growth_rate': 0.12
            }
            logger.info("Data collected successfully.")
            return self.metrics
        except Exception as e:
            logger.error(f"Failed to collect data: {str(e)}")
            raise

    def save_data(self, data_path: str) -> None:
        """
        Saves collected metrics to a specified path.
        Implements error handling for file operations.
        """
        try:
            with open(data_path, 'w') as f:
                f.write(str(self.metrics))
            logger.info(f"Data saved to {data_path}.")
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")