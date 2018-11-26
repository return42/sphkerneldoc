.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-s3c24xx/cpufreq-utils.c

.. _`s3c2410_cpufreq_setrefresh`:

s3c2410_cpufreq_setrefresh
==========================

.. c:function:: void s3c2410_cpufreq_setrefresh(struct s3c_cpufreq_config *cfg)

    set SDRAM refresh value

    :param cfg:
        The frequency configuration
    :type cfg: struct s3c_cpufreq_config \*

.. _`s3c2410_cpufreq_setrefresh.description`:

Description
-----------

Set the SDRAM refresh value appropriately for the configured
frequency.

.. _`s3c2410_set_fvco`:

s3c2410_set_fvco
================

.. c:function:: void s3c2410_set_fvco(struct s3c_cpufreq_config *cfg)

    set the PLL value

    :param cfg:
        The frequency configuration
    :type cfg: struct s3c_cpufreq_config \*

.. This file was automatic generated / don't edit.

