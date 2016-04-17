.. -*- coding: utf-8; mode: rst -*-

======
pnfs.c
======


.. _`pnfs_mark_matching_lsegs_return`:

pnfs_mark_matching_lsegs_return
===============================

.. c:function:: int pnfs_mark_matching_lsegs_return (struct pnfs_layout_hdr *lo, struct list_head *tmp_list, const struct pnfs_layout_range *return_range)

    Free or return matching layout segments

    :param struct pnfs_layout_hdr \*lo:
        pointer to layout header

    :param struct list_head \*tmp_list:
        list header to be used with :c:func:`pnfs_free_lseg_list`

    :param const struct pnfs_layout_range \*return_range:
        describe layout segment ranges to be returned



.. _`pnfs_mark_matching_lsegs_return.description`:

Description
-----------

This function is mainly intended for use by layoutrecall. It attempts
to free the layout segment immediately, or else to mark it for return
as soon as its reference count drops to zero.

