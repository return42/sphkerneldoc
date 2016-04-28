.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-kfree:

==========
devm_kfree
==========

*man devm_kfree(9)*

*4.6.0-rc5*

Resource-managed kfree


Synopsis
========

.. c:function:: void devm_kfree( struct device * dev, void * p )

Arguments
=========

``dev``
    Device this memory belongs to

``p``
    Memory to free


Description
===========

Free memory allocated with ``devm_kmalloc``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
