.. -*- coding: utf-8; mode: rst -*-

.. _API-iget-failed:

===========
iget_failed
===========

*man iget_failed(9)*

*4.6.0-rc5*

Mark an under-construction inode as dead and release it


Synopsis
========

.. c:function:: void iget_failed( struct inode * inode )

Arguments
=========

``inode``
    The inode to discard


Description
===========

Mark an under-construction inode as dead and release it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
