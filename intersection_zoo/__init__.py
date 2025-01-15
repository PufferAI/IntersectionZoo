from pathlib import Path

# Absolute paths for loading resources
INTERSECTION_ZOO_PATH = Path('/'.join(__path__[0].split('/')[:-1]))
DATA_PATH = INTERSECTION_ZOO_PATH / 'dataset'
RESOURCES_PATH = INTERSECTION_ZOO_PATH / 'resources'

from .env.task_context import PathTaskContext, TaskContext
from .env.config import IntersectionZooEnvConfig
from .env.pz_environment import IntersectionZooPZEnv

