.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/s3c24xx-cpufreq.c

.. _`s3c_cpufreq_freq_min`:

s3c_cpufreq_freq_min
====================

.. c:function:: void s3c_cpufreq_freq_min(struct s3c_freq *dst, struct s3c_freq *a, struct s3c_freq *b)

    find the minimum settings for the given freq.

    :param dst:
        The destination structure
    :type dst: struct s3c_freq \*

    :param a:
        One argument.
    :type a: struct s3c_freq \*

    :param b:
        The other argument.
    :type b: struct s3c_freq \*

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

    :param plls:
        The list of PLL entries.
    :type plls: struct cpufreq_frequency_table \*

    :param plls_no:
        The size of the PLL entries \ ``plls``\ .
    :type plls_no: unsigned int

.. _`s3c_plltab_register.description`:

Description
-----------

Register the given set of PLLs with the system.

.. This file was automatic generated / don't edit.

