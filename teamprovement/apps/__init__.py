import os

current_dir = os.path.dirname(__file__)
__all__ = [d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d))]
