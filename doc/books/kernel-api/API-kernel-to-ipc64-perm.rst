
.. _API-kernel-to-ipc64-perm:

====================
kernel_to_ipc64_perm
====================

*man kernel_to_ipc64_perm(9)*

*4.6.0-rc1*

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

Turn the kernel object ``in`` into a set of permissions descriptions for returning to userspace (``out``).
