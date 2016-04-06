
.. _API-devm-kfree:

==========
devm_kfree
==========

*man devm_kfree(9)*

*4.6.0-rc1*

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
