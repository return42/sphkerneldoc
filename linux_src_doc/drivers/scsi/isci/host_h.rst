.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/host.h

.. _`sci_power_control`:

struct sci_power_control
========================

.. c:type:: struct sci_power_control


.. _`sci_power_control.definition`:

Definition
----------

.. code-block:: c

    struct sci_power_control {
        bool timer_started;
        struct sci_timer timer;
        u8 phys_waiting;
        u8 phys_granted_power;
        struct isci_phy *requesters[SCI_MAX_PHYS];
    }

.. _`sci_power_control.members`:

Members
-------

timer_started
    *undescribed*

timer
    *undescribed*

phys_waiting
    *undescribed*

phys_granted_power
    *undescribed*

requesters
    *undescribed*

.. _`sci_power_control.description`:

Description
-----------

This structure defines the fields for managing power control for direct
attached disk devices.

.. _`sci_controller_states`:

enum sci_controller_states
==========================

.. c:type:: enum sci_controller_states

    This enumeration depicts all the states for the common controller state machine.

.. _`sci_controller_states.definition`:

Definition
----------

.. code-block:: c

    enum sci_controller_states {
        SCIC_INITIAL,
        SCIC_RESET,
        SCIC_INITIALIZING,
        SCIC_INITIALIZED,
        SCIC_STARTING,
        SCIC_READY,
        SCIC_RESETTING,
        SCIC_STOPPING,
        SCIC_FAILED
    };

.. _`sci_controller_states.constants`:

Constants
---------

SCIC_INITIAL
    *undescribed*

SCIC_RESET
    *undescribed*

SCIC_INITIALIZING
    *undescribed*

SCIC_INITIALIZED
    *undescribed*

SCIC_STARTING
    *undescribed*

SCIC_READY
    *undescribed*

SCIC_RESETTING
    *undescribed*

SCIC_STOPPING
    *undescribed*

SCIC_FAILED
    *undescribed*

.. _`sci_controller_clear_invalid_phy`:

sci_controller_clear_invalid_phy
================================

.. c:function::  sci_controller_clear_invalid_phy( controller,  phy)

    :param  controller:
        *undescribed*

    :param  phy:
        *undescribed*

.. _`sci_controller_clear_invalid_phy.description`:

Description
-----------

This macro will clear the bit in the invalid phy mask for this controller
object.  This is used to control messages reported for invalid link up
notifications.

.. This file was automatic generated / don't edit.

