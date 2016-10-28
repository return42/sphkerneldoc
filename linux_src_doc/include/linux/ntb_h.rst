.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ntb.h

.. _`ntb_topo`:

enum ntb_topo
=============

.. c:type:: enum ntb_topo

    NTB connection topology

.. _`ntb_topo.definition`:

Definition
----------

.. code-block:: c

    enum ntb_topo {
        NTB_TOPO_NONE,
        NTB_TOPO_PRI,
        NTB_TOPO_SEC,
        NTB_TOPO_B2B_USD,
        NTB_TOPO_B2B_DSD
    };

.. _`ntb_topo.constants`:

Constants
---------

NTB_TOPO_NONE
    Topology is unknown or invalid.

NTB_TOPO_PRI
    On primary side of local ntb.

NTB_TOPO_SEC
    On secondary side of remote ntb.

NTB_TOPO_B2B_USD
    On primary side of local ntb upstream of remote ntb.

NTB_TOPO_B2B_DSD
    On primary side of local ntb downstream of remote ntb.

.. _`ntb_speed`:

enum ntb_speed
==============

.. c:type:: enum ntb_speed

    NTB link training speed

.. _`ntb_speed.definition`:

Definition
----------

.. code-block:: c

    enum ntb_speed {
        NTB_SPEED_AUTO,
        NTB_SPEED_NONE,
        NTB_SPEED_GEN1,
        NTB_SPEED_GEN2,
        NTB_SPEED_GEN3
    };

.. _`ntb_speed.constants`:

Constants
---------

NTB_SPEED_AUTO
    Request the max supported speed.

NTB_SPEED_NONE
    Link is not trained to any speed.

NTB_SPEED_GEN1
    Link is trained to gen1 speed.

NTB_SPEED_GEN2
    Link is trained to gen2 speed.

NTB_SPEED_GEN3
    Link is trained to gen3 speed.

.. _`ntb_width`:

enum ntb_width
==============

.. c:type:: enum ntb_width

    NTB link training width

.. _`ntb_width.definition`:

Definition
----------

.. code-block:: c

    enum ntb_width {
        NTB_WIDTH_AUTO,
        NTB_WIDTH_NONE,
        NTB_WIDTH_1,
        NTB_WIDTH_2,
        NTB_WIDTH_4,
        NTB_WIDTH_8,
        NTB_WIDTH_12,
        NTB_WIDTH_16,
        NTB_WIDTH_32
    };

.. _`ntb_width.constants`:

Constants
---------

NTB_WIDTH_AUTO
    Request the max supported width.

NTB_WIDTH_NONE
    Link is not trained to any width.

NTB_WIDTH_1
    Link is trained to 1 lane width.

NTB_WIDTH_2
    Link is trained to 2 lane width.

NTB_WIDTH_4
    Link is trained to 4 lane width.

NTB_WIDTH_8
    Link is trained to 8 lane width.

NTB_WIDTH_12
    Link is trained to 12 lane width.

NTB_WIDTH_16
    Link is trained to 16 lane width.

NTB_WIDTH_32
    Link is trained to 32 lane width.

.. _`ntb_client_ops`:

struct ntb_client_ops
=====================

.. c:type:: struct ntb_client_ops

    ntb client operations

.. _`ntb_client_ops.definition`:

Definition
----------

.. code-block:: c

    struct ntb_client_ops {
        int (*probe)(struct ntb_client *client, struct ntb_dev *ntb);
        void (*remove)(struct ntb_client *client, struct ntb_dev *ntb);
    }

.. _`ntb_client_ops.members`:

Members
-------

probe
    Notify client of a new device.

remove
    Notify client to remove a device.

.. _`ntb_ctx_ops`:

struct ntb_ctx_ops
==================

.. c:type:: struct ntb_ctx_ops

    ntb driver context operations

.. _`ntb_ctx_ops.definition`:

Definition
----------

.. code-block:: c

    struct ntb_ctx_ops {
        void (*link_event)(void *ctx);
        void (*db_event)(void *ctx, int db_vector);
    }

.. _`ntb_ctx_ops.members`:

Members
-------

link_event
    See \ :c:func:`ntb_link_event`\ .

db_event
    See \ :c:func:`ntb_db_event`\ .

.. _`ntb_dev_ops`:

struct ntb_dev_ops
==================

.. c:type:: struct ntb_dev_ops

    ntb device operations

.. _`ntb_dev_ops.definition`:

Definition
----------

.. code-block:: c

    struct ntb_dev_ops {
        int (*mw_count)(struct ntb_dev *ntb);
        int (*mw_get_range)(struct ntb_dev *ntb, int idx,phys_addr_t *base, resource_size_t *size,resource_size_t *align, resource_size_t *align_size);
        int (*mw_set_trans)(struct ntb_dev *ntb, int idx,dma_addr_t addr, resource_size_t size);
        int (*mw_clear_trans)(struct ntb_dev *ntb, int idx);
        int (*link_is_up)(struct ntb_dev *ntb,enum ntb_speed *speed, enum ntb_width *width);
        int (*link_enable)(struct ntb_dev *ntb,enum ntb_speed max_speed, enum ntb_width max_width);
        int (*link_disable)(struct ntb_dev *ntb);
        int (*db_is_unsafe)(struct ntb_dev *ntb);
        u64 (*db_valid_mask)(struct ntb_dev *ntb);
        int (*db_vector_count)(struct ntb_dev *ntb);
        u64 (*db_vector_mask)(struct ntb_dev *ntb, int db_vector);
        u64 (*db_read)(struct ntb_dev *ntb);
        int (*db_set)(struct ntb_dev *ntb, u64 db_bits);
        int (*db_clear)(struct ntb_dev *ntb, u64 db_bits);
        u64 (*db_read_mask)(struct ntb_dev *ntb);
        int (*db_set_mask)(struct ntb_dev *ntb, u64 db_bits);
        int (*db_clear_mask)(struct ntb_dev *ntb, u64 db_bits);
        int (*peer_db_addr)(struct ntb_dev *ntb,phys_addr_t *db_addr, resource_size_t *db_size);
        u64 (*peer_db_read)(struct ntb_dev *ntb);
        int (*peer_db_set)(struct ntb_dev *ntb, u64 db_bits);
        int (*peer_db_clear)(struct ntb_dev *ntb, u64 db_bits);
        u64 (*peer_db_read_mask)(struct ntb_dev *ntb);
        int (*peer_db_set_mask)(struct ntb_dev *ntb, u64 db_bits);
        int (*peer_db_clear_mask)(struct ntb_dev *ntb, u64 db_bits);
        int (*spad_is_unsafe)(struct ntb_dev *ntb);
        int (*spad_count)(struct ntb_dev *ntb);
        u32 (*spad_read)(struct ntb_dev *ntb, int idx);
        int (*spad_write)(struct ntb_dev *ntb, int idx, u32 val);
        int (*peer_spad_addr)(struct ntb_dev *ntb, int idx,phys_addr_t *spad_addr);
        u32 (*peer_spad_read)(struct ntb_dev *ntb, int idx);
        int (*peer_spad_write)(struct ntb_dev *ntb, int idx, u32 val);
    }

.. _`ntb_dev_ops.members`:

Members
-------

mw_count
    See \ :c:func:`ntb_mw_count`\ .

mw_get_range
    See \ :c:func:`ntb_mw_get_range`\ .

mw_set_trans
    See \ :c:func:`ntb_mw_set_trans`\ .

mw_clear_trans
    See \ :c:func:`ntb_mw_clear_trans`\ .

link_is_up
    See \ :c:func:`ntb_link_is_up`\ .

link_enable
    See \ :c:func:`ntb_link_enable`\ .

link_disable
    See \ :c:func:`ntb_link_disable`\ .

db_is_unsafe
    See \ :c:func:`ntb_db_is_unsafe`\ .

db_valid_mask
    See \ :c:func:`ntb_db_valid_mask`\ .

db_vector_count
    See \ :c:func:`ntb_db_vector_count`\ .

db_vector_mask
    See \ :c:func:`ntb_db_vector_mask`\ .

db_read
    See \ :c:func:`ntb_db_read`\ .

db_set
    See \ :c:func:`ntb_db_set`\ .

db_clear
    See \ :c:func:`ntb_db_clear`\ .

db_read_mask
    See \ :c:func:`ntb_db_read_mask`\ .

db_set_mask
    See \ :c:func:`ntb_db_set_mask`\ .

db_clear_mask
    See \ :c:func:`ntb_db_clear_mask`\ .

peer_db_addr
    See \ :c:func:`ntb_peer_db_addr`\ .

peer_db_read
    See \ :c:func:`ntb_peer_db_read`\ .

peer_db_set
    See \ :c:func:`ntb_peer_db_set`\ .

peer_db_clear
    See \ :c:func:`ntb_peer_db_clear`\ .

peer_db_read_mask
    See \ :c:func:`ntb_peer_db_read_mask`\ .

peer_db_set_mask
    See \ :c:func:`ntb_peer_db_set_mask`\ .

peer_db_clear_mask
    See \ :c:func:`ntb_peer_db_clear_mask`\ .

spad_is_unsafe
    See \ :c:func:`ntb_spad_is_unsafe`\ .

spad_count
    See \ :c:func:`ntb_spad_count`\ .

spad_read
    See \ :c:func:`ntb_spad_read`\ .

spad_write
    See \ :c:func:`ntb_spad_write`\ .

peer_spad_addr
    See \ :c:func:`ntb_peer_spad_addr`\ .

peer_spad_read
    See \ :c:func:`ntb_peer_spad_read`\ .

peer_spad_write
    See \ :c:func:`ntb_peer_spad_write`\ .

.. _`ntb_client`:

struct ntb_client
=================

.. c:type:: struct ntb_client

    client interested in ntb devices

.. _`ntb_client.definition`:

Definition
----------

.. code-block:: c

    struct ntb_client {
        struct device_driver drv;
        const struct ntb_client_ops ops;
    }

.. _`ntb_client.members`:

Members
-------

drv
    Linux driver object.

ops
    See \ :c:type:`struct ntb_client_ops <ntb_client_ops>`.

.. _`ntb_dev`:

struct ntb_dev
==============

.. c:type:: struct ntb_dev

    ntb device

.. _`ntb_dev.definition`:

Definition
----------

.. code-block:: c

    struct ntb_dev {
        struct device dev;
        struct pci_dev *pdev;
        enum ntb_topo topo;
        const struct ntb_dev_ops *ops;
        void *ctx;
        const struct ntb_ctx_ops *ctx_ops;
    }

.. _`ntb_dev.members`:

Members
-------

dev
    Linux device object.

pdev
    Pci device entry of the ntb.

topo
    Detected topology of the ntb.

ops
    See \ :c:type:`struct ntb_dev_ops <ntb_dev_ops>`.

ctx
    See \ :c:type:`struct ntb_ctx_ops <ntb_ctx_ops>`.

ctx_ops
    See \ :c:type:`struct ntb_ctx_ops <ntb_ctx_ops>`.

.. _`ntb_register_client`:

ntb_register_client
===================

.. c:function::  ntb_register_client( client)

    register a client for interest in ntb devices

    :param  client:
        Client context.

.. _`ntb_register_client.description`:

Description
-----------

The client will be added to the list of clients interested in ntb devices.
The client will be notified of any ntb devices that are not already
associated with a client, or if ntb devices are registered later.

.. _`ntb_register_client.return`:

Return
------

Zero if the client is registered, otherwise an error number.

.. _`ntb_unregister_client`:

ntb_unregister_client
=====================

.. c:function:: void ntb_unregister_client(struct ntb_client *client)

    unregister a client for interest in ntb devices

    :param struct ntb_client \*client:
        Client context.

.. _`ntb_unregister_client.description`:

Description
-----------

The client will be removed from the list of clients interested in ntb
devices.  If any ntb devices are associated with the client, the client will
be notified to remove those devices.

.. _`ntb_register_device`:

ntb_register_device
===================

.. c:function:: int ntb_register_device(struct ntb_dev *ntb)

    register a ntb device

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_register_device.description`:

Description
-----------

The device will be added to the list of ntb devices.  If any clients are
interested in ntb devices, each client will be notified of the ntb device,
until at most one client accepts the device.

.. _`ntb_register_device.return`:

Return
------

Zero if the device is registered, otherwise an error number.

.. _`ntb_unregister_device`:

ntb_unregister_device
=====================

.. c:function:: void ntb_unregister_device(struct ntb_dev *ntb)

    unregister a ntb device

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_unregister_device.description`:

Description
-----------

The device will be removed from the list of ntb devices.  If the ntb device
is associated with a client, the client will be notified to remove the
device.

.. _`ntb_set_ctx`:

ntb_set_ctx
===========

.. c:function:: int ntb_set_ctx(struct ntb_dev *ntb, void *ctx, const struct ntb_ctx_ops *ctx_ops)

    associate a driver context with an ntb device

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param void \*ctx:
        Driver context.

    :param const struct ntb_ctx_ops \*ctx_ops:
        Driver context operations.

.. _`ntb_set_ctx.description`:

Description
-----------

Associate a driver context and operations with a ntb device.  The context is
provided by the client driver, and the driver may associate a different
context with each ntb device.

.. _`ntb_set_ctx.return`:

Return
------

Zero if the context is associated, otherwise an error number.

.. _`ntb_clear_ctx`:

ntb_clear_ctx
=============

.. c:function:: void ntb_clear_ctx(struct ntb_dev *ntb)

    disassociate any driver context from an ntb device

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_clear_ctx.description`:

Description
-----------

Clear any association that may exist between a driver context and the ntb
device.

.. _`ntb_link_event`:

ntb_link_event
==============

.. c:function:: void ntb_link_event(struct ntb_dev *ntb)

    notify driver context of a change in link status

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_link_event.description`:

Description
-----------

Notify the driver context that the link status may have changed.  The driver
should call \ :c:func:`ntb_link_is_up`\  to get the current status.

.. _`ntb_db_event`:

ntb_db_event
============

.. c:function:: void ntb_db_event(struct ntb_dev *ntb, int vector)

    notify driver context of a doorbell event

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int vector:
        Interrupt vector number.

.. _`ntb_db_event.description`:

Description
-----------

Notify the driver context of a doorbell event.  If hardware supports
multiple interrupt vectors for doorbells, the vector number indicates which
vector received the interrupt.  The vector number is relative to the first
vector used for doorbells, starting at zero, and must be less than
\* \ :c:func:`ntb_db_vector_count`\ .  The driver may call \ :c:func:`ntb_db_read`\  to check which
doorbell bits need service, and \ :c:func:`ntb_db_vector_mask`\  to determine which of
those bits are associated with the vector number.

.. _`ntb_mw_count`:

ntb_mw_count
============

.. c:function:: int ntb_mw_count(struct ntb_dev *ntb)

    get the number of memory windows

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_mw_count.description`:

Description
-----------

Hardware and topology may support a different number of memory windows.

.. _`ntb_mw_count.return`:

Return
------

the number of memory windows.

.. _`ntb_mw_get_range`:

ntb_mw_get_range
================

.. c:function:: int ntb_mw_get_range(struct ntb_dev *ntb, int idx, phys_addr_t *base, resource_size_t *size, resource_size_t *align, resource_size_t *align_size)

    get the range of a memory window

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Memory window number.

    :param phys_addr_t \*base:
        OUT - the base address for mapping the memory window

    :param resource_size_t \*size:
        OUT - the size for mapping the memory window

    :param resource_size_t \*align:
        OUT - the base alignment for translating the memory window

    :param resource_size_t \*align_size:
        OUT - the size alignment for translating the memory window

.. _`ntb_mw_get_range.description`:

Description
-----------

Get the range of a memory window.  NULL may be given for any output
parameter if the value is not needed.  The base and size may be used for
mapping the memory window, to access the peer memory.  The alignment and
size may be used for translating the memory window, for the peer to access
memory on the local system.

.. _`ntb_mw_get_range.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_mw_set_trans`:

ntb_mw_set_trans
================

.. c:function:: int ntb_mw_set_trans(struct ntb_dev *ntb, int idx, dma_addr_t addr, resource_size_t size)

    set the translation of a memory window

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Memory window number.

    :param dma_addr_t addr:
        The dma address local memory to expose to the peer.

    :param resource_size_t size:
        The size of the local memory to expose to the peer.

.. _`ntb_mw_set_trans.description`:

Description
-----------

Set the translation of a memory window.  The peer may access local memory
through the window starting at the address, up to the size.  The address
must be aligned to the alignment specified by \ :c:func:`ntb_mw_get_range`\ .  The size
must be aligned to the size alignment specified by \ :c:func:`ntb_mw_get_range`\ .

.. _`ntb_mw_set_trans.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_mw_clear_trans`:

ntb_mw_clear_trans
==================

.. c:function:: int ntb_mw_clear_trans(struct ntb_dev *ntb, int idx)

    clear the translation of a memory window

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Memory window number.

.. _`ntb_mw_clear_trans.description`:

Description
-----------

Clear the translation of a memory window.  The peer may no longer access
local memory through the window.

.. _`ntb_mw_clear_trans.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_link_is_up`:

ntb_link_is_up
==============

.. c:function:: int ntb_link_is_up(struct ntb_dev *ntb, enum ntb_speed *speed, enum ntb_width *width)

    get the current ntb link state

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param enum ntb_speed \*speed:
        OUT - The link speed expressed as PCIe generation number.

    :param enum ntb_width \*width:
        OUT - The link width expressed as the number of PCIe lanes.

.. _`ntb_link_is_up.description`:

Description
-----------

Get the current state of the ntb link.  It is recommended to query the link
state once after every link event.  It is safe to query the link state in
the context of the link event callback.

.. _`ntb_link_is_up.return`:

Return
------

One if the link is up, zero if the link is down, otherwise a
negative value indicating the error number.

.. _`ntb_link_enable`:

ntb_link_enable
===============

.. c:function:: int ntb_link_enable(struct ntb_dev *ntb, enum ntb_speed max_speed, enum ntb_width max_width)

    enable the link on the secondary side of the ntb

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param enum ntb_speed max_speed:
        The maximum link speed expressed as PCIe generation number.

    :param enum ntb_width max_width:
        The maximum link width expressed as the number of PCIe lanes.

.. _`ntb_link_enable.description`:

Description
-----------

Enable the link on the secondary side of the ntb.  This can only be done
from the primary side of the ntb in primary or b2b topology.  The ntb device
should train the link to its maximum speed and width, or the requested speed
and width, whichever is smaller, if supported.

.. _`ntb_link_enable.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_link_disable`:

ntb_link_disable
================

.. c:function:: int ntb_link_disable(struct ntb_dev *ntb)

    disable the link on the secondary side of the ntb

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_link_disable.description`:

Description
-----------

Disable the link on the secondary side of the ntb.  This can only be
done from the primary side of the ntb in primary or b2b topology.  The ntb
device should disable the link.  Returning from this call must indicate that
a barrier has passed, though with no more writes may pass in either
direction across the link, except if this call returns an error number.

.. _`ntb_link_disable.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_db_is_unsafe`:

ntb_db_is_unsafe
================

.. c:function:: int ntb_db_is_unsafe(struct ntb_dev *ntb)

    check if it is safe to use hardware doorbell

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_db_is_unsafe.description`:

Description
-----------

It is possible for some ntb hardware to be affected by errata.  Hardware
drivers can advise clients to avoid using doorbells.  Clients may ignore
this advice, though caution is recommended.

.. _`ntb_db_is_unsafe.return`:

Return
------

Zero if it is safe to use doorbells, or One if it is not safe.

.. _`ntb_db_valid_mask`:

ntb_db_valid_mask
=================

.. c:function:: u64 ntb_db_valid_mask(struct ntb_dev *ntb)

    get a mask of doorbell bits supported by the ntb

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_db_valid_mask.description`:

Description
-----------

Hardware may support different number or arrangement of doorbell bits.

.. _`ntb_db_valid_mask.return`:

Return
------

A mask of doorbell bits supported by the ntb.

.. _`ntb_db_vector_count`:

ntb_db_vector_count
===================

.. c:function:: int ntb_db_vector_count(struct ntb_dev *ntb)

    get the number of doorbell interrupt vectors

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_db_vector_count.description`:

Description
-----------

Hardware may support different number of interrupt vectors.

.. _`ntb_db_vector_count.return`:

Return
------

The number of doorbell interrupt vectors.

.. _`ntb_db_vector_mask`:

ntb_db_vector_mask
==================

.. c:function:: u64 ntb_db_vector_mask(struct ntb_dev *ntb, int vector)

    get a mask of doorbell bits serviced by a vector

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int vector:
        Doorbell vector number.

.. _`ntb_db_vector_mask.description`:

Description
-----------

Each interrupt vector may have a different number or arrangement of bits.

.. _`ntb_db_vector_mask.return`:

Return
------

A mask of doorbell bits serviced by a vector.

.. _`ntb_db_read`:

ntb_db_read
===========

.. c:function:: u64 ntb_db_read(struct ntb_dev *ntb)

    read the local doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_db_read.description`:

Description
-----------

Read the local doorbell register, and return the bits that are set.

.. _`ntb_db_read.return`:

Return
------

The bits currently set in the local doorbell register.

.. _`ntb_db_set`:

ntb_db_set
==========

.. c:function:: int ntb_db_set(struct ntb_dev *ntb, u64 db_bits)

    set bits in the local doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell bits to set.

.. _`ntb_db_set.description`:

Description
-----------

Set bits in the local doorbell register, which may generate a local doorbell
interrupt.  Bits that were already set must remain set.

This is unusual, and hardware may not support it.

.. _`ntb_db_set.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_db_clear`:

ntb_db_clear
============

.. c:function:: int ntb_db_clear(struct ntb_dev *ntb, u64 db_bits)

    clear bits in the local doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell bits to clear.

.. _`ntb_db_clear.description`:

Description
-----------

Clear bits in the local doorbell register, arming the bits for the next
doorbell.

.. _`ntb_db_clear.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_db_read_mask`:

ntb_db_read_mask
================

.. c:function:: u64 ntb_db_read_mask(struct ntb_dev *ntb)

    read the local doorbell mask

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_db_read_mask.description`:

Description
-----------

Read the local doorbell mask register, and return the bits that are set.

This is unusual, though hardware is likely to support it.

.. _`ntb_db_read_mask.return`:

Return
------

The bits currently set in the local doorbell mask register.

.. _`ntb_db_set_mask`:

ntb_db_set_mask
===============

.. c:function:: int ntb_db_set_mask(struct ntb_dev *ntb, u64 db_bits)

    set bits in the local doorbell mask

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell mask bits to set.

.. _`ntb_db_set_mask.description`:

Description
-----------

Set bits in the local doorbell mask register, preventing doorbell interrupts
from being generated for those doorbell bits.  Bits that were already set
must remain set.

.. _`ntb_db_set_mask.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_db_clear_mask`:

ntb_db_clear_mask
=================

.. c:function:: int ntb_db_clear_mask(struct ntb_dev *ntb, u64 db_bits)

    clear bits in the local doorbell mask

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell bits to clear.

.. _`ntb_db_clear_mask.description`:

Description
-----------

Clear bits in the local doorbell mask register, allowing doorbell interrupts
from being generated for those doorbell bits.  If a doorbell bit is already
set at the time the mask is cleared, and the corresponding mask bit is
changed from set to clear, then the ntb driver must ensure that
\ :c:func:`ntb_db_event`\  is called.  If the hardware does not generate the interrupt
on clearing the mask bit, then the driver must call \ :c:func:`ntb_db_event`\  anyway.

.. _`ntb_db_clear_mask.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_db_addr`:

ntb_peer_db_addr
================

.. c:function:: int ntb_peer_db_addr(struct ntb_dev *ntb, phys_addr_t *db_addr, resource_size_t *db_size)

    address and size of the peer doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param phys_addr_t \*db_addr:
        OUT - The address of the peer doorbell register.

    :param resource_size_t \*db_size:
        OUT - The number of bytes to write the peer doorbell register.

.. _`ntb_peer_db_addr.description`:

Description
-----------

Return the address of the peer doorbell register.  This may be used, for
example, by drivers that offload memory copy operations to a dma engine.
The drivers may wish to ring the peer doorbell at the completion of memory
copy operations.  For efficiency, and to simplify ordering of operations
between the dma memory copies and the ringing doorbell, the driver may
append one additional dma memory copy with the doorbell register as the
destination, after the memory copy operations.

.. _`ntb_peer_db_addr.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_db_read`:

ntb_peer_db_read
================

.. c:function:: u64 ntb_peer_db_read(struct ntb_dev *ntb)

    read the peer doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_peer_db_read.description`:

Description
-----------

Read the peer doorbell register, and return the bits that are set.

This is unusual, and hardware may not support it.

.. _`ntb_peer_db_read.return`:

Return
------

The bits currently set in the peer doorbell register.

.. _`ntb_peer_db_set`:

ntb_peer_db_set
===============

.. c:function:: int ntb_peer_db_set(struct ntb_dev *ntb, u64 db_bits)

    set bits in the peer doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell bits to set.

.. _`ntb_peer_db_set.description`:

Description
-----------

Set bits in the peer doorbell register, which may generate a peer doorbell
interrupt.  Bits that were already set must remain set.

.. _`ntb_peer_db_set.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_db_clear`:

ntb_peer_db_clear
=================

.. c:function:: int ntb_peer_db_clear(struct ntb_dev *ntb, u64 db_bits)

    clear bits in the peer doorbell register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell bits to clear.

.. _`ntb_peer_db_clear.description`:

Description
-----------

Clear bits in the peer doorbell register, arming the bits for the next
doorbell.

This is unusual, and hardware may not support it.

.. _`ntb_peer_db_clear.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_db_read_mask`:

ntb_peer_db_read_mask
=====================

.. c:function:: u64 ntb_peer_db_read_mask(struct ntb_dev *ntb)

    read the peer doorbell mask

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_peer_db_read_mask.description`:

Description
-----------

Read the peer doorbell mask register, and return the bits that are set.

This is unusual, and hardware may not support it.

.. _`ntb_peer_db_read_mask.return`:

Return
------

The bits currently set in the peer doorbell mask register.

.. _`ntb_peer_db_set_mask`:

ntb_peer_db_set_mask
====================

.. c:function:: int ntb_peer_db_set_mask(struct ntb_dev *ntb, u64 db_bits)

    set bits in the peer doorbell mask

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell mask bits to set.

.. _`ntb_peer_db_set_mask.description`:

Description
-----------

Set bits in the peer doorbell mask register, preventing doorbell interrupts
from being generated for those doorbell bits.  Bits that were already set
must remain set.

This is unusual, and hardware may not support it.

.. _`ntb_peer_db_set_mask.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_db_clear_mask`:

ntb_peer_db_clear_mask
======================

.. c:function:: int ntb_peer_db_clear_mask(struct ntb_dev *ntb, u64 db_bits)

    clear bits in the peer doorbell mask

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param u64 db_bits:
        Doorbell bits to clear.

.. _`ntb_peer_db_clear_mask.description`:

Description
-----------

Clear bits in the peer doorbell mask register, allowing doorbell interrupts
from being generated for those doorbell bits.  If the hardware does not
generate the interrupt on clearing the mask bit, then the driver should not
implement this function!

This is unusual, and hardware may not support it.

.. _`ntb_peer_db_clear_mask.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_spad_is_unsafe`:

ntb_spad_is_unsafe
==================

.. c:function:: int ntb_spad_is_unsafe(struct ntb_dev *ntb)

    check if it is safe to use the hardware scratchpads

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_spad_is_unsafe.description`:

Description
-----------

It is possible for some ntb hardware to be affected by errata.  Hardware
drivers can advise clients to avoid using scratchpads.  Clients may ignore
this advice, though caution is recommended.

.. _`ntb_spad_is_unsafe.return`:

Return
------

Zero if it is safe to use scratchpads, or One if it is not safe.

.. _`ntb_spad_count`:

ntb_spad_count
==============

.. c:function:: int ntb_spad_count(struct ntb_dev *ntb)

    get the number of scratchpads

    :param struct ntb_dev \*ntb:
        NTB device context.

.. _`ntb_spad_count.description`:

Description
-----------

Hardware and topology may support a different number of scratchpads.

.. _`ntb_spad_count.return`:

Return
------

the number of scratchpads.

.. _`ntb_spad_read`:

ntb_spad_read
=============

.. c:function:: u32 ntb_spad_read(struct ntb_dev *ntb, int idx)

    read the local scratchpad register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Scratchpad index.

.. _`ntb_spad_read.description`:

Description
-----------

Read the local scratchpad register, and return the value.

.. _`ntb_spad_read.return`:

Return
------

The value of the local scratchpad register.

.. _`ntb_spad_write`:

ntb_spad_write
==============

.. c:function:: int ntb_spad_write(struct ntb_dev *ntb, int idx, u32 val)

    write the local scratchpad register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Scratchpad index.

    :param u32 val:
        Scratchpad value.

.. _`ntb_spad_write.description`:

Description
-----------

Write the value to the local scratchpad register.

.. _`ntb_spad_write.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_spad_addr`:

ntb_peer_spad_addr
==================

.. c:function:: int ntb_peer_spad_addr(struct ntb_dev *ntb, int idx, phys_addr_t *spad_addr)

    address of the peer scratchpad register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Scratchpad index.

    :param phys_addr_t \*spad_addr:
        OUT - The address of the peer scratchpad register.

.. _`ntb_peer_spad_addr.description`:

Description
-----------

Return the address of the peer doorbell register.  This may be used, for
example, by drivers that offload memory copy operations to a dma engine.

.. _`ntb_peer_spad_addr.return`:

Return
------

Zero on success, otherwise an error number.

.. _`ntb_peer_spad_read`:

ntb_peer_spad_read
==================

.. c:function:: u32 ntb_peer_spad_read(struct ntb_dev *ntb, int idx)

    read the peer scratchpad register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Scratchpad index.

.. _`ntb_peer_spad_read.description`:

Description
-----------

Read the peer scratchpad register, and return the value.

.. _`ntb_peer_spad_read.return`:

Return
------

The value of the local scratchpad register.

.. _`ntb_peer_spad_write`:

ntb_peer_spad_write
===================

.. c:function:: int ntb_peer_spad_write(struct ntb_dev *ntb, int idx, u32 val)

    write the peer scratchpad register

    :param struct ntb_dev \*ntb:
        NTB device context.

    :param int idx:
        Scratchpad index.

    :param u32 val:
        Scratchpad value.

.. _`ntb_peer_spad_write.description`:

Description
-----------

Write the value to the peer scratchpad register.

.. _`ntb_peer_spad_write.return`:

Return
------

Zero on success, otherwise an error number.

.. This file was automatic generated / don't edit.

