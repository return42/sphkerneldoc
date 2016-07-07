.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/ap_bus.h

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
        unsigned int queue_empty:1;
        unsigned int replies_waiting:1;
        unsigned int queue_full:1;
        unsigned int pad1:4;
        unsigned int int_enabled:1;
        unsigned int response_code:8;
        unsigned int pad2:16;
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

pad1
    *undescribed*

int_enabled
    Shows if interrupts are enabled for the AP

response_code
    *undescribed*

pad2
    A 16 bit pad

.. _`ap_queue_status.description`:

Description
-----------

The ap queue status word is returned by all three AP functions
(PQAP, NQAP and DQAP).  There's a set of flags in the first
byte, followed by a 1 byte response code.

.. _`ap_init_message`:

ap_init_message
===============

.. c:function:: void ap_init_message(struct ap_message *ap_msg)

    Initialize ap_message. Initialize a message before using. Otherwise this might result in unexpected behaviour.

    :param struct ap_message \*ap_msg:
        *undescribed*

.. This file was automatic generated / don't edit.

