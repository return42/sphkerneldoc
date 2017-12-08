.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dpaa2-io.h

.. _`dpio-service`:

DPIO Service
============

The DPIO service provides APIs for users to interact with the datapath
by enqueueing and dequeing frame descriptors.

The following set of APIs can be used to enqueue and dequeue frames
as well as producing notification callbacks when data is available
for dequeue.

.. _`dpaa2_io_desc`:

struct dpaa2_io_desc
====================

.. c:type:: struct dpaa2_io_desc

    The DPIO descriptor

.. _`dpaa2_io_desc.definition`:

Definition
----------

.. code-block:: c

    struct dpaa2_io_desc {
        int receives_notifications;
        int has_8prio;
        int cpu;
        void *regs_cena;
        void *regs_cinh;
        int dpio_id;
        u32 qman_version;
    }

.. _`dpaa2_io_desc.members`:

Members
-------

receives_notifications
    Use notificaton mode. Non-zero if the DPIO
    has a channel.

has_8prio
    Set to non-zero for channel with 8 priority WQs.  Ignored
    unless receives_notification is TRUE.

cpu
    The cpu index that at least interrupt handlers will
    execute on.

regs_cena
    The cache enabled regs.

regs_cinh
    The cache inhibited regs

dpio_id
    The dpio index

qman_version
    The qman version

.. _`dpaa2_io_desc.description`:

Description
-----------

Describes the attributes and features of the DPIO object.

.. _`dpaa2_io_notification_ctx`:

struct dpaa2_io_notification_ctx
================================

.. c:type:: struct dpaa2_io_notification_ctx

    The DPIO notification context structure

.. _`dpaa2_io_notification_ctx.definition`:

Definition
----------

.. code-block:: c

    struct dpaa2_io_notification_ctx {
        void (*cb)(struct dpaa2_io_notification_ctx *);
        int is_cdan;
        u32 id;
        int desired_cpu;
        int dpio_id;
        u64 qman64;
        struct list_head node;
        void *dpio_private;
    }

.. _`dpaa2_io_notification_ctx.members`:

Members
-------

cb
    The callback to be invoked when the notification arrives

is_cdan
    Zero for FQDAN, non-zero for CDAN

id
    FQID or channel ID, needed for rearm

desired_cpu
    The cpu on which the notifications will show up. Use
    DPAA2_IO_ANY_CPU if don't care

dpio_id
    The dpio index

qman64
    The 64-bit context value shows up in the FQDAN/CDAN.

node
    The list node

dpio_private
    The dpio object internal to dpio_service

.. _`dpaa2_io_notification_ctx.description`:

Description
-----------

Used when a FQDAN/CDAN registration is made by drivers.

.. This file was automatic generated / don't edit.

