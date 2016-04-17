.. -*- coding: utf-8; mode: rst -*-

==========
ctcm_mpc.c
==========


.. _`ctcmpc_unpack_skb`:

ctcmpc_unpack_skb
=================

.. c:function:: void ctcmpc_unpack_skb (struct channel *ch, struct sk_buff *pskb)

    :param struct channel \*ch:

        *undescribed*

    :param struct sk_buff \*pskb:

        *undescribed*



.. _`ctcmpc_unpack_skb.description`:

Description
-----------

upper layers.
special MPC version of unpack_skb.

ch                The channel where this skb has been received.
pskb                The received skb.



.. _`ctcmpc_bh`:

ctcmpc_bh
=========

.. c:function:: void ctcmpc_bh (unsigned long thischan)

    :param unsigned long thischan:

        *undescribed*



.. _`ctcmpc_bh.description`:

Description
-----------


ch                The channel to work on.
Allow flow control back pressure to occur here.
Throttling back channel can result in excessive
channel inactivity and system deact of channel



.. _`mpc_action_nop`:

mpc_action_nop
==============

.. c:function:: void mpc_action_nop (fsm_instance *fi, int event, void *arg)

    :param fsm_instance \*fi:

        *undescribed*

    :param int event:

        *undescribed*

    :param void \*arg:

        *undescribed*



.. _`mpc_action_timeout`:

mpc_action_timeout
==================

.. c:function:: void mpc_action_timeout (fsm_instance *fi, int event, void *arg)

    :param fsm_instance \*fi:

        *undescribed*

    :param int event:

        *undescribed*

    :param void \*arg:

        *undescribed*



.. _`mpc_action_timeout.description`:

Description
-----------

MPC Group Station FSM action
CTCM_PROTO_MPC only

fi                An instance of an mpc_group fsm.
event        The event, just happened.
arg                Generic pointer, casted from net_device * upon call.

