.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_ddcb.c

.. _`queue_empty`:

queue_empty
===========

.. c:function:: int queue_empty(struct ddcb_queue *queue)

    :param struct ddcb_queue \*queue:
        *undescribed*

.. _`queue_empty.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`queue_empty.author`:

Author
------

Frank Haverkamp <haver@linux.vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt@de.ibm.com>

Michael Jung <mijung@gmx.net>

Michael Ruettger <michael@ibmra.de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 2 only)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`genwqe_crc16`:

genwqe_crc16
============

.. c:function:: u16 genwqe_crc16(const u8 *buff, size_t len, u16 init)

    Generate 16-bit crc as required for DDCBs

    :param const u8 \*buff:
        pointer to data buffer

    :param size_t len:
        length of data for calculation

    :param u16 init:
        initial crc (0xffff at start)

.. _`genwqe_crc16.description`:

Description
-----------

Polynomial = x^16 + x^12 + x^5 + 1   (0x1021)

.. _`genwqe_crc16.example`:

Example
-------

.. code-block:: c

    4 bytes 0x01 0x02 0x03 0x04 with init = 0xffff
             should result in a crc16 of 0x89c3


.. _`genwqe_crc16.return`:

Return
------

crc16 checksum in big endian format !

.. _`ddcb_requ_finished`:

ddcb_requ_finished
==================

.. c:function:: int ddcb_requ_finished(struct genwqe_dev *cd, struct ddcb_requ *req)

    Returns the hardware state of the associated DDCB

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

    :param struct ddcb_requ \*req:
        DDCB work request

.. _`ddcb_requ_finished.description`:

Description
-----------

Status of ddcb_requ mirrors this hardware state, but is copied in
the ddcb_requ on interrupt/polling function. The lowlevel code
should check the hardware state directly, the higher level code
should check the copy.

This function will also return true if the state of the queue is
not GENWQE_CARD_USED. This enables us to purge all DDCBs in the
shutdown case.

.. _`ret_ddcb_appended`:

RET_DDCB_APPENDED
=================

.. c:function::  RET_DDCB_APPENDED()

    Enqueue a DDCB

.. _`ret_ddcb_appended.description`:

Description
-----------

Start execution of DDCB by tapping or append to queue via NEXT
bit. This is done by an atomic 'compare and swap' instruction and
checking SHI and HSI of the previous DDCB.

This function must only be called with ddcb_lock held.

.. _`ret_ddcb_appended.return`:

Return
------

1 if new DDCB is appended to previous
2 if DDCB queue is tapped via register/simulation

.. _`copy_ddcb_results`:

copy_ddcb_results
=================

.. c:function:: void copy_ddcb_results(struct ddcb_requ *req, int ddcb_no)

    Copy output state from real DDCB to request

    :param struct ddcb_requ \*req:
        *undescribed*

    :param int ddcb_no:
        *undescribed*

.. _`copy_ddcb_results.description`:

Description
-----------

Copy DDCB ASV to request struct. There is no endian
conversion made, since data structure in ASV is still
unknown here.

.. _`copy_ddcb_results.this-is-needed-by`:

This is needed by
-----------------

- \ :c:func:`genwqe_purge_ddcb`\ 
- \ :c:func:`genwqe_check_ddcb_queue`\ 

.. _`genwqe_check_ddcb_queue`:

genwqe_check_ddcb_queue
=======================

.. c:function:: int genwqe_check_ddcb_queue(struct genwqe_dev *cd, struct ddcb_queue *queue)

    Checks DDCB queue for completed work equests.

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

    :param struct ddcb_queue \*queue:
        *undescribed*

.. _`genwqe_check_ddcb_queue.return`:

Return
------

Number of DDCBs which were finished

.. _`__genwqe_wait_ddcb`:

__genwqe_wait_ddcb
==================

.. c:function:: int __genwqe_wait_ddcb(struct genwqe_dev *cd, struct ddcb_requ *req)

    Waits until DDCB is completed

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

    :param struct ddcb_requ \*req:
        pointer to requsted DDCB parameters

.. _`__genwqe_wait_ddcb.description`:

Description
-----------

The Service Layer will update the RETC in DDCB when processing is
pending or done.

.. _`__genwqe_wait_ddcb.return`:

Return
------

> 0 remaining jiffies, DDCB completed
-ETIMEDOUT when timeout
-ERESTARTSYS when ^C
-EINVAL when unknown error condition

When an error is returned the called needs to ensure that
\ :c:func:`purge_ddcb`\  is being called to get the \ :c:type:`struct req <req>`\  removed from the
queue.

.. _`get_next_ddcb`:

get_next_ddcb
=============

.. c:function:: struct ddcb *get_next_ddcb(struct genwqe_dev *cd, struct ddcb_queue *queue, int *num)

    Get next available DDCB

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

    :param struct ddcb_queue \*queue:
        *undescribed*

    :param int \*num:
        *undescribed*

.. _`get_next_ddcb.description`:

Description
-----------

DDCB's content is completely cleared but presets for PRE and
SEQNUM. This function must only be called when ddcb_lock is held.

.. _`get_next_ddcb.return`:

Return
------

NULL if no empty DDCB available otherwise ptr to next DDCB.

.. _`__genwqe_purge_ddcb`:

__genwqe_purge_ddcb
===================

.. c:function:: int __genwqe_purge_ddcb(struct genwqe_dev *cd, struct ddcb_requ *req)

    Remove a DDCB from the workqueue

    :param struct genwqe_dev \*cd:
        genwqe device descriptor

    :param struct ddcb_requ \*req:
        DDCB request

.. _`__genwqe_purge_ddcb.description`:

Description
-----------

This will fail when the request was already FETCHED. In this case
we need to wait until it is finished. Else the DDCB can be
reused. This function also ensures that the request data structure
is removed from ddcb_req[].

Do not forget to call this function when \ :c:func:`genwqe_wait_ddcb`\  fails,
such that the request gets really removed from ddcb_req[].

.. _`__genwqe_purge_ddcb.return`:

Return
------

0 success

.. _`__genwqe_enqueue_ddcb`:

__genwqe_enqueue_ddcb
=====================

.. c:function:: int __genwqe_enqueue_ddcb(struct genwqe_dev *cd, struct ddcb_requ *req, unsigned int f_flags)

    Enqueue a DDCB

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

    :param struct ddcb_requ \*req:
        pointer to DDCB execution request

    :param unsigned int f_flags:
        file mode: blocking, non-blocking

.. _`__genwqe_enqueue_ddcb.return`:

Return
------

0 if enqueuing succeeded
-EIO if card is unusable/PCIe problems
-EBUSY if enqueuing failed

.. _`__genwqe_execute_raw_ddcb`:

__genwqe_execute_raw_ddcb
=========================

.. c:function:: int __genwqe_execute_raw_ddcb(struct genwqe_dev *cd, struct genwqe_ddcb_cmd *cmd, unsigned int f_flags)

    Setup and execute DDCB

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

    :param struct genwqe_ddcb_cmd \*cmd:
        *undescribed*

    :param unsigned int f_flags:
        file mode: blocking, non-blocking

.. _`genwqe_next_ddcb_ready`:

genwqe_next_ddcb_ready
======================

.. c:function:: int genwqe_next_ddcb_ready(struct genwqe_dev *cd)

    Figure out if the next DDCB is already finished

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_next_ddcb_ready.description`:

Description
-----------

We use this as condition for our wait-queue code.

.. _`genwqe_ddcbs_in_flight`:

genwqe_ddcbs_in_flight
======================

.. c:function:: int genwqe_ddcbs_in_flight(struct genwqe_dev *cd)

    Check how many DDCBs are in flight

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_ddcbs_in_flight.description`:

Description
-----------

Keep track on the number of DDCBs which ware currently in the
queue. This is needed for statistics as well as conditon if we want
to wait or better do polling in case of no interrupts available.

.. _`genwqe_card_thread`:

genwqe_card_thread
==================

.. c:function:: int genwqe_card_thread(void *data)

    Work thread for the DDCB queue

    :param void \*data:
        *undescribed*

.. _`genwqe_card_thread.description`:

Description
-----------

The idea is to check if there are DDCBs in processing. If there are
some finished DDCBs, we process them and wakeup the
requestors. Otherwise we give other processes time using
\ :c:func:`cond_resched`\ .

.. _`genwqe_setup_service_layer`:

genwqe_setup_service_layer
==========================

.. c:function:: int genwqe_setup_service_layer(struct genwqe_dev *cd)

    Setup DDCB queue

    :param struct genwqe_dev \*cd:
        pointer to genwqe device descriptor

.. _`genwqe_setup_service_layer.description`:

Description
-----------

Allocate DDCBs. Configure Service Layer Controller (SLC).

.. _`genwqe_setup_service_layer.return`:

Return
------

0 success

.. _`queue_wake_up_all`:

queue_wake_up_all
=================

.. c:function:: int queue_wake_up_all(struct genwqe_dev *cd)

    Handles fatal error case

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`queue_wake_up_all.description`:

Description
-----------

The PCI device got unusable and we have to stop all pending
requests as fast as we can. The code after this must purge the
DDCBs in question and ensure that all mappings are freed.

.. _`genwqe_finish_queue`:

genwqe_finish_queue
===================

.. c:function:: int genwqe_finish_queue(struct genwqe_dev *cd)

    Remove any genwqe devices and user-interfaces

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_finish_queue.description`:

Description
-----------

Relies on the pre-condition that there are no users of the card
device anymore e.g. with open file-descriptors.

This function must be robust enough to be called twice.

.. _`genwqe_release_service_layer`:

genwqe_release_service_layer
============================

.. c:function:: int genwqe_release_service_layer(struct genwqe_dev *cd)

    Shutdown DDCB queue

    :param struct genwqe_dev \*cd:
        genwqe device descriptor

.. _`genwqe_release_service_layer.description`:

Description
-----------

This function must be robust enough to be called twice.

.. This file was automatic generated / don't edit.

