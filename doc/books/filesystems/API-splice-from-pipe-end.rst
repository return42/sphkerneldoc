.. -*- coding: utf-8; mode: rst -*-

.. _API-splice-from-pipe-end:

====================
splice_from_pipe_end
====================

*man splice_from_pipe_end(9)*

*4.6.0-rc5*

finish splicing from pipe


Synopsis
========

.. c:function:: void splice_from_pipe_end( struct pipe_inode_info * pipe, struct splice_desc * sd )

Arguments
=========

``pipe``
    pipe to splice from

``sd``
    information about the splice operation


Description
===========

This function will wake up pipe writers if necessary. It should be
called after a loop containing ``splice_from_pipe_next`` and
``splice_from_pipe_feed``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
