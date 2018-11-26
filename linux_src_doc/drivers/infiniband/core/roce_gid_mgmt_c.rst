.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/roce_gid_mgmt.c

.. _`is_upper_ndev_bond_master_filter`:

is_upper_ndev_bond_master_filter
================================

.. c:function:: bool is_upper_ndev_bond_master_filter(struct ib_device *ib_dev, u8 port, struct net_device *rdma_ndev, void *cookie)

    Check if a given netdevice is bond master device of netdevice of the the RDMA device of port.

    :param ib_dev:
        IB device to check
    :type ib_dev: struct ib_device \*

    :param port:
        Port to consider for adding default GID
    :type port: u8

    :param rdma_ndev:
        Pointer to rdma netdevice
    :type rdma_ndev: struct net_device \*

    :param cookie:
        Netdevice to consider to form a default GID
    :type cookie: void \*

.. _`is_upper_ndev_bond_master_filter.description`:

Description
-----------

\ :c:func:`is_upper_ndev_bond_master_filter`\  returns true if a cookie_netdev
is bond master device and rdma_ndev is its lower netdevice. It might
not have been established as slave device yet.

.. _`del_default_gids`:

del_default_gids
================

.. c:function:: void del_default_gids(struct ib_device *ib_dev, u8 port, struct net_device *rdma_ndev, void *cookie)

    Delete default GIDs of the event/cookie netdevice

    :param ib_dev:
        RDMA device pointer
    :type ib_dev: struct ib_device \*

    :param port:
        Port of the RDMA device whose GID table to consider
    :type port: u8

    :param rdma_ndev:
        Unused rdma netdevice
    :type rdma_ndev: struct net_device \*

    :param cookie:
        Pointer to event netdevice
    :type cookie: void \*

.. _`del_default_gids.description`:

Description
-----------

\ :c:func:`del_default_gids`\  deletes the default GIDs of the event/cookie netdevice.

.. _`rdma_roce_rescan_device`:

rdma_roce_rescan_device
=======================

.. c:function:: void rdma_roce_rescan_device(struct ib_device *ib_dev)

    Rescan all of the network devices in the system and add their gids, as needed, to the relevant RoCE devices.

    :param ib_dev:
        *undescribed*
    :type ib_dev: struct ib_device \*

.. This file was automatic generated / don't edit.

