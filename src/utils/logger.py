import logging

logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)