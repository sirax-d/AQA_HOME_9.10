from pathlib import Path


def path(picture_name):
    return str(Path(__file__).parent.joinpath(f'resources/{picture_name}'))