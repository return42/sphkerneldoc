.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fcoe/fcoe.c

.. _`fcoe_interface_setup`:

fcoe_interface_setup
====================

.. c:function:: int fcoe_interface_setup(struct fcoe_interface *fcoe, struct net_device *netdev)

    Setup a FCoE interface

    :param fcoe:
        The new FCoE interface
    :type fcoe: struct fcoe_interface \*

    :param netdev:
        The net device that the fcoe interface is on
    :type netdev: struct net_device \*

.. _`fcoe_interface_setup.description`:

Description
-----------

Returns : 0 for success

.. _`fcoe_interface_setup.locking`:

Locking
-------

must be called with the RTNL mutex held

.. _`fcoe_interface_create`:

fcoe_interface_create
=====================

.. c:function:: struct fcoe_interface *fcoe_interface_create(struct net_device *netdev, enum fip_state fip_mode)

    Create a FCoE interface on a net device

    :param netdev:
        The net device to create the FCoE interface on
    :type netdev: struct net_device \*

    :param fip_mode:
        The mode to use for FIP
    :type fip_mode: enum fip_state

.. _`fcoe_interface_create.return`:

Return
------

pointer to a struct fcoe_interface or NULL on error

.. _`fcoe_interface_remove`:

fcoe_interface_remove
=====================

.. c:function:: void fcoe_interface_remove(struct fcoe_interface *fcoe)

    remove FCoE interface from netdev

    :param fcoe:
        The FCoE interface to be cleaned up
    :type fcoe: struct fcoe_interface \*

.. _`fcoe_interface_remove.description`:

Description
-----------

Caller must be holding the RTNL mutex

.. _`fcoe_interface_cleanup`:

fcoe_interface_cleanup
======================

.. c:function:: void fcoe_interface_cleanup(struct fcoe_interface *fcoe)

    Clean up a FCoE interface

    :param fcoe:
        The FCoE interface to be cleaned up
    :type fcoe: struct fcoe_interface \*

.. _`fcoe_fip_recv`:

fcoe_fip_recv
=============

.. c:function:: int fcoe_fip_recv(struct sk_buff *skb, struct net_device *netdev, struct packet_type *ptype, struct net_device *orig_dev)

    Handler for received FIP frames

    :param skb:
        The receive skb
    :type skb: struct sk_buff \*

    :param netdev:
        The associated net device
    :type netdev: struct net_device \*

    :param ptype:
        The packet_type structure which was used to register this handler
    :type ptype: struct packet_type \*

    :param orig_dev:
        The original net_device the skb was received on.
        (in case dev is a bond)
    :type orig_dev: struct net_device \*

.. _`fcoe_fip_recv.return`:

Return
------

0 for success

.. _`fcoe_fip_vlan_recv`:

fcoe_fip_vlan_recv
==================

.. c:function:: int fcoe_fip_vlan_recv(struct sk_buff *skb, struct net_device *netdev, struct packet_type *ptype, struct net_device *orig_dev)

    Handler for received FIP VLAN discovery frames

    :param skb:
        The receive skb
    :type skb: struct sk_buff \*

    :param netdev:
        The associated net device
    :type netdev: struct net_device \*

    :param ptype:
        The packet_type structure which was used to register this handler
    :type ptype: struct packet_type \*

    :param orig_dev:
        The original net_device the skb was received on.
        (in case dev is a bond)
    :type orig_dev: struct net_device \*

.. _`fcoe_fip_vlan_recv.return`:

Return
------

0 for success

.. _`fcoe_port_send`:

fcoe_port_send
==============

.. c:function:: void fcoe_port_send(struct fcoe_port *port, struct sk_buff *skb)

    Send an Ethernet-encapsulated FIP/FCoE frame

    :param port:
        The FCoE port
    :type port: struct fcoe_port \*

    :param skb:
        The FIP/FCoE packet to be sent
    :type skb: struct sk_buff \*

.. _`fcoe_fip_send`:

fcoe_fip_send
=============

.. c:function:: void fcoe_fip_send(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Send an Ethernet-encapsulated FIP frame

    :param fip:
        The FCoE controller
    :type fip: struct fcoe_ctlr \*

    :param skb:
        The FIP packet to be sent
    :type skb: struct sk_buff \*

.. _`fcoe_update_src_mac`:

fcoe_update_src_mac
===================

.. c:function:: void fcoe_update_src_mac(struct fc_lport *lport, u8 *addr)

    Update the Ethernet MAC filters

    :param lport:
        The local port to update the source MAC on
    :type lport: struct fc_lport \*

    :param addr:
        Unicast MAC address to add
    :type addr: u8 \*

.. _`fcoe_update_src_mac.description`:

Description
-----------

Remove any previously-set unicast MAC filter.
Add secondary FCoE MAC address filter for our OUI.

.. _`fcoe_get_src_mac`:

fcoe_get_src_mac
================

.. c:function:: u8 *fcoe_get_src_mac(struct fc_lport *lport)

    return the Ethernet source address for an lport

    :param lport:
        libfc lport
    :type lport: struct fc_lport \*

.. _`fcoe_lport_config`:

fcoe_lport_config
=================

.. c:function:: int fcoe_lport_config(struct fc_lport *lport)

    Set up a local port

    :param lport:
        The local port to be setup
    :type lport: struct fc_lport \*

.. _`fcoe_lport_config.return`:

Return
------

0 for success

.. _`fcoe_netdev_features_change`:

fcoe_netdev_features_change
===========================

.. c:function:: void fcoe_netdev_features_change(struct fc_lport *lport, struct net_device *netdev)

    Updates the lport's offload flags based on the LLD netdev's FCoE feature flags

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`fcoe_netdev_config`:

fcoe_netdev_config
==================

.. c:function:: int fcoe_netdev_config(struct fc_lport *lport, struct net_device *netdev)

    Set up net devive for SW FCoE

    :param lport:
        The local port that is associated with the net device
    :type lport: struct fc_lport \*

    :param netdev:
        The associated net device
    :type netdev: struct net_device \*

.. _`fcoe_netdev_config.description`:

Description
-----------

Must be called after \ :c:func:`fcoe_lport_config`\  as it will use local port mutex

.. _`fcoe_netdev_config.return`:

Return
------

0 for success

.. _`fcoe_shost_config`:

fcoe_shost_config
=================

.. c:function:: int fcoe_shost_config(struct fc_lport *lport, struct device *dev)

    Set up the SCSI host associated with a local port

    :param lport:
        The local port
    :type lport: struct fc_lport \*

    :param dev:
        The device associated with the SCSI host
    :type dev: struct device \*

.. _`fcoe_shost_config.description`:

Description
-----------

Must be called after \ :c:func:`fcoe_lport_config`\  and \ :c:func:`fcoe_netdev_config`\ 

.. _`fcoe_shost_config.return`:

Return
------

0 for success

.. _`fcoe_fdmi_info`:

fcoe_fdmi_info
==============

.. c:function:: void fcoe_fdmi_info(struct fc_lport *lport, struct net_device *netdev)

    Get FDMI related info from net devive for SW FCoE

    :param lport:
        The local port that is associated with the net device
    :type lport: struct fc_lport \*

    :param netdev:
        The associated net device
    :type netdev: struct net_device \*

.. _`fcoe_fdmi_info.description`:

Description
-----------

Must be called after \ :c:func:`fcoe_shost_config`\  as it will use local port mutex

.. _`fcoe_oem_match`:

fcoe_oem_match
==============

.. c:function:: bool fcoe_oem_match(struct fc_frame *fp)

    The match routine for the offloaded exchange manager

    :param fp:
        The I/O frame
    :type fp: struct fc_frame \*

.. _`fcoe_oem_match.description`:

Description
-----------

This routine will be associated with an exchange manager (EM). When
the libfc exchange handling code is looking for an EM to use it will
call this routine and pass it the frame that it wishes to send. This
routine will return True if the associated EM is to be used and False
if the echange code should continue looking for an EM.

The offload EM that this routine is associated with will handle any
packets that are for SCSI read requests.

This has been enhanced to work when FCoE stack is operating in target
mode.

.. _`fcoe_oem_match.return`:

Return
------

True for read types I/O, otherwise returns false.

.. _`fcoe_em_config`:

fcoe_em_config
==============

.. c:function:: int fcoe_em_config(struct fc_lport *lport)

    Allocate and configure an exchange manager

    :param lport:
        The local port that the new EM will be associated with
    :type lport: struct fc_lport \*

.. _`fcoe_em_config.return`:

Return
------

0 on success

.. _`fcoe_if_destroy`:

fcoe_if_destroy
===============

.. c:function:: void fcoe_if_destroy(struct fc_lport *lport)

    Tear down a SW FCoE instance

    :param lport:
        The local port to be destroyed
    :type lport: struct fc_lport \*

.. _`fcoe_if_destroy.locking`:

Locking
-------

Must be called with the RTNL mutex held.

.. _`fcoe_ddp_setup`:

fcoe_ddp_setup
==============

.. c:function:: int fcoe_ddp_setup(struct fc_lport *lport, u16 xid, struct scatterlist *sgl, unsigned int sgc)

    Call a LLD's ddp_setup through the net device

    :param lport:
        The local port to setup DDP for
    :type lport: struct fc_lport \*

    :param xid:
        The exchange ID for this DDP transfer
    :type xid: u16

    :param sgl:
        The scatterlist describing this transfer
    :type sgl: struct scatterlist \*

    :param sgc:
        The number of sg items
    :type sgc: unsigned int

.. _`fcoe_ddp_setup.return`:

Return
------

0 if the DDP context was not configured

.. _`fcoe_ddp_target`:

fcoe_ddp_target
===============

.. c:function:: int fcoe_ddp_target(struct fc_lport *lport, u16 xid, struct scatterlist *sgl, unsigned int sgc)

    Call a LLD's ddp_target through the net device

    :param lport:
        The local port to setup DDP for
    :type lport: struct fc_lport \*

    :param xid:
        The exchange ID for this DDP transfer
    :type xid: u16

    :param sgl:
        The scatterlist describing this transfer
    :type sgl: struct scatterlist \*

    :param sgc:
        The number of sg items
    :type sgc: unsigned int

.. _`fcoe_ddp_target.return`:

Return
------

0 if the DDP context was not configured

.. _`fcoe_ddp_done`:

fcoe_ddp_done
=============

.. c:function:: int fcoe_ddp_done(struct fc_lport *lport, u16 xid)

    Call a LLD's ddp_done through the net device

    :param lport:
        The local port to complete DDP on
    :type lport: struct fc_lport \*

    :param xid:
        The exchange ID for this DDP transfer
    :type xid: u16

.. _`fcoe_ddp_done.return`:

Return
------

the length of data that have been completed by DDP

.. _`fcoe_if_create`:

fcoe_if_create
==============

.. c:function:: struct fc_lport *fcoe_if_create(struct fcoe_interface *fcoe, struct device *parent, int npiv)

    Create a FCoE instance on an interface

    :param fcoe:
        The FCoE interface to create a local port on
    :type fcoe: struct fcoe_interface \*

    :param parent:
        The device pointer to be the parent in sysfs for the SCSI host
    :type parent: struct device \*

    :param npiv:
        Indicates if the port is a vport or not
    :type npiv: int

.. _`fcoe_if_create.description`:

Description
-----------

Creates a fc_lport instance and a Scsi_Host instance and configure them.

.. _`fcoe_if_create.return`:

Return
------

The allocated fc_lport or an error pointer

.. _`fcoe_if_init`:

fcoe_if_init
============

.. c:function:: int fcoe_if_init( void)

    Initialization routine for fcoe.ko

    :param void:
        no arguments
    :type void: 

.. _`fcoe_if_init.description`:

Description
-----------

Attaches the SW FCoE transport to the FC transport

.. _`fcoe_if_init.return`:

Return
------

0 on success

.. _`fcoe_if_exit`:

fcoe_if_exit
============

.. c:function:: int __exit fcoe_if_exit( void)

    Tear down fcoe.ko

    :param void:
        no arguments
    :type void: 

.. _`fcoe_if_exit.description`:

Description
-----------

Detaches the SW FCoE transport from the FC transport

.. _`fcoe_if_exit.return`:

Return
------

0 on success

.. _`fcoe_select_cpu`:

fcoe_select_cpu
===============

.. c:function:: unsigned int fcoe_select_cpu( void)

    Selects CPU to handle post-processing of incoming command.

    :param void:
        no arguments
    :type void: 

.. _`fcoe_select_cpu.description`:

Description
-----------

This routine selects next CPU based on cpumask to distribute
incoming requests in round robin.

.. _`fcoe_select_cpu.return`:

Return
------

int CPU number

.. _`fcoe_rcv`:

fcoe_rcv
========

.. c:function:: int fcoe_rcv(struct sk_buff *skb, struct net_device *netdev, struct packet_type *ptype, struct net_device *olddev)

    Receive packets from a net device

    :param skb:
        The received packet
    :type skb: struct sk_buff \*

    :param netdev:
        The net device that the packet was received on
    :type netdev: struct net_device \*

    :param ptype:
        The packet type context
    :type ptype: struct packet_type \*

    :param olddev:
        The last device net device
    :type olddev: struct net_device \*

.. _`fcoe_rcv.description`:

Description
-----------

This routine is called by NET_RX_SOFTIRQ. It receives a packet, builds a
FC frame and passes the frame to libfc.

.. _`fcoe_rcv.return`:

Return
------

0 for success

.. _`fcoe_alloc_paged_crc_eof`:

fcoe_alloc_paged_crc_eof
========================

.. c:function:: int fcoe_alloc_paged_crc_eof(struct sk_buff *skb, int tlen)

    Allocate a page to be used for the trailer CRC

    :param skb:
        The packet to be transmitted
    :type skb: struct sk_buff \*

    :param tlen:
        The total length of the trailer
    :type tlen: int

.. _`fcoe_alloc_paged_crc_eof.return`:

Return
------

0 for success

.. _`fcoe_xmit`:

fcoe_xmit
=========

.. c:function:: int fcoe_xmit(struct fc_lport *lport, struct fc_frame *fp)

    Transmit a FCoE frame

    :param lport:
        The local port that the frame is to be transmitted for
    :type lport: struct fc_lport \*

    :param fp:
        The frame to be transmitted
    :type fp: struct fc_frame \*

.. _`fcoe_xmit.return`:

Return
------

0 for success

.. _`fcoe_filter_frames`:

fcoe_filter_frames
==================

.. c:function:: int fcoe_filter_frames(struct fc_lport *lport, struct fc_frame *fp)

    filter out bad fcoe frames, i.e. bad CRC

    :param lport:
        The local port the frame was received on
    :type lport: struct fc_lport \*

    :param fp:
        The received frame
    :type fp: struct fc_frame \*

.. _`fcoe_filter_frames.return`:

Return
------

0 on passing filtering checks

.. _`fcoe_recv_frame`:

fcoe_recv_frame
===============

.. c:function:: void fcoe_recv_frame(struct sk_buff *skb)

    process a single received frame

    :param skb:
        frame to process
    :type skb: struct sk_buff \*

.. _`fcoe_receive_work`:

fcoe_receive_work
=================

.. c:function:: void fcoe_receive_work(struct work_struct *work)

    The per-CPU worker

    :param work:
        The work struct
    :type work: struct work_struct \*

.. _`fcoe_dev_setup`:

fcoe_dev_setup
==============

.. c:function:: void fcoe_dev_setup( void)

    Setup the link change notification interface

    :param void:
        no arguments
    :type void: 

.. _`fcoe_dev_cleanup`:

fcoe_dev_cleanup
================

.. c:function:: void fcoe_dev_cleanup( void)

    Cleanup the link change notification interface

    :param void:
        no arguments
    :type void: 

.. _`fcoe_device_notification`:

fcoe_device_notification
========================

.. c:function:: int fcoe_device_notification(struct notifier_block *notifier, ulong event, void *ptr)

    Handler for net device events

    :param notifier:
        The context of the notification
    :type notifier: struct notifier_block \*

    :param event:
        The type of event
    :type event: ulong

    :param ptr:
        The net device that the event was on
    :type ptr: void \*

.. _`fcoe_device_notification.description`:

Description
-----------

This function is called by the Ethernet driver in case of link change event.

.. _`fcoe_device_notification.return`:

Return
------

0 for success

.. _`fcoe_disable`:

fcoe_disable
============

.. c:function:: int fcoe_disable(struct net_device *netdev)

    Disables a FCoE interface

    :param netdev:
        The net_device object the Ethernet interface to create on
    :type netdev: struct net_device \*

.. _`fcoe_disable.description`:

Description
-----------

Called from fcoe transport.

.. _`fcoe_disable.return`:

Return
------

0 for success

.. _`fcoe_disable.deprecated`:

Deprecated
----------

use \ :c:func:`fcoe_ctlr_enabled`\ 

.. _`fcoe_enable`:

fcoe_enable
===========

.. c:function:: int fcoe_enable(struct net_device *netdev)

    Enables a FCoE interface

    :param netdev:
        The net_device object the Ethernet interface to create on
    :type netdev: struct net_device \*

.. _`fcoe_enable.description`:

Description
-----------

Called from fcoe transport.

.. _`fcoe_enable.return`:

Return
------

0 for success

.. _`fcoe_ctlr_enabled`:

fcoe_ctlr_enabled
=================

.. c:function:: int fcoe_ctlr_enabled(struct fcoe_ctlr_device *cdev)

    Enable or disable an FCoE Controller

    :param cdev:
        The FCoE Controller that is being enabled or disabled
    :type cdev: struct fcoe_ctlr_device \*

.. _`fcoe_ctlr_enabled.description`:

Description
-----------

fcoe_sysfs will ensure that the state of 'enabled' has
changed, so no checking is necessary here. This routine simply
calls fcoe_enable or fcoe_disable, both of which are deprecated.
When those routines are removed the functionality can be merged
here.

.. _`fcoe_ctlr_mode`:

fcoe_ctlr_mode
==============

.. c:function:: void fcoe_ctlr_mode(struct fcoe_ctlr_device *ctlr_dev)

    Switch FIP mode

    :param ctlr_dev:
        *undescribed*
    :type ctlr_dev: struct fcoe_ctlr_device \*

.. _`fcoe_ctlr_mode.description`:

Description
-----------

When the FIP mode has been changed we need to update
the multicast addresses to ensure we get the correct
frames.

.. _`fcoe_destroy`:

fcoe_destroy
============

.. c:function:: int fcoe_destroy(struct net_device *netdev)

    Destroy a FCoE interface

    :param netdev:
        The net_device object the Ethernet interface to create on
    :type netdev: struct net_device \*

.. _`fcoe_destroy.description`:

Description
-----------

Called from fcoe transport

.. _`fcoe_destroy.return`:

Return
------

0 for success

.. _`fcoe_destroy_work`:

fcoe_destroy_work
=================

.. c:function:: void fcoe_destroy_work(struct work_struct *work)

    Destroy a FCoE port in a deferred work context

    :param work:
        Handle to the FCoE port to be destroyed
    :type work: struct work_struct \*

.. _`fcoe_match`:

fcoe_match
==========

.. c:function:: bool fcoe_match(struct net_device *netdev)

    Check if the FCoE is supported on the given netdevice

    :param netdev:
        The net_device object the Ethernet interface to create on
    :type netdev: struct net_device \*

.. _`fcoe_match.description`:

Description
-----------

Called from fcoe transport.

.. _`fcoe_match.return`:

Return
------

always returns true as this is the default FCoE transport,
i.e., support all netdevs.

.. _`fcoe_dcb_create`:

fcoe_dcb_create
===============

.. c:function:: void fcoe_dcb_create(struct fcoe_interface *fcoe)

    Initialize DCB attributes and hooks

    :param fcoe:
        *undescribed*
    :type fcoe: struct fcoe_interface \*

.. _`_fcoe_create`:

\_fcoe_create
=============

.. c:function:: int _fcoe_create(struct net_device *netdev, enum fip_mode fip_mode, enum fcoe_create_link_state link_state)

    (internal) Create a fcoe interface

    :param netdev:
        The net_device object the Ethernet interface to create on
    :type netdev: struct net_device \*

    :param fip_mode:
        The FIP mode for this creation
    :type fip_mode: enum fip_mode

    :param link_state:
        The ctlr link state on creation
    :type link_state: enum fcoe_create_link_state

.. _`_fcoe_create.description`:

Description
-----------

Called from either the libfcoe 'create' module parameter
via fcoe_create or from fcoe_syfs's ctlr_create file.

libfcoe's 'create' module parameter is deprecated so some
consolidation of code can be done when that interface is
removed.

.. _`fcoe_create`:

fcoe_create
===========

.. c:function:: int fcoe_create(struct net_device *netdev, enum fip_mode fip_mode)

    Create a fcoe interface

    :param netdev:
        The net_device object the Ethernet interface to create on
    :type netdev: struct net_device \*

    :param fip_mode:
        The FIP mode for this creation
    :type fip_mode: enum fip_mode

.. _`fcoe_create.description`:

Description
-----------

Called from fcoe transport

.. _`fcoe_create.return`:

Return
------

0 for success

.. _`fcoe_ctlr_alloc`:

fcoe_ctlr_alloc
===============

.. c:function:: int fcoe_ctlr_alloc(struct net_device *netdev)

    Allocate a fcoe interface from fcoe_sysfs

    :param netdev:
        The net_device to be used by the allocated FCoE Controller
    :type netdev: struct net_device \*

.. _`fcoe_ctlr_alloc.description`:

Description
-----------

This routine is called from fcoe_sysfs. It will start the fcoe_ctlr
in a link_down state. The allows the user an opportunity to configure
the FCoE Controller from sysfs before enabling the FCoE Controller.

Creating in with this routine starts the FCoE Controller in Fabric
mode. The user can change to VN2VN or another mode before enabling.

.. _`fcoe_link_ok`:

fcoe_link_ok
============

.. c:function:: int fcoe_link_ok(struct fc_lport *lport)

    Check if the link is OK for a local port

    :param lport:
        The local port to check link on
    :type lport: struct fc_lport \*

.. _`fcoe_link_ok.return`:

Return
------

0 if link is UP and OK, -1 if not

.. _`fcoe_percpu_clean`:

fcoe_percpu_clean
=================

.. c:function:: void fcoe_percpu_clean(struct fc_lport *lport)

    Clear all pending skbs for an local port

    :param lport:
        The local port whose skbs are to be cleared
    :type lport: struct fc_lport \*

.. _`fcoe_percpu_clean.description`:

Description
-----------

Must be called with fcoe_create_mutex held to single-thread completion.

This flushes the pending skbs by flush the work item for each CPU. The work
item on each possible CPU is flushed because we may have used the per-CPU
struct of an offline CPU.

.. _`fcoe_reset`:

fcoe_reset
==========

.. c:function:: int fcoe_reset(struct Scsi_Host *shost)

    Reset a local port

    :param shost:
        The SCSI host associated with the local port to be reset
    :type shost: struct Scsi_Host \*

.. _`fcoe_reset.return`:

Return
------

Always 0 (return value required by FC transport template)

.. _`fcoe_hostlist_lookup_port`:

fcoe_hostlist_lookup_port
=========================

.. c:function:: struct fcoe_interface *fcoe_hostlist_lookup_port(const struct net_device *netdev)

    Find the FCoE interface associated with a net device

    :param netdev:
        The net device used as a key
    :type netdev: const struct net_device \*

.. _`fcoe_hostlist_lookup_port.locking`:

Locking
-------

Must be called with the RNL mutex held.

.. _`fcoe_hostlist_lookup_port.return`:

Return
------

NULL or the FCoE interface

.. _`fcoe_hostlist_lookup`:

fcoe_hostlist_lookup
====================

.. c:function:: struct fc_lport *fcoe_hostlist_lookup(const struct net_device *netdev)

    Find the local port associated with a given net device

    :param netdev:
        The netdevice used as a key
    :type netdev: const struct net_device \*

.. _`fcoe_hostlist_lookup.locking`:

Locking
-------

Must be called with the RTNL mutex held

.. _`fcoe_hostlist_lookup.return`:

Return
------

NULL or the local port

.. _`fcoe_hostlist_add`:

fcoe_hostlist_add
=================

.. c:function:: int fcoe_hostlist_add(const struct fc_lport *lport)

    Add the FCoE interface identified by a local port to the hostlist

    :param lport:
        The local port that identifies the FCoE interface to be added
    :type lport: const struct fc_lport \*

.. _`fcoe_hostlist_add.locking`:

Locking
-------

must be called with the RTNL mutex held

.. _`fcoe_hostlist_add.return`:

Return
------

0 for success

.. _`fcoe_hostlist_del`:

fcoe_hostlist_del
=================

.. c:function:: void fcoe_hostlist_del(const struct fc_lport *lport)

    Remove the FCoE interface identified by a local port to the hostlist

    :param lport:
        The local port that identifies the FCoE interface to be added
    :type lport: const struct fc_lport \*

.. _`fcoe_hostlist_del.locking`:

Locking
-------

must be called with the RTNL mutex held

.. _`fcoe_init`:

fcoe_init
=========

.. c:function:: int fcoe_init( void)

    Initialize fcoe.ko

    :param void:
        no arguments
    :type void: 

.. _`fcoe_init.return`:

Return
------

0 on success, or a negative value on failure

.. _`fcoe_exit`:

fcoe_exit
=========

.. c:function:: void __exit fcoe_exit( void)

    Clean up fcoe.ko

    :param void:
        no arguments
    :type void: 

.. _`fcoe_exit.return`:

Return
------

0 on success or a  negative value on failure

.. _`fcoe_flogi_resp`:

fcoe_flogi_resp
===============

.. c:function:: void fcoe_flogi_resp(struct fc_seq *seq, struct fc_frame *fp, void *arg)

    FCoE specific FLOGI and FDISC response handler

    :param seq:
        active sequence in the FLOGI or FDISC exchange
    :type seq: struct fc_seq \*

    :param fp:
        response frame, or error encoded in a pointer (timeout)
    :type fp: struct fc_frame \*

    :param arg:
        pointer to the fcoe_ctlr structure
    :type arg: void \*

.. _`fcoe_flogi_resp.description`:

Description
-----------

This handles MAC address management for FCoE, then passes control on to
the libfc FLOGI response handler.

.. _`fcoe_logo_resp`:

fcoe_logo_resp
==============

.. c:function:: void fcoe_logo_resp(struct fc_seq *seq, struct fc_frame *fp, void *arg)

    FCoE specific LOGO response handler

    :param seq:
        active sequence in the LOGO exchange
    :type seq: struct fc_seq \*

    :param fp:
        response frame, or error encoded in a pointer (timeout)
    :type fp: struct fc_frame \*

    :param arg:
        pointer to the fcoe_ctlr structure
    :type arg: void \*

.. _`fcoe_logo_resp.description`:

Description
-----------

This handles MAC address management for FCoE, then passes control on to
the libfc LOGO response handler.

.. _`fcoe_elsct_send`:

fcoe_elsct_send
===============

.. c:function:: struct fc_seq *fcoe_elsct_send(struct fc_lport *lport, u32 did, struct fc_frame *fp, unsigned int op, void (*resp)(struct fc_seq *, struct fc_frame *, void *), void *arg, u32 timeout)

    FCoE specific ELS handler

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param did:
        *undescribed*
    :type did: u32

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

    :param op:
        *undescribed*
    :type op: unsigned int

    :param void (\*resp)(struct fc_seq \*, struct fc_frame \*, void \*):
        *undescribed*

    :param arg:
        *undescribed*
    :type arg: void \*

    :param timeout:
        *undescribed*
    :type timeout: u32

.. _`fcoe_elsct_send.description`:

Description
-----------

This does special case handling of FIP encapsualted ELS exchanges for FCoE,
using FCoE specific response handlers and passing the FIP controller as
the argument (the lport is still available from the exchange).

Most of the work here is just handed off to the libfc routine.

.. _`fcoe_vport_create`:

fcoe_vport_create
=================

.. c:function:: int fcoe_vport_create(struct fc_vport *vport, bool disabled)

    create an fc_host/scsi_host for a vport

    :param vport:
        fc_vport object to create a new fc_host for
    :type vport: struct fc_vport \*

    :param disabled:
        start the new fc_host in a disabled state by default?
    :type disabled: bool

.. _`fcoe_vport_create.return`:

Return
------

0 for success

.. _`fcoe_vport_destroy`:

fcoe_vport_destroy
==================

.. c:function:: int fcoe_vport_destroy(struct fc_vport *vport)

    destroy the fc_host/scsi_host for a vport

    :param vport:
        fc_vport object that is being destroyed
    :type vport: struct fc_vport \*

.. _`fcoe_vport_destroy.return`:

Return
------

0 for success

.. _`fcoe_vport_remove`:

fcoe_vport_remove
=================

.. c:function:: void fcoe_vport_remove(struct fc_lport *lport)

    remove attached vports

    :param lport:
        lport for which the vports should be removed
    :type lport: struct fc_lport \*

.. _`fcoe_vport_disable`:

fcoe_vport_disable
==================

.. c:function:: int fcoe_vport_disable(struct fc_vport *vport, bool disable)

    change vport state

    :param vport:
        vport to bring online/offline
    :type vport: struct fc_vport \*

    :param disable:
        should the vport be disabled?
    :type disable: bool

.. _`fcoe_set_vport_symbolic_name`:

fcoe_set_vport_symbolic_name
============================

.. c:function:: void fcoe_set_vport_symbolic_name(struct fc_vport *vport)

    append vport string to symbolic name

    :param vport:
        fc_vport with a new symbolic name string
    :type vport: struct fc_vport \*

.. _`fcoe_set_vport_symbolic_name.description`:

Description
-----------

After generating a new symbolic name string, a new RSPN_ID request is
sent to the name server.  There is no response handler, so if it fails
for some reason it will not be retried.

.. _`fcoe_set_port_id`:

fcoe_set_port_id
================

.. c:function:: void fcoe_set_port_id(struct fc_lport *lport, u32 port_id, struct fc_frame *fp)

    Callback from libfc when Port_ID is set.

    :param lport:
        the local port
    :type lport: struct fc_lport \*

    :param port_id:
        the port ID
    :type port_id: u32

    :param fp:
        the received frame, if any, that caused the port_id to be set.
    :type fp: struct fc_frame \*

.. _`fcoe_set_port_id.description`:

Description
-----------

This routine handles the case where we received a FLOGI and are
entering point-to-point mode.  We need to call \ :c:func:`fcoe_ctlr_recv_flogi`\ 
so it can set the non-mapped mode and gateway address.

The FLOGI LS_ACC is handled by \ :c:func:`fcoe_flogi_resp`\ .

.. This file was automatic generated / don't edit.

