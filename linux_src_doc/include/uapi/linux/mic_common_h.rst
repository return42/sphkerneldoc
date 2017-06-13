.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/mic_common.h

.. _`mic_device_desc`:

struct mic_device_desc
======================

.. c:type:: struct mic_device_desc

    Virtio device information shared between the virtio driver and userspace backend

.. _`mic_device_desc.definition`:

Definition
----------

.. code-block:: c

    struct mic_device_desc {
        __s8 type;
        __u8 num_vq;
        __u8 feature_len;
        __u8 config_len;
        __u8 status;
        __le64 config;
    }

.. _`mic_device_desc.members`:

Members
-------

type
    Device type: console/network/disk etc.  Type 0/-1 terminates.

num_vq
    Number of virtqueues.

feature_len
    Number of bytes of feature bits.  Multiply by 2: one for

config_len
    Number of bytes of the config array after virtqueues.

status
    A status byte, written by the Guest.

config
    Start of the following variable length config.

.. _`mic_device_ctrl`:

struct mic_device_ctrl
======================

.. c:type:: struct mic_device_ctrl

    Per virtio device information in the device page used internally by the host and card side drivers.

.. _`mic_device_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct mic_device_ctrl {
        __le64 vdev;
        __u8 config_change;
        __u8 vdev_reset;
        __u8 guest_ack;
        __u8 host_ack;
        __u8 used_address_updated;
        __s8 c2h_vdev_db;
        __s8 h2c_vdev_db;
    }

.. _`mic_device_ctrl.members`:

Members
-------

vdev
    Used for storing MIC vdev information by the guest.

config_change
    Set to 1 by host when a config change is requested.

vdev_reset
    Set to 1 by guest to indicate virtio device has been reset.

guest_ack
    Set to 1 by guest to ack a command.

host_ack
    Set to 1 by host to ack a command.

used_address_updated
    Set to 1 by guest when the used address should be
    updated.

c2h_vdev_db
    The doorbell number to be used by guest. Set by host.

h2c_vdev_db
    The doorbell number to be used by host. Set by guest.

.. _`mic_bootparam`:

struct mic_bootparam
====================

.. c:type:: struct mic_bootparam

    Virtio device independent information in device page

.. _`mic_bootparam.definition`:

Definition
----------

.. code-block:: c

    struct mic_bootparam {
        __le32 magic;
        __s8 h2c_config_db;
        __u8 node_id;
        __u8 h2c_scif_db;
        __u8 c2h_scif_db;
        __u64 scif_host_dma_addr;
        __u64 scif_card_dma_addr;
    }

.. _`mic_bootparam.members`:

Members
-------

magic
    A magic value used by the card to ensure it can see the host

h2c_config_db
    Host to Card Virtio config doorbell set by card

node_id
    Unique id of the node
    \ ``h2c_scif_db``\  - Host to card SCIF doorbell set by card
    \ ``c2h_scif_db``\  - Card to host SCIF doorbell set by host
    \ ``scif_host_dma_addr``\  - SCIF host queue pair DMA address
    \ ``scif_card_dma_addr``\  - SCIF card queue pair DMA address

h2c_scif_db
    *undescribed*

c2h_scif_db
    *undescribed*

scif_host_dma_addr
    *undescribed*

scif_card_dma_addr
    *undescribed*

.. _`mic_device_page`:

struct mic_device_page
======================

.. c:type:: struct mic_device_page

    High level representation of the device page

.. _`mic_device_page.definition`:

Definition
----------

.. code-block:: c

    struct mic_device_page {
        struct mic_bootparam bootparam;
        struct mic_device_desc desc;
    }

.. _`mic_device_page.members`:

Members
-------

bootparam
    The bootparam structure is used for sharing information and
    status updates between MIC host and card drivers.

desc
    Array of MIC virtio device descriptors.

.. _`mic_vqconfig`:

struct mic_vqconfig
===================

.. c:type:: struct mic_vqconfig

    This is how we expect the device configuration field for a virtqueue to be laid out in config space.

.. _`mic_vqconfig.definition`:

Definition
----------

.. code-block:: c

    struct mic_vqconfig {
        __le64 address;
        __le64 used_address;
        __le16 num;
    }

.. _`mic_vqconfig.members`:

Members
-------

address
    Guest/MIC physical address of the virtio ring
    (avail and desc rings)

used_address
    Guest/MIC physical address of the used ring

num
    The number of entries in the virtio_ring

.. _`mic_max_desc_blk_size`:

MIC_MAX_DESC_BLK_SIZE
=====================

.. c:function::  MIC_MAX_DESC_BLK_SIZE()

    includes: - struct mic_device_desc - struct mic_vqconfig (num_vq of these) - host and guest features - virtio device config space

.. _`_mic_vring_info`:

struct \_mic_vring_info
=======================

.. c:type:: struct _mic_vring_info

    Host vring info exposed to userspace backend for the avail index and magic for the card.

.. _`_mic_vring_info.definition`:

Definition
----------

.. code-block:: c

    struct _mic_vring_info {
        __u16 avail_idx;
        __le32 magic;
    }

.. _`_mic_vring_info.members`:

Members
-------

avail_idx
    host avail idx

magic
    A magic debug cookie.

.. _`mic_vring`:

struct mic_vring
================

.. c:type:: struct mic_vring

    Vring information.

.. _`mic_vring.definition`:

Definition
----------

.. code-block:: c

    struct mic_vring {
        struct vring vr;
        struct _mic_vring_info *info;
        void *va;
        int len;
    }

.. _`mic_vring.members`:

Members
-------

vr
    The virtio ring.

info
    Host vring information exposed to the userspace backend for the
    avail index and magic for the card.

va
    The va for the buffer allocated for vr and info.

len
    The length of the buffer required for allocating vr and info.

.. _`mic_states`:

enum mic_states
===============

.. c:type:: enum mic_states

    MIC states.

.. _`mic_states.definition`:

Definition
----------

.. code-block:: c

    enum mic_states {
        MIC_READY,
        MIC_BOOTING,
        MIC_ONLINE,
        MIC_SHUTTING_DOWN,
        MIC_RESETTING,
        MIC_RESET_FAILED,
        MIC_LAST
    };

.. _`mic_states.constants`:

Constants
---------

MIC_READY
    *undescribed*

MIC_BOOTING
    *undescribed*

MIC_ONLINE
    *undescribed*

MIC_SHUTTING_DOWN
    *undescribed*

MIC_RESETTING
    *undescribed*

MIC_RESET_FAILED
    *undescribed*

MIC_LAST
    *undescribed*

.. _`mic_status`:

enum mic_status
===============

.. c:type:: enum mic_status

    MIC status reported by card after a host or card initiated shutdown or a card crash.

.. _`mic_status.definition`:

Definition
----------

.. code-block:: c

    enum mic_status {
        MIC_NOP,
        MIC_CRASHED,
        MIC_HALTED,
        MIC_POWER_OFF,
        MIC_RESTART,
        MIC_STATUS_LAST
    };

.. _`mic_status.constants`:

Constants
---------

MIC_NOP
    *undescribed*

MIC_CRASHED
    *undescribed*

MIC_HALTED
    *undescribed*

MIC_POWER_OFF
    *undescribed*

MIC_RESTART
    *undescribed*

MIC_STATUS_LAST
    *undescribed*

.. This file was automatic generated / don't edit.

