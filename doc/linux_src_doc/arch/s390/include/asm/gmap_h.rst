.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/gmap.h

.. _`gmap`:

struct gmap
===========

.. c:type:: struct gmap

    guest address space

.. _`gmap.definition`:

Definition
----------

.. code-block:: c

    struct gmap {
        struct list_head list;
        struct list_head crst_list;
        struct mm_struct *mm;
        struct radix_tree_root guest_to_host;
        struct radix_tree_root host_to_guest;
        spinlock_t guest_table_lock;
        unsigned long *table;
        unsigned long asce;
        unsigned long asce_end;
        void *private;
        bool pfault_enabled;
    }

.. _`gmap.members`:

Members
-------

list
    *undescribed*

crst_list
    list of all crst tables used in the guest address space

mm
    pointer to the parent mm_struct

guest_to_host
    radix tree with guest to host address translation

host_to_guest
    radix tree with pointer to segment table entries

guest_table_lock
    spinlock to protect all entries in the guest page table

table
    pointer to the page directory

asce
    address space control element for gmap page table

asce_end
    *undescribed*

private
    *undescribed*

pfault_enabled
    defines if pfaults are applicable for the guest

.. _`gmap_notifier`:

struct gmap_notifier
====================

.. c:type:: struct gmap_notifier

    notify function block for page invalidation

.. _`gmap_notifier.definition`:

Definition
----------

.. code-block:: c

    struct gmap_notifier {
        struct list_head list;
        void (* notifier_call) (struct gmap *gmap, unsigned long gaddr);
    }

.. _`gmap_notifier.members`:

Members
-------

list
    *undescribed*

notifier_call
    address of callback function

.. This file was automatic generated / don't edit.

