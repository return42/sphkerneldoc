.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fnic/fnic_fcs.c

.. _`is_fnic_fip_flogi_reject`:

is_fnic_fip_flogi_reject
========================

.. c:function:: int is_fnic_fip_flogi_reject(struct fcoe_ctlr *fip, struct sk_buff *skb)

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the frame

    :param struct sk_buff \*skb:
        The received FIP frame

.. _`is_fnic_fip_flogi_reject.description`:

Description
-----------

Returns non-zero if the frame is rejected with unsupported cmd with
insufficient resource els explanation.

.. _`fnic_import_rq_eth_pkt`:

fnic_import_rq_eth_pkt
======================

.. c:function:: int fnic_import_rq_eth_pkt(struct fnic *fnic, struct sk_buff *skb)

    handle received FCoE or FIP frame.

    :param struct fnic \*fnic:
        fnic instance.

    :param struct sk_buff \*skb:
        Ethernet Frame.

.. _`fnic_update_mac_locked`:

fnic_update_mac_locked
======================

.. c:function:: void fnic_update_mac_locked(struct fnic *fnic, u8 *new)

    set data MAC address and filters.

    :param struct fnic \*fnic:
        fnic instance.

    :param u8 \*new:
        newly-assigned FCoE MAC address.

.. _`fnic_update_mac_locked.description`:

Description
-----------

Called with the fnic lock held.

.. _`fnic_update_mac`:

fnic_update_mac
===============

.. c:function:: void fnic_update_mac(struct fc_lport *lport, u8 *new)

    set data MAC address and filters.

    :param struct fc_lport \*lport:
        local port.

    :param u8 \*new:
        newly-assigned FCoE MAC address.

.. _`fnic_set_port_id`:

fnic_set_port_id
================

.. c:function:: void fnic_set_port_id(struct fc_lport *lport, u32 port_id, struct fc_frame *fp)

    set the port_ID after successful FLOGI.

    :param struct fc_lport \*lport:
        local port.

    :param u32 port_id:
        assigned FC_ID.

    :param struct fc_frame \*fp:
        received frame containing the FLOGI accept or NULL.

.. _`fnic_set_port_id.description`:

Description
-----------

This is called from libfc when a new FC_ID has been assigned.
This causes us to reset the firmware to FC_MODE and setup the new MAC
address and FC_ID.

It is also called with FC_ID 0 when we're logged off.

If the FC_ID is due to point-to-point, fp may be NULL.

.. _`fnic_eth_send`:

fnic_eth_send
=============

.. c:function:: void fnic_eth_send(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Send Ethernet frame.

    :param struct fcoe_ctlr \*fip:
        fcoe_ctlr instance.

    :param struct sk_buff \*skb:
        Ethernet Frame, FIP, without VLAN encapsulation.

.. _`fnic_flush_tx`:

fnic_flush_tx
=============

.. c:function:: void fnic_flush_tx(struct fnic *fnic)

    send queued frames.

    :param struct fnic \*fnic:
        fnic device

.. _`fnic_flush_tx.description`:

Description
-----------

Send frames that were waiting to go out in FC or Ethernet mode.
Whenever changing modes we purge queued frames, so these frames should
be queued for the stable mode that we're in, either FC or Ethernet.

Called without fnic_lock held.

.. _`fnic_set_eth_mode`:

fnic_set_eth_mode
=================

.. c:function:: void fnic_set_eth_mode(struct fnic *fnic)

    put fnic into ethernet mode.

    :param struct fnic \*fnic:
        fnic device

.. _`fnic_set_eth_mode.description`:

Description
-----------

Called without fnic lock held.

.. This file was automatic generated / don't edit.

