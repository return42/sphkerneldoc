.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-free-pages:

===============
devm_free_pages
===============

*man devm_free_pages(9)*

*4.6.0-rc5*

Resource-managed free_pages


Synopsis
========

.. c:function:: void devm_free_pages( struct device * dev, unsigned long addr )

Arguments
=========

``dev``
    Device this memory belongs to

``addr``
    Memory to free


Description
===========

Free memory allocated with ``devm_get_free_pages``. Unlike free_pages,
there is no need to supply the ``order``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
