from ...file import File
from .header import Header
from .trailer import Trailer


class FileV83(File):

    def __init__(self):
        File.__init__(self,
            header=Header(),
            trailer=Trailer()
        )