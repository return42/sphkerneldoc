.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/sa.c

.. _`aac_sa_disable_interrupt`:

aac_sa_disable_interrupt
========================

.. c:function:: void aac_sa_disable_interrupt(struct aac_dev *dev)

    disable interrupt

    :param struct aac_dev \*dev:
        Which adapter to enable.

.. _`aac_sa_enable_interrupt`:

aac_sa_enable_interrupt
=======================

.. c:function:: void aac_sa_enable_interrupt(struct aac_dev *dev)

    enable interrupt

    :param struct aac_dev \*dev:
        Which adapter to enable.

.. _`aac_sa_notify_adapter`:

aac_sa_notify_adapter
=====================

.. c:function:: void aac_sa_notify_adapter(struct aac_dev *dev, u32 event)

    handle adapter notification

    :param struct aac_dev \*dev:
        Adapter that notification is for

    :param u32 event:
        Event to notidy

.. _`aac_sa_notify_adapter.description`:

Description
-----------

Notify the adapter of an event

.. _`sa_sync_cmd`:

sa_sync_cmd
===========

.. c:function:: int sa_sync_cmd(struct aac_dev *dev, u32 command, u32 p1, u32 p2, u32 p3, u32 p4, u32 p5, u32 p6, u32 *ret, u32 *r1, u32 *r2, u32 *r3, u32 *r4)

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

    :param u32 \*ret:
        adapter status

    :param u32 \*r1:
        *undescribed*

    :param u32 \*r2:
        *undescribed*

    :param u32 \*r3:
        *undescribed*

    :param u32 \*r4:
        *undescribed*

.. _`sa_sync_cmd.description`:

Description
-----------

This routine will send a synchronous command to the adapter and wait
for its completion.

.. _`aac_sa_interrupt_adapter`:

aac_sa_interrupt_adapter
========================

.. c:function:: void aac_sa_interrupt_adapter(struct aac_dev *dev)

    interrupt an adapter

    :param struct aac_dev \*dev:
        Which adapter to enable.

.. _`aac_sa_interrupt_adapter.description`:

Description
-----------

Breakpoint an adapter.

.. _`aac_sa_start_adapter`:

aac_sa_start_adapter
====================

.. c:function:: void aac_sa_start_adapter(struct aac_dev *dev)

    activate adapter

    :param struct aac_dev \*dev:
        Adapter

.. _`aac_sa_start_adapter.description`:

Description
-----------

Start up processing on an ARM based AAC adapter

.. _`aac_sa_check_health`:

aac_sa_check_health
===================

.. c:function:: int aac_sa_check_health(struct aac_dev *dev)

    :param struct aac_dev \*dev:
        device to check if healthy

.. _`aac_sa_check_health.description`:

Description
-----------

Will attempt to determine if the specified adapter is alive and
capable of handling requests, returning 0 if alive.

.. _`aac_sa_ioremap`:

aac_sa_ioremap
==============

.. c:function:: int aac_sa_ioremap(struct aac_dev *dev, u32 size)

    :param struct aac_dev \*dev:
        *undescribed*

    :param u32 size:
        mapping resize request

.. _`aac_sa_init`:

aac_sa_init
===========

.. c:function:: int aac_sa_init(struct aac_dev *dev)

    initialize an ARM based AAC card

    :param struct aac_dev \*dev:
        device to configure

.. _`aac_sa_init.description`:

Description
-----------

Allocate and set up resources for the ARM based AAC variants. The
device_interface in the commregion will be allocated and linked
to the comm region.

.. This file was automatic generated / don't edit.

