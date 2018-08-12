.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/src.c

.. _`aac_src_disable_interrupt`:

aac_src_disable_interrupt
=========================

.. c:function:: void aac_src_disable_interrupt(struct aac_dev *dev)

    Disable interrupts

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_src_enable_interrupt_message`:

aac_src_enable_interrupt_message
================================

.. c:function:: void aac_src_enable_interrupt_message(struct aac_dev *dev)

    Enable interrupts

    :param struct aac_dev \*dev:
        Adapter

.. _`src_sync_cmd`:

src_sync_cmd
============

.. c:function:: int src_sync_cmd(struct aac_dev *dev, u32 command, u32 p1, u32 p2, u32 p3, u32 p4, u32 p5, u32 p6, u32 *status, u32 *r1, u32 *r2, u32 *r3, u32 *r4)

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

.. _`src_sync_cmd.description`:

Description
-----------

This routine will send a synchronous command to the adapter and wait
for its completion.

.. _`aac_src_interrupt_adapter`:

aac_src_interrupt_adapter
=========================

.. c:function:: void aac_src_interrupt_adapter(struct aac_dev *dev)

    interrupt adapter

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_src_interrupt_adapter.description`:

Description
-----------

Send an interrupt to the i960 and breakpoint it.

.. _`aac_src_notify_adapter`:

aac_src_notify_adapter
======================

.. c:function:: void aac_src_notify_adapter(struct aac_dev *dev, u32 event)

    send an event to the adapter

    :param struct aac_dev \*dev:
        Adapter

    :param u32 event:
        Event to send

.. _`aac_src_notify_adapter.description`:

Description
-----------

Notify the i960 that something it probably cares about has
happened.

.. _`aac_src_start_adapter`:

aac_src_start_adapter
=====================

.. c:function:: void aac_src_start_adapter(struct aac_dev *dev)

    activate adapter

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_src_start_adapter.description`:

Description
-----------

Start up processing on an i960 based AAC adapter

.. _`aac_src_check_health`:

aac_src_check_health
====================

.. c:function:: int aac_src_check_health(struct aac_dev *dev)

    :param struct aac_dev \*dev:
        device to check if healthy

.. _`aac_src_check_health.description`:

Description
-----------

Will attempt to determine if the specified adapter is alive and
capable of handling requests, returning 0 if alive.

.. _`aac_src_deliver_message`:

aac_src_deliver_message
=======================

.. c:function:: int aac_src_deliver_message(struct fib *fib)

    :param struct fib \*fib:
        fib to issue

.. _`aac_src_deliver_message.description`:

Description
-----------

Will send a fib, returning 0 if successful.

.. _`aac_src_ioremap`:

aac_src_ioremap
===============

.. c:function:: int aac_src_ioremap(struct aac_dev *dev, u32 size)

    :param struct aac_dev \*dev:
        *undescribed*

    :param u32 size:
        mapping resize request

.. _`aac_srcv_ioremap`:

aac_srcv_ioremap
================

.. c:function:: int aac_srcv_ioremap(struct aac_dev *dev, u32 size)

    :param struct aac_dev \*dev:
        *undescribed*

    :param u32 size:
        mapping resize request

.. _`aac_src_select_comm`:

aac_src_select_comm
===================

.. c:function:: int aac_src_select_comm(struct aac_dev *dev, int comm)

    Select communications method

    :param struct aac_dev \*dev:
        Adapter

    :param int comm:
        communications method

.. _`aac_src_init`:

aac_src_init
============

.. c:function:: int aac_src_init(struct aac_dev *dev)

    initialize an Cardinal Frey Bar card

    :param struct aac_dev \*dev:
        device to configure

.. _`aac_src_soft_reset`:

aac_src_soft_reset
==================

.. c:function:: int aac_src_soft_reset(struct aac_dev *dev)

    perform soft reset to speed up access

    :param struct aac_dev \*dev:
        device to configure

.. _`aac_src_soft_reset.assumptions`:

Assumptions
-----------

That the controller is in a state where we can
bring it back to life with an init struct. We can only use
fast sync commands, as the timeout is 5 seconds.

.. _`aac_srcv_init`:

aac_srcv_init
=============

.. c:function:: int aac_srcv_init(struct aac_dev *dev)

    initialize an SRCv card

    :param struct aac_dev \*dev:
        device to configure

.. This file was automatic generated / don't edit.

