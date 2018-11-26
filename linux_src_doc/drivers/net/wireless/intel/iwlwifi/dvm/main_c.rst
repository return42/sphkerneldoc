.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/main.c

.. _`iwl_bg_statistics_periodic`:

iwl_bg_statistics_periodic
==========================

.. c:function:: void iwl_bg_statistics_periodic(struct timer_list *t)

    Timer callback to queue statistics

    :param t:
        *undescribed*
    :type t: struct timer_list \*

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

    :param t:
        *undescribed*
    :type t: struct timer_list \*

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

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

.. _`iwl_clear_driver_stations`:

iwl_clear_driver_stations
=========================

.. c:function:: void iwl_clear_driver_stations(struct iwl_priv *priv)

    clear knowledge of all stations from driver

    :param priv:
        iwl priv struct
    :type priv: struct iwl_priv \*

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

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param start_idx:
        *undescribed*
    :type start_idx: u32

    :param num_events:
        *undescribed*
    :type num_events: u32

    :param mode:
        *undescribed*
    :type mode: u32

    :param pos:
        *undescribed*
    :type pos: int

    :param buf:
        *undescribed*
    :type buf: char \*\*

    :param bufsz:
        *undescribed*
    :type bufsz: size_t

.. _`iwl_print_last_event_logs`:

iwl_print_last_event_logs
=========================

.. c:function:: int iwl_print_last_event_logs(struct iwl_priv *priv, u32 capacity, u32 num_wraps, u32 next_entry, u32 size, u32 mode, int pos, char **buf, size_t bufsz)

    Dump the newest # of event log to syslog

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param capacity:
        *undescribed*
    :type capacity: u32

    :param num_wraps:
        *undescribed*
    :type num_wraps: u32

    :param next_entry:
        *undescribed*
    :type next_entry: u32

    :param size:
        *undescribed*
    :type size: u32

    :param mode:
        *undescribed*
    :type mode: u32

    :param pos:
        *undescribed*
    :type pos: int

    :param buf:
        *undescribed*
    :type buf: char \*\*

    :param bufsz:
        *undescribed*
    :type bufsz: size_t

.. This file was automatic generated / don't edit.

