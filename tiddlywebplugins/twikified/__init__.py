__version__ = '0.1.1'

# for sake of making config calls clean, we import render
# into this space
from .render import render as twikified_render

# keep linters happy
render = twikified_render
