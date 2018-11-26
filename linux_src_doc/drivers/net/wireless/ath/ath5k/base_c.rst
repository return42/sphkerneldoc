.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/base.c

.. _`ath5k_drain_tx_buffs`:

ath5k_drain_tx_buffs
====================

.. c:function:: void ath5k_drain_tx_buffs(struct ath5k_hw *ah)

    Empty tx buffers

    :param ah:
        *undescribed*
    :type ah: struct ath5k_hw \*

.. _`ath5k_drain_tx_buffs.description`:

Description
-----------

\ ``ah``\  The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

Empty tx buffers from all queues in preparation
of a reset or during shutdown.

NB:  this assumes output has been stopped and
we do not need to block ath5k_tx_tasklet

.. _`ath5k_beacon_update_timers`:

ath5k_beacon_update_timers
==========================

.. c:function:: void ath5k_beacon_update_timers(struct ath5k_hw *ah, u64 bc_tsf)

    update beacon timers

    :param ah:
        struct ath5k_hw pointer we are operating on
    :type ah: struct ath5k_hw \*

    :param bc_tsf:
        the timestamp of the beacon. 0 to reset the TSF. -1 to perform a
        beacon timer update based on the current HW TSF.
    :type bc_tsf: u64

.. _`ath5k_beacon_update_timers.description`:

Description
-----------

Calculate the next target beacon transmit time (TBTT) based on the timestamp
of a received beacon or the current local hardware TSF and write it to the
beacon timer registers.

This is called in a variety of situations, e.g. when a beacon is received,
when a TSF update has been detected, but also when an new IBSS is created or
when we otherwise know we have to update the timers, but we keep it in this
function to have it all together in one place.

.. _`ath5k_beacon_config`:

ath5k_beacon_config
===================

.. c:function:: void ath5k_beacon_config(struct ath5k_hw *ah)

    Configure the beacon queues and interrupts

    :param ah:
        struct ath5k_hw pointer we are operating on
    :type ah: struct ath5k_hw \*

.. _`ath5k_beacon_config.description`:

Description
-----------

In IBSS mode we use a self-linked tx descriptor if possible. We enable SWBA
interrupts to detect TSF updates only.

.. This file was automatic generated / don't edit.

