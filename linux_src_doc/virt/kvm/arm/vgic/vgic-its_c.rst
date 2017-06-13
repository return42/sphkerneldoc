.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-its.c

.. _`vgic_its_abi`:

struct vgic_its_abi
===================

.. c:type:: struct vgic_its_abi

    ITS abi ops and settings

.. _`vgic_its_abi.definition`:

Definition
----------

.. code-block:: c

    struct vgic_its_abi {
        int cte_esz;
        int dte_esz;
        int ite_esz;
        int (*save_tables)(struct vgic_its *its);
        int (*restore_tables)(struct vgic_its *its);
        int (*commit)(struct vgic_its *its);
    }

.. _`vgic_its_abi.members`:

Members
-------

cte_esz
    collection table entry size

dte_esz
    device table entry size

ite_esz
    interrupt translation table entry size

save_tables
    *undescribed*

restore_tables
    restore the ITS internal structs from tables
    stored in guest RAM

commit
    initialize the registers which expose the ABI settings,
    especially the entry sizes

.. _`entry_fn_t`:

entry_fn_t
==========

.. c:function:: int entry_fn_t(struct vgic_its *its, u32 id, void *entry, void *opaque)

    Callback called on a table entry restore path

    :param struct vgic_its \*its:
        its handle

    :param u32 id:
        id of the entry

    :param void \*entry:
        pointer to the entry

    :param void \*opaque:
        pointer to an opaque data

.. _`entry_fn_t.return`:

Return
------

< 0 on error, 0 if last element was identified, id offset to next
element otherwise

.. _`scan_its_table`:

scan_its_table
==============

.. c:function:: int scan_its_table(struct vgic_its *its, gpa_t base, int size, int esz, int start_id, entry_fn_t fn, void *opaque)

    Scan a contiguous table in guest RAM and applies a function to each entry

    :param struct vgic_its \*its:
        its handle

    :param gpa_t base:
        base gpa of the table

    :param int size:
        size of the table in bytes

    :param int esz:
        entry size in bytes

    :param int start_id:
        the ID of the first entry in the table
        (non zero for 2d level tables)

    :param entry_fn_t fn:
        function to apply on each entry

    :param void \*opaque:
        *undescribed*

.. _`scan_its_table.return`:

Return
------

< 0 on error, 0 if last element was identified, 1 otherwise
(the last element may not be found on second level tables)

.. _`vgic_its_save_ite`:

vgic_its_save_ite
=================

.. c:function:: int vgic_its_save_ite(struct vgic_its *its, struct its_device *dev, struct its_ite *ite, gpa_t gpa, int ite_esz)

    Save an interrupt translation entry at \ ``gpa``\ 

    :param struct vgic_its \*its:
        *undescribed*

    :param struct its_device \*dev:
        *undescribed*

    :param struct its_ite \*ite:
        *undescribed*

    :param gpa_t gpa:
        *undescribed*

    :param int ite_esz:
        *undescribed*

.. _`vgic_its_restore_ite`:

vgic_its_restore_ite
====================

.. c:function:: int vgic_its_restore_ite(struct vgic_its *its, u32 event_id, void *ptr, void *opaque)

    restore an interrupt translation entry

    :param struct vgic_its \*its:
        *undescribed*

    :param u32 event_id:
        id used for indexing

    :param void \*ptr:
        pointer to the ITE entry

    :param void \*opaque:
        pointer to the its_device

.. _`vgic_its_save_dte`:

vgic_its_save_dte
=================

.. c:function:: int vgic_its_save_dte(struct vgic_its *its, struct its_device *dev, gpa_t ptr, int dte_esz)

    Save a device table entry at a given GPA

    :param struct vgic_its \*its:
        ITS handle

    :param struct its_device \*dev:
        ITS device

    :param gpa_t ptr:
        GPA

    :param int dte_esz:
        *undescribed*

.. _`vgic_its_restore_dte`:

vgic_its_restore_dte
====================

.. c:function:: int vgic_its_restore_dte(struct vgic_its *its, u32 id, void *ptr, void *opaque)

    restore a device table entry

    :param struct vgic_its \*its:
        its handle

    :param u32 id:
        device id the DTE corresponds to

    :param void \*ptr:
        kernel VA where the 8 byte DTE is located

    :param void \*opaque:
        unused

.. _`vgic_its_restore_dte.return`:

Return
------

< 0 on error, 0 if the dte is the last one, id offset to the
next dte otherwise

.. _`vgic_its_save_device_tables`:

vgic_its_save_device_tables
===========================

.. c:function:: int vgic_its_save_device_tables(struct vgic_its *its)

    Save the device table and all ITT into guest RAM

    :param struct vgic_its \*its:
        *undescribed*

.. _`vgic_its_save_device_tables.description`:

Description
-----------

L1/L2 handling is hidden by \ :c:func:`vgic_its_check_id`\  helper which directly
returns the GPA of the device entry

.. _`handle_l1_dte`:

handle_l1_dte
=============

.. c:function:: int handle_l1_dte(struct vgic_its *its, u32 id, void *addr, void *opaque)

    callback used for L1 device table entries (2 stage case)

    :param struct vgic_its \*its:
        its handle

    :param u32 id:
        index of the entry in the L1 table

    :param void \*addr:
        kernel VA

    :param void \*opaque:
        unused

.. _`handle_l1_dte.description`:

Description
-----------

L1 table entries are scanned by steps of 1 entry
Return < 0 if error, 0 if last dte was found when scanning the L2
table, +1 otherwise (meaning next L1 entry must be scanned)

.. _`vgic_its_restore_device_tables`:

vgic_its_restore_device_tables
==============================

.. c:function:: int vgic_its_restore_device_tables(struct vgic_its *its)

    Restore the device table and all ITT from guest RAM to internal data structs

    :param struct vgic_its \*its:
        *undescribed*

.. _`vgic_its_save_collection_table`:

vgic_its_save_collection_table
==============================

.. c:function:: int vgic_its_save_collection_table(struct vgic_its *its)

    Save the collection table into guest RAM

    :param struct vgic_its \*its:
        *undescribed*

.. _`vgic_its_restore_collection_table`:

vgic_its_restore_collection_table
=================================

.. c:function:: int vgic_its_restore_collection_table(struct vgic_its *its)

    reads the collection table in guest memory and restores the ITS internal state. Requires the BASER registers to be restored before.

    :param struct vgic_its \*its:
        *undescribed*

.. _`vgic_its_save_tables_v0`:

vgic_its_save_tables_v0
=======================

.. c:function:: int vgic_its_save_tables_v0(struct vgic_its *its)

    Save the ITS tables into guest ARM according to v0 ABI

    :param struct vgic_its \*its:
        *undescribed*

.. _`vgic_its_restore_tables_v0`:

vgic_its_restore_tables_v0
==========================

.. c:function:: int vgic_its_restore_tables_v0(struct vgic_its *its)

    Restore the ITS tables from guest RAM to internal data structs according to V0 ABI

    :param struct vgic_its \*its:
        *undescribed*

.. This file was automatic generated / don't edit.

