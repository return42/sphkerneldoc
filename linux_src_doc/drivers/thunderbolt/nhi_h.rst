.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/nhi.h

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
        struct mutex lock;
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
        struct mutex lock;
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

.. _`ring_frame`:

struct ring_frame
=================

.. c:type:: struct ring_frame

    for use with ring_rx/ring_tx

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
    *undescribed*

callback
    *undescribed*

list
    *undescribed*

size
    *undescribed*

flags
    *undescribed*

eof
    *undescribed*

sof
    *undescribed*

.. _`ring_rx`:

ring_rx
=======

.. c:function:: int ring_rx(struct tb_ring *ring, struct ring_frame *frame)

    enqueue a frame on an RX ring

    :param struct tb_ring \*ring:
        *undescribed*

    :param struct ring_frame \*frame:
        *undescribed*

.. _`ring_rx.description`:

Description
-----------

frame->buffer, frame->buffer_phy and frame->callback have to be set. The
buffer must contain at least TB_FRAME_SIZE bytes.

frame->callback will be invoked with frame->size, frame->flags, frame->eof,
frame->sof set once the frame has been received.

If ring_stop is called after the packet has been enqueued frame->callback
will be called with canceled set to true.

.. _`ring_rx.return`:

Return
------

Returns ESHUTDOWN if ring_stop has been called. Zero otherwise.

.. _`ring_tx`:

ring_tx
=======

.. c:function:: int ring_tx(struct tb_ring *ring, struct ring_frame *frame)

    enqueue a frame on an TX ring

    :param struct tb_ring \*ring:
        *undescribed*

    :param struct ring_frame \*frame:
        *undescribed*

.. _`ring_tx.description`:

Description
-----------

frame->buffer, frame->buffer_phy, frame->callback, frame->size, frame->eof
and frame->sof have to be set.

frame->callback will be invoked with once the frame has been transmitted.

If ring_stop is called after the packet has been enqueued frame->callback
will be called with canceled set to true.

.. _`ring_tx.return`:

Return
------

Returns ESHUTDOWN if ring_stop has been called. Zero otherwise.

.. This file was automatic generated / don't edit.

