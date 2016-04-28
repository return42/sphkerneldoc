.. -*- coding: utf-8; mode: rst -*-

.. _API-ll-rw-block:

===========
ll_rw_block
===========

*man ll_rw_block(9)*

*4.6.0-rc5*

level access to block devices (DEPRECATED)


Synopsis
========

.. c:function:: void ll_rw_block( int rw, int nr, struct buffer_head * bhs[] )

Arguments
=========

``rw``
    whether to ``READ`` or ``WRITE`` or maybe ``READA`` (readahead)

``nr``
    number of ``struct buffer_heads`` in the array

``bhs[]``
    array of pointers to ``struct buffer_head``


Description
===========

``ll_rw_block`` takes an array of pointers to ``struct buffer_heads``,
and requests an I/O operation on them, either a ``READ`` or a ``WRITE``.
The third ``READA`` option is described in the documentation for
``generic_make_request`` which ``ll_rw_block`` calls.

This function drops any buffer that it cannot get a lock on (with the
BH_Lock state bit), any buffer that appears to be clean when doing a
write request, and any buffer that appears to be up-to-date when doing
read request. Further it marks as clean buffers that are processed for
writing (the buffer cache won't assume that they are actually clean
until the buffer gets unlocked).

ll_rw_block sets b_end_io to simple completion handler that marks
the buffer up-to-date (if appropriate), unlocks the buffer and wakes any
waiters.

All of the buffers must be for the same device, and must also be a
multiple of the current approved size for the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
