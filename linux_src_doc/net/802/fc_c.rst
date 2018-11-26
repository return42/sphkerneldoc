.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/802/fc.c

.. _`alloc_fcdev`:

alloc_fcdev
===========

.. c:function:: struct net_device *alloc_fcdev(int sizeof_priv)

    Register fibre channel device

    :param sizeof_priv:
        Size of additional driver-private structure to be allocated
        for this fibre channel device
    :type sizeof_priv: int

.. _`alloc_fcdev.description`:

Description
-----------

Fill in the fields of the device structure with fibre channel-generic values.

Constructs a new net device, complete with a private data area of
size \ ``sizeof_priv``\ .  A 32-byte (not bit) alignment is enforced for
this private data area.

.. This file was automatic generated / don't edit.

