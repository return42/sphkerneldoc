.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/bonding/bond_alb.c

.. _`alb_change_hw_addr_on_detach`:

alb_change_hw_addr_on_detach
============================

.. c:function:: void alb_change_hw_addr_on_detach(struct bonding *bond, struct slave *slave)

    :param bond:
        bonding we're working on
    :type bond: struct bonding \*

    :param slave:
        the slave that was just detached
    :type slave: struct slave \*

.. _`alb_change_hw_addr_on_detach.description`:

Description
-----------

We assume that \ ``slave``\  was already detached from the slave list.

If \ ``slave``\ 's permanent hw address is different both from its current
address and from \ ``bond``\ 's address, then somewhere in the bond there's
a slave that has \ ``slave``\ 's permanet address as its current address.
We'll make sure that that slave no longer uses \ ``slave``\ 's permanent address.

Caller must hold RTNL and no other locks

.. _`alb_handle_addr_collision_on_attach`:

alb_handle_addr_collision_on_attach
===================================

.. c:function:: int alb_handle_addr_collision_on_attach(struct bonding *bond, struct slave *slave)

    :param bond:
        bonding we're working on
    :type bond: struct bonding \*

    :param slave:
        the slave that was just attached
    :type slave: struct slave \*

.. _`alb_handle_addr_collision_on_attach.description`:

Description
-----------

checks uniqueness of slave's mac address and handles the case the
new slave uses the bonds mac address.

If the permanent hw address of \ ``slave``\  is \ ``bond``\ 's hw address, we need to
find a different hw address to give \ ``slave``\ , that isn't in use by any other
slave in the bond. This address must be, of course, one of the permanent
addresses of the other slaves.

We go over the slave list, and for each slave there we compare its
permanent hw address with the current address of all the other slaves.
If no match was found, then we've found a slave with a permanent address
that isn't used by any other slave in the bond, so we can assign it to
\ ``slave``\ .

.. _`alb_handle_addr_collision_on_attach.assumption`:

assumption
----------

this function is called before \ ``slave``\  is attached to the
bond slave list.

.. _`alb_set_mac_address`:

alb_set_mac_address
===================

.. c:function:: int alb_set_mac_address(struct bonding *bond, void *addr)

    :param bond:
        *undescribed*
    :type bond: struct bonding \*

    :param addr:
        *undescribed*
    :type addr: void \*

.. _`alb_set_mac_address.description`:

Description
-----------

In TLB mode all slaves are configured to the bond's hw address, but set
their dev_addr field to different addresses (based on their permanent hw
addresses).

For each slave, this function sets the interface to the new address and then
changes its dev_addr field to its previous value.

Unwinding assumes bond's mac address has not yet changed.

.. _`bond_alb_handle_active_change`:

bond_alb_handle_active_change
=============================

.. c:function:: void bond_alb_handle_active_change(struct bonding *bond, struct slave *new_slave)

    assign new curr_active_slave

    :param bond:
        our bonding struct
    :type bond: struct bonding \*

    :param new_slave:
        new slave to assign
    :type new_slave: struct slave \*

.. _`bond_alb_handle_active_change.description`:

Description
-----------

Set the bond->curr_active_slave to \ ``new_slave``\  and handle
mac address swapping and promiscuity changes as needed.

Caller must hold RTNL

.. This file was automatic generated / don't edit.

