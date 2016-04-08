
.. _API-sk-has-allocations:

==================
sk_has_allocations
==================

*man sk_has_allocations(9)*

*4.6.0-rc1*

check if allocations are outstanding


Synopsis
========

.. c:function:: bool sk_has_allocations( const struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

Returns true if socket has write or read allocations
