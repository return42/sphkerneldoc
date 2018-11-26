.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/processor_idle.c

.. _`acpi_idle_bm_check`:

acpi_idle_bm_check
==================

.. c:function:: int acpi_idle_bm_check( void)

    checks if bus master activity was detected

    :param void:
        no arguments
    :type void: 

.. _`acpi_idle_do_entry`:

acpi_idle_do_entry
==================

.. c:function:: void __cpuidle acpi_idle_do_entry(struct acpi_processor_cx *cx)

    enter idle state using the appropriate method

    :param cx:
        cstate data
    :type cx: struct acpi_processor_cx \*

.. _`acpi_idle_do_entry.description`:

Description
-----------

Caller disables interrupt before call and enables interrupt after return.

.. _`acpi_idle_play_dead`:

acpi_idle_play_dead
===================

.. c:function:: int acpi_idle_play_dead(struct cpuidle_device *dev, int index)

    enters an ACPI state for long-term idle (i.e. off-lining)

    :param dev:
        the target CPU
    :type dev: struct cpuidle_device \*

    :param index:
        the index of suggested state
    :type index: int

.. _`acpi_idle_enter_bm`:

acpi_idle_enter_bm
==================

.. c:function:: void acpi_idle_enter_bm(struct acpi_processor *pr, struct acpi_processor_cx *cx, bool timer_bc)

    enters C3 with proper BM handling

    :param pr:
        Target processor
    :type pr: struct acpi_processor \*

    :param cx:
        Target state context
    :type cx: struct acpi_processor_cx \*

    :param timer_bc:
        Whether or not to change timer mode to broadcast
    :type timer_bc: bool

.. _`combine_lpi_states`:

combine_lpi_states
==================

.. c:function:: bool combine_lpi_states(struct acpi_lpi_state *local, struct acpi_lpi_state *parent, struct acpi_lpi_state *result)

    combine local and parent LPI states to form a composite LPI state

    :param local:
        local LPI state
    :type local: struct acpi_lpi_state \*

    :param parent:
        parent LPI state
    :type parent: struct acpi_lpi_state \*

    :param result:
        composite LPI state
    :type result: struct acpi_lpi_state \*

.. _`acpi_idle_lpi_enter`:

acpi_idle_lpi_enter
===================

.. c:function:: int acpi_idle_lpi_enter(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    enters an ACPI any LPI state

    :param dev:
        the target CPU
    :type dev: struct cpuidle_device \*

    :param drv:
        cpuidle driver containing cpuidle state info
    :type drv: struct cpuidle_driver \*

    :param index:
        index of target state
    :type index: int

.. _`acpi_idle_lpi_enter.return`:

Return
------

0 for success or negative value for error

.. _`acpi_processor_setup_cpuidle_states`:

acpi_processor_setup_cpuidle_states
===================================

.. c:function:: int acpi_processor_setup_cpuidle_states(struct acpi_processor *pr)

    prepares and configures cpuidle global state data i.e. idle routines

    :param pr:
        the ACPI processor
    :type pr: struct acpi_processor \*

.. _`acpi_processor_setup_cpuidle_dev`:

acpi_processor_setup_cpuidle_dev
================================

.. c:function:: int acpi_processor_setup_cpuidle_dev(struct acpi_processor *pr, struct cpuidle_device *dev)

    prepares and configures CPUIDLE device i.e. per-cpu data

    :param pr:
        the ACPI processor
    :type pr: struct acpi_processor \*

    :param dev:
        the cpuidle device
    :type dev: struct cpuidle_device \*

.. This file was automatic generated / don't edit.

