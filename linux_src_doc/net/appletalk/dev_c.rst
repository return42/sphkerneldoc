.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/appletalk/dev.c

.. _`alloc_ltalkdev`:

alloc_ltalkdev
==============

.. c:function:: struct net_device *alloc_ltalkdev(int sizeof_priv)

    Allocates and sets up an localtalk device

    :param sizeof_priv:
        Size of additional driver-private structure to be allocated
        for this localtalk device
    :type sizeof_priv: int

.. _`alloc_ltalkdev.description`:

Description
-----------

Fill in the fields of the device structure with localtalk-generic
values. Basically does everything except registering the device.

Constructs a new net device, complete with a private data area of
size \ ``sizeof_priv``\ .  A 32-byte (not bit) alignment is enforced for
this private data area.

.. This file was automatic generated / don't edit.

