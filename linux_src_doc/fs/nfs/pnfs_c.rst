.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/pnfs.c

.. _`pnfs_mark_matching_lsegs_invalid`:

pnfs_mark_matching_lsegs_invalid
================================

.. c:function:: int pnfs_mark_matching_lsegs_invalid(struct pnfs_layout_hdr *lo, struct list_head *tmp_list, const struct pnfs_layout_range *recall_range, u32 seq)

    tear down lsegs or mark them for later

    :param struct pnfs_layout_hdr \*lo:
        layout header containing the lsegs

    :param struct list_head \*tmp_list:
        list head where doomed lsegs should go

    :param const struct pnfs_layout_range \*recall_range:
        optional recall range argument to match (may be NULL)

    :param u32 seq:
        only invalidate lsegs obtained prior to this sequence (may be 0)

.. _`pnfs_mark_matching_lsegs_invalid.description`:

Description
-----------

Walk the list of lsegs in the layout header, and tear down any that should
be destroyed. If "recall_range" is specified then the segment must match
that range. If "seq" is non-zero, then only match segments that were handed
out at or before that sequence.

Returns number of matching invalid lsegs remaining in list after scanning
it and purging them.

.. _`pnfs_mark_matching_lsegs_return`:

pnfs_mark_matching_lsegs_return
===============================

.. c:function:: int pnfs_mark_matching_lsegs_return(struct pnfs_layout_hdr *lo, struct list_head *tmp_list, const struct pnfs_layout_range *return_range, u32 seq)

    Free or return matching layout segments

    :param struct pnfs_layout_hdr \*lo:
        pointer to layout header

    :param struct list_head \*tmp_list:
        list header to be used with \ :c:func:`pnfs_free_lseg_list`\ 

    :param const struct pnfs_layout_range \*return_range:
        describe layout segment ranges to be returned

    :param u32 seq:
        *undescribed*

.. _`pnfs_mark_matching_lsegs_return.description`:

Description
-----------

This function is mainly intended for use by layoutrecall. It attempts
to free the layout segment immediately, or else to mark it for return
as soon as its reference count drops to zero.

.. This file was automatic generated / don't edit.

