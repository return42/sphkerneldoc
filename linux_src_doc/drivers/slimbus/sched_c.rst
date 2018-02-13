.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/slimbus/sched.c

.. _`slim_ctrl_clk_pause`:

slim_ctrl_clk_pause
===================

.. c:function:: int slim_ctrl_clk_pause(struct slim_controller *ctrl, bool wakeup, u8 restart)

    Called by slimbus controller to enter/exit 'clock pause'

    :param struct slim_controller \*ctrl:
        controller requesting bus to be paused or woken up

    :param bool wakeup:
        Wakeup this controller from clock pause.

    :param u8 restart:
        Restart time value per spec used for clock pause. This value
        isn't used when controller is to be woken up.

.. _`slim_ctrl_clk_pause.description`:

Description
-----------

Slimbus specification needs this sequence to turn-off clocks for the bus.
The sequence involves sending 3 broadcast messages (reconfiguration
sequence) to inform all devices on the bus.
To exit clock-pause, controller typically wakes up active framer device.
This API executes clock pause reconfiguration sequence if wakeup is false.
If wakeup is true, controller's wakeup is called.
For entering clock-pause, -EBUSY is returned if a message txn in pending.

.. This file was automatic generated / don't edit.

