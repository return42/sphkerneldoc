.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/thunderbolt.h

.. _`tb_security_level`:

enum tb_security_level
======================

.. c:type:: enum tb_security_level

    Thunderbolt security level

.. _`tb_security_level.definition`:

Definition
----------

.. code-block:: c

    enum tb_security_level {
        TB_SECURITY_NONE,
        TB_SECURITY_USER,
        TB_SECURITY_SECURE,
        TB_SECURITY_DPONLY
    };

.. _`tb_security_level.constants`:

Constants
---------

TB_SECURITY_NONE
    No security, legacy mode

TB_SECURITY_USER
    User approval required at minimum

TB_SECURITY_SECURE
    One time saved key required at minimum

TB_SECURITY_DPONLY
    Only tunnel Display port (and USB)

.. _`tb`:

struct tb
=========

.. c:type:: struct tb

    main thunderbolt bus structure

.. _`tb.definition`:

Definition
----------

.. code-block:: c

    struct tb {
        struct device dev;
        struct mutex lock;
        struct tb_nhi *nhi;
        struct tb_ctl *ctl;
        struct workqueue_struct *wq;
        struct tb_switch *root_switch;
        const struct tb_cm_ops *cm_ops;
        int index;
        enum tb_security_level security_level;
        unsigned long privdata[0];
    }

.. _`tb.members`:

Members
-------

dev
    Domain device

lock
    Big lock. Must be held when accessing any struct
    tb_switch / struct tb_port.

nhi
    Pointer to the NHI structure

ctl
    Control channel for this domain

wq
    Ordered workqueue for all domain specific work

root_switch
    Root switch of this domain

cm_ops
    Connection manager specific operations vector

index
    Linux assigned domain number

security_level
    Current security level

privdata
    Private connection manager specific data

.. _`tb_property_dir`:

struct tb_property_dir
======================

.. c:type:: struct tb_property_dir

    XDomain property directory

.. _`tb_property_dir.definition`:

Definition
----------

.. code-block:: c

    struct tb_property_dir {
        const uuid_t *uuid;
        struct list_head properties;
    }

.. _`tb_property_dir.members`:

Members
-------

uuid
    Directory UUID or \ ``NULL``\  if root directory

properties
    List of properties in this directory

.. _`tb_property_dir.description`:

Description
-----------

User needs to provide serialization if needed.

.. _`tb_property`:

struct tb_property
==================

.. c:type:: struct tb_property

    XDomain property

.. _`tb_property.definition`:

Definition
----------

.. code-block:: c

    struct tb_property {
        struct list_head list;
        char key[TB_PROPERTY_KEY_SIZE + 1];
        enum tb_property_type type;
        size_t length;
        union {
            struct tb_property_dir *dir;
            u8 *data;
            char *text;
            u32 immediate;
        } value;
    }

.. _`tb_property.members`:

Members
-------

list
    Used to link properties together in a directory

key
    Key for the property (always terminated).

type
    Type of the property

length
    Length of the property data in dwords

value
    Property value

.. _`tb_property.description`:

Description
-----------

Users use \ ``type``\  to determine which field in \ ``value``\  is filled.

.. _`tb_xdomain`:

struct tb_xdomain
=================

.. c:type:: struct tb_xdomain

    Cross-domain (XDomain) connection

.. _`tb_xdomain.definition`:

Definition
----------

.. code-block:: c

    struct tb_xdomain {
        struct device dev;
        struct tb *tb;
        uuid_t *remote_uuid;
        const uuid_t *local_uuid;
        u64 route;
        u16 vendor;
        u16 device;
        struct mutex lock;
        const char *vendor_name;
        const char *device_name;
        bool is_unplugged;
        bool resume;
        u16 transmit_path;
        u16 transmit_ring;
        u16 receive_path;
        u16 receive_ring;
        struct ida service_ids;
        struct tb_property_dir *properties;
        u32 property_block_gen;
        struct delayed_work get_properties_work;
        int properties_retries;
        struct delayed_work properties_changed_work;
        int properties_changed_retries;
        u8 link;
        u8 depth;
    }

.. _`tb_xdomain.members`:

Members
-------

dev
    XDomain device

tb
    Pointer to the domain

remote_uuid
    UUID of the remote domain (host)

local_uuid
    Cached local UUID

route
    Route string the other domain can be reached

vendor
    Vendor ID of the remote domain

device
    Device ID of the demote domain

lock
    Lock to serialize access to the following fields of this structure

vendor_name
    Name of the vendor (or \ ``NULL``\  if not known)

device_name
    Name of the device (or \ ``NULL``\  if not known)

is_unplugged
    The XDomain is unplugged

resume
    The XDomain is being resumed

transmit_path
    HopID which the remote end expects us to transmit

transmit_ring
    Local ring (hop) where outgoing packets are pushed

receive_path
    HopID which we expect the remote end to transmit

receive_ring
    Local ring (hop) where incoming packets arrive

service_ids
    Used to generate IDs for the services

properties
    Properties exported by the remote domain

property_block_gen
    Generation of \ ``properties``\ 

get_properties_work
    Work used to get remote domain properties

properties_retries
    Number of times left to read properties

properties_changed_work
    Work used to notify the remote domain that
    our properties have changed

properties_changed_retries
    Number of times left to send properties
    changed notification

link
    Root switch link the remote domain is connected (ICM only)

depth
    Depth in the chain the remote domain is connected (ICM only)

.. _`tb_xdomain.description`:

Description
-----------

This structure represents connection across two domains (hosts).
Each XDomain contains zero or more services which are exposed as
\ :c:type:`struct tb_service <tb_service>`\  objects.

Service drivers may access this structure if they need to enumerate
non-standard properties but they need hold \ ``lock``\  when doing so
because properties can be changed asynchronously in response to
changes in the remote domain.

.. _`tb_service`:

struct tb_service
=================

.. c:type:: struct tb_service

    Thunderbolt service

.. _`tb_service.definition`:

Definition
----------

.. code-block:: c

    struct tb_service {
        struct device dev;
        int id;
        const char *key;
        u32 prtcid;
        u32 prtcvers;
        u32 prtcrevs;
        u32 prtcstns;
    }

.. _`tb_service.members`:

Members
-------

dev
    XDomain device

id
    ID of the service (shown in sysfs)

key
    Protocol key from the properties directory

prtcid
    Protocol ID from the properties directory

prtcvers
    Protocol version from the properties directory

prtcrevs
    Protocol software revision from the properties directory

prtcstns
    Protocol settings mask from the properties directory

.. _`tb_service.description`:

Description
-----------

Each domain exposes set of services it supports as collection of
properties. For each service there will be one corresponding
\ :c:type:`struct tb_service <tb_service>`\ . Service drivers are bound to these.

.. _`tb_nhi`:

struct tb_nhi
=============

.. c:type:: struct tb_nhi

    thunderbolt native host interface

.. _`tb_nhi.definition`:

Definition
----------

.. code-block:: c

    struct tb_nhi {
        spinlock_t lock;
        struct pci_dev *pdev;
        void __iomem *iobase;
        struct tb_ring **tx_rings;
        struct tb_ring **rx_rings;
        struct ida msix_ida;
        bool going_away;
        struct work_struct interrupt_work;
        u32 hop_count;
    }

.. _`tb_nhi.members`:

Members
-------

lock
    Must be held during ring creation/destruction. Is acquired by
    interrupt_work when dispatching interrupts to individual rings.

pdev
    Pointer to the PCI device

iobase
    MMIO space of the NHI

tx_rings
    All Tx rings available on this host controller

rx_rings
    All Rx rings available on this host controller

msix_ida
    Used to allocate MSI-X vectors for rings

going_away
    The host controller device is about to disappear so when
    this flag is set, avoid touching the hardware anymore.

interrupt_work
    Work scheduled to handle ring interrupt when no
    MSI-X is used.

hop_count
    Number of rings (end point hops) supported by NHI.

.. _`tb_ring`:

struct tb_ring
==============

.. c:type:: struct tb_ring

    thunderbolt TX or RX ring associated with a NHI

.. _`tb_ring.definition`:

Definition
----------

.. code-block:: c

    struct tb_ring {
        spinlock_t lock;
        struct tb_nhi *nhi;
        int size;
        int hop;
        int head;
        int tail;
        struct ring_desc *descriptors;
        dma_addr_t descriptors_dma;
        struct list_head queue;
        struct list_head in_flight;
        struct work_struct work;
        bool is_tx:1;
        bool running:1;
        int irq;
        u8 vector;
        unsigned int flags;
        u16 sof_mask;
        u16 eof_mask;
        void (*start_poll)(void *data);
        void *poll_data;
    }

.. _`tb_ring.members`:

Members
-------

lock
    Lock serializing actions to this ring. Must be acquired after
    nhi->lock.

nhi
    Pointer to the native host controller interface

size
    Size of the ring

hop
    Hop (DMA channel) associated with this ring

head
    Head of the ring (write next descriptor here)

tail
    Tail of the ring (complete next descriptor here)

descriptors
    Allocated descriptors for this ring

descriptors_dma
    *undescribed*

queue
    Queue holding frames to be transferred over this ring

in_flight
    Queue holding frames that are currently in flight

work
    Interrupt work structure

is_tx
    Is the ring Tx or Rx

running
    Is the ring running

irq
    MSI-X irq number if the ring uses MSI-X. \ ``0``\  otherwise.

vector
    MSI-X vector number the ring uses (only set if \ ``irq``\  is > 0)

flags
    Ring specific flags

sof_mask
    Bit mask used to detect start of frame PDF

eof_mask
    Bit mask used to detect end of frame PDF

start_poll
    Called when ring interrupt is triggered to start
    polling. Passing \ ``NULL``\  keeps the ring in interrupt mode.

poll_data
    Data passed to \ ``start_poll``\ 

.. _`ring_desc_flags`:

enum ring_desc_flags
====================

.. c:type:: enum ring_desc_flags

    Flags for DMA ring descriptor \ ``RING_DESC_ISOCH``\ : Enable isonchronous DMA (Tx only) \ ``RING_DESC_CRC_ERROR``\ : In frame mode CRC check failed for the frame (Rx only) \ ``RING_DESC_COMPLETED``\ : Descriptor completed (set by NHI) \ ``RING_DESC_POSTED``\ : Always set this \ ``RING_DESC_BUFFER_OVERRUN``\ : RX buffer overrun \ ``RING_DESC_INTERRUPT``\ : Request an interrupt on completion

.. _`ring_desc_flags.definition`:

Definition
----------

.. code-block:: c

    enum ring_desc_flags {
        RING_DESC_ISOCH,
        RING_DESC_CRC_ERROR,
        RING_DESC_COMPLETED,
        RING_DESC_POSTED,
        RING_DESC_BUFFER_OVERRUN,
        RING_DESC_INTERRUPT
    };

.. _`ring_desc_flags.constants`:

Constants
---------

RING_DESC_ISOCH
    *undescribed*

RING_DESC_CRC_ERROR
    *undescribed*

RING_DESC_COMPLETED
    *undescribed*

RING_DESC_POSTED
    *undescribed*

RING_DESC_BUFFER_OVERRUN
    *undescribed*

RING_DESC_INTERRUPT
    *undescribed*

.. _`ring_frame`:

struct ring_frame
=================

.. c:type:: struct ring_frame

    For use with ring_rx/ring_tx

.. _`ring_frame.definition`:

Definition
----------

.. code-block:: c

    struct ring_frame {
        dma_addr_t buffer_phy;
        ring_cb callback;
        struct list_head list;
        u32 size:12;
        u32 flags:12;
        u32 eof:4;
        u32 sof:4;
    }

.. _`ring_frame.members`:

Members
-------

buffer_phy
    DMA mapped address of the frame

callback
    Callback called when the frame is finished (optional)

list
    Frame is linked to a queue using this

size
    Size of the frame in bytes (%0 means \ ``4096``\ )

flags
    Flags for the frame (see \ :c:type:`enum ring_desc_flags <ring_desc_flags>`\ )

eof
    End of frame protocol defined field

sof
    Start of frame protocol defined field

.. _`tb_ring_rx`:

tb_ring_rx
==========

.. c:function:: int tb_ring_rx(struct tb_ring *ring, struct ring_frame *frame)

    enqueue a frame on an RX ring

    :param struct tb_ring \*ring:
        Ring to enqueue the frame

    :param struct ring_frame \*frame:
        Frame to enqueue

.. _`tb_ring_rx.description`:

Description
-----------

@frame->buffer, \ ``frame``\ ->buffer_phy have to be set. The buffer must
contain at least \ ``TB_FRAME_SIZE``\  bytes.

\ ``frame``\ ->callback will be invoked with \ ``frame``\ ->size, \ ``frame``\ ->flags,
\ ``frame``\ ->eof, \ ``frame``\ ->sof set once the frame has been received.

If \ :c:func:`ring_stop`\  is called after the packet has been enqueued
\ ``frame``\ ->callback will be called with canceled set to true.

.. _`tb_ring_rx.return`:

Return
------

Returns \ ``-ESHUTDOWN``\  if ring_stop has been called. Zero otherwise.

.. _`tb_ring_tx`:

tb_ring_tx
==========

.. c:function:: int tb_ring_tx(struct tb_ring *ring, struct ring_frame *frame)

    enqueue a frame on an TX ring

    :param struct tb_ring \*ring:
        Ring the enqueue the frame

    :param struct ring_frame \*frame:
        Frame to enqueue

.. _`tb_ring_tx.description`:

Description
-----------

@frame->buffer, \ ``frame``\ ->buffer_phy, \ ``frame``\ ->size, \ ``frame``\ ->eof and
\ ``frame``\ ->sof have to be set.

\ ``frame``\ ->callback will be invoked with once the frame has been transmitted.

If \ :c:func:`ring_stop`\  is called after the packet has been enqueued \ ``frame``\ ->callback
will be called with canceled set to true.

.. _`tb_ring_tx.return`:

Return
------

Returns \ ``-ESHUTDOWN``\  if ring_stop has been called. Zero otherwise.

.. _`tb_ring_dma_device`:

tb_ring_dma_device
==================

.. c:function:: struct device *tb_ring_dma_device(struct tb_ring *ring)

    Return device used for DMA mapping

    :param struct tb_ring \*ring:
        Ring whose DMA device is retrieved

.. _`tb_ring_dma_device.description`:

Description
-----------

Use this function when you are mapping DMA for buffers that are
passed to the ring for sending/receiving.

.. This file was automatic generated / don't edit.

