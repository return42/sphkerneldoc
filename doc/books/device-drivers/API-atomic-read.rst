.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-read:

===========
atomic_read
===========

*man atomic_read(9)*

*4.6.0-rc5*

read atomic variable


Synopsis
========

.. c:function:: int atomic_read( const atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically reads the value of ``v``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
