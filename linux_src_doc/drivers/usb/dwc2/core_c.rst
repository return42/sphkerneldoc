.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/core.c

.. _`dwc2_backup_global_registers`:

dwc2_backup_global_registers
============================

.. c:function:: int dwc2_backup_global_registers(struct dwc2_hsotg *hsotg)

    Backup global controller registers. When suspending usb bus, registers needs to be backuped if controller power is disabled once suspended.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. _`dwc2_restore_global_registers`:

dwc2_restore_global_registers
=============================

.. c:function:: int dwc2_restore_global_registers(struct dwc2_hsotg *hsotg)

    Restore controller global registers. When resuming usb bus, device registers needs to be restored if controller power were disabled.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. _`dwc2_exit_hibernation`:

dwc2_exit_hibernation
=====================

.. c:function:: int dwc2_exit_hibernation(struct dwc2_hsotg *hsotg, bool restore)

    Exit controller from Partial Power Down.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

    :param bool restore:
        Controller registers need to be restored

.. _`dwc2_enter_hibernation`:

dwc2_enter_hibernation
======================

.. c:function:: int dwc2_enter_hibernation(struct dwc2_hsotg *hsotg)

    Put controller in Partial Power Down.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. _`dwc2_wait_for_mode`:

dwc2_wait_for_mode
==================

.. c:function:: void dwc2_wait_for_mode(struct dwc2_hsotg *hsotg, bool host_mode)

    Waits for the controller mode.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller.

    :param bool host_mode:
        If true, waits for host mode, otherwise device mode.

.. _`dwc2_iddig_filter_enabled`:

dwc2_iddig_filter_enabled
=========================

.. c:function:: bool dwc2_iddig_filter_enabled(struct dwc2_hsotg *hsotg)

    Returns true if the IDDIG debounce filter is enabled.

    :param struct dwc2_hsotg \*hsotg:
        *undescribed*

.. _`dwc2_clear_force_mode`:

dwc2_clear_force_mode
=====================

.. c:function:: void dwc2_clear_force_mode(struct dwc2_hsotg *hsotg)

    Clears the force mode bits.

    :param struct dwc2_hsotg \*hsotg:
        *undescribed*

.. _`dwc2_clear_force_mode.description`:

Description
-----------

After clearing the bits, wait up to 100 ms to account for any
potential IDDIG filter delay. We can't know if we expect this delay
or not because the value of the connector ID status is affected by
the force mode. We only need to call this once during probe if
dr_mode == OTG.

.. _`dwc2_dump_host_registers`:

dwc2_dump_host_registers
========================

.. c:function:: void dwc2_dump_host_registers(struct dwc2_hsotg *hsotg)

    Prints the host registers

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_dump_host_registers.note`:

NOTE
----

This function will be removed once the peripheral controller code
is integrated and the driver is stable

.. _`dwc2_dump_global_registers`:

dwc2_dump_global_registers
==========================

.. c:function:: void dwc2_dump_global_registers(struct dwc2_hsotg *hsotg)

    Prints the core global registers

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_dump_global_registers.note`:

NOTE
----

This function will be removed once the peripheral controller code
is integrated and the driver is stable

.. _`dwc2_flush_tx_fifo`:

dwc2_flush_tx_fifo
==================

.. c:function:: void dwc2_flush_tx_fifo(struct dwc2_hsotg *hsotg, const int num)

    Flushes a Tx FIFO

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param const int num:
        Tx FIFO to flush

.. _`dwc2_flush_rx_fifo`:

dwc2_flush_rx_fifo
==================

.. c:function:: void dwc2_flush_rx_fifo(struct dwc2_hsotg *hsotg)

    Flushes the Rx FIFO

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_enable_global_interrupts`:

dwc2_enable_global_interrupts
=============================

.. c:function:: void dwc2_enable_global_interrupts(struct dwc2_hsotg *hsotg)

    Enables the controller's Global Interrupt in the AHB Config register

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_disable_global_interrupts`:

dwc2_disable_global_interrupts
==============================

.. c:function:: void dwc2_disable_global_interrupts(struct dwc2_hsotg *hsotg)

    Disables the controller's Global Interrupt in the AHB Config register

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. This file was automatic generated / don't edit.

