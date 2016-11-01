.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/processor_idle.c

.. _`acpi_idle_bm_check`:

acpi_idle_bm_check
==================

.. c:function:: int acpi_idle_bm_check( void)

    checks if bus master activity was detected

    :param  void:
        no arguments

.. _`acpi_idle_do_entry`:

acpi_idle_do_entry
==================

.. c:function:: void __cpuidle acpi_idle_do_entry(struct acpi_processor_cx *cx)

    enter idle state using the appropriate method

    :param struct acpi_processor_cx \*cx:
        cstate data

.. _`acpi_idle_do_entry.description`:

Description
-----------

Caller disables interrupt before call and enables interrupt after return.

.. _`acpi_idle_play_dead`:

acpi_idle_play_dead
===================

.. c:function:: int acpi_idle_play_dead(struct cpuidle_device *dev, int index)

    enters an ACPI state for long-term idle (i.e. off-lining)

    :param struct cpuidle_device \*dev:
        the target CPU

    :param int index:
        the index of suggested state

.. _`acpi_idle_enter_bm`:

acpi_idle_enter_bm
==================

.. c:function:: void acpi_idle_enter_bm(struct acpi_processor *pr, struct acpi_processor_cx *cx, bool timer_bc)

    enters C3 with proper BM handling

    :param struct acpi_processor \*pr:
        Target processor

    :param struct acpi_processor_cx \*cx:
        Target state context

    :param bool timer_bc:
        Whether or not to change timer mode to broadcast

.. _`combine_lpi_states`:

combine_lpi_states
==================

.. c:function:: bool combine_lpi_states(struct acpi_lpi_state *local, struct acpi_lpi_state *parent, struct acpi_lpi_state *result)

    combine local and parent LPI states to form a composite LPI state

    :param struct acpi_lpi_state \*local:
        local LPI state

    :param struct acpi_lpi_state \*parent:
        parent LPI state

    :param struct acpi_lpi_state \*result:
        composite LPI state

.. _`acpi_idle_lpi_enter`:

acpi_idle_lpi_enter
===================

.. c:function:: int acpi_idle_lpi_enter(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    enters an ACPI any LPI state

    :param struct cpuidle_device \*dev:
        the target CPU

    :param struct cpuidle_driver \*drv:
        cpuidle driver containing cpuidle state info

    :param int index:
        index of target state

.. _`acpi_idle_lpi_enter.return`:

Return
------

0 for success or negative value for error

.. _`acpi_processor_setup_cpuidle_states`:

acpi_processor_setup_cpuidle_states
===================================

.. c:function:: int acpi_processor_setup_cpuidle_states(struct acpi_processor *pr)

    prepares and configures cpuidle global state data i.e. idle routines

    :param struct acpi_processor \*pr:
        the ACPI processor

.. _`acpi_processor_setup_cpuidle_dev`:

acpi_processor_setup_cpuidle_dev
================================

.. c:function:: int acpi_processor_setup_cpuidle_dev(struct acpi_processor *pr, struct cpuidle_device *dev)

    prepares and configures CPUIDLE device i.e. per-cpu data

    :param struct acpi_processor \*pr:
        the ACPI processor

    :param struct cpuidle_device \*dev:
        the cpuidle device

.. This file was automatic generated / don't edit.

