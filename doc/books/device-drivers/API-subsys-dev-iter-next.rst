.. -*- coding: utf-8; mode: rst -*-

.. _API-subsys-dev-iter-next:

====================
subsys_dev_iter_next
====================

*man subsys_dev_iter_next(9)*

*4.6.0-rc5*

iterate to the next device


Synopsis
========

.. c:function:: struct device * subsys_dev_iter_next( struct subsys_dev_iter * iter )

Arguments
=========

``iter``
    subsys iterator to proceed


Description
===========

Proceed ``iter`` to the next device and return it. Returns NULL if
iteration is complete.

The returned device is referenced and won't be released till iterator is
proceed to the next device or exited. The caller is free to do whatever
it wants to do with the device including calling back into subsys code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
