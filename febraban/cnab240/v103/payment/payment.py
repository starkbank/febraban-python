from cnab240.payment import Payment
from cnab240.v103.payment.header import Header
from cnab240.v103.payment.segmentA import SegmentA
from cnab240.v103.payment.trailer import Trailer


class PaymentV103(Payment):

    def __init__(self):
        Payment.__init__(self,
            header=Header(),
            segmentA=SegmentA(),
            trailer=Trailer()
        )