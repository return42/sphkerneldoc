
.. _API-sk-set-memalloc:

===============
sk_set_memalloc
===============

*man sk_set_memalloc(9)*

*4.6.0-rc1*

sets ``SOCK_MEMALLOC``


Synopsis
========

.. c:function:: void sk_set_memalloc( struct sock * sk )

Arguments
=========

``sk``
    socket to set it on


Description
===========

Set ``SOCK_MEMALLOC`` on a socket for access to emergency reserves. It's the responsibility of the admin to adjust min_free_kbytes to meet the requirements
