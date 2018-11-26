.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_s_ac.c

.. _`llc_sap_action_unitdata_ind`:

llc_sap_action_unitdata_ind
===========================

.. c:function:: int llc_sap_action_unitdata_ind(struct llc_sap *sap, struct sk_buff *skb)

    forward UI PDU to network layer

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to forward
    :type skb: struct sk_buff \*

.. _`llc_sap_action_unitdata_ind.description`:

Description
-----------

Received a UI PDU from MAC layer; forward to network layer as a
UNITDATA INDICATION; verify our event is the kind we expect

.. _`llc_sap_action_send_ui`:

llc_sap_action_send_ui
======================

.. c:function:: int llc_sap_action_send_ui(struct llc_sap *sap, struct sk_buff *skb)

    sends UI PDU resp to UNITDATA REQ to MAC layer

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_send_ui.description`:

Description
-----------

Sends a UI PDU to the MAC layer in response to a UNITDATA REQUEST
primitive from the network layer. Verifies event is a primitive type of
event. Verify the primitive is a UNITDATA REQUEST.

.. _`llc_sap_action_send_xid_c`:

llc_sap_action_send_xid_c
=========================

.. c:function:: int llc_sap_action_send_xid_c(struct llc_sap *sap, struct sk_buff *skb)

    send XID PDU as response to XID REQ

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_send_xid_c.description`:

Description
-----------

Send a XID command PDU to MAC layer in response to a XID REQUEST
primitive from the network layer. Verify event is a primitive type
event. Verify the primitive is a XID REQUEST.

.. _`llc_sap_action_send_xid_r`:

llc_sap_action_send_xid_r
=========================

.. c:function:: int llc_sap_action_send_xid_r(struct llc_sap *sap, struct sk_buff *skb)

    send XID PDU resp to MAC for received XID

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_send_xid_r.description`:

Description
-----------

Send XID response PDU to MAC in response to an earlier received XID
command PDU. Verify event is a PDU type event

.. _`llc_sap_action_send_test_c`:

llc_sap_action_send_test_c
==========================

.. c:function:: int llc_sap_action_send_test_c(struct llc_sap *sap, struct sk_buff *skb)

    send TEST PDU to MAC in resp to TEST REQ

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_send_test_c.description`:

Description
-----------

Send a TEST command PDU to the MAC layer in response to a TEST REQUEST
primitive from the network layer. Verify event is a primitive type
event; verify the primitive is a TEST REQUEST.

.. _`llc_sap_action_report_status`:

llc_sap_action_report_status
============================

.. c:function:: int llc_sap_action_report_status(struct llc_sap *sap, struct sk_buff *skb)

    report data link status to layer mgmt

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_report_status.description`:

Description
-----------

Report data link status to layer management. Verify our event is the
kind we expect.

.. _`llc_sap_action_xid_ind`:

llc_sap_action_xid_ind
======================

.. c:function:: int llc_sap_action_xid_ind(struct llc_sap *sap, struct sk_buff *skb)

    send XID PDU resp to net layer via XID IND

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_xid_ind.description`:

Description
-----------

Send a XID response PDU to the network layer via a XID INDICATION
primitive.

.. _`llc_sap_action_test_ind`:

llc_sap_action_test_ind
=======================

.. c:function:: int llc_sap_action_test_ind(struct llc_sap *sap, struct sk_buff *skb)

    send TEST PDU to net layer via TEST IND

    :param sap:
        SAP
    :type sap: struct llc_sap \*

    :param skb:
        the event to send
    :type skb: struct sk_buff \*

.. _`llc_sap_action_test_ind.description`:

Description
-----------

Send a TEST response PDU to the network layer via a TEST INDICATION
primitive. Verify our event is a PDU type event.

.. This file was automatic generated / don't edit.

