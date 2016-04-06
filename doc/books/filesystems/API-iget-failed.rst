
.. _API-iget-failed:

===========
iget_failed
===========

*man iget_failed(9)*

*4.6.0-rc1*

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
