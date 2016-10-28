.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/802/hippi.c

.. _`alloc_hippi_dev`:

alloc_hippi_dev
===============

.. c:function:: struct net_device *alloc_hippi_dev(int sizeof_priv)

    Register HIPPI device

    :param int sizeof_priv:
        Size of additional driver-private structure to be allocated
        for this HIPPI device

.. _`alloc_hippi_dev.description`:

Description
-----------

Fill in the fields of the device structure with HIPPI-generic values.

Constructs a new net device, complete with a private data area of
size \ ``sizeof_priv``\ .  A 32-byte (not bit) alignment is enforced for
this private data area.

.. This file was automatic generated / don't edit.

