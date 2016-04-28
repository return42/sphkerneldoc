.. -*- coding: utf-8; mode: rst -*-

.. _API-d-delete:

========
d_delete
========

*man d_delete(9)*

*4.6.0-rc5*

delete a dentry


Synopsis
========

.. c:function:: void d_delete( struct dentry * dentry )

Arguments
=========

``dentry``
    The dentry to delete


Description
===========

Turn the dentry into a negative dentry if possible, otherwise remove it
from the hash queues so it can be deleted later


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
