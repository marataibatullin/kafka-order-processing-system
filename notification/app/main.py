import logging
import sys

from consumer import consume_notifications


logging.basicConfig( 
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

def process():
    for notification in consume_notifications():
        logger.info(f"Notification: {notification}")


if __name__ == "__main__":
    try:
        process()
    except Exception as e:
        logger.error(f"Critical error: {e}", exc_info=True)
        sys.exit(1)