.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-clone-lock:

=============
sk_clone_lock
=============

*man sk_clone_lock(9)*

*4.6.0-rc5*

clone a socket, and lock its clone


Synopsis
========

.. c:function:: struct sock * sk_clone_lock( const struct sock * sk, const gfp_t priority )

Arguments
=========

``sk``
    the socket to clone

``priority``
    for allocation (``GFP_KERNEL``, ``GFP_ATOMIC``, etc)


Description
===========

Caller must unlock socket even in error path (bh_unlock_sock(newsk))


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
