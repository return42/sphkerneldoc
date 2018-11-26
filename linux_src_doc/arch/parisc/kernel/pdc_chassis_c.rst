.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/parisc/kernel/pdc_chassis.c

.. _`pdc_chassis_setup`:

pdc_chassis_setup
=================

.. c:function:: int pdc_chassis_setup(char *str)

    Enable/disable pdc_chassis code at boot time.

    :param str:
        0 to disable chassis log
        \ ``return``\  1
    :type str: char \*

.. _`pdc_chassis_checkold`:

pdc_chassis_checkold
====================

.. c:function:: void pdc_chassis_checkold( void)

    Checks for old PDC_CHASSIS compatibility

    :param void:
        no arguments
    :type void: 

.. _`pdc_chassis_checkold.description`:

Description
-----------

Currently, only E class and A180 are known to work with this.
Inspired by Christoph Plattner

.. _`pdc_chassis_panic_event`:

pdc_chassis_panic_event
=======================

.. c:function:: int pdc_chassis_panic_event(struct notifier_block *this, unsigned long event, void *ptr)

    Called by the panic handler.

    :param this:
        *undescribed*
    :type this: struct notifier_block \*

    :param event:
        *undescribed*
    :type event: unsigned long

    :param ptr:
        *undescribed*
    :type ptr: void \*

.. _`pdc_chassis_panic_event.description`:

Description
-----------

As soon as a panic occurs, we should inform the PDC.

.. _`pdc_chassis_reboot_event`:

pdc_chassis_reboot_event
========================

.. c:function:: int pdc_chassis_reboot_event(struct notifier_block *this, unsigned long event, void *ptr)

    Called by the reboot handler.

    :param this:
        *undescribed*
    :type this: struct notifier_block \*

    :param event:
        *undescribed*
    :type event: unsigned long

    :param ptr:
        *undescribed*
    :type ptr: void \*

.. _`pdc_chassis_reboot_event.description`:

Description
-----------

As soon as a reboot occurs, we should inform the PDC.

.. _`parisc_pdc_chassis_init`:

parisc_pdc_chassis_init
=======================

.. c:function:: void parisc_pdc_chassis_init( void)

    Called at boot time.

    :param void:
        no arguments
    :type void: 

.. _`pdc_chassis_send_status`:

pdc_chassis_send_status
=======================

.. c:function:: int pdc_chassis_send_status(int message)

    Sends a predefined message to the chassis, and changes the front panel LEDs according to the new system state

    :param message:
        *undescribed*
    :type message: int

.. _`pdc_chassis_send_status.description`:

Description
-----------

Only machines with 64 bits PDC PAT and those reported in
\ :c:func:`pdc_chassis_checkold`\  are supported atm.

returns 0 if no error, -1 if no supported PDC is present or invalid message,
else returns the appropriate PDC error code.

For a list of predefined messages, see asm-parisc/pdc_chassis.h

.. This file was automatic generated / don't edit.

