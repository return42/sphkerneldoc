.. -*- coding: utf-8; mode: rst -*-

.. _API-unregister-chrdev-region:

========================
unregister_chrdev_region
========================

*man unregister_chrdev_region(9)*

*4.6.0-rc5*

unregister a range of device numbers


Synopsis
========

.. c:function:: void unregister_chrdev_region( dev_t from, unsigned count )

Arguments
=========

``from``
    the first in the range of numbers to unregister

``count``
    the number of device numbers to unregister


Description
===========

This function will unregister a range of ``count`` device numbers,
starting with ``from``. The caller should normally be the one who
allocated those numbers in the first place...


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
