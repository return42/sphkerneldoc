.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/s3c24xx-cpufreq.c

.. _`s3c_cpufreq_freq_min`:

s3c_cpufreq_freq_min
====================

.. c:function:: void s3c_cpufreq_freq_min(struct s3c_freq *dst, struct s3c_freq *a, struct s3c_freq *b)

    find the minimum settings for the given freq.

    :param struct s3c_freq \*dst:
        The destination structure

    :param struct s3c_freq \*a:
        One argument.

    :param struct s3c_freq \*b:
        The other argument.

.. _`s3c_cpufreq_freq_min.description`:

Description
-----------

Create a minimum of each frequency entry in the 'struct s3c_freq',
unless the entry is zero when it is ignored and the non-zero argument
used.

.. _`s3c_plltab_register`:

s3c_plltab_register
===================

.. c:function:: int s3c_plltab_register(struct cpufreq_frequency_table *plls, unsigned int plls_no)

    register CPU PLL table.

    :param struct cpufreq_frequency_table \*plls:
        The list of PLL entries.

    :param unsigned int plls_no:
        The size of the PLL entries \ ``plls``\ .

.. _`s3c_plltab_register.description`:

Description
-----------

Register the given set of PLLs with the system.

.. This file was automatic generated / don't edit.

