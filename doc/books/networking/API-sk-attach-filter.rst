
.. _API-sk-attach-filter:

================
sk_attach_filter
================

*man sk_attach_filter(9)*

*4.6.0-rc1*

attach a socket filter


Synopsis
========

.. c:function:: int sk_attach_filter( struct sock_fprog * fprog, struct sock * sk )

Arguments
=========

``fprog``
    the filter program

``sk``
    the socket to use


Description
===========

Attach the user's filter code. We first run some sanity checks on it to make sure it does not explode on us later. If an error occurs or there is insufficient memory for the filter
a negative errno code is returned. On success the return is zero.
