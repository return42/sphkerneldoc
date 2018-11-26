.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/trans.c

.. _`gfs2_trans_add_data`:

gfs2_trans_add_data
===================

.. c:function:: void gfs2_trans_add_data(struct gfs2_glock *gl, struct buffer_head *bh)

    Add a databuf to the transaction.

    :param gl:
        The inode glock associated with the buffer
    :type gl: struct gfs2_glock \*

    :param bh:
        The buffer to add
    :type bh: struct buffer_head \*

.. _`gfs2_trans_add_data.description`:

Description
-----------

This is used in journaled data mode.
We need to journal the data block in the same way as metadata in
the functions above. The difference is that here we have a tag
which is two \__be64's being the block number (as per meta data)
and a flag which says whether the data block needs escaping or
not. This means we need a new log entry for each 251 or so data
blocks, which isn't an enormous overhead but twice as much as
for normal metadata blocks.

.. This file was automatic generated / don't edit.

