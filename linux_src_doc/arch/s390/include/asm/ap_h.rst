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

.. _`ap_instructions_available`:

ap_instructions_available
=========================

.. c:function:: bool ap_instructions_available( void)

    Test if AP instructions are available.

    :param void:
        no arguments
    :type void: 

.. _`ap_instructions_available.description`:

Description
-----------

Returns true if the AP instructions are installed, otherwise false.

.. _`ap_tapq`:

ap_tapq
=======

.. c:function:: struct ap_queue_status ap_tapq(ap_qid_t qid, unsigned long *info)

    Test adjunct processor queue.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param info:
        Pointer to queue descriptor
    :type info: unsigned long \*

.. _`ap_tapq.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_test_queue`:

ap_test_queue
=============

.. c:function:: struct ap_queue_status ap_test_queue(ap_qid_t qid, int tbit, unsigned long *info)

    Test adjunct processor queue.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param tbit:
        Test facilities bit
    :type tbit: int

    :param info:
        Pointer to queue descriptor
    :type info: unsigned long \*

.. _`ap_test_queue.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_rapq`:

ap_rapq
=======

.. c:function:: struct ap_queue_status ap_rapq(ap_qid_t qid)

    Reset adjunct processor queue.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

.. _`ap_rapq.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_zapq`:

ap_zapq
=======

.. c:function:: struct ap_queue_status ap_zapq(ap_qid_t qid)

    Reset and zeroize adjunct processor queue.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

.. _`ap_zapq.description`:

Description
-----------

Returns AP queue status structure.

.. _`ap_config_info`:

struct ap_config_info
=====================

.. c:type:: struct ap_config_info

    convenience struct for AP crypto config info as returned by the \ :c:func:`ap_qci`\  function.

.. _`ap_config_info.definition`:

Definition
----------

.. code-block:: c

    struct ap_config_info {
        unsigned int apsc : 1;
        unsigned int apxa : 1;
        unsigned int qact : 1;
        unsigned int rc8a : 1;
        unsigned char _reserved1 : 4;
        unsigned char _reserved2[3];
        unsigned char Na;
        unsigned char Nd;
        unsigned char _reserved3[10];
        unsigned int apm[8];
        unsigned int aqm[8];
        unsigned int adm[8];
        unsigned char _reserved4[16];
    }

.. _`ap_config_info.members`:

Members
-------

apsc
    *undescribed*

apxa
    *undescribed*

qact
    *undescribed*

rc8a
    *undescribed*

\_reserved1
    *undescribed*

\_reserved2
    *undescribed*

Na
    *undescribed*

Nd
    *undescribed*

\_reserved3
    *undescribed*

apm
    *undescribed*

aqm
    *undescribed*

adm
    *undescribed*

\_reserved4
    *undescribed*

.. _`ap_qci`:

ap_qci
======

.. c:function:: int ap_qci(struct ap_config_info *config)

    Get AP configuration data

    :param config:
        *undescribed*
    :type config: struct ap_config_info \*

.. _`ap_qci.description`:

Description
-----------

Returns 0 on success, or -EOPNOTSUPP.

.. _`ap_aqic`:

ap_aqic
=======

.. c:function:: struct ap_queue_status ap_aqic(ap_qid_t qid, struct ap_qirq_ctrl qirqctrl, void *ind)

    Control interruption for a specific AP.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param qirqctrl:
        struct ap_qirq_ctrl (64 bit value)
    :type qirqctrl: struct ap_qirq_ctrl

    :param ind:
        The notification indicator byte
    :type ind: void \*

.. _`ap_aqic.description`:

Description
-----------

Returns AP queue status.

.. _`ap_qact`:

ap_qact
=======

.. c:function:: struct ap_queue_status ap_qact(ap_qid_t qid, int ifbit, union ap_qact_ap_info *apinfo)

    Query AP combatibility type.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param ifbit:
        *undescribed*
    :type ifbit: int

    :param apinfo:
        On input the info about the AP queue. On output the
        alternate AP queue info provided by the qact function
        in GR2 is stored in.
    :type apinfo: union ap_qact_ap_info \*

.. _`ap_qact.description`:

Description
-----------

Returns AP queue status. Check response_code field for failures.

.. _`ap_nqap`:

ap_nqap
=======

.. c:function:: struct ap_queue_status ap_nqap(ap_qid_t qid, unsigned long long psmid, void *msg, size_t length)

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

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param psmid:
        Pointer to program supplied message identifier
    :type psmid: unsigned long long \*

    :param msg:
        The message text
    :type msg: void \*

    :param length:
        The message length
    :type length: size_t

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

