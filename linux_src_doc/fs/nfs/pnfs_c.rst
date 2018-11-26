.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/pnfs.c

.. _`pnfs_mark_matching_lsegs_invalid`:

pnfs_mark_matching_lsegs_invalid
================================

.. c:function:: int pnfs_mark_matching_lsegs_invalid(struct pnfs_layout_hdr *lo, struct list_head *tmp_list, const struct pnfs_layout_range *recall_range, u32 seq)

    tear down lsegs or mark them for later

    :param lo:
        layout header containing the lsegs
    :type lo: struct pnfs_layout_hdr \*

    :param tmp_list:
        list head where doomed lsegs should go
    :type tmp_list: struct list_head \*

    :param recall_range:
        optional recall range argument to match (may be NULL)
    :type recall_range: const struct pnfs_layout_range \*

    :param seq:
        only invalidate lsegs obtained prior to this sequence (may be 0)
    :type seq: u32

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

    :param lo:
        pointer to layout header
    :type lo: struct pnfs_layout_hdr \*

    :param tmp_list:
        list header to be used with \ :c:func:`pnfs_free_lseg_list`\ 
    :type tmp_list: struct list_head \*

    :param return_range:
        describe layout segment ranges to be returned
    :type return_range: const struct pnfs_layout_range \*

    :param seq:
        stateid seqid to match
    :type seq: u32

.. _`pnfs_mark_matching_lsegs_return.description`:

Description
-----------

This function is mainly intended for use by layoutrecall. It attempts
to free the layout segment immediately, or else to mark it for return
as soon as its reference count drops to zero.

Returns
- 0: a layoutreturn needs to be scheduled.
- EBUSY: there are layout segment that are still in use.
- ENOENT: there are no layout segments that need to be returned.

.. This file was automatic generated / don't edit.

