.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x.h

.. _`bnx2x_set_mac_one`:

bnx2x_set_mac_one
=================

.. c:function:: int bnx2x_set_mac_one(struct bnx2x *bp, u8 *mac, struct bnx2x_vlan_mac_obj *obj, bool set, int mac_type, unsigned long *ramrod_flags)

    configure a single MAC address

    :param bp:
        driver handle
    :type bp: struct bnx2x \*

    :param mac:
        MAC to configure
    :type mac: u8 \*

    :param obj:
        MAC object handle
    :type obj: struct bnx2x_vlan_mac_obj \*

    :param set:
        if 'true' add a new MAC, otherwise - delete
    :type set: bool

    :param mac_type:
        the type of the MAC to configure (e.g. ETH, UC list)
    :type mac_type: int

    :param ramrod_flags:
        RAMROD_XXX flags (e.g. RAMROD_CONT, RAMROD_COMP_WAIT)
    :type ramrod_flags: unsigned long \*

.. _`bnx2x_set_mac_one.description`:

Description
-----------

Configures one MAC according to provided parameters or continues the
execution of previously scheduled commands if RAMROD_CONT is set in
ramrod_flags.

Returns zero if operation has successfully completed, a positive value if the
operation has been successfully scheduled and a negative - if a requested
operations has failed.

.. _`bnx2x_del_all_macs`:

bnx2x_del_all_macs
==================

.. c:function:: int bnx2x_del_all_macs(struct bnx2x *bp, struct bnx2x_vlan_mac_obj *mac_obj, int mac_type, bool wait_for_comp)

    delete all MACs configured for the specific MAC object

    :param bp:
        driver handle
    :type bp: struct bnx2x \*

    :param mac_obj:
        MAC object handle
    :type mac_obj: struct bnx2x_vlan_mac_obj \*

    :param mac_type:
        type of the MACs to clear (BNX2X_XXX_MAC)
    :type mac_type: int

    :param wait_for_comp:
        if 'true' block until completion
    :type wait_for_comp: bool

.. _`bnx2x_del_all_macs.description`:

Description
-----------

Deletes all MACs of the specific type (e.g. ETH, UC list).

Returns zero if operation has successfully completed, a positive value if the
operation has been successfully scheduled and a negative - if a requested
operations has failed.

.. This file was automatic generated / don't edit.

