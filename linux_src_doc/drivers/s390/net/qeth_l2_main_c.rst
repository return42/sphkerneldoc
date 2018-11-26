.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_l2_main.c

.. _`qeth_bridge_emit_host_event`:

qeth_bridge_emit_host_event
===========================

.. c:function:: void qeth_bridge_emit_host_event(struct qeth_card *card, enum qeth_an_event_type evtype, u8 code, struct net_if_token *token, struct mac_addr_lnid *addr_lnid)

    bridgeport address change notification

    :param card:
        qeth_card structure pointer, for udev events.
    :type card: struct qeth_card \*

    :param evtype:
        "normal" register/unregister, or abort, or reset. For abort
        and reset token and addr_lnid are unused and may be NULL.
    :type evtype: enum qeth_an_event_type

    :param code:
        event bitmask: high order bit 0x80 value 1 means removal of an
        object, 0 - addition of an object.
        0x01 - VLAN, 0x02 - MAC, 0x03 - VLAN and MAC.
    :type code: u8

    :param token:
        "network token" structure identifying physical address of the port.
    :type token: struct net_if_token \*

    :param addr_lnid:
        pointer to structure with MAC address and VLAN ID.
    :type addr_lnid: struct mac_addr_lnid \*

.. _`qeth_bridge_emit_host_event.description`:

Description
-----------

This function is called when registrations and deregistrations are
reported by the hardware, and also when notifications are enabled -
for all currently registered addresses.

.. _`qeth_bridgeport_makerc`:

qeth_bridgeport_makerc
======================

.. c:function:: int qeth_bridgeport_makerc(struct qeth_card *card, struct _qeth_sbp_cbctl *cbctl, enum qeth_ipa_sbp_cmd setcmd)

    derive "traditional" error from hardware codes.

    :param card:
        qeth_card structure pointer, for debug messages.
    :type card: struct qeth_card \*

    :param cbctl:
        state structure with hardware return codes.
    :type cbctl: struct _qeth_sbp_cbctl \*

    :param setcmd:
        IPA command code
    :type setcmd: enum qeth_ipa_sbp_cmd

.. _`qeth_bridgeport_makerc.description`:

Description
-----------

Returns negative errno-compatible error indication or 0 on success.

.. _`qeth_bridgeport_query_support`:

qeth_bridgeport_query_support
=============================

.. c:function:: void qeth_bridgeport_query_support(struct qeth_card *card)

    store bitmask of supported subfunctions.

    :param card:
        qeth_card structure pointer.
    :type card: struct qeth_card \*

.. _`qeth_bridgeport_query_support.description`:

Description
-----------

Sets bitmask of supported setbridgeport subfunctions in the qeth_card

.. _`qeth_bridgeport_query_support.strucutre`:

strucutre
---------

card->options.sbp.supported_funcs.

.. _`qeth_bridgeport_query_ports`:

qeth_bridgeport_query_ports
===========================

.. c:function:: int qeth_bridgeport_query_ports(struct qeth_card *card, enum qeth_sbp_roles *role, enum qeth_sbp_states *state)

    query local bridgeport status.

    :param card:
        qeth_card structure pointer.
    :type card: struct qeth_card \*

    :param role:
        Role of the port: 0-none, 1-primary, 2-secondary.
    :type role: enum qeth_sbp_roles \*

    :param state:
        State of the port: 0-inactive, 1-standby, 2-active.
    :type state: enum qeth_sbp_states \*

.. _`qeth_bridgeport_query_ports.description`:

Description
-----------

Returns negative errno-compatible error indication or 0 on success.

'role' and 'state' are not updated in case of hardware operation failure.

.. _`qeth_bridgeport_setrole`:

qeth_bridgeport_setrole
=======================

.. c:function:: int qeth_bridgeport_setrole(struct qeth_card *card, enum qeth_sbp_roles role)

    Assign primary role to the port.

    :param card:
        qeth_card structure pointer.
    :type card: struct qeth_card \*

    :param role:
        Role to assign.
    :type role: enum qeth_sbp_roles

.. _`qeth_bridgeport_setrole.description`:

Description
-----------

Returns negative errno-compatible error indication or 0 on success.

.. _`qeth_anset_makerc`:

qeth_anset_makerc
=================

.. c:function:: int qeth_anset_makerc(struct qeth_card *card, int pnso_rc, u16 response)

    derive "traditional" error from hardware codes.

    :param card:
        qeth_card structure pointer, for debug messages.
    :type card: struct qeth_card \*

    :param pnso_rc:
        *undescribed*
    :type pnso_rc: int

    :param response:
        *undescribed*
    :type response: u16

.. _`qeth_anset_makerc.description`:

Description
-----------

Returns negative errno-compatible error indication or 0 on success.

.. _`qeth_bridgeport_an_set`:

qeth_bridgeport_an_set
======================

.. c:function:: int qeth_bridgeport_an_set(struct qeth_card *card, int enable)

    Enable or disable bridgeport address notification

    :param card:
        qeth_card structure pointer.
    :type card: struct qeth_card \*

    :param enable:
        0 - disable, non-zero - enable notifications
    :type enable: int

.. _`qeth_bridgeport_an_set.description`:

Description
-----------

Returns negative errno-compatible error indication or 0 on success.

On enable, emits a series of address notifications udev events for all
currently registered hosts.

.. This file was automatic generated / don't edit.

