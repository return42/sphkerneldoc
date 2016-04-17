.. -*- coding: utf-8; mode: rst -*-

==========
ethernet.c
==========


.. _`cvm_oct_free_work`:

cvm_oct_free_work
=================

.. c:function:: int cvm_oct_free_work (void *work_queue_entry)

    Free a work queue entry

    :param void \*work_queue_entry:
        Work queue entry to free



.. _`cvm_oct_free_work.description`:

Description
-----------

Returns Zero on success, Negative on failure.



.. _`cvm_oct_common_get_stats`:

cvm_oct_common_get_stats
========================

.. c:function:: struct net_device_stats *cvm_oct_common_get_stats (struct net_device *dev)

    get the low level ethernet statistics

    :param struct net_device \*dev:
        Device to get the statistics from



.. _`cvm_oct_common_get_stats.description`:

Description
-----------

Returns Pointer to the statistics



.. _`cvm_oct_common_change_mtu`:

cvm_oct_common_change_mtu
=========================

.. c:function:: int cvm_oct_common_change_mtu (struct net_device *dev, int new_mtu)

    change the link MTU

    :param struct net_device \*dev:
        Device to change

    :param int new_mtu:
        The new MTU



.. _`cvm_oct_common_change_mtu.description`:

Description
-----------

Returns Zero on success



.. _`cvm_oct_common_set_multicast_list`:

cvm_oct_common_set_multicast_list
=================================

.. c:function:: void cvm_oct_common_set_multicast_list (struct net_device *dev)

    set the multicast list

    :param struct net_device \*dev:
        Device to work on



.. _`cvm_oct_common_set_mac_address`:

cvm_oct_common_set_mac_address
==============================

.. c:function:: int cvm_oct_common_set_mac_address (struct net_device *dev, void *addr)

    set the hardware MAC address for a device

    :param struct net_device \*dev:
        The device in question.

    :param void \*addr:
        Socket address.



.. _`cvm_oct_common_set_mac_address.description`:

Description
-----------

Returns Zero on success



.. _`cvm_oct_common_init`:

cvm_oct_common_init
===================

.. c:function:: int cvm_oct_common_init (struct net_device *dev)

    per network device initialization

    :param struct net_device \*dev:
        Device to initialize



.. _`cvm_oct_common_init.description`:

Description
-----------

Returns Zero on success

