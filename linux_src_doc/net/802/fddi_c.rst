.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/802/fddi.c

.. _`alloc_fddidev`:

alloc_fddidev
=============

.. c:function:: struct net_device *alloc_fddidev(int sizeof_priv)

    Register FDDI device

    :param int sizeof_priv:
        Size of additional driver-private structure to be allocated
        for this FDDI device

.. _`alloc_fddidev.description`:

Description
-----------

Fill in the fields of the device structure with FDDI-generic values.

Constructs a new net device, complete with a private data area of
size \ ``sizeof_priv``\ .  A 32-byte (not bit) alignment is enforced for
this private data area.

.. This file was automatic generated / don't edit.

