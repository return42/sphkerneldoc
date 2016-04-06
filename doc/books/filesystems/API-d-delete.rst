
.. _API-d-delete:

========
d_delete
========

*man d_delete(9)*

*4.6.0-rc1*

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

Turn the dentry into a negative dentry if possible, otherwise remove it from the hash queues so it can be deleted later
