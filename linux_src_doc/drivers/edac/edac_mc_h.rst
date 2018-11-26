.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_mc.h

.. _`edac_mc_alloc`:

edac_mc_alloc
=============

.. c:function:: struct mem_ctl_info *edac_mc_alloc(unsigned mc_num, unsigned n_layers, struct edac_mc_layer *layers, unsigned sz_pvt)

    Allocate and partially fill a struct \ :c:type:`struct mem_ctl_info <mem_ctl_info>`\ .

    :param mc_num:
        Memory controller number
    :type mc_num: unsigned

    :param n_layers:
        Number of MC hierarchy layers
    :type n_layers: unsigned

    :param layers:
        Describes each layer as seen by the Memory Controller
    :type layers: struct edac_mc_layer \*

    :param sz_pvt:
        size of private storage needed
    :type sz_pvt: unsigned

.. _`edac_mc_alloc.description`:

Description
-----------


Everything is kmalloc'ed as one big chunk - more efficient.
Only can be used if all structures have the same lifetime - otherwise
you have to allocate and initialize your own structures.

Use \ :c:func:`edac_mc_free`\  to free mc structures allocated by this function.

.. note::

  drivers handle multi-rank memories in different ways: in some
  drivers, one multi-rank memory stick is mapped as one entry, while, in
  others, a single multi-rank memory stick would be mapped into several
  entries. Currently, this function will allocate multiple struct dimm_info
  on such scenarios, as grouping the multiple ranks require drivers change.

.. _`edac_mc_alloc.return`:

Return
------

     On success, return a pointer to struct mem_ctl_info pointer;
     \ ``NULL``\  otherwise

.. _`edac_get_owner`:

edac_get_owner
==============

.. c:function:: const char *edac_get_owner( void)

    Return the owner's mod_name of EDAC MC

    :param void:
        no arguments
    :type void: 

.. _`edac_get_owner.return`:

Return
------

     Pointer to mod_name string when EDAC MC is owned. NULL otherwise.

.. _`edac_mc_free`:

edac_mc_free
============

.. c:function:: void edac_mc_free(struct mem_ctl_info *mci)

    Frees a previously allocated \ ``mci``\  structure

    :param mci:
        pointer to a struct mem_ctl_info structure
    :type mci: struct mem_ctl_info \*

.. _`edac_has_mcs`:

edac_has_mcs
============

.. c:function:: bool edac_has_mcs( void)

    Check if any MCs have been allocated.

    :param void:
        no arguments
    :type void: 

.. _`edac_has_mcs.return`:

Return
------

     True if MC instances have been registered successfully.
     False otherwise.

.. _`edac_mc_find`:

edac_mc_find
============

.. c:function:: struct mem_ctl_info *edac_mc_find(int idx)

    Search for a mem_ctl_info structure whose index is \ ``idx``\ .

    :param idx:
        index to be seek
    :type idx: int

.. _`edac_mc_find.description`:

Description
-----------

If found, return a pointer to the structure.
Else return NULL.

.. _`find_mci_by_dev`:

find_mci_by_dev
===============

.. c:function:: struct mem_ctl_info *find_mci_by_dev(struct device *dev)

    Scan list of controllers looking for the one that manages the \ ``dev``\  device.

    :param dev:
        pointer to a struct device related with the MCI
    :type dev: struct device \*

.. _`find_mci_by_dev.return`:

Return
------

on success, returns a pointer to struct \ :c:type:`struct mem_ctl_info <mem_ctl_info>`\ ;
\ ``NULL``\  otherwise.

.. _`edac_mc_del_mc`:

edac_mc_del_mc
==============

.. c:function:: struct mem_ctl_info *edac_mc_del_mc(struct device *dev)

    Remove sysfs entries for mci structure associated with \ ``dev``\  and remove mci structure from global list.

    :param dev:
        Pointer to struct \ :c:type:`struct device <device>`\  representing mci structure to remove.
    :type dev: struct device \*

.. _`edac_mc_del_mc.return`:

Return
------

pointer to removed mci structure, or \ ``NULL``\  if device not found.

.. _`edac_mc_find_csrow_by_page`:

edac_mc_find_csrow_by_page
==========================

.. c:function:: int edac_mc_find_csrow_by_page(struct mem_ctl_info *mci, unsigned long page)

    Ancillary routine to identify what csrow contains a memory page.

    :param mci:
        pointer to a struct mem_ctl_info structure
    :type mci: struct mem_ctl_info \*

    :param page:
        memory page to find
    :type page: unsigned long

.. _`edac_mc_find_csrow_by_page.return`:

Return
------

on success, returns the csrow. -1 if not found.

.. _`edac_raw_mc_handle_error`:

edac_raw_mc_handle_error
========================

.. c:function:: void edac_raw_mc_handle_error(const enum hw_event_mc_err_type type, struct mem_ctl_info *mci, struct edac_raw_error_desc *e)

    Reports a memory event to userspace without doing anything to discover the error location.

    :param type:
        severity of the error (CE/UE/Fatal)
    :type type: const enum hw_event_mc_err_type

    :param mci:
        a struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

    :param e:
        error description
    :type e: struct edac_raw_error_desc \*

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

    Reports a memory event to userspace.

    :param type:
        severity of the error (CE/UE/Fatal)
    :type type: const enum hw_event_mc_err_type

    :param mci:
        a struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

    :param error_count:
        Number of errors of the same type
    :type error_count: const u16

    :param page_frame_number:
        mem page where the error occurred
    :type page_frame_number: const unsigned long

    :param offset_in_page:
        offset of the error inside the page
    :type offset_in_page: const unsigned long

    :param syndrome:
        ECC syndrome
    :type syndrome: const unsigned long

    :param top_layer:
        Memory layer[0] position
    :type top_layer: const int

    :param mid_layer:
        Memory layer[1] position
    :type mid_layer: const int

    :param low_layer:
        Memory layer[2] position
    :type low_layer: const int

    :param msg:
        Message meaningful to the end users that
        explains the event
    :type msg: const char \*

    :param other_detail:
        Technical details about the event that
        may help hardware manufacturers and
        EDAC developers to analyse the event
    :type other_detail: const char \*

.. This file was automatic generated / don't edit.

