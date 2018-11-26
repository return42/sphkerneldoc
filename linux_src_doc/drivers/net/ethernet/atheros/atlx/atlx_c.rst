.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/atheros/atlx/atlx.c

.. _`atlx_set_mac`:

atlx_set_mac
============

.. c:function:: int atlx_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`atlx_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`atlx_set_multi`:

atlx_set_multi
==============

.. c:function:: void atlx_set_multi(struct net_device *netdev)

    Multicast and Promiscuous mode set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`atlx_set_multi.description`:

Description
-----------

The set_multi entry point is called whenever the multicast address
list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper multicast,
promiscuous mode, and all-multi behavior.

.. _`atlx_irq_enable`:

atlx_irq_enable
===============

.. c:function:: void atlx_irq_enable(struct atlx_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct atlx_adapter \*

.. _`atlx_irq_disable`:

atlx_irq_disable
================

.. c:function:: void atlx_irq_disable(struct atlx_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct atlx_adapter \*

.. _`atlx_tx_timeout`:

atlx_tx_timeout
===============

.. c:function:: void atlx_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. This file was automatic generated / don't edit.

