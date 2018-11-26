.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/s3c2440-cpufreq.c

.. _`s3c2440_cpufreq_calcdivs`:

s3c2440_cpufreq_calcdivs
========================

.. c:function:: int s3c2440_cpufreq_calcdivs(struct s3c_cpufreq_config *cfg)

    calculate divider settings

    :param cfg:
        The cpu frequency settings.
    :type cfg: struct s3c_cpufreq_config \*

.. _`s3c2440_cpufreq_calcdivs.description`:

Description
-----------

Calcualte the divider values for the given frequency settings
specified in \ ``cfg``\ . The values are stored in \ ``cfg``\  for later use
by the relevant set routine if the request settings can be reached.

.. _`s3c2440_cpufreq_setdivs`:

s3c2440_cpufreq_setdivs
=======================

.. c:function:: void s3c2440_cpufreq_setdivs(struct s3c_cpufreq_config *cfg)

    set the cpu frequency divider settings

    :param cfg:
        The cpu frequency settings.
    :type cfg: struct s3c_cpufreq_config \*

.. _`s3c2440_cpufreq_setdivs.description`:

Description
-----------

Set the divisors from the settings in \ ``cfg``\ , which where generated
during the calculation phase by \ :c:func:`s3c2440_cpufreq_calcdivs`\ .

.. This file was automatic generated / don't edit.

