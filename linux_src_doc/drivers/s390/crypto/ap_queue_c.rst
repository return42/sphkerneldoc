.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/ap_queue.c

.. _`ap_queue_enable_interruption`:

ap_queue_enable_interruption
============================

.. c:function:: int ap_queue_enable_interruption(struct ap_queue *aq, void *ind)

    Enable interruption on an AP queue.

    :param aq:
        *undescribed*
    :type aq: struct ap_queue \*

    :param ind:
        the notification indicator byte
    :type ind: void \*

.. _`ap_queue_enable_interruption.description`:

Description
-----------

Enables interruption on AP queue via \ :c:func:`ap_aqic`\ . Based on the return
value it waits a while and tests the AP queue if interrupts
have been switched on using \ :c:func:`ap_test_queue`\ .

.. _`__ap_send`:

\__ap_send
==========

.. c:function:: struct ap_queue_status __ap_send(ap_qid_t qid, unsigned long long psmid, void *msg, size_t length, unsigned int special)

    Send message to adjunct processor queue.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param psmid:
        The program supplied message identifier
    :type psmid: unsigned long long

    :param msg:
        The message text
    :type msg: void \*

    :param length:
        The message length
    :type length: size_t

    :param special:
        Special Bit
    :type special: unsigned int

.. _`__ap_send.description`:

Description
-----------

Returns AP queue status structure.
Condition code 1 on NQAP can't happen because the L bit is 1.
Condition code 2 on NQAP also means the send is incomplete,
because a segment boundary was reached. The NQAP is repeated.

.. _`ap_sm_recv`:

ap_sm_recv
==========

.. c:function:: struct ap_queue_status ap_sm_recv(struct ap_queue *aq)

    Receive pending reply messages from an AP queue but do not change the state of the device.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_recv.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT

.. _`ap_sm_read`:

ap_sm_read
==========

.. c:function:: enum ap_wait ap_sm_read(struct ap_queue *aq)

    Receive pending reply messages from an AP queue.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_read.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT

.. _`ap_sm_suspend_read`:

ap_sm_suspend_read
==================

.. c:function:: enum ap_wait ap_sm_suspend_read(struct ap_queue *aq)

    Receive pending reply messages from an AP queue without changing the device state in between. In suspend mode we don't allow sending new requests, therefore just fetch pending replies.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_suspend_read.description`:

Description
-----------

Returns AP_WAIT_NONE or AP_WAIT_AGAIN

.. _`ap_sm_write`:

ap_sm_write
===========

.. c:function:: enum ap_wait ap_sm_write(struct ap_queue *aq)

    Send messages from the request queue to an AP queue.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_write.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT

.. _`ap_sm_read_write`:

ap_sm_read_write
================

.. c:function:: enum ap_wait ap_sm_read_write(struct ap_queue *aq)

    Send and receive messages to/from an AP queue.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_read_write.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT

.. _`ap_sm_reset`:

ap_sm_reset
===========

.. c:function:: enum ap_wait ap_sm_reset(struct ap_queue *aq)

    Reset an AP queue.

    :param aq:
        *undescribed*
    :type aq: struct ap_queue \*

.. _`ap_sm_reset.description`:

Description
-----------

Submit the Reset command to an AP queue.

.. _`ap_sm_reset_wait`:

ap_sm_reset_wait
================

.. c:function:: enum ap_wait ap_sm_reset_wait(struct ap_queue *aq)

    Test queue for completion of the reset operation

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_reset_wait.description`:

Description
-----------

Returns AP_POLL_IMMEDIATELY, AP_POLL_AFTER_TIMEROUT or 0.

.. _`ap_sm_setirq_wait`:

ap_sm_setirq_wait
=================

.. c:function:: enum ap_wait ap_sm_setirq_wait(struct ap_queue *aq)

    Test queue for completion of the irq enablement

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`ap_sm_setirq_wait.description`:

Description
-----------

Returns AP_POLL_IMMEDIATELY, AP_POLL_AFTER_TIMEROUT or 0.

.. _`ap_queue_message`:

ap_queue_message
================

.. c:function:: void ap_queue_message(struct ap_queue *aq, struct ap_message *ap_msg)

    Queue a request to an AP device.

    :param aq:
        The AP device to queue the message to
    :type aq: struct ap_queue \*

    :param ap_msg:
        The message that is to be added
    :type ap_msg: struct ap_message \*

.. _`ap_cancel_message`:

ap_cancel_message
=================

.. c:function:: void ap_cancel_message(struct ap_queue *aq, struct ap_message *ap_msg)

    Cancel a crypto request.

    :param aq:
        The AP device that has the message queued
    :type aq: struct ap_queue \*

    :param ap_msg:
        The message that is to be removed
    :type ap_msg: struct ap_message \*

.. _`ap_cancel_message.description`:

Description
-----------

Cancel a crypto request. This is done by removing the request
from the device pending or request queue. Note that the
request stays on the AP queue. When it finishes the message
reply will be discarded because the psmid can't be found.

.. _`__ap_flush_queue`:

\__ap_flush_queue
=================

.. c:function:: void __ap_flush_queue(struct ap_queue *aq)

    Flush requests.

    :param aq:
        Pointer to the AP queue
    :type aq: struct ap_queue \*

.. _`__ap_flush_queue.description`:

Description
-----------

Flush all requests from the request/pending queue of an AP device.

.. This file was automatic generated / don't edit.

