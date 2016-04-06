
.. _API-atomic-sub-return:

=================
atomic_sub_return
=================

*man atomic_sub_return(9)*

*4.6.0-rc1*

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
