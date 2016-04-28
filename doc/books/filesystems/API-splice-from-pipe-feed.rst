.. -*- coding: utf-8; mode: rst -*-

.. _API-splice-from-pipe-feed:

=====================
splice_from_pipe_feed
=====================

*man splice_from_pipe_feed(9)*

*4.6.0-rc5*

feed available data from a pipe to a file


Synopsis
========

.. c:function:: int splice_from_pipe_feed( struct pipe_inode_info * pipe, struct splice_desc * sd, splice_actor * actor )

Arguments
=========

``pipe``
    pipe to splice from

``sd``
    information to ``actor``

``actor``
    handler that splices the data


Description
===========

This function loops over the pipe and calls ``actor`` to do the actual
moving of a single struct pipe_buffer to the desired destination. It
returns when there's no more buffers left in the pipe or if the
requested number of bytes (``sd``->total_len) have been copied. It
returns a positive number (one) if the pipe needs to be filled with more
data, zero if the required number of bytes have been copied and -errno
on error.

This, together with splice_from_pipe_{begin,end,next}, may be used to
implement the functionality of ``__splice_from_pipe`` when locking is
required around copying the pipe buffers to the destination.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
