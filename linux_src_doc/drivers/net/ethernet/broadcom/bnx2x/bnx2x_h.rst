.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x.h

.. _`bnx2x_set_mac_one`:

bnx2x_set_mac_one
=================

.. c:function:: int bnx2x_set_mac_one(struct bnx2x *bp, u8 *mac, struct bnx2x_vlan_mac_obj *obj, bool set, int mac_type, unsigned long *ramrod_flags)

    configure a single MAC address

    :param struct bnx2x \*bp:
        driver handle

    :param u8 \*mac:
        MAC to configure

    :param struct bnx2x_vlan_mac_obj \*obj:
        MAC object handle

    :param bool set:
        if 'true' add a new MAC, otherwise - delete

    :param int mac_type:
        the type of the MAC to configure (e.g. ETH, UC list)

    :param unsigned long \*ramrod_flags:
        RAMROD_XXX flags (e.g. RAMROD_CONT, RAMROD_COMP_WAIT)

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

    :param struct bnx2x \*bp:
        driver handle

    :param struct bnx2x_vlan_mac_obj \*mac_obj:
        MAC object handle

    :param int mac_type:
        type of the MACs to clear (BNX2X_XXX_MAC)

    :param bool wait_for_comp:
        if 'true' block until completion

.. _`bnx2x_del_all_macs.description`:

Description
-----------

Deletes all MACs of the specific type (e.g. ETH, UC list).

Returns zero if operation has successfully completed, a positive value if the
operation has been successfully scheduled and a negative - if a requested
operations has failed.

.. This file was automatic generated / don't edit.

