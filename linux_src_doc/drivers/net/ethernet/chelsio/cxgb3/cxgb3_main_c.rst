.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb3/cxgb3_main.c

.. _`link_report`:

link_report
===========

.. c:function:: void link_report(struct net_device *dev)

    show link status and link speed/duplex

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`link_report.description`:

Description
-----------

Shows the link status, speed, and duplex of a port.

.. _`t3_os_link_changed`:

t3_os_link_changed
==================

.. c:function:: void t3_os_link_changed(struct adapter *adapter, int port_id, int link_stat, int speed, int duplex, int pause)

    handle link status changes

    :param adapter:
        the adapter associated with the link change
    :type adapter: struct adapter \*

    :param port_id:
        the port index whose limk status has changed
    :type port_id: int

    :param link_stat:
        the new status of the link
    :type link_stat: int

    :param speed:
        the new speed setting
    :type speed: int

    :param duplex:
        the new duplex setting
    :type duplex: int

    :param pause:
        the new flow-control setting
    :type pause: int

.. _`t3_os_link_changed.description`:

Description
-----------

This is the OS-dependent handler for link status changes.  The OS
neutral handler takes care of most of the processing for these events,
then calls this handler for any OS-specific processing.

.. _`t3_os_phymod_changed`:

t3_os_phymod_changed
====================

.. c:function:: void t3_os_phymod_changed(struct adapter *adap, int port_id)

    handle PHY module changes

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param port_id:
        *undescribed*
    :type port_id: int

.. _`t3_os_phymod_changed.description`:

Description
-----------

This is the OS-dependent handler for PHY module changes.  It is
invoked when a PHY module is removed or inserted for any OS-specific
processing.

.. _`link_start`:

link_start
==========

.. c:function:: void link_start(struct net_device *dev)

    enable a port

    :param dev:
        the device to enable
    :type dev: struct net_device \*

.. _`link_start.description`:

Description
-----------

Performs the MAC and PHY actions needed to enable a port.

.. _`setup_rss`:

setup_rss
=========

.. c:function:: void setup_rss(struct adapter *adap)

    configure RSS

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`setup_rss.description`:

Description
-----------

Sets up RSS to distribute packets to multiple receive queues.  We
configure the RSS CPU lookup table to distribute to the number of HW
receive queues, and the response queue lookup table to narrow that
down to the response queues actually configured for each port.
We always configure the RSS mapping for two ports since the mapping
table has plenty of entries.

.. _`setup_sge_qsets`:

setup_sge_qsets
===============

.. c:function:: int setup_sge_qsets(struct adapter *adap)

    configure SGE Tx/Rx/response queues

    :param adap:
        the adapter
    :type adap: struct adapter \*

.. _`setup_sge_qsets.description`:

Description
-----------

Determines how many sets of SGE queues to use and initializes them.
We support multiple queue sets per port if we have MSI-X, otherwise
just one queue set per port.

.. _`t3_synchronize_rx`:

t3_synchronize_rx
=================

.. c:function:: void t3_synchronize_rx(struct adapter *adap, const struct port_info *p)

    wait for current Rx processing on a port to complete

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param p:
        the port
    :type p: const struct port_info \*

.. _`t3_synchronize_rx.description`:

Description
-----------

Ensures that current Rx processing on any of the queues associated with
the given port completes before returning.  We do this by acquiring and
releasing the locks of the response queues associated with the port.

.. _`cxgb_up`:

cxgb_up
=======

.. c:function:: int cxgb_up(struct adapter *adap)

    enable the adapter

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

.. _`cxgb_up.description`:

Description
-----------

Called when the first port is enabled, this function performs the
actions necessary to make an adapter operational, such as completing
the initialization of HW modules, and enabling interrupts.

Must be called with the rtnl lock held.

.. _`t3_io_error_detected`:

t3_io_error_detected
====================

.. c:function:: pci_ers_result_t t3_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

.. _`t3_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`t3_io_slot_reset`:

t3_io_slot_reset
================

.. c:function:: pci_ers_result_t t3_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`t3_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.

.. _`t3_io_resume`:

t3_io_resume
============

.. c:function:: void t3_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`t3_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation.

.. This file was automatic generated / don't edit.

