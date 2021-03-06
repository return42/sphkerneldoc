.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fcoe/fcoe_transport.c

.. _`fcoe_link_speed_update`:

fcoe_link_speed_update
======================

.. c:function:: int fcoe_link_speed_update(struct fc_lport *lport)

    Update the supported and actual link speeds

    :param lport:
        The local port to update speeds for
    :type lport: struct fc_lport \*

.. _`fcoe_link_speed_update.return`:

Return
------

0 if the ethtool query was successful
-1 if the ethtool query failed

.. _`__fcoe_get_lesb`:

\__fcoe_get_lesb
================

.. c:function:: void __fcoe_get_lesb(struct fc_lport *lport, struct fc_els_lesb *fc_lesb, struct net_device *netdev)

    Get the Link Error Status Block (LESB) for a given lport

    :param lport:
        The local port to update speeds for
    :type lport: struct fc_lport \*

    :param fc_lesb:
        Pointer to the LESB to be filled up
    :type fc_lesb: struct fc_els_lesb \*

    :param netdev:
        Pointer to the netdev that is associated with the lport
    :type netdev: struct net_device \*

.. _`__fcoe_get_lesb.description`:

Description
-----------

Note, the Link Error Status Block (LESB) for FCoE is defined in FC-BB-6
Clause 7.11 in v1.04.

.. _`fcoe_get_lesb`:

fcoe_get_lesb
=============

.. c:function:: void fcoe_get_lesb(struct fc_lport *lport, struct fc_els_lesb *fc_lesb)

    Fill the FCoE Link Error Status Block

    :param lport:
        the local port
    :type lport: struct fc_lport \*

    :param fc_lesb:
        the link error status block
    :type fc_lesb: struct fc_els_lesb \*

.. _`fcoe_ctlr_get_lesb`:

fcoe_ctlr_get_lesb
==================

.. c:function:: void fcoe_ctlr_get_lesb(struct fcoe_ctlr_device *ctlr_dev)

    Get the Link Error Status Block (LESB) for a given fcoe controller device

    :param ctlr_dev:
        The given fcoe controller device
    :type ctlr_dev: struct fcoe_ctlr_device \*

.. _`fcoe_validate_vport_create`:

fcoe_validate_vport_create
==========================

.. c:function:: int fcoe_validate_vport_create(struct fc_vport *vport)

    Validate a vport before creating it

    :param vport:
        NPIV port to be created
    :type vport: struct fc_vport \*

.. _`fcoe_validate_vport_create.description`:

Description
-----------

This routine is meant to add validation for a vport before creating it
via \ :c:func:`fcoe_vport_create`\ .

.. _`fcoe_validate_vport_create.current-validations-are`:

Current validations are
-----------------------

- WWPN supplied is unique for given lport

.. _`fcoe_get_wwn`:

fcoe_get_wwn
============

.. c:function:: int fcoe_get_wwn(struct net_device *netdev, u64 *wwn, int type)

    Get the world wide name from LLD if it supports it

    :param netdev:
        the associated net device
    :type netdev: struct net_device \*

    :param wwn:
        the output WWN
    :type wwn: u64 \*

    :param type:
        the type of WWN (WWPN or WWNN)
    :type type: int

.. _`fcoe_get_wwn.return`:

Return
------

0 for success

.. _`fcoe_fc_crc`:

fcoe_fc_crc
===========

.. c:function:: u32 fcoe_fc_crc(struct fc_frame *fp)

    Calculates the CRC for a given frame

    :param fp:
        The frame to be checksumed
    :type fp: struct fc_frame \*

.. _`fcoe_fc_crc.description`:

Description
-----------

This uses \ :c:func:`crc32`\  routine to calculate the CRC for a frame

.. _`fcoe_fc_crc.return`:

Return
------

The 32 bit CRC value

.. _`fcoe_start_io`:

fcoe_start_io
=============

.. c:function:: int fcoe_start_io(struct sk_buff *skb)

    Start FCoE I/O

    :param skb:
        The packet to be transmitted
    :type skb: struct sk_buff \*

.. _`fcoe_start_io.description`:

Description
-----------

This routine is called from the net device to start transmitting
FCoE packets.

.. _`fcoe_start_io.return`:

Return
------

0 for success

.. _`fcoe_clean_pending_queue`:

fcoe_clean_pending_queue
========================

.. c:function:: void fcoe_clean_pending_queue(struct fc_lport *lport)

    Dequeue a skb and free it

    :param lport:
        The local port to dequeue a skb on
    :type lport: struct fc_lport \*

.. _`fcoe_check_wait_queue`:

fcoe_check_wait_queue
=====================

.. c:function:: void fcoe_check_wait_queue(struct fc_lport *lport, struct sk_buff *skb)

    Attempt to clear the transmit backlog

    :param lport:
        The local port whose backlog is to be cleared
    :type lport: struct fc_lport \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`fcoe_check_wait_queue.description`:

Description
-----------

This empties the wait_queue, dequeues the head of the wait_queue queue
and calls \ :c:func:`fcoe_start_io`\  for each packet. If all skb have been
transmitted it returns the qlen. If an error occurs it restores
wait_queue (to try again later) and returns -1.

The wait_queue is used when the skb transmit fails. The failed skb
will go in the wait_queue which will be emptied by the timer function or
by the next skb transmit.

.. _`fcoe_queue_timer`:

fcoe_queue_timer
================

.. c:function:: void fcoe_queue_timer(struct timer_list *t)

    The fcoe queue timer

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`fcoe_queue_timer.description`:

Description
-----------

Calls fcoe_check_wait_queue on timeout

.. _`fcoe_get_paged_crc_eof`:

fcoe_get_paged_crc_eof
======================

.. c:function:: int fcoe_get_paged_crc_eof(struct sk_buff *skb, int tlen, struct fcoe_percpu_s *fps)

    Allocate a page to be used for the trailer CRC

    :param skb:
        The packet to be transmitted
    :type skb: struct sk_buff \*

    :param tlen:
        The total length of the trailer
    :type tlen: int

    :param fps:
        The fcoe context
    :type fps: struct fcoe_percpu_s \*

.. _`fcoe_get_paged_crc_eof.description`:

Description
-----------

This routine allocates a page for frame trailers. The page is re-used if
there is enough room left on it for the current trailer. If there isn't
enough buffer left a new page is allocated for the trailer. Reference to
the page from this function as well as the skbs using the page fragments
ensure that the page is freed at the appropriate time.

.. _`fcoe_get_paged_crc_eof.return`:

Return
------

0 for success

.. _`fcoe_transport_lookup`:

fcoe_transport_lookup
=====================

.. c:function:: struct fcoe_transport *fcoe_transport_lookup(struct net_device *netdev)

    find an fcoe transport that matches a netdev

    :param netdev:
        The netdev to look for from all attached transports
    :type netdev: struct net_device \*

.. _`fcoe_transport_lookup.description`:

Description
-----------

Returns : ptr to the fcoe transport that supports this netdev or NULL
if not found.

The ft_mutex should be held when this is called

.. _`fcoe_transport_attach`:

fcoe_transport_attach
=====================

.. c:function:: int fcoe_transport_attach(struct fcoe_transport *ft)

    Attaches an FCoE transport

    :param ft:
        The fcoe transport to be attached
    :type ft: struct fcoe_transport \*

.. _`fcoe_transport_attach.description`:

Description
-----------

Returns : 0 for success

.. _`fcoe_transport_detach`:

fcoe_transport_detach
=====================

.. c:function:: int fcoe_transport_detach(struct fcoe_transport *ft)

    Detaches an FCoE transport

    :param ft:
        The fcoe transport to be attached
    :type ft: struct fcoe_transport \*

.. _`fcoe_transport_detach.description`:

Description
-----------

Returns : 0 for success

.. _`fcoe_netdev_map_lookup`:

fcoe_netdev_map_lookup
======================

.. c:function:: struct fcoe_transport *fcoe_netdev_map_lookup(struct net_device *netdev)

    find the fcoe transport that matches the netdev on which it was created

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`fcoe_netdev_map_lookup.description`:

Description
-----------

Returns : ptr to the fcoe transport that supports this netdev or NULL
if not found.

The ft_mutex should be held when this is called

.. _`fcoe_if_to_netdev`:

fcoe_if_to_netdev
=================

.. c:function:: struct net_device *fcoe_if_to_netdev(const char *buffer)

    Parse a name buffer to get a net device

    :param buffer:
        The name of the net device
    :type buffer: const char \*

.. _`fcoe_if_to_netdev.return`:

Return
------

NULL or a ptr to net_device

.. _`libfcoe_device_notification`:

libfcoe_device_notification
===========================

.. c:function:: int libfcoe_device_notification(struct notifier_block *notifier, ulong event, void *ptr)

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

.. _`libfcoe_device_notification.description`:

Description
-----------

This function is called by the Ethernet driver in case of link change event.

.. _`libfcoe_device_notification.return`:

Return
------

0 for success

.. _`fcoe_transport_create`:

fcoe_transport_create
=====================

.. c:function:: int fcoe_transport_create(const char *buffer, const struct kernel_param *kp)

    Create a fcoe interface

    :param buffer:
        The name of the Ethernet interface to create on
    :type buffer: const char \*

    :param kp:
        The associated kernel param
    :type kp: const struct kernel_param \*

.. _`fcoe_transport_create.description`:

Description
-----------

Called from sysfs. This holds the ft_mutex while calling the
registered fcoe transport's create function.

.. _`fcoe_transport_create.return`:

Return
------

0 for success

.. _`fcoe_transport_destroy`:

fcoe_transport_destroy
======================

.. c:function:: int fcoe_transport_destroy(const char *buffer, const struct kernel_param *kp)

    Destroy a FCoE interface

    :param buffer:
        The name of the Ethernet interface to be destroyed
    :type buffer: const char \*

    :param kp:
        The associated kernel parameter
    :type kp: const struct kernel_param \*

.. _`fcoe_transport_destroy.description`:

Description
-----------

Called from sysfs. This holds the ft_mutex while calling the
registered fcoe transport's destroy function.

.. _`fcoe_transport_destroy.return`:

Return
------

0 for success

.. _`fcoe_transport_disable`:

fcoe_transport_disable
======================

.. c:function:: int fcoe_transport_disable(const char *buffer, const struct kernel_param *kp)

    Disables a FCoE interface

    :param buffer:
        The name of the Ethernet interface to be disabled
    :type buffer: const char \*

    :param kp:
        The associated kernel parameter
    :type kp: const struct kernel_param \*

.. _`fcoe_transport_disable.description`:

Description
-----------

Called from sysfs.

.. _`fcoe_transport_disable.return`:

Return
------

0 for success

.. _`fcoe_transport_enable`:

fcoe_transport_enable
=====================

.. c:function:: int fcoe_transport_enable(const char *buffer, const struct kernel_param *kp)

    Enables a FCoE interface

    :param buffer:
        The name of the Ethernet interface to be enabled
    :type buffer: const char \*

    :param kp:
        The associated kernel parameter
    :type kp: const struct kernel_param \*

.. _`fcoe_transport_enable.description`:

Description
-----------

Called from sysfs.

.. _`fcoe_transport_enable.return`:

Return
------

0 for success

.. _`libfcoe_init`:

libfcoe_init
============

.. c:function:: int libfcoe_init( void)

    Initialization routine for libfcoe.ko

    :param void:
        no arguments
    :type void: 

.. _`libfcoe_exit`:

libfcoe_exit
============

.. c:function:: void __exit libfcoe_exit( void)

    Tear down libfcoe.ko

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

