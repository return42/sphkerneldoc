.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/io.c

.. _`ubifs_ro_mode`:

ubifs_ro_mode
=============

.. c:function:: void ubifs_ro_mode(struct ubifs_info *c, int err)

    switch UBIFS to read read-only mode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param err:
        error code which is the reason of switching to R/O mode
    :type err: int

.. _`ubifs_check_node`:

ubifs_check_node
================

.. c:function:: int ubifs_check_node(const struct ubifs_info *c, const void *buf, int lnum, int offs, int quiet, int must_chk_crc)

    check node.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param buf:
        node to check
    :type buf: const void \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset within the logical eraseblock
    :type offs: int

    :param quiet:
        print no messages
    :type quiet: int

    :param must_chk_crc:
        indicates whether to always check the CRC
    :type must_chk_crc: int

.. _`ubifs_check_node.description`:

Description
-----------

This function checks node magic number and CRC checksum. This function also
validates node length to prevent UBIFS from becoming crazy when an attacker
feeds it a file-system image with incorrect nodes. For example, too large
node length in the common header could cause UBIFS to read memory outside of
allocated buffer when checking the CRC checksum.

This function may skip data nodes CRC checking if \ ``c->no_chk_data_crc``\  is
true, which is controlled by corresponding UBIFS mount option. However, if
\ ``must_chk_crc``\  is true, then \ ``c->no_chk_data_crc``\  is ignored and CRC is
checked. Similarly, if \ ``c->mounting``\  or \ ``c->remounting_rw``\  is true (we are
mounting or re-mounting to R/W mode), \ ``c->no_chk_data_crc``\  is ignored and CRC
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

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param buf:
        buffer to put padding to
    :type buf: void \*

    :param pad:
        how many bytes to pad
    :type pad: int

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

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_prepare_node_hmac`:

ubifs_prepare_node_hmac
=======================

.. c:function:: int ubifs_prepare_node_hmac(struct ubifs_info *c, void *node, int len, int hmac_offs, int pad)

    prepare node to be written to flash.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param node:
        the node to pad
    :type node: void \*

    :param len:
        node length
    :type len: int

    :param hmac_offs:
        offset of the HMAC in the node
    :type hmac_offs: int

    :param pad:
        if the buffer has to be padded
    :type pad: int

.. _`ubifs_prepare_node_hmac.description`:

Description
-----------

This function prepares node at \ ``node``\  to be written to the media - it
calculates node CRC, fills the common header, and adds proper padding up to
the next minimum I/O unit if \ ``pad``\  is not zero. if \ ``hmac_offs``\  is positive then
a HMAC is inserted into the node at the given offset.

This function returns 0 for success or a negative error code otherwise.

.. _`ubifs_prepare_node`:

ubifs_prepare_node
==================

.. c:function:: void ubifs_prepare_node(struct ubifs_info *c, void *node, int len, int pad)

    prepare node to be written to flash.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param node:
        the node to pad
    :type node: void \*

    :param len:
        node length
    :type len: int

    :param pad:
        if the buffer has to be padded
    :type pad: int

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

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param node:
        the node to pad
    :type node: void \*

    :param len:
        node length
    :type len: int

    :param last:
        indicates the last node of the group
    :type last: int

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

    :param timer:
        timer data (write-buffer descriptor)
    :type timer: struct hrtimer \*

.. _`wbuf_timer_callback_nolock.description`:

Description
-----------

This function is called when the write-buffer timer expires.

.. _`new_wbuf_timer_nolock`:

new_wbuf_timer_nolock
=====================

.. c:function:: void new_wbuf_timer_nolock(struct ubifs_info *c, struct ubifs_wbuf *wbuf)

    start new write-buffer timer.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param wbuf:
        write-buffer descriptor
    :type wbuf: struct ubifs_wbuf \*

.. _`cancel_wbuf_timer_nolock`:

cancel_wbuf_timer_nolock
========================

.. c:function:: void cancel_wbuf_timer_nolock(struct ubifs_wbuf *wbuf)

    cancel write-buffer timer.

    :param wbuf:
        write-buffer descriptor
    :type wbuf: struct ubifs_wbuf \*

.. _`ubifs_wbuf_sync_nolock`:

ubifs_wbuf_sync_nolock
======================

.. c:function:: int ubifs_wbuf_sync_nolock(struct ubifs_wbuf *wbuf)

    synchronize write-buffer.

    :param wbuf:
        write-buffer to synchronize
    :type wbuf: struct ubifs_wbuf \*

.. _`ubifs_wbuf_sync_nolock.description`:

Description
-----------

This function synchronizes write-buffer \ ``buf``\  and returns zero in case of
success or a negative error code in case of failure.

Note, although write-buffers are of \ ``c->max_write_size``\ , this function does
not necessarily writes all \ ``c->max_write_size``\  bytes to the flash. Instead,
if the write-buffer is only partially filled with data, only the used part
of the write-buffer (aligned on \ ``c->min_io_size``\  boundary) is synchronized.
This way we waste less space.

.. _`ubifs_wbuf_seek_nolock`:

ubifs_wbuf_seek_nolock
======================

.. c:function:: int ubifs_wbuf_seek_nolock(struct ubifs_wbuf *wbuf, int lnum, int offs)

    seek write-buffer.

    :param wbuf:
        write-buffer
    :type wbuf: struct ubifs_wbuf \*

    :param lnum:
        logical eraseblock number to seek to
    :type lnum: int

    :param offs:
        logical eraseblock offset to seek to
    :type offs: int

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

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

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

    :param wbuf:
        write-buffer
    :type wbuf: struct ubifs_wbuf \*

    :param buf:
        node to write
    :type buf: void \*

    :param len:
        node length
    :type len: int

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

.. _`ubifs_write_node_hmac`:

ubifs_write_node_hmac
=====================

.. c:function:: int ubifs_write_node_hmac(struct ubifs_info *c, void *buf, int len, int lnum, int offs, int hmac_offs)

    write node to the media.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param buf:
        the node to write
    :type buf: void \*

    :param len:
        node length
    :type len: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset within the logical eraseblock
    :type offs: int

    :param hmac_offs:
        offset of the HMAC within the node
    :type hmac_offs: int

.. _`ubifs_write_node_hmac.description`:

Description
-----------

This function automatically fills node magic number, assigns sequence
number, and calculates node CRC checksum. The length of the \ ``buf``\  buffer has
to be aligned to the minimal I/O unit size. This function automatically
appends padding node and padding bytes if needed. Returns zero in case of
success and a negative error code in case of failure.

.. _`ubifs_write_node`:

ubifs_write_node
================

.. c:function:: int ubifs_write_node(struct ubifs_info *c, void *buf, int len, int lnum, int offs)

    write node to the media.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param buf:
        the node to write
    :type buf: void \*

    :param len:
        node length
    :type len: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset within the logical eraseblock
    :type offs: int

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

    :param wbuf:
        wbuf to check for un-written data
    :type wbuf: struct ubifs_wbuf \*

    :param buf:
        buffer to read to
    :type buf: void \*

    :param type:
        node type
    :type type: int

    :param len:
        node length
    :type len: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset within the logical eraseblock
    :type offs: int

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

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param buf:
        buffer to read to
    :type buf: void \*

    :param type:
        node type
    :type type: int

    :param len:
        node length (not aligned)
    :type len: int

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param offs:
        offset within the logical eraseblock
    :type offs: int

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

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param wbuf:
        write-buffer to initialize
    :type wbuf: struct ubifs_wbuf \*

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

    :param wbuf:
        the write-buffer where to add
    :type wbuf: struct ubifs_wbuf \*

    :param inum:
        the inode number
    :type inum: ino_t

.. _`ubifs_wbuf_add_ino_nolock.description`:

Description
-----------

This function adds an inode number to the inode array of the write-buffer.

.. _`wbuf_has_ino`:

wbuf_has_ino
============

.. c:function:: int wbuf_has_ino(struct ubifs_wbuf *wbuf, ino_t inum)

    returns if the wbuf contains data from the inode.

    :param wbuf:
        the write-buffer
    :type wbuf: struct ubifs_wbuf \*

    :param inum:
        the inode number
    :type inum: ino_t

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

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode to synchronize
    :type inode: struct inode \*

.. _`ubifs_sync_wbufs_by_inode.description`:

Description
-----------

This function synchronizes write-buffers which contain nodes belonging to
\ ``inode``\ . Returns zero in case of success and a negative error code in case of
failure.

.. This file was automatic generated / don't edit.

