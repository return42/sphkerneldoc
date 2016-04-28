.. -*- coding: utf-8; mode: rst -*-

.. _API-kernel-to-ipc64-perm:

====================
kernel_to_ipc64_perm
====================

*man kernel_to_ipc64_perm(9)*

*4.6.0-rc5*

convert kernel ipc permissions to user


Synopsis
========

.. c:function:: void kernel_to_ipc64_perm( struct kern_ipc_perm * in, struct ipc64_perm * out )

Arguments
=========

``in``
    kernel permissions

``out``
    new style ipc permissions


Description
===========

Turn the kernel object ``in`` into a set of permissions descriptions for
returning to userspace (``out``).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
