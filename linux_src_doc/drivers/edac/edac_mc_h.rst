.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_mc.h

.. _`edac_mc_alloc`:

edac_mc_alloc
=============

.. c:function:: struct mem_ctl_info *edac_mc_alloc(unsigned mc_num, unsigned n_layers, struct edac_mc_layer *layers, unsigned sz_pvt)

    Allocate and partially fill a struct \ :c:type:`struct mem_ctl_info <mem_ctl_info>`\ .

    :param unsigned mc_num:
        Memory controller number

    :param unsigned n_layers:
        Number of MC hierarchy layers

    :param struct edac_mc_layer \*layers:
        Describes each layer as seen by the Memory Controller

    :param unsigned sz_pvt:
        size of private storage needed

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

    :param  void:
        no arguments

.. _`edac_get_owner.return`:

Return
------

     Pointer to mod_name string when EDAC MC is owned. NULL otherwise.

.. _`edac_mc_free`:

edac_mc_free
============

.. c:function:: void edac_mc_free(struct mem_ctl_info *mci)

    Frees a previously allocated \ ``mci``\  structure

    :param struct mem_ctl_info \*mci:
        pointer to a struct mem_ctl_info structure

.. _`edac_has_mcs`:

edac_has_mcs
============

.. c:function:: bool edac_has_mcs( void)

    Check if any MCs have been allocated.

    :param  void:
        no arguments

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

    :param int idx:
        index to be seek

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

    :param struct device \*dev:
        pointer to a struct device related with the MCI

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

    :param struct device \*dev:
        Pointer to struct \ :c:type:`struct device <device>`\  representing mci structure to remove.

.. _`edac_mc_del_mc.return`:

Return
------

pointer to removed mci structure, or \ ``NULL``\  if device not found.

.. _`edac_mc_find_csrow_by_page`:

edac_mc_find_csrow_by_page
==========================

.. c:function:: int edac_mc_find_csrow_by_page(struct mem_ctl_info *mci, unsigned long page)

    Ancillary routine to identify what csrow contains a memory page.

    :param struct mem_ctl_info \*mci:
        pointer to a struct mem_ctl_info structure

    :param unsigned long page:
        memory page to find

.. _`edac_mc_find_csrow_by_page.return`:

Return
------

on success, returns the csrow. -1 if not found.

.. _`edac_raw_mc_handle_error`:

edac_raw_mc_handle_error
========================

.. c:function:: void edac_raw_mc_handle_error(const enum hw_event_mc_err_type type, struct mem_ctl_info *mci, struct edac_raw_error_desc *e)

    Reports a memory event to userspace without doing anything to discover the error location.

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

    Reports a memory event to userspace.

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

