.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_smpt.h

.. _`mic_smpt_ops`:

struct mic_smpt_ops
===================

.. c:type:: struct mic_smpt_ops

    MIC HW specific SMPT operations.

.. _`mic_smpt_ops.definition`:

Definition
----------

.. code-block:: c

    struct mic_smpt_ops {
        void (*init)(struct mic_device *mdev);
        void (*set)(struct mic_device *mdev, dma_addr_t dma_addr, u8 index);
    }

.. _`mic_smpt_ops.members`:

Members
-------

init
    Initialize hardware specific SMPT information in mic_smpt_hw_info.

set
    Set the value for a particular SMPT entry.

.. _`mic_smpt`:

struct mic_smpt
===============

.. c:type:: struct mic_smpt

    MIC SMPT entry information.

.. _`mic_smpt.definition`:

Definition
----------

.. code-block:: c

    struct mic_smpt {
        dma_addr_t dma_addr;
        s64 ref_count;
    }

.. _`mic_smpt.members`:

Members
-------

dma_addr
    Base DMA address for this SMPT entry.

ref_count
    Number of active mappings for this SMPT entry in bytes.

.. _`mic_smpt_hw_info`:

struct mic_smpt_hw_info
=======================

.. c:type:: struct mic_smpt_hw_info

    MIC SMPT hardware specific information.

.. _`mic_smpt_hw_info.definition`:

Definition
----------

.. code-block:: c

    struct mic_smpt_hw_info {
        u8 num_reg;
        u8 page_shift;
        u64 page_size;
        u64 base;
    }

.. _`mic_smpt_hw_info.members`:

Members
-------

num_reg
    Number of SMPT registers.

page_shift
    System memory page shift.

page_size
    System memory page size.

base
    System address base.

.. _`mic_smpt_info`:

struct mic_smpt_info
====================

.. c:type:: struct mic_smpt_info

    MIC SMPT information.

.. _`mic_smpt_info.definition`:

Definition
----------

.. code-block:: c

    struct mic_smpt_info {
        struct mic_smpt *entry;
        spinlock_t smpt_lock;
        struct mic_smpt_hw_info info;
        s64 ref_count;
        s64 map_count;
        s64 unmap_count;
    }

.. _`mic_smpt_info.members`:

Members
-------

entry
    Array of SMPT entries.

smpt_lock
    Spin lock protecting access to SMPT data structures.

info
    Hardware specific SMPT information.

ref_count
    Number of active SMPT mappings (for debug).

map_count
    Number of SMPT mappings created (for debug).

unmap_count
    Number of SMPT mappings destroyed (for debug).

.. _`mic_map_error`:

mic_map_error
=============

.. c:function:: bool mic_map_error(dma_addr_t mic_addr)

    Check a MIC address for errors.

    :param mic_addr:
        *undescribed*
    :type mic_addr: dma_addr_t

.. _`mic_map_error.description`:

Description
-----------

returns Whether there was an error during mic_map..(..) APIs.

.. This file was automatic generated / don't edit.

