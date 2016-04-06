
.. _API-blk-free-devt:

=============
blk_free_devt
=============

*man blk_free_devt(9)*

*4.6.0-rc1*

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
