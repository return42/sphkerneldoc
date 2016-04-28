.. -*- coding: utf-8; mode: rst -*-

.. _API-cdev-del:

========
cdev_del
========

*man cdev_del(9)*

*4.6.0-rc5*

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

``cdev_del`` removes ``p`` from the system, possibly freeing the
structure itself.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
