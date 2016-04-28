.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-add-return:

=================
atomic_add_return
=================

*man atomic_add_return(9)*

*4.6.0-rc5*

add integer and return


Synopsis
========

.. c:function:: int atomic_add_return( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to add

``v``
    pointer of type atomic_t


Description
===========

Atomically adds ``i`` to ``v`` and returns ``i`` + ``v``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
