.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/main.c

.. _`iwl_bg_statistics_periodic`:

iwl_bg_statistics_periodic
==========================

.. c:function:: void iwl_bg_statistics_periodic(struct timer_list *t)

    Timer callback to queue statistics

    :param struct timer_list \*t:
        *undescribed*

.. _`iwl_bg_statistics_periodic.description`:

Description
-----------

This callback is provided in order to send a statistics request.

This timer function is continually reset to execute within
REG_RECALIB_PERIOD seconds since the last STATISTICS_NOTIFICATION
was received.  We need to ensure we receive the statistics in order
to update the temperature used for calibrating the TXPOWER.

.. _`iwl_bg_ucode_trace`:

iwl_bg_ucode_trace
==================

.. c:function:: void iwl_bg_ucode_trace(struct timer_list *t)

    Timer callback to log ucode event

    :param struct timer_list \*t:
        *undescribed*

.. _`iwl_bg_ucode_trace.description`:

Description
-----------

The timer is continually set to execute every
UCODE_TRACE_PERIOD milliseconds after the last timer expired
this function is to perform continuous uCode event logging operation
if enabled

.. _`iwl_alive_start`:

iwl_alive_start
===============

.. c:function:: int iwl_alive_start(struct iwl_priv *priv)

    called after REPLY_ALIVE notification received from protocol/runtime uCode (initialization uCode's Alive gets handled by \ :c:func:`iwl_init_alive_start`\ ).

    :param struct iwl_priv \*priv:
        *undescribed*

.. _`iwl_clear_driver_stations`:

iwl_clear_driver_stations
=========================

.. c:function:: void iwl_clear_driver_stations(struct iwl_priv *priv)

    clear knowledge of all stations from driver

    :param struct iwl_priv \*priv:
        iwl priv struct

.. _`iwl_clear_driver_stations.description`:

Description
-----------

This is called during \ :c:func:`iwl_down`\  to make sure that in the case
we're coming there from a hardware restart mac80211 will be
able to reconfigure stations -- if we're getting there in the
normal down flow then the stations will already be cleared.

.. _`iwl_print_event_log`:

iwl_print_event_log
===================

.. c:function:: int iwl_print_event_log(struct iwl_priv *priv, u32 start_idx, u32 num_events, u32 mode, int pos, char **buf, size_t bufsz)

    Dump error event log to syslog

    :param struct iwl_priv \*priv:
        *undescribed*

    :param u32 start_idx:
        *undescribed*

    :param u32 num_events:
        *undescribed*

    :param u32 mode:
        *undescribed*

    :param int pos:
        *undescribed*

    :param char \*\*buf:
        *undescribed*

    :param size_t bufsz:
        *undescribed*

.. _`iwl_print_last_event_logs`:

iwl_print_last_event_logs
=========================

.. c:function:: int iwl_print_last_event_logs(struct iwl_priv *priv, u32 capacity, u32 num_wraps, u32 next_entry, u32 size, u32 mode, int pos, char **buf, size_t bufsz)

    Dump the newest # of event log to syslog

    :param struct iwl_priv \*priv:
        *undescribed*

    :param u32 capacity:
        *undescribed*

    :param u32 num_wraps:
        *undescribed*

    :param u32 next_entry:
        *undescribed*

    :param u32 size:
        *undescribed*

    :param u32 mode:
        *undescribed*

    :param int pos:
        *undescribed*

    :param char \*\*buf:
        *undescribed*

    :param size_t bufsz:
        *undescribed*

.. This file was automatic generated / don't edit.

