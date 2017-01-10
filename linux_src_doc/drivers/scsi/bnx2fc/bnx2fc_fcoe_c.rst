.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2fc/bnx2fc_fcoe.c

.. _`bnx2fc_xmit`:

bnx2fc_xmit
===========

.. c:function:: int bnx2fc_xmit(struct fc_lport *lport, struct fc_frame *fp)

    bnx2fc's FCoE frame transmit function

    :param struct fc_lport \*lport:
        the associated local port

    :param struct fc_frame \*fp:
        the fc_frame to be transmitted

.. _`bnx2fc_rcv`:

bnx2fc_rcv
==========

.. c:function:: int bnx2fc_rcv(struct sk_buff *skb, struct net_device *dev, struct packet_type *ptype, struct net_device *olddev)

    This is bnx2fc's receive function called by NET_RX_SOFTIRQ

    :param struct sk_buff \*skb:
        the receive socket buffer

    :param struct net_device \*dev:
        associated net device

    :param struct packet_type \*ptype:
        context

    :param struct net_device \*olddev:
        last device

.. _`bnx2fc_rcv.description`:

Description
-----------

This function receives the packet and builds FC frame and passes it up

.. _`bnx2fc_percpu_io_thread`:

bnx2fc_percpu_io_thread
=======================

.. c:function:: int bnx2fc_percpu_io_thread(void *arg)

    thread per cpu for ios

    :param void \*arg:
        ptr to bnx2fc_percpu_info structure

.. _`bnx2fc_get_link_state`:

bnx2fc_get_link_state
=====================

.. c:function:: void bnx2fc_get_link_state(struct bnx2fc_hba *hba)

    get network link state

    :param struct bnx2fc_hba \*hba:
        adapter instance pointer

.. _`bnx2fc_get_link_state.description`:

Description
-----------

updates adapter structure flag based on netdev state

.. _`bnx2fc_indicate_netevent`:

bnx2fc_indicate_netevent
========================

.. c:function:: void bnx2fc_indicate_netevent(void *context, unsigned long event, u16 vlan_id)

    Generic netdev event handler

    :param void \*context:
        adapter structure pointer

    :param unsigned long event:
        event type

    :param u16 vlan_id:
        vlan id - associated vlan id with this event

.. _`bnx2fc_indicate_netevent.description`:

Description
-----------

Handles NETDEV_UP, NETDEV_DOWN, NETDEV_GOING_DOWN,NETDEV_CHANGE and
NETDEV_CHANGE_MTU events. Handle NETDEV_UNREGISTER only for vlans.

.. _`bnx2fc_fip_recv`:

bnx2fc_fip_recv
===============

.. c:function:: int bnx2fc_fip_recv(struct sk_buff *skb, struct net_device *dev, struct packet_type *ptype, struct net_device *orig_dev)

    handle a received FIP frame.

    :param struct sk_buff \*skb:
        the received skb

    :param struct net_device \*dev:
        associated \ :c:type:`struct net_device <net_device>`\ 

    :param struct packet_type \*ptype:
        the \ :c:type:`struct packet_type <packet_type>`\  structure which was used to register this handler.

    :param struct net_device \*orig_dev:
        original receive \ :c:type:`struct net_device <net_device>`\ , in case @ dev is a bond.

.. _`bnx2fc_fip_recv.return`:

Return
------

0 for success

.. _`bnx2fc_update_src_mac`:

bnx2fc_update_src_mac
=====================

.. c:function:: void bnx2fc_update_src_mac(struct fc_lport *lport, u8 *addr)

    Update Ethernet MAC filters.

    :param struct fc_lport \*lport:
        *undescribed*

    :param u8 \*addr:
        *undescribed*

.. _`bnx2fc_update_src_mac.description`:

Description
-----------

Remove any previously-set unicast MAC filter.
Add secondary FCoE MAC address filter for our OUI.

.. _`bnx2fc_get_src_mac`:

bnx2fc_get_src_mac
==================

.. c:function:: u8 *bnx2fc_get_src_mac(struct fc_lport *lport)

    return the ethernet source address for an lport

    :param struct fc_lport \*lport:
        libfc port

.. _`bnx2fc_fip_send`:

bnx2fc_fip_send
===============

.. c:function:: void bnx2fc_fip_send(struct fcoe_ctlr *fip, struct sk_buff *skb)

    send an Ethernet-encapsulated FIP frame.

    :param struct fcoe_ctlr \*fip:
        FCoE controller.

    :param struct sk_buff \*skb:
        FIP Packet.

.. _`bnx2fc_hba_create`:

bnx2fc_hba_create
=================

.. c:function:: struct bnx2fc_hba *bnx2fc_hba_create(struct cnic_dev *cnic)

    create a new bnx2fc hba

    :param struct cnic_dev \*cnic:
        pointer to cnic device

.. _`bnx2fc_hba_create.description`:

Description
-----------

Creates a new FCoE hba on the given device.

.. _`bnx2fc_if_create`:

bnx2fc_if_create
================

.. c:function:: struct fc_lport *bnx2fc_if_create(struct bnx2fc_interface *interface, struct device *parent, int npiv)

    Create FCoE instance on a given interface

    :param struct bnx2fc_interface \*interface:
        FCoE interface to create a local port on

    :param struct device \*parent:
        Device pointer to be the parent in sysfs for the SCSI host

    :param int npiv:
        Indicates if the port is vport or not

.. _`bnx2fc_if_create.description`:

Description
-----------

Creates a fc_lport instance and a Scsi_Host instance and configure them.

.. _`bnx2fc_if_create.return`:

Return
------

Allocated fc_lport or an error pointer

.. _`bnx2fc_destroy`:

bnx2fc_destroy
==============

.. c:function:: int bnx2fc_destroy(struct net_device *netdev)

    Destroy a bnx2fc FCoE interface

    :param struct net_device \*netdev:
        *undescribed*

.. _`bnx2fc_destroy.description`:

Description
-----------

Called from sysfs.

.. _`bnx2fc_destroy.return`:

Return
------

0 for success

.. _`bnx2fc_bind_adapter_devices`:

bnx2fc_bind_adapter_devices
===========================

.. c:function:: int bnx2fc_bind_adapter_devices(struct bnx2fc_hba *hba)

    binds bnx2fc adapter with the associated pci structure

    :param struct bnx2fc_hba \*hba:
        Adapter instance

.. _`bnx2fc_ulp_get_stats`:

bnx2fc_ulp_get_stats
====================

.. c:function:: int bnx2fc_ulp_get_stats(void *handle)

    cnic callback to populate FCoE stats

    :param void \*handle:
        transport handle pointing to adapter struture

.. _`bnx2fc_ulp_start`:

bnx2fc_ulp_start
================

.. c:function:: void bnx2fc_ulp_start(void *handle)

    cnic callback to initialize & start adapter instance

    :param void \*handle:
        transport handle pointing to adapter structure

.. _`bnx2fc_ulp_start.description`:

Description
-----------

This function maps adapter structure to pcidev structure and initiates
firmware handshake to enable/initialize on-chip FCoE components.
This bnx2fc - cnic interface api callback is used after following
conditions are met -
a) underlying network interface is up (marked by event NETDEV_UP
from netdev
b) bnx2fc adatper structure is registered.

.. _`bnx2fc_ulp_stop`:

bnx2fc_ulp_stop
===============

.. c:function:: void bnx2fc_ulp_stop(void *handle)

    cnic callback to shutdown adapter instance

    :param void \*handle:
        transport handle pointing to adapter structure

.. _`bnx2fc_ulp_stop.description`:

Description
-----------

Driver checks if adapter is already in shutdown mode, if not start
the shutdown process.

.. _`bnx2fc_ulp_init`:

bnx2fc_ulp_init
===============

.. c:function:: void bnx2fc_ulp_init(struct cnic_dev *dev)

    Initialize an adapter instance

    :param struct cnic_dev \*dev:
        cnic device handle
        Called from \ :c:func:`cnic_register_driver`\  context to initialize all
        enumerated cnic devices. This routine allocates adapter structure
        and other device specific resources.

.. _`bnx2fc_disable`:

bnx2fc_disable
==============

.. c:function:: int bnx2fc_disable(struct net_device *netdev)

    Use \ :c:func:`bnx2fc_enabled`\ 

    :param struct net_device \*netdev:
        *undescribed*

.. _`bnx2fc_enable`:

bnx2fc_enable
=============

.. c:function:: int bnx2fc_enable(struct net_device *netdev)

    Use \ :c:func:`bnx2fc_enabled`\ 

    :param struct net_device \*netdev:
        *undescribed*

.. _`bnx2fc_ctlr_enabled`:

bnx2fc_ctlr_enabled
===================

.. c:function:: int bnx2fc_ctlr_enabled(struct fcoe_ctlr_device *cdev)

    Enable or disable an FCoE Controller

    :param struct fcoe_ctlr_device \*cdev:
        The FCoE Controller that is being enabled or disabled

.. _`bnx2fc_ctlr_enabled.description`:

Description
-----------

fcoe_sysfs will ensure that the state of 'enabled' has
changed, so no checking is necessary here. This routine simply
calls fcoe_enable or fcoe_disable, both of which are deprecated.
When those routines are removed the functionality can be merged
here.

.. _`_bnx2fc_create`:

_bnx2fc_create
==============

.. c:function:: int _bnx2fc_create(struct net_device *netdev, enum fip_mode fip_mode, enum bnx2fc_create_link_state link_state)

    Create bnx2fc FCoE interface

    :param struct net_device \*netdev:
        The net_device object the Ethernet interface to create on

    :param enum fip_mode fip_mode:
        The FIP mode for this creation

    :param enum bnx2fc_create_link_state link_state:
        The ctlr link state on creation

.. _`_bnx2fc_create.description`:

Description
-----------

Called from either the libfcoe 'create' module parameter
via fcoe_create or from fcoe_syfs's ctlr_create file.

libfcoe's 'create' module parameter is deprecated so some
consolidation of code can be done when that interface is
removed.

.. _`_bnx2fc_create.return`:

Return
------

0 for success

.. _`bnx2fc_create`:

bnx2fc_create
=============

.. c:function:: int bnx2fc_create(struct net_device *netdev, enum fip_mode fip_mode)

    Create a bnx2fc interface

    :param struct net_device \*netdev:
        The net_device object the Ethernet interface to create on

    :param enum fip_mode fip_mode:
        The FIP mode for this creation

.. _`bnx2fc_create.description`:

Description
-----------

Called from fcoe transport

.. _`bnx2fc_create.return`:

Return
------

0 for success

.. _`bnx2fc_ctlr_alloc`:

bnx2fc_ctlr_alloc
=================

.. c:function:: int bnx2fc_ctlr_alloc(struct net_device *netdev)

    Allocate a bnx2fc interface from fcoe_sysfs

    :param struct net_device \*netdev:
        The net_device to be used by the allocated FCoE Controller

.. _`bnx2fc_ctlr_alloc.description`:

Description
-----------

This routine is called from fcoe_sysfs. It will start the fcoe_ctlr
in a link_down state. The allows the user an opportunity to configure
the FCoE Controller from sysfs before enabling the FCoE Controller.

Creating in with this routine starts the FCoE Controller in Fabric
mode. The user can change to VN2VN or another mode before enabling.

.. _`bnx2fc_find_hba_for_cnic`:

bnx2fc_find_hba_for_cnic
========================

.. c:function:: struct bnx2fc_hba *bnx2fc_find_hba_for_cnic(struct cnic_dev *cnic)

    maps cnic instance to bnx2fc hba instance

    :param struct cnic_dev \*cnic:
        Pointer to cnic device instance

.. _`bnx2fc_ulp_exit`:

bnx2fc_ulp_exit
===============

.. c:function:: void bnx2fc_ulp_exit(struct cnic_dev *dev)

    shuts down adapter instance and frees all resources

    :param struct cnic_dev \*dev:
        *undescribed*

.. _`bnx2fc_ulp_exit.description`:

Description
-----------

@dev         cnic device handle

.. _`bnx2fc_fcoe_reset`:

bnx2fc_fcoe_reset
=================

.. c:function:: int bnx2fc_fcoe_reset(struct Scsi_Host *shost)

    Resets the fcoe

    :param struct Scsi_Host \*shost:
        shost the reset is from

.. _`bnx2fc_fcoe_reset.return`:

Return
------

always 0

.. _`bnx2fc_percpu_thread_create`:

bnx2fc_percpu_thread_create
===========================

.. c:function:: void bnx2fc_percpu_thread_create(unsigned int cpu)

    Create a receive thread for an online CPU

    :param unsigned int cpu:
        cpu index for the online cpu

.. _`bnx2fc_mod_init`:

bnx2fc_mod_init
===============

.. c:function:: int bnx2fc_mod_init( void)

    module init entry point

    :param  void:
        no arguments

.. _`bnx2fc_mod_init.description`:

Description
-----------

Initialize driver wide global data structures, and register
with cnic module

.. This file was automatic generated / don't edit.

