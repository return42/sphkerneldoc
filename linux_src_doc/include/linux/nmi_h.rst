.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nmi.h

.. _`touch_nmi_watchdog`:

touch_nmi_watchdog
==================

.. c:function:: void touch_nmi_watchdog( void)

    restart NMI watchdog timeout.

    :param void:
        no arguments
    :type void: 

.. _`touch_nmi_watchdog.description`:

Description
-----------

If the architecture supports the NMI watchdog, \ :c:func:`touch_nmi_watchdog`\ 
may be used to reset the timeout - for code which intentionally
disables interrupts for a long time. This call is stateless.

.. This file was automatic generated / don't edit.

