from ...payment import Payment
from .header import Header
from .segmentA import SegmentA
from .trailer import Trailer


class PaymentV83(Payment):

    def __init__(self):
        Payment.__init__(self,
            header=Header(),
            segmentA=SegmentA(),
            trailer=Trailer()
        )