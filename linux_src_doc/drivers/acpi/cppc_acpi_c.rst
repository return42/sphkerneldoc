.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/cppc_acpi.c

.. _`acpi_get_psd_map`:

acpi_get_psd_map
================

.. c:function:: int acpi_get_psd_map(struct cppc_cpudata **all_cpu_data)

    Map the CPUs in a common freq domain.

    :param struct cppc_cpudata \*\*all_cpu_data:
        Ptrs to CPU specific CPPC data including PSD info.

.. _`acpi_get_psd_map.return`:

Return
------

0 for success or negative value for err.

.. _`cpc_ffh_supported`:

cpc_ffh_supported
=================

.. c:function:: bool cpc_ffh_supported( void)

    check if FFH reading supported

    :param  void:
        no arguments

.. _`cpc_ffh_supported.description`:

Description
-----------

Check if the architecture has support for functional fixed hardware
read/write capability.

.. _`cpc_ffh_supported.return`:

Return
------

true for supported, false for not supported

.. _`acpi_cppc_processor_probe`:

acpi_cppc_processor_probe
=========================

.. c:function:: int acpi_cppc_processor_probe(struct acpi_processor *pr)

    Search for per CPU \_CPC objects.

    :param struct acpi_processor \*pr:
        Ptr to acpi_processor containing this CPUs logical Id.

.. _`acpi_cppc_processor_probe.return`:

Return
------

0 for success or negative value for err.

.. _`acpi_cppc_processor_exit`:

acpi_cppc_processor_exit
========================

.. c:function:: void acpi_cppc_processor_exit(struct acpi_processor *pr)

    Cleanup CPC structs.

    :param struct acpi_processor \*pr:
        Ptr to acpi_processor containing this CPUs logical Id.

.. _`acpi_cppc_processor_exit.return`:

Return
------

Void

.. _`cpc_read_ffh`:

cpc_read_ffh
============

.. c:function:: int cpc_read_ffh(int cpunum, struct cpc_reg *reg, u64 *val)

    Read FFH register

    :param int cpunum:
        cpu number to read

    :param struct cpc_reg \*reg:
        cppc register information

    :param u64 \*val:
        place holder for return value

.. _`cpc_read_ffh.description`:

Description
-----------

Read bit_width bits from a specified address and bit_offset

.. _`cpc_read_ffh.return`:

Return
------

0 for success and error code

.. _`cpc_write_ffh`:

cpc_write_ffh
=============

.. c:function:: int cpc_write_ffh(int cpunum, struct cpc_reg *reg, u64 val)

    Write FFH register

    :param int cpunum:
        cpu number to write

    :param struct cpc_reg \*reg:
        cppc register information

    :param u64 val:
        value to write

.. _`cpc_write_ffh.description`:

Description
-----------

Write value of bit_width bits to a specified address and bit_offset

.. _`cpc_write_ffh.return`:

Return
------

0 for success and error code

.. _`cppc_get_perf_caps`:

cppc_get_perf_caps
==================

.. c:function:: int cppc_get_perf_caps(int cpunum, struct cppc_perf_caps *perf_caps)

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

.. c:function:: int cppc_get_perf_ctrs(int cpunum, struct cppc_perf_fb_ctrs *perf_fb_ctrs)

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

.. c:function:: int cppc_set_perf(int cpu, struct cppc_perf_ctrls *perf_ctrls)

    Set a CPUs performance controls.

    :param int cpu:
        CPU for which to set performance controls.

    :param struct cppc_perf_ctrls \*perf_ctrls:
        ptr to cppc_perf_ctrls. See cppc_acpi.h

.. _`cppc_set_perf.return`:

Return
------

0 for success, -ERRNO otherwise.

.. _`cppc_get_transition_latency`:

cppc_get_transition_latency
===========================

.. c:function:: unsigned int cppc_get_transition_latency(int cpu_num)

    returns frequency transition latency in ns

    :param int cpu_num:
        *undescribed*

.. _`cppc_get_transition_latency.description`:

Description
-----------

ACPI CPPC does not explicitly specifiy how a platform can specify the
transition latency for perfromance change requests. The closest we have
is the timing information from the PCCT tables which provides the info
on the number and frequency of PCC commands the platform can handle.

.. This file was automatic generated / don't edit.

