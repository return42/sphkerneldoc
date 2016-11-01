.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/io.c

.. _`ubifs_ro_mode`:

ubifs_ro_mode
=============

.. c:function:: void ubifs_ro_mode(struct ubifs_info *c, int err)

    switch UBIFS to read read-only mode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int err:
        error code which is the reason of switching to R/O mode

.. _`ubifs_check_node`:

ubifs_check_node
================

.. c:function:: int ubifs_check_node(const struct ubifs_info *c, const void *buf, int lnum, int offs, int quiet, int must_chk_crc)

    check node.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*buf:
        node to check

    :param int lnum:
        logical eraseblock number

    :param int offs:
        offset within the logical eraseblock

    :param int quiet:
        print no messages

    :param int must_chk_crc:
        indicates whether to always check the CRC

.. _`ubifs_check_node.description`:

Description
-----------

This function checks node magic number and CRC checksum. This function also
validates node length to prevent UBIFS from becoming crazy when an attacker
feeds it a file-system image with incorrect nodes. For example, too large
node length in the common header could cause UBIFS to read memory outside of
allocated buffer when checking the CRC checksum.

This function may skip data nodes CRC checking if \ ``c``\ ->no_chk_data_crc is
true, which is controlled by corresponding UBIFS mount option. However, if
\ ``must_chk_crc``\  is true, then \ ``c``\ ->no_chk_data_crc is ignored and CRC is
checked. Similarly, if \ ``c``\ ->mounting or \ ``c``\ ->remounting_rw is true (we are
mounting or re-mounting to R/W mode), \ ``c``\ ->no_chk_data_crc is ignored and CRC
is checked. This is because during mounting or re-mounting from R/O mode to
R/W mode we may read journal nodes (when replying the journal or doing the
recovery) and the journal nodes may potentially be corrupted, so checking is
required.

This function returns zero in case of success and \ ``-EUCLEAN``\  in case of bad
CRC or magic.

.. _`ubifs_pad`:

ubifs_pad
=========

.. c:function:: void ubifs_pad(const struct ubifs_info *c, void *buf, int pad)

    pad flash space.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer to put padding to

    :param int pad:
        how many bytes to pad

.. _`ubifs_pad.description`:

Description
-----------

The flash media obliges us to write only in chunks of \ ``c-``\ >min_io_size and
when we have to write less data we add padding node to the write-buffer and
pad it to the next minimal I/O unit's boundary. Padding nodes help when the
media is being scanned. If the amount of wasted space is not enough to fit a
padding node which takes \ ``UBIFS_PAD_NODE_SZ``\  bytes, we write padding bytes
pattern (%UBIFS_PADDING_BYTE).

Padding nodes are also used to fill gaps when the "commit-in-gaps" method is
used.

.. _`next_sqnum`:

next_sqnum
==========

.. c:function:: unsigned long long next_sqnum(struct ubifs_info *c)

    get next sequence number.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_prepare_node`:

ubifs_prepare_node
==================

.. c:function:: void ubifs_prepare_node(struct ubifs_info *c, void *node, int len, int pad)

    prepare node to be written to flash.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*node:
        the node to pad

    :param int len:
        node length

    :param int pad:
        if the buffer has to be padded

.. _`ubifs_prepare_node.description`:

Description
-----------

This function prepares node at \ ``node``\  to be written to the media - it
calculates node CRC, fills the common header, and adds proper padding up to
the next minimum I/O unit if \ ``pad``\  is not zero.

.. _`ubifs_prep_grp_node`:

ubifs_prep_grp_node
===================

.. c:function:: void ubifs_prep_grp_node(struct ubifs_info *c, void *node, int len, int last)

    prepare node of a group to be written to flash.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*node:
        the node to pad

    :param int len:
        node length

    :param int last:
        indicates the last node of the group

.. _`ubifs_prep_grp_node.description`:

Description
-----------

This function prepares node at \ ``node``\  to be written to the media - it
calculates node CRC and fills the common header.

.. _`wbuf_timer_callback_nolock`:

wbuf_timer_callback_nolock
==========================

.. c:function:: enum hrtimer_restart wbuf_timer_callback_nolock(struct hrtimer *timer)

    write-buffer timer callback function.

    :param struct hrtimer \*timer:
        timer data (write-buffer descriptor)

.. _`wbuf_timer_callback_nolock.description`:

Description
-----------

This function is called when the write-buffer timer expires.

.. _`new_wbuf_timer_nolock`:

new_wbuf_timer_nolock
=====================

.. c:function:: void new_wbuf_timer_nolock(struct ubifs_wbuf *wbuf)

    start new write-buffer timer.

    :param struct ubifs_wbuf \*wbuf:
        write-buffer descriptor

.. _`cancel_wbuf_timer_nolock`:

cancel_wbuf_timer_nolock
========================

.. c:function:: void cancel_wbuf_timer_nolock(struct ubifs_wbuf *wbuf)

    cancel write-buffer timer.

    :param struct ubifs_wbuf \*wbuf:
        write-buffer descriptor

.. _`ubifs_wbuf_sync_nolock`:

ubifs_wbuf_sync_nolock
======================

.. c:function:: int ubifs_wbuf_sync_nolock(struct ubifs_wbuf *wbuf)

    synchronize write-buffer.

    :param struct ubifs_wbuf \*wbuf:
        write-buffer to synchronize

.. _`ubifs_wbuf_sync_nolock.description`:

Description
-----------

This function synchronizes write-buffer \ ``buf``\  and returns zero in case of
success or a negative error code in case of failure.

Note, although write-buffers are of \ ``c``\ ->max_write_size, this function does
not necessarily writes all \ ``c``\ ->max_write_size bytes to the flash. Instead,
if the write-buffer is only partially filled with data, only the used part
of the write-buffer (aligned on \ ``c``\ ->min_io_size boundary) is synchronized.
This way we waste less space.

.. _`ubifs_wbuf_seek_nolock`:

ubifs_wbuf_seek_nolock
======================

.. c:function:: int ubifs_wbuf_seek_nolock(struct ubifs_wbuf *wbuf, int lnum, int offs)

    seek write-buffer.

    :param struct ubifs_wbuf \*wbuf:
        write-buffer

    :param int lnum:
        logical eraseblock number to seek to

    :param int offs:
        logical eraseblock offset to seek to

.. _`ubifs_wbuf_seek_nolock.description`:

Description
-----------

This function targets the write-buffer to logical eraseblock \ ``lnum``\ :@offs.
The write-buffer has to be empty. Returns zero in case of success and a
negative error code in case of failure.

.. _`ubifs_bg_wbufs_sync`:

ubifs_bg_wbufs_sync
===================

.. c:function:: int ubifs_bg_wbufs_sync(struct ubifs_info *c)

    synchronize write-buffers.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_bg_wbufs_sync.description`:

Description
-----------

This function is called by background thread to synchronize write-buffers.
Returns zero in case of success and a negative error code in case of
failure.

.. _`ubifs_wbuf_write_nolock`:

ubifs_wbuf_write_nolock
=======================

.. c:function:: int ubifs_wbuf_write_nolock(struct ubifs_wbuf *wbuf, void *buf, int len)

    write data to flash via write-buffer.

    :param struct ubifs_wbuf \*wbuf:
        write-buffer

    :param void \*buf:
        node to write

    :param int len:
        node length

.. _`ubifs_wbuf_write_nolock.description`:

Description
-----------

This function writes data to flash via write-buffer \ ``wbuf``\ . This means that
the last piece of the node won't reach the flash media immediately if it
does not take whole max. write unit (@c->max_write_size). Instead, the node
will sit in RAM until the write-buffer is synchronized (e.g., by timer, or
because more data are appended to the write-buffer).

This function returns zero in case of success and a negative error code in
case of failure. If the node cannot be written because there is no more
space in this logical eraseblock, \ ``-ENOSPC``\  is returned.

.. _`ubifs_write_node`:

ubifs_write_node
================

.. c:function:: int ubifs_write_node(struct ubifs_info *c, void *buf, int len, int lnum, int offs)

    write node to the media.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        the node to write

    :param int len:
        node length

    :param int lnum:
        logical eraseblock number

    :param int offs:
        offset within the logical eraseblock

.. _`ubifs_write_node.description`:

Description
-----------

This function automatically fills node magic number, assigns sequence
number, and calculates node CRC checksum. The length of the \ ``buf``\  buffer has
to be aligned to the minimal I/O unit size. This function automatically
appends padding node and padding bytes if needed. Returns zero in case of
success and a negative error code in case of failure.

.. _`ubifs_read_node_wbuf`:

ubifs_read_node_wbuf
====================

.. c:function:: int ubifs_read_node_wbuf(struct ubifs_wbuf *wbuf, void *buf, int type, int len, int lnum, int offs)

    read node from the media or write-buffer.

    :param struct ubifs_wbuf \*wbuf:
        wbuf to check for un-written data

    :param void \*buf:
        buffer to read to

    :param int type:
        node type

    :param int len:
        node length

    :param int lnum:
        logical eraseblock number

    :param int offs:
        offset within the logical eraseblock

.. _`ubifs_read_node_wbuf.description`:

Description
-----------

This function reads a node of known type and length, checks it and stores
in \ ``buf``\ . If the node partially or fully sits in the write-buffer, this
function takes data from the buffer, otherwise it reads the flash media.
Returns zero in case of success, \ ``-EUCLEAN``\  if CRC mismatched and a negative
error code in case of failure.

.. _`ubifs_read_node`:

ubifs_read_node
===============

.. c:function:: int ubifs_read_node(const struct ubifs_info *c, void *buf, int type, int len, int lnum, int offs)

    read node.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer to read to

    :param int type:
        node type

    :param int len:
        node length (not aligned)

    :param int lnum:
        logical eraseblock number

    :param int offs:
        offset within the logical eraseblock

.. _`ubifs_read_node.description`:

Description
-----------

This function reads a node of known type and and length, checks it and
stores in \ ``buf``\ . Returns zero in case of success, \ ``-EUCLEAN``\  if CRC mismatched
and a negative error code in case of failure.

.. _`ubifs_wbuf_init`:

ubifs_wbuf_init
===============

.. c:function:: int ubifs_wbuf_init(struct ubifs_info *c, struct ubifs_wbuf *wbuf)

    initialize write-buffer.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_wbuf \*wbuf:
        write-buffer to initialize

.. _`ubifs_wbuf_init.description`:

Description
-----------

This function initializes write-buffer. Returns zero in case of success
\ ``-ENOMEM``\  in case of failure.

.. _`ubifs_wbuf_add_ino_nolock`:

ubifs_wbuf_add_ino_nolock
=========================

.. c:function:: void ubifs_wbuf_add_ino_nolock(struct ubifs_wbuf *wbuf, ino_t inum)

    add an inode number into the wbuf inode array.

    :param struct ubifs_wbuf \*wbuf:
        the write-buffer where to add

    :param ino_t inum:
        the inode number

.. _`ubifs_wbuf_add_ino_nolock.description`:

Description
-----------

This function adds an inode number to the inode array of the write-buffer.

.. _`wbuf_has_ino`:

wbuf_has_ino
============

.. c:function:: int wbuf_has_ino(struct ubifs_wbuf *wbuf, ino_t inum)

    returns if the wbuf contains data from the inode.

    :param struct ubifs_wbuf \*wbuf:
        the write-buffer

    :param ino_t inum:
        the inode number

.. _`wbuf_has_ino.description`:

Description
-----------

This function returns with \ ``1``\  if the write-buffer contains some data from the
given inode otherwise it returns with \ ``0``\ .

.. _`ubifs_sync_wbufs_by_inode`:

ubifs_sync_wbufs_by_inode
=========================

.. c:function:: int ubifs_sync_wbufs_by_inode(struct ubifs_info *c, struct inode *inode)

    synchronize write-buffers for an inode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct inode \*inode:
        inode to synchronize

.. _`ubifs_sync_wbufs_by_inode.description`:

Description
-----------

This function synchronizes write-buffers which contain nodes belonging to
\ ``inode``\ . Returns zero in case of success and a negative error code in case of
failure.

.. This file was automatic generated / don't edit.

