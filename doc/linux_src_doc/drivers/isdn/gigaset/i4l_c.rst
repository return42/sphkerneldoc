.. -*- coding: utf-8; mode: rst -*-

=====
i4l.c
=====


.. _`gigaset_skb_sent`:

gigaset_skb_sent
================

.. c:function:: void gigaset_skb_sent (struct bc_state *bcs, struct sk_buff *skb)

    acknowledge sending an skb

    :param struct bc_state \*bcs:
        B channel descriptor structure.

    :param struct sk_buff \*skb:
        sent data.



.. _`gigaset_skb_sent.description`:

Description
-----------

Called by hardware module {bas,ser,usb}_gigaset when the data in a
skb has been successfully sent, for signalling completion to the LL.



.. _`gigaset_skb_rcvd`:

gigaset_skb_rcvd
================

.. c:function:: void gigaset_skb_rcvd (struct bc_state *bcs, struct sk_buff *skb)

    pass received skb to LL

    :param struct bc_state \*bcs:
        B channel descriptor structure.

    :param struct sk_buff \*skb:
        received data.



.. _`gigaset_skb_rcvd.description`:

Description
-----------

Called by hardware module {bas,ser,usb}_gigaset when user data has
been successfully received, for passing to the LL.



.. _`gigaset_skb_rcvd.warning`:

Warning
-------

skb must not be accessed anymore!



.. _`gigaset_isdn_rcv_err`:

gigaset_isdn_rcv_err
====================

.. c:function:: void gigaset_isdn_rcv_err (struct bc_state *bcs)

    signal receive error

    :param struct bc_state \*bcs:
        B channel descriptor structure.



.. _`gigaset_isdn_rcv_err.description`:

Description
-----------

Called by hardware module {bas,ser,usb}_gigaset when a receive error
has occurred, for signalling to the LL.



.. _`gigaset_isdn_icall`:

gigaset_isdn_icall
==================

.. c:function:: int gigaset_isdn_icall (struct at_state_t *at_state)

    signal incoming call

    :param struct at_state_t \*at_state:
        connection state structure.



.. _`gigaset_isdn_icall.description`:

Description
-----------

Called by main module to notify the LL that an incoming call has been
received. ``at_state`` contains the parameters of the call.



.. _`gigaset_isdn_icall.return-value`:

Return value
------------

call disposition (ICALL\_\*)



.. _`gigaset_isdn_connd`:

gigaset_isdn_connD
==================

.. c:function:: void gigaset_isdn_connD (struct bc_state *bcs)

    signal D channel connect

    :param struct bc_state \*bcs:
        B channel descriptor structure.



.. _`gigaset_isdn_connd.description`:

Description
-----------

Called by main module to notify the LL that the D channel connection has
been established.



.. _`gigaset_isdn_hupd`:

gigaset_isdn_hupD
=================

.. c:function:: void gigaset_isdn_hupD (struct bc_state *bcs)

    signal D channel hangup

    :param struct bc_state \*bcs:
        B channel descriptor structure.



.. _`gigaset_isdn_hupd.description`:

Description
-----------

Called by main module to notify the LL that the D channel connection has
been shut down.



.. _`gigaset_isdn_connb`:

gigaset_isdn_connB
==================

.. c:function:: void gigaset_isdn_connB (struct bc_state *bcs)

    signal B channel connect

    :param struct bc_state \*bcs:
        B channel descriptor structure.



.. _`gigaset_isdn_connb.description`:

Description
-----------

Called by main module to notify the LL that the B channel connection has
been established.



.. _`gigaset_isdn_hupb`:

gigaset_isdn_hupB
=================

.. c:function:: void gigaset_isdn_hupB (struct bc_state *bcs)

    signal B channel hangup

    :param struct bc_state \*bcs:
        B channel descriptor structure.



.. _`gigaset_isdn_hupb.description`:

Description
-----------

Called by main module to notify the LL that the B channel connection has
been shut down.



.. _`gigaset_isdn_start`:

gigaset_isdn_start
==================

.. c:function:: void gigaset_isdn_start (struct cardstate *cs)

    signal device availability

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_isdn_start.description`:

Description
-----------

Called by main module to notify the LL that the device is available for
use.



.. _`gigaset_isdn_stop`:

gigaset_isdn_stop
=================

.. c:function:: void gigaset_isdn_stop (struct cardstate *cs)

    signal device unavailability

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_isdn_stop.description`:

Description
-----------

Called by main module to notify the LL that the device is no longer
available for use.



.. _`gigaset_isdn_regdev`:

gigaset_isdn_regdev
===================

.. c:function:: int gigaset_isdn_regdev (struct cardstate *cs, const char *isdnid)

    register to LL

    :param struct cardstate \*cs:
        device descriptor structure.

    :param const char \*isdnid:
        device name.



.. _`gigaset_isdn_regdev.return-value`:

Return value
------------

0 on success, error code < 0 on failure



.. _`gigaset_isdn_unregdev`:

gigaset_isdn_unregdev
=====================

.. c:function:: void gigaset_isdn_unregdev (struct cardstate *cs)

    unregister device from LL

    :param struct cardstate \*cs:
        device descriptor structure.



.. _`gigaset_isdn_regdrv`:

gigaset_isdn_regdrv
===================

.. c:function:: void gigaset_isdn_regdrv ( void)

    register driver to LL

    :param void:
        no arguments



.. _`gigaset_isdn_unregdrv`:

gigaset_isdn_unregdrv
=====================

.. c:function:: void gigaset_isdn_unregdrv ( void)

    unregister driver from LL

    :param void:
        no arguments

