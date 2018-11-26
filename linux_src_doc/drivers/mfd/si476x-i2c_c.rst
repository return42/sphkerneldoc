.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/si476x-i2c.c

.. _`si476x_core_config_pinmux`:

si476x_core_config_pinmux
=========================

.. c:function:: int si476x_core_config_pinmux(struct si476x_core *core)

    pin function configuration function

    :param core:
        Core device structure
    :type core: struct si476x_core \*

.. _`si476x_core_config_pinmux.description`:

Description
-----------

Configure the functions of the pins of the radio chip.

The function returns zero in case of succes or negative error code
otherwise.

.. _`si476x_core_start`:

si476x_core_start
=================

.. c:function:: int si476x_core_start(struct si476x_core *core, bool soft)

    early chip startup function

    :param core:
        Core device structure
    :type core: struct si476x_core \*

    :param soft:
        When set, this flag forces "soft" startup, where "soft"
        power down is the one done by sending appropriate command instead
        of using reset pin of the tuner
    :type soft: bool

.. _`si476x_core_start.description`:

Description
-----------

Perform required startup sequence to correctly power
up the chip and perform initial configuration. It does the

.. _`si476x_core_start.following-sequence-of-actions`:

following sequence of actions
-----------------------------

1. Claims and enables the power supplies VD and VIO1 required
for I2C interface of the chip operation.
2. Waits for 100us, pulls the reset line up, enables irq,
waits for another 100us as it is specified by the
datasheet.
3. Sends 'POWER_UP' command to the device with all provided
information about power-up parameters.
4. Configures, pin multiplexor, disables digital audio and
configures interrupt sources.

The function returns zero in case of succes or negative error code
otherwise.

.. _`si476x_core_stop`:

si476x_core_stop
================

.. c:function:: int si476x_core_stop(struct si476x_core *core, bool soft)

    chip power-down function

    :param core:
        Core device structure
    :type core: struct si476x_core \*

    :param soft:
        When set, function sends a POWER_DOWN command instead of
        bringing reset line low
    :type soft: bool

.. _`si476x_core_stop.power-down-the-chip-by-performing-following-actions`:

Power down the chip by performing following actions
---------------------------------------------------

1. Disable IRQ or stop the polling worker
2. Send the POWER_DOWN command if the power down is soft or bring
reset line low if not.

The function returns zero in case of succes or negative error code
otherwise.

.. _`si476x_core_set_power_state`:

si476x_core_set_power_state
===========================

.. c:function:: int si476x_core_set_power_state(struct si476x_core *core, enum si476x_power_state next_state)

    set the level at which the power is supplied for the chip.

    :param core:
        Core device structure
    :type core: struct si476x_core \*

    :param next_state:
        enum si476x_power_state describing power state to
        switch to.
    :type next_state: enum si476x_power_state

.. _`si476x_core_set_power_state.description`:

Description
-----------

Switch on all the required power supplies

This function returns 0 in case of suvccess and negative error code
otherwise.

.. _`si476x_core_report_drainer_stop`:

si476x_core_report_drainer_stop
===============================

.. c:function:: void si476x_core_report_drainer_stop(struct si476x_core *core)

    mark the completion of the RDS buffer drain porcess by the worker.

    :param core:
        Core device structure
    :type core: struct si476x_core \*

.. _`si476x_core_start_rds_drainer_once`:

si476x_core_start_rds_drainer_once
==================================

.. c:function:: void si476x_core_start_rds_drainer_once(struct si476x_core *core)

    start RDS drainer worker if ther is none working, do nothing otherwise

    :param core:
        Datastructure corresponding to the chip.
    :type core: struct si476x_core \*

.. _`si476x_core_drain_rds_fifo`:

si476x_core_drain_rds_fifo
==========================

.. c:function:: void si476x_core_drain_rds_fifo(struct work_struct *work)

    RDS buffer drainer.

    :param work:
        struct work_struct being ppassed to the function by the
        kernel.
    :type work: struct work_struct \*

.. _`si476x_core_drain_rds_fifo.description`:

Description
-----------

Drain the contents of the RDS FIFO of

.. _`si476x_core_pronounce_dead`:

si476x_core_pronounce_dead
==========================

.. c:function:: void si476x_core_pronounce_dead(struct si476x_core *core)

    :param core:
        Core device structure
    :type core: struct si476x_core \*

.. _`si476x_core_pronounce_dead.description`:

Description
-----------

Mark the device as being dead and wake up all potentially waiting
threads of execution.

.. _`si476x_core_i2c_xfer`:

si476x_core_i2c_xfer
====================

.. c:function:: int si476x_core_i2c_xfer(struct si476x_core *core, enum si476x_i2c_type type, char *buf, int count)

    :param core:
        Core device structure
    :type core: struct si476x_core \*

    :param type:
        Transfer type
    :type type: enum si476x_i2c_type

    :param buf:
        Transfer buffer for/with data
    :type buf: char \*

    :param count:
        Transfer buffer size
    :type count: int

.. _`si476x_core_i2c_xfer.description`:

Description
-----------

Perfrom and I2C transfer(either read or write) and keep a counter
of I/O errors. If the error counter rises above the threshold
pronounce device dead.

The function returns zero on succes or negative error code on
failure.

.. _`si476x_core_get_status`:

si476x_core_get_status
======================

.. c:function:: int si476x_core_get_status(struct si476x_core *core)

    :param core:
        Core device structure
    :type core: struct si476x_core \*

.. _`si476x_core_get_status.description`:

Description
-----------

Get the status byte of the core device by berforming one byte I2C
read.

The function returns a status value or a negative error code on
error.

.. _`si476x_core_get_and_signal_status`:

si476x_core_get_and_signal_status
=================================

.. c:function:: void si476x_core_get_and_signal_status(struct si476x_core *core)

    IRQ dispatcher

    :param core:
        Core device structure
    :type core: struct si476x_core \*

.. _`si476x_core_get_and_signal_status.description`:

Description
-----------

Dispatch the arrived interrupt request based on the value of the
status byte reported by the tuner.

.. _`si476x_core_fwver_to_revision`:

si476x_core_fwver_to_revision
=============================

.. c:function:: int si476x_core_fwver_to_revision(struct si476x_core *core, int func, int major, int minor1, int minor2)

    :param core:
        Core device structure
    :type core: struct si476x_core \*

    :param func:
        *undescribed*
    :type func: int

    :param major:
        Firmware major number
    :type major: int

    :param minor1:
        Firmware first minor number
    :type minor1: int

    :param minor2:
        Firmware second minor number
    :type minor2: int

.. _`si476x_core_fwver_to_revision.description`:

Description
-----------

Convert a chip's firmware version number into an offset that later
will be used to as offset in "vtable" of tuner functions

This function returns a positive offset in case of success and a -1
in case of failure.

.. _`si476x_core_get_revision_info`:

si476x_core_get_revision_info
=============================

.. c:function:: int si476x_core_get_revision_info(struct si476x_core *core)

    :param core:
        Core device structure
    :type core: struct si476x_core \*

.. _`si476x_core_get_revision_info.description`:

Description
-----------

Get the firmware version number of the device. It is done in

.. _`si476x_core_get_revision_info.following-three-steps`:

following three steps
---------------------

1. Power-up the device
2. Send the 'FUNC_INFO' command
3. Powering the device down.

The function return zero on success and a negative error code on
failure.

.. This file was automatic generated / don't edit.

