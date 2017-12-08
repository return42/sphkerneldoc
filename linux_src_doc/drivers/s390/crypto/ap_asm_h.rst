.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/ap_asm.h

.. _`ap_instructions_available`:

ap_instructions_available
=========================

.. c:function:: int ap_instructions_available( void)

    Test if AP instructions are available.

    :param  void:
        no arguments

.. _`ap_instructions_available.description`:

Description
-----------

Returns 0 if the AP instructions are installed.

.. _`ap_tapq`:

ap_tapq
=======

.. c:function:: struct ap_queue_status ap_tapq(ap_qid_t qid, unsigned long *info)

    Test adjunct processor queue.

    :param ap_qid_t qid:
        The AP queue number

    :param unsigned long \*info:
        Pointer to queue descriptor

.. _`ap_tapq.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_rapq`:

ap_rapq
=======

.. c:function:: struct ap_queue_status ap_rapq(ap_qid_t qid)

    Reset adjunct processor queue.

    :param ap_qid_t qid:
        The AP queue number

.. _`ap_rapq.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_aqic`:

ap_aqic
=======

.. c:function:: struct ap_queue_status ap_aqic(ap_qid_t qid, struct ap_qirq_ctrl qirqctrl, void *ind)

    Control interruption for a specific AP.

    :param ap_qid_t qid:
        The AP queue number

    :param struct ap_qirq_ctrl qirqctrl:
        struct ap_qirq_ctrl (64 bit value)

    :param void \*ind:
        The notification indicator byte

.. _`ap_aqic.description`:

Description
-----------

Returns AP queue status.

.. _`ap_qci`:

ap_qci
======

.. c:function:: int ap_qci(void *config)

    Get AP configuration data

    :param void \*config:
        *undescribed*

.. _`ap_qci.description`:

Description
-----------

Returns 0 on success, or -EOPNOTSUPP.

.. _`ap_qact`:

ap_qact
=======

.. c:function:: struct ap_queue_status ap_qact(ap_qid_t qid, int ifbit, union ap_qact_ap_info *apinfo)

    Query AP combatibility type.

    :param ap_qid_t qid:
        The AP queue number

    :param int ifbit:
        *undescribed*

    :param union ap_qact_ap_info \*apinfo:
        On input the info about the AP queue. On output the
        alternate AP queue info provided by the qact function
        in GR2 is stored in.

.. _`ap_qact.description`:

Description
-----------

Returns AP queue status. Check response_code field for failures.

.. _`ap_nqap`:

ap_nqap
=======

.. c:function:: struct ap_queue_status ap_nqap(ap_qid_t qid, unsigned long long psmid, void *msg, size_t length)

    Send message to adjunct processor queue.

    :param ap_qid_t qid:
        The AP queue number

    :param unsigned long long psmid:
        The program supplied message identifier

    :param void \*msg:
        The message text

    :param size_t length:
        The message length

.. _`ap_nqap.description`:

Description
-----------

Returns AP queue status structure.
Condition code 1 on NQAP can't happen because the L bit is 1.
Condition code 2 on NQAP also means the send is incomplete,
because a segment boundary was reached. The NQAP is repeated.

.. _`ap_dqap`:

ap_dqap
=======

.. c:function:: struct ap_queue_status ap_dqap(ap_qid_t qid, unsigned long long *psmid, void *msg, size_t length)

    Receive message from adjunct processor queue.

    :param ap_qid_t qid:
        The AP queue number

    :param unsigned long long \*psmid:
        Pointer to program supplied message identifier

    :param void \*msg:
        The message text

    :param size_t length:
        The message length

.. _`ap_dqap.description`:

Description
-----------

Returns AP queue status structure.
Condition code 1 on DQAP means the receive has taken place
but only partially.  The response is incomplete, hence the
DQAP is repeated.
Condition code 2 on DQAP also means the receive is incomplete,
this time because a segment boundary was reached. Again, the
DQAP is repeated.
Note that gpr2 is used by the DQAP instruction to keep track of
any 'residual' length, in case the instruction gets interrupted.
Hence it gets zeroed before the instruction.

.. This file was automatic generated / don't edit.

