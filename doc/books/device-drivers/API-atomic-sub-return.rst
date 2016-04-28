.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-sub-return:

=================
atomic_sub_return
=================

*man atomic_sub_return(9)*

*4.6.0-rc5*

subtract integer and return


Synopsis
========

.. c:function:: int atomic_sub_return( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to subtract

``v``
    pointer of type atomic_t


Description
===========

Atomically subtracts ``i`` from ``v`` and returns ``v`` - ``i``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
