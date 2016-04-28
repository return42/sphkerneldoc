.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-free-devt:

=============
blk_free_devt
=============

*man blk_free_devt(9)*

*4.6.0-rc5*

free a dev_t


Synopsis
========

.. c:function:: void blk_free_devt( dev_t devt )

Arguments
=========

``devt``
    dev_t to free


Description
===========

Free ``devt`` which was allocated using ``blk_alloc_devt``.


CONTEXT
=======

Might sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
