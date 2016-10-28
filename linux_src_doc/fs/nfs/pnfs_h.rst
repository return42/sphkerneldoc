.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/pnfs.h

.. _`pnfs_mark_layout_returned_if_empty`:

pnfs_mark_layout_returned_if_empty
==================================

.. c:function:: void pnfs_mark_layout_returned_if_empty(struct pnfs_layout_hdr *lo)

    marks the layout as returned

    :param struct pnfs_layout_hdr \*lo:
        layout header

.. _`pnfs_mark_layout_returned_if_empty.note`:

Note
----

Caller must hold inode->i_lock

.. This file was automatic generated / don't edit.

