.. -*- coding: utf-8; mode: rst -*-

.. _API-sock-unregister:

===============
sock_unregister
===============

*man sock_unregister(9)*

*4.6.0-rc5*

remove a protocol handler


Synopsis
========

.. c:function:: void sock_unregister( int family )

Arguments
=========

``family``
    protocol family to remove


Description
===========

This function is called by a protocol handler that wants to remove its
address family, and have it unlinked from the new socket creation.

If protocol handler is a module, then it can use module reference counts
to protect against new references. If protocol handler is not a module
then it needs to provide its own protection in the ops->create routine.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
