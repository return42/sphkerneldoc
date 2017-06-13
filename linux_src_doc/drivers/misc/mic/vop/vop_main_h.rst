.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/vop/vop_main.h

.. _`vop_vringh`:

struct vop_vringh
=================

.. c:type:: struct vop_vringh

    Virtio ring host information.

.. _`vop_vringh.definition`:

Definition
----------

.. code-block:: c

    struct vop_vringh {
        struct mic_vring vring;
        struct vringh vrh;
        struct vringh_kiov riov;
        struct vringh_kiov wiov;
        u16 head;
        struct mutex vr_mutex;
        void *buf;
        dma_addr_t buf_da;
        struct vop_vdev *vdev;
    }

.. _`vop_vringh.members`:

Members
-------

vring
    The VOP vring used for setting up user space mappings.

vrh
    The host VRINGH used for accessing the card vrings.

riov
    The VRINGH read kernel IOV.

wiov
    The VRINGH write kernel IOV.

head
    The VRINGH head index address passed to vringh_getdesc_kern(..).

vr_mutex
    Mutex for synchronizing access to the VRING.

buf
    Temporary kernel buffer used to copy in/out data
    from/to the card via DMA.

buf_da
    dma address of buf.

vdev
    Back pointer to VOP virtio device for vringh_notify(..).

.. _`vop_vdev`:

struct vop_vdev
===============

.. c:type:: struct vop_vdev

    Host information for a card Virtio device.

.. _`vop_vdev.definition`:

Definition
----------

.. code-block:: c

    struct vop_vdev {
        int virtio_id;
        wait_queue_head_t waitq;
        struct vop_device *vpdev;
        int poll_wake;
        unsigned long out_bytes;
        unsigned long in_bytes;
        unsigned long out_bytes_dma;
        unsigned long in_bytes_dma;
        unsigned long tx_len_unaligned;
        unsigned long tx_dst_unaligned;
        unsigned long rx_dst_unaligned;
        struct vop_vringh vvr;
        struct work_struct virtio_bh_work;
        struct mic_device_desc *dd;
        struct mic_device_ctrl *dc;
        struct list_head list;
        int virtio_db;
        struct mic_irq *virtio_cookie;
        struct vop_info *vi;
        struct mutex vdev_mutex;
        struct completion destroy;
        bool deleted;
    }

.. _`vop_vdev.members`:

Members
-------

virtio_id
    *undescribed*

waitq
    *undescribed*

vpdev
    *undescribed*

poll_wake
    *undescribed*

out_bytes
    *undescribed*

in_bytes
    *undescribed*

out_bytes_dma
    *undescribed*

in_bytes_dma
    *undescribed*

tx_len_unaligned
    *undescribed*

tx_dst_unaligned
    *undescribed*

rx_dst_unaligned
    *undescribed*

vvr
    *undescribed*

virtio_bh_work
    *undescribed*

dd
    *undescribed*

dc
    *undescribed*

list
    *undescribed*

virtio_db
    *undescribed*

virtio_cookie
    *undescribed*

vi
    Transport information.

vdev_mutex
    Mutex synchronizing virtio device injection,
    removal and data transfers.

destroy
    Track if a virtio device is being destroyed.

deleted
    The virtio device has been deleted.

.. _`vop_vdev.description`:

Description
-----------

@virtio_id - Virtio device id.
\ ``waitq``\  - Waitqueue to allow ring3 apps to poll.
\ ``vpdev``\  - pointer to VOP bus device.
\ ``poll_wake``\  - Used for waking up threads blocked in poll.
\ ``out_bytes``\  - Debug stats for number of bytes copied from host to card.
\ ``in_bytes``\  - Debug stats for number of bytes copied from card to host.
\ ``out_bytes_dma``\  - Debug stats for number of bytes copied from host to card
using DMA.
\ ``in_bytes_dma``\  - Debug stats for number of bytes copied from card to host
using DMA.
\ ``tx_len_unaligned``\  - Debug stats for number of bytes copied to the card where
the transfer length did not have the required DMA alignment.
\ ``tx_dst_unaligned``\  - Debug stats for number of bytes copied where the
destination address on the card did not have the required DMA alignment.
\ ``vvr``\  - Store per VRING data structures.
\ ``virtio_bh_work``\  - Work struct used to schedule virtio bottom half handling.
\ ``dd``\  - Virtio device descriptor.
\ ``dc``\  - Virtio device control fields.
\ ``list``\  - List of Virtio devices.
\ ``virtio_db``\  - The doorbell used by the card to interrupt the host.
\ ``virtio_cookie``\  - The cookie returned while requesting interrupts.

.. This file was automatic generated / don't edit.

