.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_intr.h

.. _`mic_intr_info`:

struct mic_intr_info
====================

.. c:type:: struct mic_intr_info

    Contains h/w specific interrupt sources information.

.. _`mic_intr_info.definition`:

Definition
----------

.. code-block:: c

    struct mic_intr_info {
        u16 intr_start_idx[MIC_NUM_INTR_TYPES];
        u16 intr_len[MIC_NUM_INTR_TYPES];
    }

.. _`mic_intr_info.members`:

Members
-------

intr_start_idx
    Contains the starting indexes of the
    interrupt types.

intr_len
    Contains the length of the interrupt types.

.. _`mic_irq_info`:

struct mic_irq_info
===================

.. c:type:: struct mic_irq_info

    OS specific irq information

.. _`mic_irq_info.definition`:

Definition
----------

.. code-block:: c

    struct mic_irq_info {
        int next_avail_src;
        struct msix_entry *msix_entries;
        u32 *mic_msi_map;
        u16 num_vectors;
        struct ida cb_ida;
        spinlock_t mic_intr_lock;
        spinlock_t mic_thread_lock;
        struct list_head *cb_list;
        unsigned long mask;
    }

.. _`mic_irq_info.members`:

Members
-------

next_avail_src
    next available doorbell that can be assigned.

msix_entries
    msix entries allocated while setting up MSI-x

mic_msi_map
    The MSI/MSI-x mapping information.

num_vectors
    The number of MSI/MSI-x vectors that have been allocated.

cb_ida
    callback ID allocator to track the callbacks registered.

mic_intr_lock
    spinlock to protect the interrupt callback list.

mic_thread_lock
    spinlock to protect the thread callback list.
    This lock is used to protect against thread_fn while
    mic_intr_lock is used to protect against interrupt handler.

cb_list
    Array of callback lists one for each source.

mask
    Mask used by the main thread fn to call the underlying thread fns.

.. _`mic_intr_cb`:

struct mic_intr_cb
==================

.. c:type:: struct mic_intr_cb

    Interrupt callback structure.

.. _`mic_intr_cb.definition`:

Definition
----------

.. code-block:: c

    struct mic_intr_cb {
        irq_handler_t handler;
        irq_handler_t thread_fn;
        void *data;
        int cb_id;
        struct list_head list;
    }

.. _`mic_intr_cb.members`:

Members
-------

handler
    The callback function

thread_fn
    The thread_fn.

data
    Private data of the requester.

cb_id
    The callback id. Identifies this callback.

list
    list head pointing to the next callback structure.

.. _`mic_hw_intr_ops`:

struct mic_hw_intr_ops
======================

.. c:type:: struct mic_hw_intr_ops

    MIC HW specific interrupt operations

.. _`mic_hw_intr_ops.definition`:

Definition
----------

.. code-block:: c

    struct mic_hw_intr_ops {
        void (*intr_init)(struct mic_device *mdev);
        void (*enable_interrupts)(struct mic_device *mdev);
        void (*disable_interrupts)(struct mic_device *mdev);
        void (*program_msi_to_src_map)(struct mic_device *mdev,int idx, int intr_src, bool set);
        u32 (*read_msi_to_src_map)(struct mic_device *mdev,int idx);
    }

.. _`mic_hw_intr_ops.members`:

Members
-------

intr_init
    Initialize H/W specific interrupt information.

enable_interrupts
    Enable interrupts from the hardware.

disable_interrupts
    Disable interrupts from the hardware.

program_msi_to_src_map
    Update MSI mapping registers with
    irq information.

read_msi_to_src_map
    Read MSI mapping registers containing
    irq information.

.. This file was automatic generated / don't edit.

