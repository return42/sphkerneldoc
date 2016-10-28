.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/bonding/bond_main.c

.. _`bond_dev_queue_xmit`:

bond_dev_queue_xmit
===================

.. c:function:: void bond_dev_queue_xmit(struct bonding *bond, struct sk_buff *skb, struct net_device *slave_dev)

    Prepare skb for xmit.

    :param struct bonding \*bond:
        bond device that got this skb for tx.

    :param struct sk_buff \*skb:
        hw accel VLAN tagged skb to transmit

    :param struct net_device \*slave_dev:
        slave that is supposed to xmit this skbuff

.. _`bond_vlan_rx_add_vid`:

bond_vlan_rx_add_vid
====================

.. c:function:: int bond_vlan_rx_add_vid(struct net_device *bond_dev, __be16 proto, u16 vid)

    Propagates adding an id to slaves

    :param struct net_device \*bond_dev:
        bonding net device that got called

    :param __be16 proto:
        *undescribed*

    :param u16 vid:
        vlan id being added

.. _`bond_vlan_rx_kill_vid`:

bond_vlan_rx_kill_vid
=====================

.. c:function:: int bond_vlan_rx_kill_vid(struct net_device *bond_dev, __be16 proto, u16 vid)

    Propagates deleting an id to slaves

    :param struct net_device \*bond_dev:
        bonding net device that got called

    :param __be16 proto:
        *undescribed*

    :param u16 vid:
        vlan id being removed

.. _`bond_set_dev_addr`:

bond_set_dev_addr
=================

.. c:function:: void bond_set_dev_addr(struct net_device *bond_dev, struct net_device *slave_dev)

    clone slave's address to bond

    :param struct net_device \*bond_dev:
        bond net device

    :param struct net_device \*slave_dev:
        slave net device

.. _`bond_set_dev_addr.description`:

Description
-----------

Should be called with RTNL held.

.. _`bond_find_best_slave`:

bond_find_best_slave
====================

.. c:function:: struct slave *bond_find_best_slave(struct bonding *bond)

    select the best available slave to be the active one

    :param struct bonding \*bond:
        our bonding struct

.. _`bond_change_active_slave`:

bond_change_active_slave
========================

.. c:function:: void bond_change_active_slave(struct bonding *bond, struct slave *new_active)

    change the active slave into the specified one

    :param struct bonding \*bond:
        our bonding struct

    :param struct slave \*new_active:
        *undescribed*

.. _`bond_change_active_slave.description`:

Description
-----------

Set the new slave to the bond's settings and unset them on the old
curr_active_slave.
Setting include flags, mc-list, promiscuity, allmulti, etc.

If \ ``new``\ 's link state is \ ``BOND_LINK_BACK``\  we'll set it to \ ``BOND_LINK_UP``\ ,
because it is apparently the best available slave we have, even though its
updelay hasn't timed out yet.

Caller must hold RTNL.

.. _`bond_select_active_slave`:

bond_select_active_slave
========================

.. c:function:: void bond_select_active_slave(struct bonding *bond)

    select a new active slave, if needed

    :param struct bonding \*bond:
        our bonding struct

.. _`bond_select_active_slave.this-functions-should-be-called-when-one-of-the-following-occurs`:

This functions should be called when one of the following occurs
----------------------------------------------------------------

- The old curr_active_slave has been released or lost its link.
- The primary_slave has got its link back.
- A slave has got its link back and there's no old curr_active_slave.

Caller must hold RTNL.

.. _`bond_xmit_hash`:

bond_xmit_hash
==============

.. c:function:: u32 bond_xmit_hash(struct bonding *bond, struct sk_buff *skb)

    generate a hash value based on the xmit policy

    :param struct bonding \*bond:
        bonding device

    :param struct sk_buff \*skb:
        buffer to use for headers

.. _`bond_xmit_hash.description`:

Description
-----------

This function will extract the necessary headers from the skb buffer and use
them to generate a hash based on the xmit_policy set in the bonding device

.. _`bond_xmit_slave_id`:

bond_xmit_slave_id
==================

.. c:function:: void bond_xmit_slave_id(struct bonding *bond, struct sk_buff *skb, int slave_id)

    transmit skb through slave with slave_id

    :param struct bonding \*bond:
        bonding device that is transmitting

    :param struct sk_buff \*skb:
        buffer to transmit

    :param int slave_id:
        slave id up to slave_cnt-1 through which to transmit

.. _`bond_xmit_slave_id.description`:

Description
-----------

This function tries to transmit through slave with slave_id but in case
it fails, it tries to find the first available slave for transmission.
The skb is consumed in all cases, thus the function is void.

.. _`bond_rr_gen_slave_id`:

bond_rr_gen_slave_id
====================

.. c:function:: u32 bond_rr_gen_slave_id(struct bonding *bond)

    generate slave id based on packets_per_slave

    :param struct bonding \*bond:
        bonding device to use

.. _`bond_rr_gen_slave_id.description`:

Description
-----------

Based on the value of the bonding device's packets_per_slave parameter
this function generates a slave id, which is usually used as the next
slave to transmit through.

.. This file was automatic generated / don't edit.

