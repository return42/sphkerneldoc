
.. _API-cdev-del:

========
cdev_del
========

*man cdev_del(9)*

*4.6.0-rc1*

remove a cdev from the system


Synopsis
========

.. c:function:: void cdev_del( struct cdev * p )

Arguments
=========

``p``
    the cdev structure to be removed


Description
===========

``cdev_del`` removes ``p`` from the system, possibly freeing the structure itself.
