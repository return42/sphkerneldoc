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
        atomic_t ref_count;
        unsigned long *table;
        unsigned long asce;
        unsigned long asce_end;
        void *private;
        bool pfault_enabled;
        struct radix_tree_root host_to_rmap;
        struct list_head children;
        struct list_head pt_list;
        spinlock_t shadow_lock;
        struct gmap *parent;
        unsigned long orig_asce;
        int edat_level;
        bool removed;
        bool initialized;
    }

.. _`gmap.members`:

Members
-------

list
    list head for the mm->context gmap list

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

ref_count
    reference counter for the gmap structure

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

host_to_rmap
    radix tree with gmap_rmap lists

children
    list of shadow gmap structures

pt_list
    list of all page tables used in the shadow guest address space

shadow_lock
    spinlock to protect the shadow gmap list

parent
    pointer to the parent gmap for shadow guest address spaces

orig_asce
    ASCE for which the shadow page table has been created

edat_level
    edat level to be used for the shadow translation

removed
    flag to indicate if a shadow guest address space has been removed

initialized
    flag to indicate if a shadow guest address space can be used

.. _`gmap_rmap`:

struct gmap_rmap
================

.. c:type:: struct gmap_rmap

    reverse mapping for shadow page table entries

.. _`gmap_rmap.definition`:

Definition
----------

.. code-block:: c

    struct gmap_rmap {
        struct gmap_rmap *next;
        unsigned long raddr;
    }

.. _`gmap_rmap.members`:

Members
-------

next
    pointer to next rmap in the list

raddr
    virtual rmap address in the shadow guest address space

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
        struct rcu_head rcu;
        void (*notifier_call)(struct gmap *gmap, unsigned long start, unsigned long end);
    }

.. _`gmap_notifier.members`:

Members
-------

list
    *undescribed*

rcu
    *undescribed*

notifier_call
    address of callback function

.. This file was automatic generated / don't edit.

