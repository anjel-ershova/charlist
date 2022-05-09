from pytest import fixture
import logging
from personages.models import Personage

logger = logging.getLogger(__name__)

@fixture
def create_personage() -> Personage:
    pass