.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-release:

===========
seq_release
===========

*man seq_release(9)*

*4.6.0-rc5*

free the structures associated with sequential file.


Synopsis
========

.. c:function:: int seq_release( struct inode * inode, struct file * file )

Arguments
=========

``inode``
    its inode

``file``
    file in question


Description
===========

Frees the structures associated with sequential file; can be used as
->f_op->``release`` if you don't have private data to destroy.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
