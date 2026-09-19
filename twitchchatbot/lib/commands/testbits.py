def testbits(user, args):
    bitsAmountTest = args[0]
    queueEvent = {}
    queueEvent = {
            'eventType' : 'electrical',
            'event'     : 'bits %s' % bitsAmountTest,
            'msg'       : 'Testing the Bits animation!'
    }

    return queueEvent
