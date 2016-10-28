.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_pmc_core.c

.. _`intel_pmc_slp_s0_counter_read`:

intel_pmc_slp_s0_counter_read
=============================

.. c:function:: int intel_pmc_slp_s0_counter_read(u32 *data)

    Read SLP_S0 residency.

    :param u32 \*data:
        Out param that contains current SLP_S0 count.

.. _`intel_pmc_slp_s0_counter_read.description`:

Description
-----------

This API currently supports Intel Skylake SoC and Sunrise
Point Platform Controller Hub. Future platform support
should be added for platforms that support low power modes
beyond Package C10 state.

SLP_S0_RESIDENCY counter counts in 100 us granularity per
step hence function populates the multiplied value in out
parameter \ ``data``\ .

.. _`intel_pmc_slp_s0_counter_read.return`:

Return
------

an error code or 0 on success.

.. This file was automatic generated / don't edit.

