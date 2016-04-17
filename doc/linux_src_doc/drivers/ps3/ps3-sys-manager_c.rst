.. -*- coding: utf-8; mode: rst -*-

=================
ps3-sys-manager.c
=================


.. _`ps3_sys_manager_service_id`:

enum ps3_sys_manager_service_id
===============================

.. c:type:: ps3_sys_manager_service_id

    Message header service_id.


.. _`ps3_sys_manager_service_id.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_service_id {
      PS3_SM_SERVICE_ID_REQUEST,
      PS3_SM_SERVICE_ID_RESPONSE,
      PS3_SM_SERVICE_ID_COMMAND,
      PS3_SM_SERVICE_ID_EXTERN_EVENT,
      PS3_SM_SERVICE_ID_SET_NEXT_OP,
      PS3_SM_SERVICE_ID_REQUEST_ERROR,
      PS3_SM_SERVICE_ID_SET_ATTR
    };


.. _`ps3_sys_manager_service_id.constants`:

Constants
---------

:``PS3_SM_SERVICE_ID_REQUEST``:
    guest --> sys_manager.

:``PS3_SM_SERVICE_ID_RESPONSE``:
    guest --> sys_manager.

:``PS3_SM_SERVICE_ID_COMMAND``:
    guest <-- sys_manager.

:``PS3_SM_SERVICE_ID_EXTERN_EVENT``:
    guest <-- sys_manager.

:``PS3_SM_SERVICE_ID_SET_NEXT_OP``:
    guest --> sys_manager.

:``PS3_SM_SERVICE_ID_REQUEST_ERROR``:
    guest <-- sys_manager.

:``PS3_SM_SERVICE_ID_SET_ATTR``:
    guest --> sys_manager.


.. _`ps3_sys_manager_service_id.description`:

Description
-----------

PS3_SM_SERVICE_ID_REQUEST_ERROR is returned for invalid data values in a
a PS3_SM_SERVICE_ID_REQUEST message.  It also seems to be returned when
a REQUEST message is sent at the wrong time.



.. _`ps3_sys_manager_attr`:

enum ps3_sys_manager_attr
=========================

.. c:type:: ps3_sys_manager_attr

    Notification attribute (bit position mask).


.. _`ps3_sys_manager_attr.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_attr {
      PS3_SM_ATTR_POWER,
      PS3_SM_ATTR_RESET,
      PS3_SM_ATTR_THERMAL,
      PS3_SM_ATTR_CONTROLLER,
      PS3_SM_ATTR_ALL
    };


.. _`ps3_sys_manager_attr.constants`:

Constants
---------

:``PS3_SM_ATTR_POWER``:
    Power button.

:``PS3_SM_ATTR_RESET``:
    Reset button, not available on retail console.

:``PS3_SM_ATTR_THERMAL``:
    System thermal alert.

:``PS3_SM_ATTR_CONTROLLER``:
    Remote controller event.

:``PS3_SM_ATTR_ALL``:
    Logical OR of all.


.. _`ps3_sys_manager_attr.description`:

Description
-----------

The guest tells the system manager which events it is interested in receiving
notice of by sending the system manager a logical OR of notification
attributes via the :c:func:`ps3_sys_manager_send_attr` routine.



.. _`ps3_sys_manager_event`:

enum ps3_sys_manager_event
==========================

.. c:type:: ps3_sys_manager_event

    External event type, reported by system manager.


.. _`ps3_sys_manager_event.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_event {
      PS3_SM_EVENT_POWER_PRESSED,
      PS3_SM_EVENT_POWER_RELEASED,
      PS3_SM_EVENT_RESET_PRESSED,
      PS3_SM_EVENT_RESET_RELEASED,
      PS3_SM_EVENT_THERMAL_ALERT,
      PS3_SM_EVENT_THERMAL_CLEARED
    };


.. _`ps3_sys_manager_event.constants`:

Constants
---------

:``PS3_SM_EVENT_POWER_PRESSED``:
    payload.value =
    enum ps3_sys_manager_button_event.

:``PS3_SM_EVENT_POWER_RELEASED``:
    payload.value = time pressed in millisec.

:``PS3_SM_EVENT_RESET_PRESSED``:
    payload.value =
    enum ps3_sys_manager_button_event.

:``PS3_SM_EVENT_RESET_RELEASED``:
    payload.value = time pressed in millisec.

:``PS3_SM_EVENT_THERMAL_ALERT``:
    payload.value = thermal zone id.

:``PS3_SM_EVENT_THERMAL_CLEARED``:
    payload.value = thermal zone id.


.. _`ps3_sys_manager_button_event`:

enum ps3_sys_manager_button_event
=================================

.. c:type:: ps3_sys_manager_button_event

    Button event payload values.


.. _`ps3_sys_manager_button_event.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_button_event {
      PS3_SM_BUTTON_EVENT_HARD,
      PS3_SM_BUTTON_EVENT_SOFT
    };


.. _`ps3_sys_manager_button_event.constants`:

Constants
---------

:``PS3_SM_BUTTON_EVENT_HARD``:
    Hardware generated event.

:``PS3_SM_BUTTON_EVENT_SOFT``:
    Software generated event.


.. _`ps3_sys_manager_next_op`:

enum ps3_sys_manager_next_op
============================

.. c:type:: ps3_sys_manager_next_op

    Operation to perform after lpar is destroyed.


.. _`ps3_sys_manager_next_op.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_next_op {
      PS3_SM_NEXT_OP_SYS_SHUTDOWN,
      PS3_SM_NEXT_OP_SYS_REBOOT,
      PS3_SM_NEXT_OP_LPAR_REBOOT
    };


.. _`ps3_sys_manager_next_op.constants`:

Constants
---------

:``PS3_SM_NEXT_OP_SYS_SHUTDOWN``:
-- undescribed --

:``PS3_SM_NEXT_OP_SYS_REBOOT``:
-- undescribed --

:``PS3_SM_NEXT_OP_LPAR_REBOOT``:
-- undescribed --


.. _`ps3_sys_manager_wake_source`:

enum ps3_sys_manager_wake_source
================================

.. c:type:: ps3_sys_manager_wake_source

    Next-op wakeup source (bit position mask).


.. _`ps3_sys_manager_wake_source.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_wake_source {
      PS3_SM_WAKE_DEFAULT,
      PS3_SM_WAKE_W_O_L,
      PS3_SM_WAKE_P_O_R
    };


.. _`ps3_sys_manager_wake_source.constants`:

Constants
---------

:``PS3_SM_WAKE_DEFAULT``:
    Disk insert, power button, eject button.

:``PS3_SM_WAKE_W_O_L``:
    Ether or wireless LAN.

:``PS3_SM_WAKE_P_O_R``:
    Power on reset.


.. _`ps3_sys_manager_wake_source.description`:

Description
-----------

Additional wakeup sources when specifying PS3_SM_NEXT_OP_SYS_SHUTDOWN.
The system will always wake from the PS3_SM_WAKE_DEFAULT sources.
Sources listed here are the only ones available to guests in the
other-os lpar.



.. _`ps3_sys_manager_cmd`:

enum ps3_sys_manager_cmd
========================

.. c:type:: ps3_sys_manager_cmd

    Command from system manager to guest.


.. _`ps3_sys_manager_cmd.definition`:

Definition
----------

.. code-block:: c

    enum ps3_sys_manager_cmd {
      PS3_SM_CMD_SHUTDOWN,
       
    };


.. _`ps3_sys_manager_cmd.constants`:

Constants
---------

:``PS3_SM_CMD_SHUTDOWN``:
-- undescribed --

:`` ``:
-- undescribed --


.. _`ps3_sys_manager_cmd.description`:

Description
-----------


The guest completes the actions needed, then acks or naks the command via
:c:func:`ps3_sys_manager_send_response`.  In the case of ``PS3_SM_CMD_SHUTDOWN``\ ,
the guest must be fully prepared for a system poweroff prior to acking the
command.



.. _`ps3_sys_manager_write`:

ps3_sys_manager_write
=====================

.. c:function:: int ps3_sys_manager_write (struct ps3_system_bus_device *dev, const struct ps3_sys_manager_header *header, const void *payload)

    Helper to write a two part message to the vuart.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*

    :param const struct ps3_sys_manager_header \*header:

        *undescribed*

    :param const void \*payload:

        *undescribed*



.. _`ps3_sys_manager_send_attr`:

ps3_sys_manager_send_attr
=========================

.. c:function:: int ps3_sys_manager_send_attr (struct ps3_system_bus_device *dev, enum ps3_sys_manager_attr attr)

    Send a 'set attribute' to the system manager.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*

    :param enum ps3_sys_manager_attr attr:

        *undescribed*



.. _`ps3_sys_manager_send_attr.description`:

Description
-----------




.. _`ps3_sys_manager_send_next_op`:

ps3_sys_manager_send_next_op
============================

.. c:function:: int ps3_sys_manager_send_next_op (struct ps3_system_bus_device *dev, enum ps3_sys_manager_next_op op, enum ps3_sys_manager_wake_source wake_source)

    Send a 'set next op' to the system manager.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*

    :param enum ps3_sys_manager_next_op op:

        *undescribed*

    :param enum ps3_sys_manager_wake_source wake_source:

        *undescribed*



.. _`ps3_sys_manager_send_next_op.description`:

Description
-----------


Tell the system manager what to do after this lpar is destroyed.



.. _`ps3_sys_manager_send_request_shutdown`:

ps3_sys_manager_send_request_shutdown
=====================================

.. c:function:: int ps3_sys_manager_send_request_shutdown (struct ps3_system_bus_device *dev)

    Send 'request' to the system manager.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_send_request_shutdown.description`:

Description
-----------


The guest sends this message to request an operation or action of the system
manager.  The reply is a command message from the system manager.  In the
command handler the guest performs the requested operation.  The result of
the command is then communicated back to the system manager with a response
message.

Currently, the only supported request is the 'shutdown self' request.



.. _`ps3_sys_manager_send_response`:

ps3_sys_manager_send_response
=============================

.. c:function:: int ps3_sys_manager_send_response (struct ps3_system_bus_device *dev, u64 status)

    Send a 'response' to the system manager.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*

    :param u64 status:
        zero = success, others fail.



.. _`ps3_sys_manager_send_response.description`:

Description
-----------

The guest sends this message to the system manager to acnowledge success or
failure of a command sent by the system manager.



.. _`ps3_sys_manager_handle_event`:

ps3_sys_manager_handle_event
============================

.. c:function:: int ps3_sys_manager_handle_event (struct ps3_system_bus_device *dev)

    Second stage event msg handler.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_handle_cmd`:

ps3_sys_manager_handle_cmd
==========================

.. c:function:: int ps3_sys_manager_handle_cmd (struct ps3_system_bus_device *dev)

    Second stage command msg handler.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_handle_cmd.description`:

Description
-----------



The system manager sends this in reply to a 'request' message from the guest.



.. _`ps3_sys_manager_handle_msg`:

ps3_sys_manager_handle_msg
==========================

.. c:function:: int ps3_sys_manager_handle_msg (struct ps3_system_bus_device *dev)

    First stage msg handler.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_handle_msg.description`:

Description
-----------


Can be called directly to manually poll vuart and pump message handler.



.. _`ps3_sys_manager_final_power_off`:

ps3_sys_manager_final_power_off
===============================

.. c:function:: void ps3_sys_manager_final_power_off (struct ps3_system_bus_device *dev)

    The final platform machine_power_off routine.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_final_power_off.description`:

Description
-----------


This routine never returns.  The routine disables asynchronous vuart reads
then spins calling :c:func:`ps3_sys_manager_handle_msg` to receive and acknowledge
the shutdown command sent from the system manager.  Soon after the
acknowledgement is sent the lpar is destroyed by the HV.  This routine
should only be called from :c:func:`ps3_power_off` through
ps3_sys_manager_ops.power_off.



.. _`ps3_sys_manager_final_restart`:

ps3_sys_manager_final_restart
=============================

.. c:function:: void ps3_sys_manager_final_restart (struct ps3_system_bus_device *dev)

    The final platform machine_restart routine.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_final_restart.description`:

Description
-----------


This routine never returns.  The routine disables asynchronous vuart reads
then spins calling :c:func:`ps3_sys_manager_handle_msg` to receive and acknowledge
the shutdown command sent from the system manager.  Soon after the
acknowledgement is sent the lpar is destroyed by the HV.  This routine
should only be called from :c:func:`ps3_restart` through ps3_sys_manager_ops.restart.



.. _`ps3_sys_manager_get_wol`:

ps3_sys_manager_get_wol
=======================

.. c:function:: int ps3_sys_manager_get_wol ( void)

    Get wake-on-lan setting.

    :param void:
        no arguments



.. _`ps3_sys_manager_set_wol`:

ps3_sys_manager_set_wol
=======================

.. c:function:: void ps3_sys_manager_set_wol (int state)

    Set wake-on-lan setting.

    :param int state:

        *undescribed*



.. _`ps3_sys_manager_work`:

ps3_sys_manager_work
====================

.. c:function:: void ps3_sys_manager_work (struct ps3_system_bus_device *dev)

    Asynchronous read handler.

    :param struct ps3_system_bus_device \*dev:

        *undescribed*



.. _`ps3_sys_manager_work.description`:

Description
-----------


Signaled when PS3_SM_RX_MSG_LEN_MIN bytes arrive at the vuart port.

