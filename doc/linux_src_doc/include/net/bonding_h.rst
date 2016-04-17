.. -*- coding: utf-8; mode: rst -*-

=========
bonding.h
=========


.. _`bond_for_each_slave`:

bond_for_each_slave
===================

.. c:function:: bond_for_each_slave ( bond,  pos,  iter)

    iterate over all slaves

    :param bond:
        the bond holding this list

    :param pos:
        current slave

    :param iter:
        list_head * iterator



.. _`bond_for_each_slave.description`:

Description
-----------

Caller must hold RTNL



.. _`bond_get_slave_by_dev`:

bond_get_slave_by_dev
=====================

.. c:function:: struct slave *bond_get_slave_by_dev (struct bonding *bond, struct net_device *slave_dev)

    :param struct bonding \*bond:

        *undescribed*

    :param struct net_device \*slave_dev:

        *undescribed*



.. _`bond_get_slave_by_dev.description`:

Description
-----------


Caller must hold bond lock for read

