.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_main.c

.. _`create_txqs`:

create_txqs
===========

.. c:function:: int create_txqs(struct hinic_dev *nic_dev)

    Create the Logical Tx Queues of specific NIC device

    :param nic_dev:
        the specific NIC device
    :type nic_dev: struct hinic_dev \*

.. _`create_txqs.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_txqs`:

free_txqs
=========

.. c:function:: void free_txqs(struct hinic_dev *nic_dev)

    Free the Logical Tx Queues of specific NIC device

    :param nic_dev:
        the specific NIC device
    :type nic_dev: struct hinic_dev \*

.. _`create_rxqs`:

create_rxqs
===========

.. c:function:: int create_rxqs(struct hinic_dev *nic_dev)

    Create the Logical Rx Queues of specific NIC device

    :param nic_dev:
        the specific NIC device
    :type nic_dev: struct hinic_dev \*

.. _`create_rxqs.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`free_rxqs`:

free_rxqs
=========

.. c:function:: void free_rxqs(struct hinic_dev *nic_dev)

    Free the Logical Rx Queues of specific NIC device

    :param nic_dev:
        the specific NIC device
    :type nic_dev: struct hinic_dev \*

.. _`change_mac_addr`:

change_mac_addr
===============

.. c:function:: int change_mac_addr(struct net_device *netdev, const u8 *addr)

    change the main mac address of network device

    :param netdev:
        network device
    :type netdev: struct net_device \*

    :param addr:
        mac address to set
    :type addr: const u8 \*

.. _`change_mac_addr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`add_mac_addr`:

add_mac_addr
============

.. c:function:: int add_mac_addr(struct net_device *netdev, const u8 *addr)

    add mac address to network device

    :param netdev:
        network device
    :type netdev: struct net_device \*

    :param addr:
        mac address to add
    :type addr: const u8 \*

.. _`add_mac_addr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`remove_mac_addr`:

remove_mac_addr
===============

.. c:function:: int remove_mac_addr(struct net_device *netdev, const u8 *addr)

    remove mac address from network device

    :param netdev:
        network device
    :type netdev: struct net_device \*

    :param addr:
        mac address to remove
    :type addr: const u8 \*

.. _`remove_mac_addr.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`link_status_event_handler`:

link_status_event_handler
=========================

.. c:function:: void link_status_event_handler(void *handle, void *buf_in, u16 in_size, void *buf_out, u16 *out_size)

    link event handler

    :param handle:
        nic device for the handler
    :type handle: void \*

    :param buf_in:
        output buffer
    :type buf_in: void \*

    :param in_size:
        input size
    :type in_size: u16

    :param buf_out:
        *undescribed*
    :type buf_out: void \*

    :param out_size:
        returned output size
    :type out_size: u16 \*

.. _`link_status_event_handler.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`nic_dev_init`:

nic_dev_init
============

.. c:function:: int nic_dev_init(struct pci_dev *pdev)

    Initialize the NIC device

    :param pdev:
        the NIC pci device
    :type pdev: struct pci_dev \*

.. _`nic_dev_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. This file was automatic generated / don't edit.

