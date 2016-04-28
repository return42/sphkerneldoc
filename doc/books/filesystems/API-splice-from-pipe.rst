.. -*- coding: utf-8; mode: rst -*-

.. _API-splice-from-pipe:

================
splice_from_pipe
================

*man splice_from_pipe(9)*

*4.6.0-rc5*

splice data from a pipe to a file


Synopsis
========

.. c:function:: ssize_t splice_from_pipe( struct pipe_inode_info * pipe, struct file * out, loff_t * ppos, size_t len, unsigned int flags, splice_actor * actor )

Arguments
=========

``pipe``
    pipe to splice from

``out``
    file to splice to

``ppos``
    position in ``out``

``len``
    how many bytes to splice

``flags``
    splice modifier flags

``actor``
    handler that splices the data


Description
===========

See __splice_from_pipe. This function locks the pipe inode,
otherwise it's identical to ``__splice_from_pipe``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
