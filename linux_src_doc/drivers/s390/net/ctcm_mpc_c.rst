.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/ctcm_mpc.c

.. _`ctcmpc_unpack_skb`:

ctcmpc_unpack_skb
=================

.. c:function:: void ctcmpc_unpack_skb(struct channel *ch, struct sk_buff *pskb)

    upper layers. special MPC version of unpack_skb.

    :param ch:
        *undescribed*
    :type ch: struct channel \*

    :param pskb:
        *undescribed*
    :type pskb: struct sk_buff \*

.. _`ctcmpc_unpack_skb.description`:

Description
-----------

ch           The channel where this skb has been received.
pskb         The received skb.

.. _`ctcmpc_bh`:

ctcmpc_bh
=========

.. c:function:: void ctcmpc_bh(unsigned long thischan)

    :param thischan:
        *undescribed*
    :type thischan: unsigned long

.. _`ctcmpc_bh.description`:

Description
-----------

ch           The channel to work on.
Allow flow control back pressure to occur here.
Throttling back channel can result in excessive
channel inactivity and system deact of channel

.. _`mpc_action_nop`:

mpc_action_nop
==============

.. c:function:: void mpc_action_nop(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`mpc_action_timeout`:

mpc_action_timeout
==================

.. c:function:: void mpc_action_timeout(fsm_instance *fi, int event, void *arg)

    MPC Group Station FSM action CTCM_PROTO_MPC only

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`mpc_action_timeout.description`:

Description
-----------

fi           An instance of an mpc_group fsm.
event        The event, just happened.
arg          Generic pointer, casted from net_device \* upon call.

.. This file was automatic generated / don't edit.

