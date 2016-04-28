.. -*- coding: utf-8; mode: rst -*-

.. _API-input-alloc-absinfo:

===================
input_alloc_absinfo
===================

*man input_alloc_absinfo(9)*

*4.6.0-rc5*

allocates array of input_absinfo structs


Synopsis
========

.. c:function:: void input_alloc_absinfo( struct input_dev * dev )

Arguments
=========

``dev``
    the input device emitting absolute events


Description
===========

If the absinfo struct the caller asked for is already allocated, this
functions will not do anything.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
