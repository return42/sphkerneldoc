.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/src.c

.. _`aac_src_disable_interrupt`:

aac_src_disable_interrupt
=========================

.. c:function:: void aac_src_disable_interrupt(struct aac_dev *dev)

    Disable interrupts

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

.. _`aac_src_enable_interrupt_message`:

aac_src_enable_interrupt_message
================================

.. c:function:: void aac_src_enable_interrupt_message(struct aac_dev *dev)

    Enable interrupts

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

.. _`src_sync_cmd`:

src_sync_cmd
============

.. c:function:: int src_sync_cmd(struct aac_dev *dev, u32 command, u32 p1, u32 p2, u32 p3, u32 p4, u32 p5, u32 p6, u32 *status, u32 *r1, u32 *r2, u32 *r3, u32 *r4)

    send a command and wait

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param command:
        Command to execute
    :type command: u32

    :param p1:
        first parameter
    :type p1: u32

    :param p2:
        *undescribed*
    :type p2: u32

    :param p3:
        *undescribed*
    :type p3: u32

    :param p4:
        *undescribed*
    :type p4: u32

    :param p5:
        *undescribed*
    :type p5: u32

    :param p6:
        *undescribed*
    :type p6: u32

    :param status:
        *undescribed*
    :type status: u32 \*

    :param r1:
        *undescribed*
    :type r1: u32 \*

    :param r2:
        *undescribed*
    :type r2: u32 \*

    :param r3:
        *undescribed*
    :type r3: u32 \*

    :param r4:
        *undescribed*
    :type r4: u32 \*

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

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

.. _`aac_src_interrupt_adapter.description`:

Description
-----------

Send an interrupt to the i960 and breakpoint it.

.. _`aac_src_notify_adapter`:

aac_src_notify_adapter
======================

.. c:function:: void aac_src_notify_adapter(struct aac_dev *dev, u32 event)

    send an event to the adapter

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param event:
        Event to send
    :type event: u32

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

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

.. _`aac_src_start_adapter.description`:

Description
-----------

Start up processing on an i960 based AAC adapter

.. _`aac_src_check_health`:

aac_src_check_health
====================

.. c:function:: int aac_src_check_health(struct aac_dev *dev)

    :param dev:
        device to check if healthy
    :type dev: struct aac_dev \*

.. _`aac_src_check_health.description`:

Description
-----------

Will attempt to determine if the specified adapter is alive and
capable of handling requests, returning 0 if alive.

.. _`aac_src_deliver_message`:

aac_src_deliver_message
=======================

.. c:function:: int aac_src_deliver_message(struct fib *fib)

    :param fib:
        fib to issue
    :type fib: struct fib \*

.. _`aac_src_deliver_message.description`:

Description
-----------

Will send a fib, returning 0 if successful.

.. _`aac_src_ioremap`:

aac_src_ioremap
===============

.. c:function:: int aac_src_ioremap(struct aac_dev *dev, u32 size)

    :param dev:
        *undescribed*
    :type dev: struct aac_dev \*

    :param size:
        mapping resize request
    :type size: u32

.. _`aac_srcv_ioremap`:

aac_srcv_ioremap
================

.. c:function:: int aac_srcv_ioremap(struct aac_dev *dev, u32 size)

    :param dev:
        *undescribed*
    :type dev: struct aac_dev \*

    :param size:
        mapping resize request
    :type size: u32

.. _`aac_src_select_comm`:

aac_src_select_comm
===================

.. c:function:: int aac_src_select_comm(struct aac_dev *dev, int comm)

    Select communications method

    :param dev:
        Adapter
    :type dev: struct aac_dev \*

    :param comm:
        communications method
    :type comm: int

.. _`aac_src_init`:

aac_src_init
============

.. c:function:: int aac_src_init(struct aac_dev *dev)

    initialize an Cardinal Frey Bar card

    :param dev:
        device to configure
    :type dev: struct aac_dev \*

.. _`aac_src_soft_reset`:

aac_src_soft_reset
==================

.. c:function:: int aac_src_soft_reset(struct aac_dev *dev)

    perform soft reset to speed up access

    :param dev:
        device to configure
    :type dev: struct aac_dev \*

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

    :param dev:
        device to configure
    :type dev: struct aac_dev \*

.. This file was automatic generated / don't edit.

