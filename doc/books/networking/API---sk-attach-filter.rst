.. -*- coding: utf-8; mode: rst -*-

.. _API---sk-attach-filter:

==================
__sk_attach_filter
==================

*man __sk_attach_filter(9)*

*4.6.0-rc5*

attach a socket filter


Synopsis
========

.. c:function:: int __sk_attach_filter( struct sock_fprog * fprog, struct sock * sk, bool locked )

Arguments
=========

``fprog``
    the filter program

``sk``
    the socket to use

``locked``
    -- undescribed --


Description
===========

Attach the user's filter code. We first run some sanity checks on it to
make sure it does not explode on us later. If an error occurs or there
is insufficient memory for the filter a negative errno code is returned.
On success the return is zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
