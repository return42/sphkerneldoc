.. -*- coding: utf-8; mode: rst -*-

.. _API-splice-from-pipe-next:

=====================
splice_from_pipe_next
=====================

*man splice_from_pipe_next(9)*

*4.6.0-rc5*

wait for some data to splice from


Synopsis
========

.. c:function:: int splice_from_pipe_next( struct pipe_inode_info * pipe, struct splice_desc * sd )

Arguments
=========

``pipe``
    pipe to splice from

``sd``
    information about the splice operation


Description
===========

This function will wait for some data and return a positive value (one)
if pipe buffers are available. It will return zero or -errno if no more
data needs to be spliced.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
