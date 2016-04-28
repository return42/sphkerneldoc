.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc64-perm-to-ipc-perm:

======================
ipc64_perm_to_ipc_perm
======================

*man ipc64_perm_to_ipc_perm(9)*

*4.6.0-rc5*

convert new ipc permissions to old


Synopsis
========

.. c:function:: void ipc64_perm_to_ipc_perm( struct ipc64_perm * in, struct ipc_perm * out )

Arguments
=========

``in``
    new style ipc permissions

``out``
    old style ipc permissions


Description
===========

Turn the new style permissions object ``in`` into a compatibility object
and store it into the ``out`` pointer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
