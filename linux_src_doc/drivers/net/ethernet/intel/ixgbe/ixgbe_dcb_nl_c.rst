.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_dcb_nl.c

.. _`ixgbe_dcbnl_getapp`:

ixgbe_dcbnl_getapp
==================

.. c:function:: int ixgbe_dcbnl_getapp(struct net_device *netdev, u8 idtype, u16 id)

    retrieve the DCBX application user priority

    :param netdev:
        the corresponding netdev
    :type netdev: struct net_device \*

    :param idtype:
        identifies the id as ether type or TCP/UDP port number
    :type idtype: u8

    :param id:
        id is either ether type or TCP/UDP port number
    :type id: u16

.. _`ixgbe_dcbnl_getapp.description`:

Description
-----------

Returns : on success, returns a non-zero 802.1p user priority bitmap
otherwise returns -EINVAL as the invalid user priority bitmap to indicate an
error.

.. This file was automatic generated / don't edit.

