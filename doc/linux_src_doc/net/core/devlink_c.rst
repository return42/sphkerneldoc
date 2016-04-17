.. -*- coding: utf-8; mode: rst -*-

=========
devlink.c
=========


.. _`devlink_alloc`:

devlink_alloc
=============

.. c:function:: struct devlink *devlink_alloc (const struct devlink_ops *ops, size_t priv_size)

    Allocate new devlink instance resources

    :param const struct devlink_ops \*ops:
        ops

    :param size_t priv_size:
        size of user private data



.. _`devlink_alloc.description`:

Description
-----------

Allocate new devlink instance resources, including devlink index
and name.



.. _`devlink_register`:

devlink_register
================

.. c:function:: int devlink_register (struct devlink *devlink, struct device *dev)

    Register devlink instance

    :param struct devlink \*devlink:
        devlink

    :param struct device \*dev:

        *undescribed*



.. _`devlink_unregister`:

devlink_unregister
==================

.. c:function:: void devlink_unregister (struct devlink *devlink)

    Unregister devlink instance

    :param struct devlink \*devlink:
        devlink



.. _`devlink_free`:

devlink_free
============

.. c:function:: void devlink_free (struct devlink *devlink)

    Free devlink instance resources

    :param struct devlink \*devlink:
        devlink



.. _`devlink_port_register`:

devlink_port_register
=====================

.. c:function:: int devlink_port_register (struct devlink *devlink, struct devlink_port *devlink_port, unsigned int port_index)

    Register devlink port

    :param struct devlink \*devlink:
        devlink

    :param struct devlink_port \*devlink_port:
        devlink port
        ``port_index``

    :param unsigned int port_index:

        *undescribed*



.. _`devlink_port_register.description`:

Description
-----------

Register devlink port with provided port index. User can use
any indexing, even hw-related one. devlink_port structure
is convenient to be embedded inside user driver private structure.
Note that the caller should take care of zeroing the devlink_port
structure.



.. _`devlink_port_unregister`:

devlink_port_unregister
=======================

.. c:function:: void devlink_port_unregister (struct devlink_port *devlink_port)

    Unregister devlink port

    :param struct devlink_port \*devlink_port:
        devlink port



.. _`devlink_port_type_eth_set`:

devlink_port_type_eth_set
=========================

.. c:function:: void devlink_port_type_eth_set (struct devlink_port *devlink_port, struct net_device *netdev)

    Set port type to Ethernet

    :param struct devlink_port \*devlink_port:
        devlink port

    :param struct net_device \*netdev:
        related netdevice



.. _`devlink_port_type_ib_set`:

devlink_port_type_ib_set
========================

.. c:function:: void devlink_port_type_ib_set (struct devlink_port *devlink_port, struct ib_device *ibdev)

    Set port type to InfiniBand

    :param struct devlink_port \*devlink_port:
        devlink port

    :param struct ib_device \*ibdev:
        related IB device



.. _`devlink_port_type_clear`:

devlink_port_type_clear
=======================

.. c:function:: void devlink_port_type_clear (struct devlink_port *devlink_port)

    Clear port type

    :param struct devlink_port \*devlink_port:
        devlink port



.. _`devlink_port_split_set`:

devlink_port_split_set
======================

.. c:function:: void devlink_port_split_set (struct devlink_port *devlink_port, u32 split_group)

    Set port is split

    :param struct devlink_port \*devlink_port:
        devlink port

    :param u32 split_group:
        split group - identifies group split port is part of

