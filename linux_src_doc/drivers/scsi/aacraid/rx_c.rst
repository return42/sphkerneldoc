.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/rx.c

.. _`aac_rx_disable_interrupt`:

aac_rx_disable_interrupt
========================

.. c:function:: void aac_rx_disable_interrupt(struct aac_dev *dev)

    Disable interrupts

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_rx_enable_interrupt_producer`:

aac_rx_enable_interrupt_producer
================================

.. c:function:: void aac_rx_enable_interrupt_producer(struct aac_dev *dev)

    Enable interrupts

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_rx_enable_interrupt_message`:

aac_rx_enable_interrupt_message
===============================

.. c:function:: void aac_rx_enable_interrupt_message(struct aac_dev *dev)

    Enable interrupts

    :param struct aac_dev \*dev:
        Adapter

.. _`rx_sync_cmd`:

rx_sync_cmd
===========

.. c:function:: int rx_sync_cmd(struct aac_dev *dev, u32 command, u32 p1, u32 p2, u32 p3, u32 p4, u32 p5, u32 p6, u32 *status, u32 *r1, u32 *r2, u32 *r3, u32 *r4)

    send a command and wait

    :param struct aac_dev \*dev:
        Adapter

    :param u32 command:
        Command to execute

    :param u32 p1:
        first parameter

    :param u32 p2:
        *undescribed*

    :param u32 p3:
        *undescribed*

    :param u32 p4:
        *undescribed*

    :param u32 p5:
        *undescribed*

    :param u32 p6:
        *undescribed*

    :param u32 \*status:
        *undescribed*

    :param u32 \*r1:
        *undescribed*

    :param u32 \*r2:
        *undescribed*

    :param u32 \*r3:
        *undescribed*

    :param u32 \*r4:
        *undescribed*

.. _`rx_sync_cmd.description`:

Description
-----------

This routine will send a synchronous command to the adapter and wait
for its completion.

.. _`aac_rx_interrupt_adapter`:

aac_rx_interrupt_adapter
========================

.. c:function:: void aac_rx_interrupt_adapter(struct aac_dev *dev)

    interrupt adapter

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_rx_interrupt_adapter.description`:

Description
-----------

Send an interrupt to the i960 and breakpoint it.

.. _`aac_rx_notify_adapter`:

aac_rx_notify_adapter
=====================

.. c:function:: void aac_rx_notify_adapter(struct aac_dev *dev, u32 event)

    send an event to the adapter

    :param struct aac_dev \*dev:
        Adapter

    :param u32 event:
        Event to send

.. _`aac_rx_notify_adapter.description`:

Description
-----------

Notify the i960 that something it probably cares about has
happened.

.. _`aac_rx_start_adapter`:

aac_rx_start_adapter
====================

.. c:function:: void aac_rx_start_adapter(struct aac_dev *dev)

    activate adapter

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_rx_start_adapter.description`:

Description
-----------

Start up processing on an i960 based AAC adapter

.. _`aac_rx_check_health`:

aac_rx_check_health
===================

.. c:function:: int aac_rx_check_health(struct aac_dev *dev)

    :param struct aac_dev \*dev:
        device to check if healthy

.. _`aac_rx_check_health.description`:

Description
-----------

Will attempt to determine if the specified adapter is alive and
capable of handling requests, returning 0 if alive.

.. _`aac_rx_deliver_producer`:

aac_rx_deliver_producer
=======================

.. c:function:: int aac_rx_deliver_producer(struct fib *fib)

    :param struct fib \*fib:
        fib to issue

.. _`aac_rx_deliver_producer.description`:

Description
-----------

Will send a fib, returning 0 if successful.

.. _`aac_rx_deliver_message`:

aac_rx_deliver_message
======================

.. c:function:: int aac_rx_deliver_message(struct fib *fib)

    :param struct fib \*fib:
        fib to issue

.. _`aac_rx_deliver_message.description`:

Description
-----------

Will send a fib, returning 0 if successful.

.. _`aac_rx_ioremap`:

aac_rx_ioremap
==============

.. c:function:: int aac_rx_ioremap(struct aac_dev *dev, u32 size)

    :param struct aac_dev \*dev:
        *undescribed*

    :param u32 size:
        mapping resize request

.. _`aac_rx_select_comm`:

aac_rx_select_comm
==================

.. c:function:: int aac_rx_select_comm(struct aac_dev *dev, int comm)

    Select communications method

    :param struct aac_dev \*dev:
        Adapter

    :param int comm:
        communications method

.. _`_aac_rx_init`:

\_aac_rx_init
=============

.. c:function:: int _aac_rx_init(struct aac_dev *dev)

    initialize an i960 based AAC card

    :param struct aac_dev \*dev:
        device to configure

.. _`_aac_rx_init.description`:

Description
-----------

Allocate and set up resources for the i960 based AAC variants. The
device_interface in the commregion will be allocated and linked
to the comm region.

.. This file was automatic generated / don't edit.

