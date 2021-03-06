.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet.c

.. _`cvm_oct_free_work`:

cvm_oct_free_work
=================

.. c:function:: int cvm_oct_free_work(void *work_queue_entry)

    Free a work queue entry

    :param work_queue_entry:
        Work queue entry to free
    :type work_queue_entry: void \*

.. _`cvm_oct_free_work.description`:

Description
-----------

Returns Zero on success, Negative on failure.

.. _`cvm_oct_common_get_stats`:

cvm_oct_common_get_stats
========================

.. c:function:: struct net_device_stats *cvm_oct_common_get_stats(struct net_device *dev)

    get the low level ethernet statistics

    :param dev:
        Device to get the statistics from
    :type dev: struct net_device \*

.. _`cvm_oct_common_get_stats.description`:

Description
-----------

Returns Pointer to the statistics

.. _`cvm_oct_common_change_mtu`:

cvm_oct_common_change_mtu
=========================

.. c:function:: int cvm_oct_common_change_mtu(struct net_device *dev, int new_mtu)

    change the link MTU

    :param dev:
        Device to change
    :type dev: struct net_device \*

    :param new_mtu:
        The new MTU
    :type new_mtu: int

.. _`cvm_oct_common_change_mtu.description`:

Description
-----------

Returns Zero on success

.. _`cvm_oct_common_set_multicast_list`:

cvm_oct_common_set_multicast_list
=================================

.. c:function:: void cvm_oct_common_set_multicast_list(struct net_device *dev)

    set the multicast list

    :param dev:
        Device to work on
    :type dev: struct net_device \*

.. _`cvm_oct_common_set_mac_address`:

cvm_oct_common_set_mac_address
==============================

.. c:function:: int cvm_oct_common_set_mac_address(struct net_device *dev, void *addr)

    set the hardware MAC address for a device

    :param dev:
        The device in question.
    :type dev: struct net_device \*

    :param addr:
        Socket address.
    :type addr: void \*

.. _`cvm_oct_common_set_mac_address.description`:

Description
-----------

Returns Zero on success

.. _`cvm_oct_common_init`:

cvm_oct_common_init
===================

.. c:function:: int cvm_oct_common_init(struct net_device *dev)

    per network device initialization

    :param dev:
        Device to initialize
    :type dev: struct net_device \*

.. _`cvm_oct_common_init.description`:

Description
-----------

Returns Zero on success

.. This file was automatic generated / don't edit.

