.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/devlink.c

.. _`devlink_alloc`:

devlink_alloc
=============

.. c:function:: struct devlink *devlink_alloc(const struct devlink_ops *ops, size_t priv_size)

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

.. c:function:: int devlink_register(struct devlink *devlink, struct device *dev)

    Register devlink instance

    :param struct devlink \*devlink:
        devlink

    :param struct device \*dev:
        *undescribed*

.. _`devlink_unregister`:

devlink_unregister
==================

.. c:function:: void devlink_unregister(struct devlink *devlink)

    Unregister devlink instance

    :param struct devlink \*devlink:
        devlink

.. _`devlink_free`:

devlink_free
============

.. c:function:: void devlink_free(struct devlink *devlink)

    Free devlink instance resources

    :param struct devlink \*devlink:
        devlink

.. _`devlink_port_register`:

devlink_port_register
=====================

.. c:function:: int devlink_port_register(struct devlink *devlink, struct devlink_port *devlink_port, unsigned int port_index)

    Register devlink port

    :param struct devlink \*devlink:
        devlink

    :param struct devlink_port \*devlink_port:
        devlink port
        \ ``port_index``\ 

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

.. c:function:: void devlink_port_unregister(struct devlink_port *devlink_port)

    Unregister devlink port

    :param struct devlink_port \*devlink_port:
        devlink port

.. _`devlink_port_type_eth_set`:

devlink_port_type_eth_set
=========================

.. c:function:: void devlink_port_type_eth_set(struct devlink_port *devlink_port, struct net_device *netdev)

    Set port type to Ethernet

    :param struct devlink_port \*devlink_port:
        devlink port

    :param struct net_device \*netdev:
        related netdevice

.. _`devlink_port_type_ib_set`:

devlink_port_type_ib_set
========================

.. c:function:: void devlink_port_type_ib_set(struct devlink_port *devlink_port, struct ib_device *ibdev)

    Set port type to InfiniBand

    :param struct devlink_port \*devlink_port:
        devlink port

    :param struct ib_device \*ibdev:
        related IB device

.. _`devlink_port_type_clear`:

devlink_port_type_clear
=======================

.. c:function:: void devlink_port_type_clear(struct devlink_port *devlink_port)

    Clear port type

    :param struct devlink_port \*devlink_port:
        devlink port

.. _`devlink_port_split_set`:

devlink_port_split_set
======================

.. c:function:: void devlink_port_split_set(struct devlink_port *devlink_port, u32 split_group)

    Set port is split

    :param struct devlink_port \*devlink_port:
        devlink port

    :param u32 split_group:
        split group - identifies group split port is part of

.. _`devlink_dpipe_headers_register`:

devlink_dpipe_headers_register
==============================

.. c:function:: int devlink_dpipe_headers_register(struct devlink *devlink, struct devlink_dpipe_headers *dpipe_headers)

    register dpipe headers

    :param struct devlink \*devlink:
        devlink

    :param struct devlink_dpipe_headers \*dpipe_headers:
        dpipe header array

.. _`devlink_dpipe_headers_register.description`:

Description
-----------

Register the headers supported by hardware.

.. _`devlink_dpipe_headers_unregister`:

devlink_dpipe_headers_unregister
================================

.. c:function:: void devlink_dpipe_headers_unregister(struct devlink *devlink)

    unregister dpipe headers

    :param struct devlink \*devlink:
        devlink

.. _`devlink_dpipe_headers_unregister.description`:

Description
-----------

Unregister the headers supported by hardware.

.. _`devlink_dpipe_table_counter_enabled`:

devlink_dpipe_table_counter_enabled
===================================

.. c:function:: bool devlink_dpipe_table_counter_enabled(struct devlink *devlink, const char *table_name)

    check if counter allocation required

    :param struct devlink \*devlink:
        devlink

    :param const char \*table_name:
        tables name

.. _`devlink_dpipe_table_counter_enabled.description`:

Description
-----------

Used by driver to check if counter allocation is required.
After counter allocation is turned on the table entries
are updated to include counter statistics.

After that point on the driver must respect the counter
state so that each entry added to the table is added
with a counter.

.. _`devlink_dpipe_table_register`:

devlink_dpipe_table_register
============================

.. c:function:: int devlink_dpipe_table_register(struct devlink *devlink, const char *table_name, struct devlink_dpipe_table_ops *table_ops, void *priv, bool counter_control_extern)

    register dpipe table

    :param struct devlink \*devlink:
        devlink

    :param const char \*table_name:
        table name

    :param struct devlink_dpipe_table_ops \*table_ops:
        table ops

    :param void \*priv:
        priv

    :param bool counter_control_extern:
        external control for counters

.. _`devlink_dpipe_table_unregister`:

devlink_dpipe_table_unregister
==============================

.. c:function:: void devlink_dpipe_table_unregister(struct devlink *devlink, const char *table_name)

    unregister dpipe table

    :param struct devlink \*devlink:
        devlink

    :param const char \*table_name:
        table name

.. This file was automatic generated / don't edit.

