.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/time-event.h

.. _`time-events---what-is-it-`:

Time Events - what is it?
=========================

Time Events are a fw feature that allows the driver to control the presence
of the device on the channel. Since the fw supports multiple channels
concurrently, the fw may choose to jump to another channel at any time.
In order to make sure that the fw is on a specific channel at a certain time
and for a certain duration, the driver needs to issue a time event.

The simplest example is for BSS association. The driver issues a time event,
waits for it to start, and only then tells mac80211 that we can start the
association. This way, we make sure that the association will be done
smoothly and won't be interrupted by channel switch decided within the fw.

.. _`abstraction-to-the-driver`:

Abstraction to the driver
=========================

In order to simplify the use of time events to the rest of the driver,
we abstract the use of time events. This component provides the functions
needed by the driver.

.. _`iwl_mvm_protect_session`:

iwl_mvm_protect_session
=======================

.. c:function:: void iwl_mvm_protect_session(struct iwl_mvm *mvm, struct ieee80211_vif *vif, u32 duration, u32 min_duration, u32 max_delay, bool wait_for_notif)

    start / extend the session protection.

    :param struct iwl_mvm \*mvm:
        the mvm component

    :param struct ieee80211_vif \*vif:
        the virtual interface for which the session is issued

    :param u32 duration:
        the duration of the session in TU.

    :param u32 min_duration:
        will start a new session if the current session will end
        in less than min_duration.

    :param u32 max_delay:
        maximum delay before starting the time event (in TU)

    :param bool wait_for_notif:
        true if it is required that a time event notification be
        waited for (that the time event has been scheduled before returning)

.. _`iwl_mvm_protect_session.description`:

Description
-----------

This function can be used to start a session protection which means that the
fw will stay on the channel for \ ``duration_ms``\  milliseconds. This function
can block (sleep) until the session starts. This function can also be used
to extend a currently running session.
This function is meant to be used for BSS association for example, where we
want to make sure that the fw stays on the channel during the association.

.. _`iwl_mvm_stop_session_protection`:

iwl_mvm_stop_session_protection
===============================

.. c:function:: void iwl_mvm_stop_session_protection(struct iwl_mvm *mvm, struct ieee80211_vif *vif)

    cancel the session protection.

    :param struct iwl_mvm \*mvm:
        the mvm component

    :param struct ieee80211_vif \*vif:
        the virtual interface for which the session is issued

.. _`iwl_mvm_stop_session_protection.description`:

Description
-----------

This functions cancels the session protection which is an act of good
citizenship. If it is not needed any more it should be canceled because
the other bindings wait for the medium during that time.
This funtions doesn't sleep.

.. _`iwl_mvm_start_p2p_roc`:

iwl_mvm_start_p2p_roc
=====================

.. c:function:: int iwl_mvm_start_p2p_roc(struct iwl_mvm *mvm, struct ieee80211_vif *vif, int duration, enum ieee80211_roc_type type)

    start remain on channel for p2p device functionality

    :param struct iwl_mvm \*mvm:
        the mvm component

    :param struct ieee80211_vif \*vif:
        the virtual interface for which the roc is requested. It is assumed
        that the vif type is NL80211_IFTYPE_P2P_DEVICE

    :param int duration:
        the requested duration in millisecond for the fw to be on the
        channel that is bound to the vif.

    :param enum ieee80211_roc_type type:
        the remain on channel request type

.. _`iwl_mvm_start_p2p_roc.description`:

Description
-----------

This function can be used to issue a remain on channel session,
which means that the fw will stay in the channel for the request \ ``duration``\ 
milliseconds. The function is async, meaning that it only issues the ROC
request but does not wait for it to start. Once the FW is ready to serve the
ROC request, it will issue a notification to the driver that it is on the
requested channel. Once the FW completes the ROC request it will issue
another notification to the driver.

.. _`iwl_mvm_stop_roc`:

iwl_mvm_stop_roc
================

.. c:function:: void iwl_mvm_stop_roc(struct iwl_mvm *mvm)

    stop remain on channel functionality

    :param struct iwl_mvm \*mvm:
        the mvm component

.. _`iwl_mvm_stop_roc.description`:

Description
-----------

This function can be used to cancel an ongoing ROC session.
The function is async, it will instruct the FW to stop serving the ROC
session, but will not wait for the actual stopping of the session.

.. _`iwl_mvm_remove_time_event`:

iwl_mvm_remove_time_event
=========================

.. c:function:: void iwl_mvm_remove_time_event(struct iwl_mvm *mvm, struct iwl_mvm_vif *mvmvif, struct iwl_mvm_time_event_data *te_data)

    general function to clean up of time event

    :param struct iwl_mvm \*mvm:
        the mvm component

    :param struct iwl_mvm_vif \*mvmvif:
        *undescribed*

    :param struct iwl_mvm_time_event_data \*te_data:
        the time event data that corresponds to that time event

.. _`iwl_mvm_remove_time_event.description`:

Description
-----------

This function can be used to cancel a time event regardless its type.
It is useful for cleaning up time events running before removing an
interface.

.. _`iwl_mvm_te_clear_data`:

iwl_mvm_te_clear_data
=====================

.. c:function:: void iwl_mvm_te_clear_data(struct iwl_mvm *mvm, struct iwl_mvm_time_event_data *te_data)

    remove time event from list

    :param struct iwl_mvm \*mvm:
        the mvm component

    :param struct iwl_mvm_time_event_data \*te_data:
        the time event data to remove

.. _`iwl_mvm_te_clear_data.description`:

Description
-----------

This function is mostly internal, it is made available here only
for firmware restart purposes.

.. _`iwl_mvm_schedule_csa_period`:

iwl_mvm_schedule_csa_period
===========================

.. c:function:: int iwl_mvm_schedule_csa_period(struct iwl_mvm *mvm, struct ieee80211_vif *vif, u32 duration, u32 apply_time)

    request channel switch absence period

    :param struct iwl_mvm \*mvm:
        the mvm component

    :param struct ieee80211_vif \*vif:
        the virtual interface for which the channel switch is issued

    :param u32 duration:
        the duration of the NoA in TU.

    :param u32 apply_time:
        NoA start time in GP2.

.. _`iwl_mvm_schedule_csa_period.description`:

Description
-----------

This function is used to schedule NoA time event and is used to perform
the channel switch flow.

.. _`iwl_mvm_te_scheduled`:

iwl_mvm_te_scheduled
====================

.. c:function:: bool iwl_mvm_te_scheduled(struct iwl_mvm_time_event_data *te_data)

    check if the fw received the TE cmd

    :param struct iwl_mvm_time_event_data \*te_data:
        the time event data that corresponds to that time event

.. _`iwl_mvm_te_scheduled.description`:

Description
-----------

This function returns true iff this TE is added to the fw.

.. This file was automatic generated / don't edit.

