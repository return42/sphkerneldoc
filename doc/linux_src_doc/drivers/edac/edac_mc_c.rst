.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_mc.c

.. _`edac_align_ptr`:

edac_align_ptr
==============

.. c:function:: void *edac_align_ptr(void **p, unsigned size, int n_elems)

    Prepares the pointer offsets for a single-shot allocation

    :param void \*\*p:
        pointer to a pointer with the memory offset to be used. At
        return, this will be incremented to point to the next offset

    :param unsigned size:
        Size of the data structure to be reserved

    :param int n_elems:
        Number of elements that should be reserved

.. _`edac_align_ptr.description`:

Description
-----------

If 'size' is a constant, the compiler will optimize this whole function
down to either a no-op or the addition of a constant to the value of '\*p'.

The 'p' pointer is absolutely needed to keep the proper advancing
further in memory to the proper offsets when allocating the struct along
with its embedded structs, as \ :c:func:`edac_device_alloc_ctl_info`\  does it
above, for example.

At return, the pointer 'p' will be incremented to be used on a next call
to this function.

.. _`edac_mc_alloc`:

edac_mc_alloc
=============

.. c:function:: struct mem_ctl_info *edac_mc_alloc(unsigned mc_num, unsigned n_layers, struct edac_mc_layer *layers, unsigned sz_pvt)

    Allocate and partially fill a struct mem_ctl_info structure

    :param unsigned mc_num:
        Memory controller number

    :param unsigned n_layers:
        Number of MC hierarchy layers

    :param struct edac_mc_layer \*layers:
        *undescribed*

    :param unsigned sz_pvt:
        *undescribed*

.. _`edac_mc_alloc.layers`:

layers
------

Describes each layer as seen by the Memory Controller

.. _`edac_mc_alloc.description`:

Description
-----------


Everything is kmalloc'ed as one big chunk - more efficient.
Only can be used if all structures have the same lifetime - otherwise
you have to allocate and initialize your own structures.

Use \ :c:func:`edac_mc_free`\  to free mc structures allocated by this function.

.. _`edac_mc_alloc.note`:

NOTE
----

drivers handle multi-rank memories in different ways: in some
drivers, one multi-rank memory stick is mapped as one entry, while, in
others, a single multi-rank memory stick would be mapped into several
entries. Currently, this function will allocate multiple struct dimm_info
on such scenarios, as grouping the multiple ranks require drivers change.

.. _`edac_mc_alloc.on-failure`:

On failure
----------

NULL

.. _`edac_mc_alloc.on-success`:

On success
----------

struct mem_ctl_info pointer

.. _`edac_mc_free`:

edac_mc_free
============

.. c:function:: void edac_mc_free(struct mem_ctl_info *mci)

    'Free' a previously allocated 'mci' structure

    :param struct mem_ctl_info \*mci:
        pointer to a struct mem_ctl_info structure

.. _`find_mci_by_dev`:

find_mci_by_dev
===============

.. c:function:: struct mem_ctl_info *find_mci_by_dev(struct device *dev)

    :param struct device \*dev:
        pointer to a struct device related with the MCI

.. _`find_mci_by_dev.description`:

Description
-----------

scan list of controllers looking for the one that manages
the 'dev' device

.. _`edac_mc_find`:

edac_mc_find
============

.. c:function:: struct mem_ctl_info *edac_mc_find(int idx)

    Search for a mem_ctl_info structure whose index is 'idx'.

    :param int idx:
        *undescribed*

.. _`edac_mc_find.description`:

Description
-----------

If found, return a pointer to the structure.
Else return NULL.

Caller must hold mem_ctls_mutex.

.. _`edac_mc_add_mc_with_groups`:

edac_mc_add_mc_with_groups
==========================

.. c:function:: int edac_mc_add_mc_with_groups(struct mem_ctl_info *mci, const struct attribute_group **groups)

    Insert the 'mci' structure into the mci global list and create sysfs entries associated with mci structure

    :param struct mem_ctl_info \*mci:
        pointer to the mci structure to be added to the list

    :param const struct attribute_group \*\*groups:
        optional attribute groups for the driver-specific sysfs entries

.. _`edac_mc_add_mc_with_groups.return`:

Return
------

0       Success
!0      Failure

.. _`edac_mc_del_mc`:

edac_mc_del_mc
==============

.. c:function:: struct mem_ctl_info *edac_mc_del_mc(struct device *dev)

    Remove sysfs entries for specified mci structure and remove mci structure from global list

    :param struct device \*dev:
        *undescribed*

.. _`edac_mc_del_mc.description`:

Description
-----------

Return pointer to removed mci structure, or NULL if device not found.

.. _`edac_raw_mc_handle_error`:

edac_raw_mc_handle_error
========================

.. c:function:: void edac_raw_mc_handle_error(const enum hw_event_mc_err_type type, struct mem_ctl_info *mci, struct edac_raw_error_desc *e)

    reports a memory event to userspace without doing anything to discover the error location

    :param const enum hw_event_mc_err_type type:
        severity of the error (CE/UE/Fatal)

    :param struct mem_ctl_info \*mci:
        a struct mem_ctl_info pointer

    :param struct edac_raw_error_desc \*e:
        error description

.. _`edac_raw_mc_handle_error.description`:

Description
-----------

This raw function is used internally by \ :c:func:`edac_mc_handle_error`\ . It should
only be called directly when the hardware error come directly from BIOS,
like in the case of APEI GHES driver.

.. _`edac_mc_handle_error`:

edac_mc_handle_error
====================

.. c:function:: void edac_mc_handle_error(const enum hw_event_mc_err_type type, struct mem_ctl_info *mci, const u16 error_count, const unsigned long page_frame_number, const unsigned long offset_in_page, const unsigned long syndrome, const int top_layer, const int mid_layer, const int low_layer, const char *msg, const char *other_detail)

    reports a memory event to userspace

    :param const enum hw_event_mc_err_type type:
        severity of the error (CE/UE/Fatal)

    :param struct mem_ctl_info \*mci:
        a struct mem_ctl_info pointer

    :param const u16 error_count:
        Number of errors of the same type

    :param const unsigned long page_frame_number:
        mem page where the error occurred

    :param const unsigned long offset_in_page:
        offset of the error inside the page

    :param const unsigned long syndrome:
        ECC syndrome

    :param const int top_layer:
        Memory layer[0] position

    :param const int mid_layer:
        Memory layer[1] position

    :param const int low_layer:
        Memory layer[2] position

    :param const char \*msg:
        Message meaningful to the end users that
        explains the event

    :param const char \*other_detail:
        Technical details about the event that
        may help hardware manufacturers and
        EDAC developers to analyse the event

.. This file was automatic generated / don't edit.

