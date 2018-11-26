.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/dpcsup.c

.. _`aac_response_normal`:

aac_response_normal
===================

.. c:function:: unsigned int aac_response_normal(struct aac_queue *q)

    Handle command replies

    :param q:
        Queue to read from
    :type q: struct aac_queue \*

.. _`aac_response_normal.description`:

Description
-----------

This DPC routine will be run when the adapter interrupts us to let us
know there is a response on our normal priority queue. We will pull off
all QE there are and wake up all the waiters before exiting. We will
take a spinlock out on the queue before operating on it.

.. _`aac_command_normal`:

aac_command_normal
==================

.. c:function:: unsigned int aac_command_normal(struct aac_queue *q)

    handle commands

    :param q:
        queue to process
    :type q: struct aac_queue \*

.. _`aac_command_normal.description`:

Description
-----------

This DPC routine will be queued when the adapter interrupts us to
let us know there is a command on our normal priority queue. We will
pull off all QE there are and wake up all the waiters before exiting.
We will take a spinlock out on the queue before operating on it.

.. _`aac_intr_normal`:

aac_intr_normal
===============

.. c:function:: unsigned int aac_intr_normal(struct aac_dev *dev, u32 index, int isAif, int isFastResponse, struct hw_fib *aif_fib)

    Handle command replies

    :param dev:
        Device
    :type dev: struct aac_dev \*

    :param index:
        completion reference
    :type index: u32

    :param isAif:
        *undescribed*
    :type isAif: int

    :param isFastResponse:
        *undescribed*
    :type isFastResponse: int

    :param aif_fib:
        *undescribed*
    :type aif_fib: struct hw_fib \*

.. _`aac_intr_normal.description`:

Description
-----------

This DPC routine will be run when the adapter interrupts us to let us
know there is a response on our normal priority queue. We will pull off
all QE there are and wake up all the waiters before exiting.

.. This file was automatic generated / don't edit.

