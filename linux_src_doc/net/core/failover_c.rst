.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/failover.c

.. _`failover_slave_register`:

failover_slave_register
=======================

.. c:function:: int failover_slave_register(struct net_device *slave_dev)

    Register a slave netdev

    :param slave_dev:
        slave netdev that is being registered
    :type slave_dev: struct net_device \*

.. _`failover_slave_register.description`:

Description
-----------

Registers a slave device to a failover instance. Only ethernet devices
are supported.

.. _`failover_slave_unregister`:

failover_slave_unregister
=========================

.. c:function:: int failover_slave_unregister(struct net_device *slave_dev)

    Unregister a slave netdev

    :param slave_dev:
        slave netdev that is being unregistered
    :type slave_dev: struct net_device \*

.. _`failover_slave_unregister.description`:

Description
-----------

Unregisters a slave device from a failover instance.

.. _`failover_register`:

failover_register
=================

.. c:function:: struct failover *failover_register(struct net_device *dev, struct failover_ops *ops)

    Register a failover instance

    :param dev:
        failover netdev
    :type dev: struct net_device \*

    :param ops:
        failover ops
    :type ops: struct failover_ops \*

.. _`failover_register.description`:

Description
-----------

Allocate and register a failover instance for a failover netdev. ops
provides handlers for slave device register/unregister/link change/
name change events.

.. _`failover_register.return`:

Return
------

pointer to failover instance

.. _`failover_unregister`:

failover_unregister
===================

.. c:function:: void failover_unregister(struct failover *failover)

    Unregister a failover instance

    :param failover:
        pointer to failover instance
    :type failover: struct failover \*

.. _`failover_unregister.description`:

Description
-----------

Unregisters and frees a failover instance.

.. This file was automatic generated / don't edit.

