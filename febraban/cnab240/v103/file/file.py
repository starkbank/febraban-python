from cnab240.file import File
from cnab240.v103.file.header import Header
from cnab240.v103.file.trailer import Trailer


class FileV103(File):

    def __init__(self):
        File.__init__(self,
            header=Header(),
            trailer=Trailer()
        )