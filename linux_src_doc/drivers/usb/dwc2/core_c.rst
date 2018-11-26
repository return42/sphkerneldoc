.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/core.c

.. _`dwc2_backup_global_registers`:

dwc2_backup_global_registers
============================

.. c:function:: int dwc2_backup_global_registers(struct dwc2_hsotg *hsotg)

    Backup global controller registers. When suspending usb bus, registers needs to be backuped if controller power is disabled once suspended.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_restore_global_registers`:

dwc2_restore_global_registers
=============================

.. c:function:: int dwc2_restore_global_registers(struct dwc2_hsotg *hsotg)

    Restore controller global registers. When resuming usb bus, device registers needs to be restored if controller power were disabled.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_exit_partial_power_down`:

dwc2_exit_partial_power_down
============================

.. c:function:: int dwc2_exit_partial_power_down(struct dwc2_hsotg *hsotg, bool restore)

    Exit controller from Partial Power Down.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param restore:
        Controller registers need to be restored
    :type restore: bool

.. _`dwc2_enter_partial_power_down`:

dwc2_enter_partial_power_down
=============================

.. c:function:: int dwc2_enter_partial_power_down(struct dwc2_hsotg *hsotg)

    Put controller in Partial Power Down.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_restore_essential_regs`:

dwc2_restore_essential_regs
===========================

.. c:function:: void dwc2_restore_essential_regs(struct dwc2_hsotg *hsotg, int rmode, int is_host)

    Restore essiential regs of core.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param rmode:
        Restore mode, enabled in case of remote-wakeup.
    :type rmode: int

    :param is_host:
        Host or device mode.
    :type is_host: int

.. _`dwc2_hib_restore_common`:

dwc2_hib_restore_common
=======================

.. c:function:: void dwc2_hib_restore_common(struct dwc2_hsotg *hsotg, int rem_wakeup, int is_host)

    Common part of restore routine.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param rem_wakeup:
        Remote-wakeup, enabled in case of remote-wakeup.
    :type rem_wakeup: int

    :param is_host:
        Host or device mode.
    :type is_host: int

.. _`dwc2_wait_for_mode`:

dwc2_wait_for_mode
==================

.. c:function:: void dwc2_wait_for_mode(struct dwc2_hsotg *hsotg, bool host_mode)

    Waits for the controller mode.

    :param hsotg:
        Programming view of the DWC_otg controller.
    :type hsotg: struct dwc2_hsotg \*

    :param host_mode:
        If true, waits for host mode, otherwise device mode.
    :type host_mode: bool

.. _`dwc2_iddig_filter_enabled`:

dwc2_iddig_filter_enabled
=========================

.. c:function:: bool dwc2_iddig_filter_enabled(struct dwc2_hsotg *hsotg)

    Returns true if the IDDIG debounce filter is enabled.

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_force_mode`:

dwc2_force_mode
===============

.. c:function:: void dwc2_force_mode(struct dwc2_hsotg *hsotg, bool host)

    Force the mode of the controller.

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param host:
        Host mode flag
    :type host: bool

.. _`dwc2_force_mode.forcing-the-mode-is-needed-for-two-cases`:

Forcing the mode is needed for two cases
----------------------------------------


1) If the dr_mode is set to either HOST or PERIPHERAL we force the
controller to stay in a particular mode regardless of ID pin
changes. We do this once during probe.

2) During probe we want to read reset values of the hw
configuration registers that are only available in either host or
device mode. We may need to force the mode if the current mode does
not allow us to access the register in the mode that we want.

In either case it only makes sense to force the mode if the
controller hardware is OTG capable.

Checks are done in this function to determine whether doing a force
would be valid or not.

If a force is done, it requires a IDDIG debounce filter delay if
the filter is configured and enabled. We poll the current mode of
the controller to account for this delay.

.. _`dwc2_clear_force_mode`:

dwc2_clear_force_mode
=====================

.. c:function:: void dwc2_clear_force_mode(struct dwc2_hsotg *hsotg)

    Clears the force mode bits.

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

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

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

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

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

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

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param num:
        Tx FIFO to flush
    :type num: const int

.. _`dwc2_flush_rx_fifo`:

dwc2_flush_rx_fifo
==================

.. c:function:: void dwc2_flush_rx_fifo(struct dwc2_hsotg *hsotg)

    Flushes the Rx FIFO

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_enable_global_interrupts`:

dwc2_enable_global_interrupts
=============================

.. c:function:: void dwc2_enable_global_interrupts(struct dwc2_hsotg *hsotg)

    Enables the controller's Global Interrupt in the AHB Config register

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_disable_global_interrupts`:

dwc2_disable_global_interrupts
==============================

.. c:function:: void dwc2_disable_global_interrupts(struct dwc2_hsotg *hsotg)

    Disables the controller's Global Interrupt in the AHB Config register

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_wait_bit_set`:

dwc2_hsotg_wait_bit_set
=======================

.. c:function:: int dwc2_hsotg_wait_bit_set(struct dwc2_hsotg *hsotg, u32 offset, u32 mask, u32 timeout)

    Waits for bit to be set.

    :param hsotg:
        Programming view of DWC_otg controller.
    :type hsotg: struct dwc2_hsotg \*

    :param offset:
        Register's offset where bit/bits must be set.
    :type offset: u32

    :param mask:
        Mask of the bit/bits which must be set.
    :type mask: u32

    :param timeout:
        Timeout to wait.
    :type timeout: u32

.. _`dwc2_hsotg_wait_bit_set.return`:

Return
------

0 if bit/bits are set or -ETIMEDOUT in case of timeout.

.. _`dwc2_hsotg_wait_bit_clear`:

dwc2_hsotg_wait_bit_clear
=========================

.. c:function:: int dwc2_hsotg_wait_bit_clear(struct dwc2_hsotg *hsotg, u32 offset, u32 mask, u32 timeout)

    Waits for bit to be clear.

    :param hsotg:
        Programming view of DWC_otg controller.
    :type hsotg: struct dwc2_hsotg \*

    :param offset:
        Register's offset where bit/bits must be set.
    :type offset: u32

    :param mask:
        Mask of the bit/bits which must be set.
    :type mask: u32

    :param timeout:
        Timeout to wait.
    :type timeout: u32

.. _`dwc2_hsotg_wait_bit_clear.return`:

Return
------

0 if bit/bits are set or -ETIMEDOUT in case of timeout.

.. This file was automatic generated / don't edit.

