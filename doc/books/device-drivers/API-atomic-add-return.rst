
.. _API-atomic-add-return:

=================
atomic_add_return
=================

*man atomic_add_return(9)*

*4.6.0-rc1*

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
