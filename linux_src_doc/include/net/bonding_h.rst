.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/bonding.h

.. _`bond_for_each_slave`:

bond_for_each_slave
===================

.. c:function::  bond_for_each_slave( bond,  pos,  iter)

    iterate over all slaves

    :param bond:
        the bond holding this list
    :type bond: 

    :param pos:
        current slave
    :type pos: 

    :param iter:
        list_head \* iterator
    :type iter: 

.. _`bond_for_each_slave.description`:

Description
-----------

Caller must hold RTNL

.. _`bond_get_slave_by_dev`:

bond_get_slave_by_dev
=====================

.. c:function:: struct slave *bond_get_slave_by_dev(struct bonding *bond, struct net_device *slave_dev)

    :param bond:
        *undescribed*
    :type bond: struct bonding \*

    :param slave_dev:
        *undescribed*
    :type slave_dev: struct net_device \*

.. _`bond_get_slave_by_dev.description`:

Description
-----------

Caller must hold bond lock for read

.. This file was automatic generated / don't edit.

