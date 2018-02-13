.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/ap.h

.. _`ap_qid_t`:

typedef ap_qid_t
================

.. c:type:: typedef ap_qid_t

    If the AP facilities test (APFT) facility is available, card and queue index are 8 bit values, otherwise card index is 6 bit and queue index a 4 bit value.

.. _`ap_queue_status`:

struct ap_queue_status
======================

.. c:type:: struct ap_queue_status

    Holds the AP queue status.

.. _`ap_queue_status.definition`:

Definition
----------

.. code-block:: c

    struct ap_queue_status {
        unsigned int queue_empty : 1;
        unsigned int replies_waiting : 1;
        unsigned int queue_full : 1;
        unsigned int _pad1 : 4;
        unsigned int irq_enabled : 1;
        unsigned int response_code : 8;
        unsigned int _pad2 : 16;
    }

.. _`ap_queue_status.members`:

Members
-------

queue_empty
    Shows if queue is empty

replies_waiting
    Waiting replies

queue_full
    Is 1 if the queue is full

\_pad1
    *undescribed*

irq_enabled
    Shows if interrupts are enabled for the AP

response_code
    Holds the 8 bit response code

\_pad2
    *undescribed*

.. _`ap_queue_status.description`:

Description
-----------

The ap queue status word is returned by all three AP functions
(PQAP, NQAP and DQAP).  There's a set of flags in the first
byte, followed by a 1 byte response code.

.. _`ap_test_queue`:

ap_test_queue
=============

.. c:function:: struct ap_queue_status ap_test_queue(ap_qid_t qid, int tbit, unsigned long *info)

    Test adjunct processor queue.

    :param ap_qid_t qid:
        The AP queue number

    :param int tbit:
        Test facilities bit

    :param unsigned long \*info:
        Pointer to queue descriptor

.. _`ap_test_queue.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_queue_irq_ctrl`:

ap_queue_irq_ctrl
=================

.. c:function:: struct ap_queue_status ap_queue_irq_ctrl(ap_qid_t qid, struct ap_qirq_ctrl qirqctrl, void *ind)

    Control interruption on a AP queue.

    :param ap_qid_t qid:
        The AP queue number

    :param struct ap_qirq_ctrl qirqctrl:
        struct ap_qirq_ctrl, see above

    :param void \*ind:
        The notification indicator byte

.. _`ap_queue_irq_ctrl.description`:

Description
-----------

Returns AP queue status.

Control interruption on the given AP queue.
Just a simple wrapper function for the low level PQAP(AQIC)
instruction available for other kernel modules.

.. This file was automatic generated / don't edit.

