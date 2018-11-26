.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-s3c24xx/iotiming-s3c2412.c

.. _`s3c2412_print_timing`:

s3c2412_print_timing
====================

.. c:function:: void s3c2412_print_timing(const char *pfx, struct s3c_iotimings *iot)

    print timing information via printk.

    :param pfx:
        The prefix to print each line with.
    :type pfx: const char \*

    :param iot:
        The IO timing information
    :type iot: struct s3c_iotimings \*

.. _`to_div`:

to_div
======

.. c:function:: unsigned int to_div(unsigned int cyc_tns, unsigned int clk_tns)

    turn a cycle length into a divisor setting.

    :param cyc_tns:
        The cycle time in 10ths of nanoseconds.
    :type cyc_tns: unsigned int

    :param clk_tns:
        The clock period in 10ths of nanoseconds.
    :type clk_tns: unsigned int

.. _`calc_timing`:

calc_timing
===========

.. c:function:: unsigned int calc_timing(unsigned int hwtm, unsigned int clk_tns, unsigned int *err)

    calculate timing divisor value and check in range.

    :param hwtm:
        The hardware timing in 10ths of nanoseconds.
    :type hwtm: unsigned int

    :param clk_tns:
        The clock period in 10ths of nanoseconds.
    :type clk_tns: unsigned int

    :param err:
        Pointer to err variable to update in event of failure.
    :type err: unsigned int \*

.. _`s3c2412_calc_bank`:

s3c2412_calc_bank
=================

.. c:function:: int s3c2412_calc_bank(struct s3c_cpufreq_config *cfg, struct s3c2412_iobank_timing *bt)

    calculate the bank divisor settings.

    :param cfg:
        The current frequency configuration.
    :type cfg: struct s3c_cpufreq_config \*

    :param bt:
        The bank timing.
    :type bt: struct s3c2412_iobank_timing \*

.. _`s3c2412_iotiming_debugfs`:

s3c2412_iotiming_debugfs
========================

.. c:function:: void s3c2412_iotiming_debugfs(struct seq_file *seq, struct s3c_cpufreq_config *cfg, union s3c_iobank *iob)

    debugfs show io bank timing information

    :param seq:
        The seq_file to write output to using \ :c:func:`seq_printf`\ .
    :type seq: struct seq_file \*

    :param cfg:
        The current configuration.
    :type cfg: struct s3c_cpufreq_config \*

    :param iob:
        The IO bank information to decode.
    :type iob: union s3c_iobank \*

.. _`s3c2412_iotiming_calc`:

s3c2412_iotiming_calc
=====================

.. c:function:: int s3c2412_iotiming_calc(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *iot)

    calculate all the bank divisor settings.

    :param cfg:
        The current frequency configuration.
    :type cfg: struct s3c_cpufreq_config \*

    :param iot:
        The bank timing information.
    :type iot: struct s3c_iotimings \*

.. _`s3c2412_iotiming_calc.description`:

Description
-----------

Calculate the timing information for all the banks that are
configured as IO, using \ :c:func:`s3c2412_calc_bank`\ .

.. _`s3c2412_iotiming_set`:

s3c2412_iotiming_set
====================

.. c:function:: void s3c2412_iotiming_set(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *iot)

    set the timing information

    :param cfg:
        The current frequency configuration.
    :type cfg: struct s3c_cpufreq_config \*

    :param iot:
        The bank timing information.
    :type iot: struct s3c_iotimings \*

.. _`s3c2412_iotiming_set.description`:

Description
-----------

Set the IO bank information from the details calculated earlier from
calling \ :c:func:`s3c2412_iotiming_calc`\ .

.. _`bank_is_io`:

bank_is_io
==========

.. c:function:: bool bank_is_io(unsigned int bank, u32 bankcfg)

    return true if bank is (possibly) IO.

    :param bank:
        The bank number.
    :type bank: unsigned int

    :param bankcfg:
        The value of S3C2412_EBI_BANKCFG.
    :type bankcfg: u32

.. This file was automatic generated / don't edit.

