.. -*- coding: utf-8; mode: rst -*-

===========
cppc_acpi.c
===========


.. _`acpi_get_psd_map`:

acpi_get_psd_map
================

.. c:function:: int acpi_get_psd_map (struct cpudata **all_cpu_data)

    Map the CPUs in a common freq domain.

    :param struct cpudata \*\*all_cpu_data:
        Ptrs to CPU specific CPPC data including PSD info.



.. _`acpi_get_psd_map.return`:

Return
------

0 for success or negative value for err.



.. _`acpi_cppc_processor_probe`:

acpi_cppc_processor_probe
=========================

.. c:function:: int acpi_cppc_processor_probe (struct acpi_processor *pr)

    Search for per CPU _CPC objects.

    :param struct acpi_processor \*pr:
        Ptr to acpi_processor containing this CPUs logical Id.



.. _`acpi_cppc_processor_probe.return`:

Return
------

0 for success or negative value for err.



.. _`acpi_cppc_processor_exit`:

acpi_cppc_processor_exit
========================

.. c:function:: void acpi_cppc_processor_exit (struct acpi_processor *pr)

    Cleanup CPC structs.

    :param struct acpi_processor \*pr:
        Ptr to acpi_processor containing this CPUs logical Id.



.. _`acpi_cppc_processor_exit.return`:

Return
------

Void



.. _`cppc_get_perf_caps`:

cppc_get_perf_caps
==================

.. c:function:: int cppc_get_perf_caps (int cpunum, struct cppc_perf_caps *perf_caps)

    Get a CPUs performance capabilities.

    :param int cpunum:
        CPU from which to get capabilities info.

    :param struct cppc_perf_caps \*perf_caps:
        ptr to cppc_perf_caps. See cppc_acpi.h



.. _`cppc_get_perf_caps.return`:

Return
------

0 for success with perf_caps populated else -ERRNO.



.. _`cppc_get_perf_ctrs`:

cppc_get_perf_ctrs
==================

.. c:function:: int cppc_get_perf_ctrs (int cpunum, struct cppc_perf_fb_ctrs *perf_fb_ctrs)

    Read a CPUs performance feedback counters.

    :param int cpunum:
        CPU from which to read counters.

    :param struct cppc_perf_fb_ctrs \*perf_fb_ctrs:
        ptr to cppc_perf_fb_ctrs. See cppc_acpi.h



.. _`cppc_get_perf_ctrs.return`:

Return
------

0 for success with perf_fb_ctrs populated else -ERRNO.



.. _`cppc_set_perf`:

cppc_set_perf
=============

.. c:function:: int cppc_set_perf (int cpu, struct cppc_perf_ctrls *perf_ctrls)

    Set a CPUs performance controls.

    :param int cpu:
        CPU for which to set performance controls.

    :param struct cppc_perf_ctrls \*perf_ctrls:
        ptr to cppc_perf_ctrls. See cppc_acpi.h



.. _`cppc_set_perf.return`:

Return
------

0 for success, -ERRNO otherwise.

