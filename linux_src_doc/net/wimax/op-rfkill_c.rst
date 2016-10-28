.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wimax/op-rfkill.c

.. _`wimax_report_rfkill_hw`:

wimax_report_rfkill_hw
======================

.. c:function:: void wimax_report_rfkill_hw(struct wimax_dev *wimax_dev, enum wimax_rf_state state)

    Reports changes in the hardware RF switch

    :param struct wimax_dev \*wimax_dev:
        WiMAX device descriptor

    :param enum wimax_rf_state state:
        New state of the RF Kill switch. \ ``WIMAX_RF_ON``\  radio on,
        \ ``WIMAX_RF_OFF``\  radio off.

.. _`wimax_report_rfkill_hw.description`:

Description
-----------

When the device detects a change in the state of thehardware RF
switch, it must call this function to let the WiMAX kernel stack
know that the state has changed so it can be properly propagated.

The WiMAX stack caches the state (the driver doesn't need to). As
well, as the change is propagated it will come back as a request to
change the software state to mirror the hardware state.

If the device doesn't have a hardware kill switch, just report
it on initialization as always on (\ ``WIMAX_RF_ON``\ , radio on).

.. _`wimax_report_rfkill_sw`:

wimax_report_rfkill_sw
======================

.. c:function:: void wimax_report_rfkill_sw(struct wimax_dev *wimax_dev, enum wimax_rf_state state)

    Reports changes in the software RF switch

    :param struct wimax_dev \*wimax_dev:
        WiMAX device descriptor

    :param enum wimax_rf_state state:
        New state of the RF kill switch. \ ``WIMAX_RF_ON``\  radio on,
        \ ``WIMAX_RF_OFF``\  radio off.

.. _`wimax_report_rfkill_sw.description`:

Description
-----------

Reports changes in the software RF switch state to the WiMAX stack.

The main use is during initialization, so the driver can query the
device for its current software radio kill switch state and feed it
to the system.

On the side, the device does not change the software state by
itself. In practice, this can happen, as the device might decide to
switch (in software) the radio off for different reasons.

.. _`wimax_rfkill`:

wimax_rfkill
============

.. c:function:: int wimax_rfkill(struct wimax_dev *wimax_dev, enum wimax_rf_state state)

    Set the software RF switch state for a WiMAX device

    :param struct wimax_dev \*wimax_dev:
        WiMAX device descriptor

    :param enum wimax_rf_state state:
        New RF state.

.. _`wimax_rfkill.return`:

Return
------


>= 0 toggle state if ok, < 0 errno code on error. The toggle state
is returned as a bitmap, bit 0 being the hardware RF state, bit 1
the software RF state.

0 means disabled (\ ``WIMAX_RF_ON``\ , radio on), 1 means enabled radio
off (\ ``WIMAX_RF_OFF``\ ).

.. _`wimax_rfkill.description`:

Description
-----------


Called by the user when he wants to request the WiMAX radio to be
switched on (\ ``WIMAX_RF_ON``\ ) or off (\ ``WIMAX_RF_OFF``\ ). With
\ ``WIMAX_RF_QUERY``\ , just the current state is returned.

.. _`wimax_rfkill.note`:

NOTE
----


This call will block until the operation is complete.

.. This file was automatic generated / don't edit.

