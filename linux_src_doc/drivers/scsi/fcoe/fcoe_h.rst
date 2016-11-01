.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fcoe/fcoe.h

.. _`fcoe_interface`:

struct fcoe_interface
=====================

.. c:type:: struct fcoe_interface

    A FCoE interface

.. _`fcoe_interface.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_interface {
        struct list_head list;
        struct net_device *netdev;
        struct net_device *realdev;
        struct packet_type fcoe_packet_type;
        struct packet_type fip_packet_type;
        struct packet_type fip_vlan_packet_type;
        struct fc_exch_mgr *oem;
        u8 removed;
        u8 priority;
    }

.. _`fcoe_interface.members`:

Members
-------

list
    Handle for a list of FCoE interfaces

netdev
    The associated net device

realdev
    *undescribed*

fcoe_packet_type
    FCoE packet type

fip_packet_type
    FIP packet type

fip_vlan_packet_type
    *undescribed*

oem
    The offload exchange manager for all local port
    instances associated with this port

removed
    Indicates fcoe interface removed from net device

priority
    Priority for the FCoE packet (DCB)
    This structure is 1:1 with a net device.

.. _`fcoe_netdev`:

fcoe_netdev
===========

.. c:function:: struct net_device *fcoe_netdev(const struct fc_lport *lport)

    Return the net device associated with a local port

    :param const struct fc_lport \*lport:
        The local port to get the net device from

.. This file was automatic generated / don't edit.

