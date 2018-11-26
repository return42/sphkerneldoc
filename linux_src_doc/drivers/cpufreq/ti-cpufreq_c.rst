.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/ti-cpufreq.c

.. _`ti_cpufreq_get_efuse`:

ti_cpufreq_get_efuse
====================

.. c:function:: int ti_cpufreq_get_efuse(struct ti_cpufreq_data *opp_data, u32 *efuse_value)

    Parse and return efuse value present on SoC

    :param opp_data:
        pointer to ti_cpufreq_data context
    :type opp_data: struct ti_cpufreq_data \*

    :param efuse_value:
        Set to the value parsed from efuse
    :type efuse_value: u32 \*

.. _`ti_cpufreq_get_efuse.description`:

Description
-----------

Returns error code if efuse not read properly.

.. _`ti_cpufreq_get_rev`:

ti_cpufreq_get_rev
==================

.. c:function:: int ti_cpufreq_get_rev(struct ti_cpufreq_data *opp_data, u32 *revision_value)

    Parse and return rev value present on SoC

    :param opp_data:
        pointer to ti_cpufreq_data context
    :type opp_data: struct ti_cpufreq_data \*

    :param revision_value:
        Set to the value parsed from revision register
    :type revision_value: u32 \*

.. _`ti_cpufreq_get_rev.description`:

Description
-----------

Returns error code if revision not read properly.

.. This file was automatic generated / don't edit.

