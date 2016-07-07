.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/charger-manager.c

.. _`is_batt_present`:

is_batt_present
===============

.. c:function:: bool is_batt_present(struct charger_manager *cm)

    See if the battery presents in place.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`is_ext_pwr_online`:

is_ext_pwr_online
=================

.. c:function:: bool is_ext_pwr_online(struct charger_manager *cm)

    See if an external power source is attached to charge

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`is_ext_pwr_online.description`:

Description
-----------

Returns true if at least one of the chargers of the battery has an external
power source attached to charge the battery regardless of whether it is
actually charging or not.

.. _`get_batt_uv`:

get_batt_uV
===========

.. c:function:: int get_batt_uV(struct charger_manager *cm, int *uV)

    Get the voltage level of the battery

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

    :param int \*uV:
        the voltage level returned.

.. _`get_batt_uv.description`:

Description
-----------

Returns 0 if there is no error.
Returns a negative value on error.

.. _`is_charging`:

is_charging
===========

.. c:function:: bool is_charging(struct charger_manager *cm)

    Returns true if the battery is being charged.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`is_full_charged`:

is_full_charged
===============

.. c:function:: bool is_full_charged(struct charger_manager *cm)

    Returns true if the battery is fully charged.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`is_polling_required`:

is_polling_required
===================

.. c:function:: bool is_polling_required(struct charger_manager *cm)

    Return true if need to continue polling for this CM.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`try_charger_enable`:

try_charger_enable
==================

.. c:function:: int try_charger_enable(struct charger_manager *cm, bool enable)

    Enable/Disable chargers altogether

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

    :param bool enable:
        true: enable / false: disable

.. _`try_charger_enable.description`:

Description
-----------

Note that Charger Manager keeps the charger enabled regardless whether
the charger is charging or not (because battery is full or no external
power source exists) except when CM needs to disable chargers forcibly
bacause of emergency causes; when the battery is overheated or too cold.

.. _`try_charger_restart`:

try_charger_restart
===================

.. c:function:: int try_charger_restart(struct charger_manager *cm)

    Restart charging.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`try_charger_restart.description`:

Description
-----------

Restart charging by turning off and on the charger.

.. _`uevent_notify`:

uevent_notify
=============

.. c:function:: void uevent_notify(struct charger_manager *cm, const char *event)

    Let users know something has changed.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

    :param const char \*event:
        the event string.

.. _`uevent_notify.description`:

Description
-----------

If \ ``event``\  is null, it implies that uevent_notify is called
by resume function. When called in the resume function, cm_suspended
should be already reset to false in order to let uevent_notify
notify the recent event during the suspend to users. While
suspended, uevent_notify does not notify users, but tracks
events so that uevent_notify can notify users later after resumed.

.. _`fullbatt_vchk`:

fullbatt_vchk
=============

.. c:function:: void fullbatt_vchk(struct work_struct *work)

    Check voltage drop some times after "FULL" event.

    :param struct work_struct \*work:
        the work_struct appointing the function

.. _`fullbatt_vchk.description`:

Description
-----------

If a user has designated "fullbatt_vchkdrop_ms/uV" values with
charger_desc, Charger Manager checks voltage drop after the battery
"FULL" event. It checks whether the voltage has dropped more than
fullbatt_vchkdrop_uV by calling this function after fullbatt_vchkrop_ms.

.. _`check_charging_duration`:

check_charging_duration
=======================

.. c:function:: int check_charging_duration(struct charger_manager *cm)

    Monitor charging/discharging duration

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`check_charging_duration.description`:

Description
-----------

If whole charging duration exceed 'charging_max_duration_ms',
cm stop charging to prevent overcharge/overheat. If discharging
duration exceed 'discharging \_max_duration_ms', charger cable is
attached, after full-batt, cm start charging to maintain fully
charged state for battery.

.. _`_cm_monitor`:

_cm_monitor
===========

.. c:function:: bool _cm_monitor(struct charger_manager *cm)

    Monitor the temperature and return true for exceptions.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`_cm_monitor.description`:

Description
-----------

Returns true if there is an event to notify for the battery.
(True if the status of "emergency_stop" changes)

.. _`cm_monitor`:

cm_monitor
==========

.. c:function:: bool cm_monitor( void)

    Monitor every battery.

    :param  void:
        no arguments

.. _`cm_monitor.description`:

Description
-----------

Returns true if there is an event to notify from any of the batteries.
(True if the status of "emergency_stop" changes)

.. _`_setup_polling`:

_setup_polling
==============

.. c:function:: void _setup_polling(struct work_struct *work)

    Setup the next instance of polling.

    :param struct work_struct \*work:
        work_struct of the function \_setup_polling.

.. _`cm_monitor_poller`:

cm_monitor_poller
=================

.. c:function:: void cm_monitor_poller(struct work_struct *work)

    The Monitor / Poller.

    :param struct work_struct \*work:
        work_struct of the function cm_monitor_poller

.. _`cm_monitor_poller.description`:

Description
-----------

During non-suspended state, cm_monitor_poller is used to poll and monitor
the batteries.

.. _`fullbatt_handler`:

fullbatt_handler
================

.. c:function:: void fullbatt_handler(struct charger_manager *cm)

    Event handler for CM_EVENT_BATT_FULL

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`battout_handler`:

battout_handler
===============

.. c:function:: void battout_handler(struct charger_manager *cm)

    Event handler for CM_EVENT_BATT_OUT

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`misc_event_handler`:

misc_event_handler
==================

.. c:function:: void misc_event_handler(struct charger_manager *cm, enum cm_event_types type)

    Handler for other evnets

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

    :param enum cm_event_types type:
        the Charger Manager representing the battery.

.. _`cm_setup_timer`:

cm_setup_timer
==============

.. c:function:: bool cm_setup_timer( void)

    For in-suspend monitoring setup wakeup alarm for suspend_again.

    :param  void:
        no arguments

.. _`cm_setup_timer.description`:

Description
-----------

Returns true if the alarm is set for Charger Manager to use.
Returns false if
cm_setup_timer fails to set an alarm,
cm_setup_timer does not need to set an alarm for Charger Manager,
or an alarm previously configured is to be used.

.. _`charger_extcon_work`:

charger_extcon_work
===================

.. c:function:: void charger_extcon_work(struct work_struct *work)

    enable/diable charger according to the state of charger cable

    :param struct work_struct \*work:
        work_struct of the function charger_extcon_work.

.. _`charger_extcon_notifier`:

charger_extcon_notifier
=======================

.. c:function:: int charger_extcon_notifier(struct notifier_block *self, unsigned long event, void *ptr)

    receive the state of charger cable when registered cable is attached or detached.

    :param struct notifier_block \*self:
        the notifier block of the charger_extcon_notifier.

    :param unsigned long event:
        the cable state.

    :param void \*ptr:
        the data pointer of notifier block.

.. _`charger_extcon_init`:

charger_extcon_init
===================

.. c:function:: int charger_extcon_init(struct charger_manager *cm, struct charger_cable *cable)

    register external connector to use it as the charger cable

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

    :param struct charger_cable \*cable:
        the Charger cable representing the external connector.

.. _`charger_manager_register_extcon`:

charger_manager_register_extcon
===============================

.. c:function:: int charger_manager_register_extcon(struct charger_manager *cm)

    Register extcon device to recevie state of charger cable.

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`charger_manager_register_extcon.description`:

Description
-----------

This function support EXTCON(External Connector) subsystem to detect the
state of charger cables for enabling or disabling charger(regulator) and
select the charger cable for charging among a number of external cable
according to policy of H/W board.

.. _`charger_manager_register_sysfs`:

charger_manager_register_sysfs
==============================

.. c:function:: int charger_manager_register_sysfs(struct charger_manager *cm)

    Register sysfs entry for each charger

    :param struct charger_manager \*cm:
        the Charger Manager representing the battery.

.. _`charger_manager_register_sysfs.description`:

Description
-----------

This function add sysfs entry for charger(regulator) to control charger from
user-space. If some development board use one more chargers for charging
but only need one charger on specific case which is dependent on user
scenario or hardware restrictions, the user enter 1 or 0(zero) to '/sys/
class/power_supply/battery/charger.[index]/externally_control'. For example,
if user enter 1 to 'sys/class/power_supply/battery/charger.[index]/
externally_control, this charger isn't controlled from charger-manager and
always stay off state of regulator.

.. _`cm_notify_event`:

cm_notify_event
===============

.. c:function:: void cm_notify_event(struct power_supply *psy, enum cm_event_types type, char *msg)

    charger driver notify Charger Manager of charger event

    :param struct power_supply \*psy:
        pointer to instance of charger's power_supply

    :param enum cm_event_types type:
        type of charger event

    :param char \*msg:
        optional message passed to uevent_notify fuction

.. This file was automatic generated / don't edit.

