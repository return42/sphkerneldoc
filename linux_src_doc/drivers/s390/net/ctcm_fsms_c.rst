.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/ctcm_fsms.c

.. _`ctcm_ccw_check_rc`:

ctcm_ccw_check_rc
=================

.. c:function:: void ctcm_ccw_check_rc(struct channel *ch, int rc, char *msg)

    :param ch:
        *undescribed*
    :type ch: struct channel \*

    :param rc:
        *undescribed*
    :type rc: int

    :param msg:
        *undescribed*
    :type msg: char \*

.. _`ctcm_ccw_check_rc.description`:

Description
-----------

ch   :       The channel, the error belongs to.
Returns the error code (!= 0) to inspect.

.. _`ctcm_action_nop`:

ctcm_action_nop
===============

.. c:function:: void ctcm_action_nop(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`chx_txdone`:

chx_txdone
==========

.. c:function:: void chx_txdone(fsm_instance *fi, int event, void *arg)

    skb (it's in io_queue), reset dev->tbusy and revert to idle state.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`chx_txdone.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_txidle`:

ctcm_chx_txidle
===============

.. c:function:: void ctcm_chx_txidle(fsm_instance *fi, int event, void *arg)

    Notify device statemachine that we are up and running.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_txidle.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`chx_rx`:

chx_rx
======

.. c:function:: void chx_rx(fsm_instance *fi, int event, void *arg)

    trigger bottom half, and initiate next read.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`chx_rx.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`chx_firstio`:

chx_firstio
===========

.. c:function:: void chx_firstio(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`chx_firstio.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`chx_rxidle`:

chx_rxidle
==========

.. c:function:: void chx_rxidle(fsm_instance *fi, int event, void *arg)

    notify device statemachine that we are up and running.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`chx_rxidle.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_setmode`:

ctcm_chx_setmode
================

.. c:function:: void ctcm_chx_setmode(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_setmode.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_start`:

ctcm_chx_start
==============

.. c:function:: void ctcm_chx_start(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_start.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_haltio`:

ctcm_chx_haltio
===============

.. c:function:: void ctcm_chx_haltio(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_haltio.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_cleanup`:

ctcm_chx_cleanup
================

.. c:function:: void ctcm_chx_cleanup(fsm_instance *fi, int state, struct channel *ch)

    cleanup channels queue and notify interface statemachine.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param state:
        *undescribed*
    :type state: int

    :param ch:
        *undescribed*
    :type ch: struct channel \*

.. _`ctcm_chx_cleanup.description`:

Description
-----------

fi           An instance of a channel statemachine.
state        The next state (depending on caller).
ch           The channel to operate on.

.. _`ctcm_chx_stopped`:

ctcm_chx_stopped
================

.. c:function:: void ctcm_chx_stopped(fsm_instance *fi, int event, void *arg)

    Cleanup it's queue and notify interface statemachine.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_stopped.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_stop`:

ctcm_chx_stop
=============

.. c:function:: void ctcm_chx_stop(fsm_instance *fi, int event, void *arg)

    not operational mode. Set state to stopped.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_stop.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_fail`:

ctcm_chx_fail
=============

.. c:function:: void ctcm_chx_fail(fsm_instance *fi, int event, void *arg)

    happened. Cleanup queue and notify interface statemachine.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_fail.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_setuperr`:

ctcm_chx_setuperr
=================

.. c:function:: void ctcm_chx_setuperr(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_setuperr.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_restart`:

ctcm_chx_restart
================

.. c:function:: void ctcm_chx_restart(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_restart.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_rxiniterr`:

ctcm_chx_rxiniterr
==================

.. c:function:: void ctcm_chx_rxiniterr(fsm_instance *fi, int event, void *arg)

    0-length block header)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_rxiniterr.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_rxinitfail`:

ctcm_chx_rxinitfail
===================

.. c:function:: void ctcm_chx_rxinitfail(fsm_instance *fi, int event, void *arg)

    of RX channel.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_rxinitfail.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_rxdisc`:

ctcm_chx_rxdisc
===============

.. c:function:: void ctcm_chx_rxdisc(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_rxdisc.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_txiniterr`:

ctcm_chx_txiniterr
==================

.. c:function:: void ctcm_chx_txiniterr(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_txiniterr.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_txretry`:

ctcm_chx_txretry
================

.. c:function:: void ctcm_chx_txretry(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_txretry.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcm_chx_iofatal`:

ctcm_chx_iofatal
================

.. c:function:: void ctcm_chx_iofatal(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcm_chx_iofatal.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcmpc_chx_txdone`:

ctcmpc_chx_txdone
=================

.. c:function:: void ctcmpc_chx_txdone(fsm_instance *fi, int event, void *arg)

    skb (it's in io_queue), reset dev->tbusy and revert to idle state.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcmpc_chx_txdone.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcmpc_chx_rx`:

ctcmpc_chx_rx
=============

.. c:function:: void ctcmpc_chx_rx(fsm_instance *fi, int event, void *arg)

    trigger bottom half, and initiate next read.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcmpc_chx_rx.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcmpc_chx_firstio`:

ctcmpc_chx_firstio
==================

.. c:function:: void ctcmpc_chx_firstio(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcmpc_chx_firstio.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`ctcmpc_chx_rxidle`:

ctcmpc_chx_rxidle
=================

.. c:function:: void ctcmpc_chx_rxidle(fsm_instance *fi, int event, void *arg)

    notify device statemachine that we are up and running.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`ctcmpc_chx_rxidle.description`:

Description
-----------

fi           An instance of a channel statemachine.
event        The event, just happened.
arg          Generic pointer, casted from channel \* upon call.

.. _`dev_action_start`:

dev_action_start
================

.. c:function:: void dev_action_start(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_start.description`:

Description
-----------

fi           An instance of an interface statemachine.
event        The event, just happened.
arg          Generic pointer, casted from struct net_device \* upon call.

.. _`dev_action_stop`:

dev_action_stop
===============

.. c:function:: void dev_action_stop(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_stop.description`:

Description
-----------

fi           An instance of an interface statemachine.
event        The event, just happened.
arg          Generic pointer, casted from struct net_device \* upon call.

.. _`dev_action_chup`:

dev_action_chup
===============

.. c:function:: void dev_action_chup(fsm_instance *fi, int event, void *arg)

    when a channel is up and running.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_chup.description`:

Description
-----------

fi           An instance of an interface statemachine.
event        The event, just happened.
arg          Generic pointer, casted from struct net_device \* upon call.

.. _`dev_action_chdown`:

dev_action_chdown
=================

.. c:function:: void dev_action_chdown(fsm_instance *fi, int event, void *arg)

    when a channel has been shutdown.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_chdown.description`:

Description
-----------

fi           An instance of an interface statemachine.
event        The event, just happened.
arg          Generic pointer, casted from struct net_device \* upon call.

.. This file was automatic generated / don't edit.

