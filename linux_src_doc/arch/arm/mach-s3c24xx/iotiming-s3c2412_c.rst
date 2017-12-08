.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-s3c24xx/iotiming-s3c2412.c

.. _`s3c2412_print_timing`:

s3c2412_print_timing
====================

.. c:function:: void s3c2412_print_timing(const char *pfx, struct s3c_iotimings *iot)

    print timing information via printk.

    :param const char \*pfx:
        The prefix to print each line with.

    :param struct s3c_iotimings \*iot:
        The IO timing information

.. _`to_div`:

to_div
======

.. c:function:: unsigned int to_div(unsigned int cyc_tns, unsigned int clk_tns)

    turn a cycle length into a divisor setting.

    :param unsigned int cyc_tns:
        The cycle time in 10ths of nanoseconds.

    :param unsigned int clk_tns:
        The clock period in 10ths of nanoseconds.

.. _`calc_timing`:

calc_timing
===========

.. c:function:: unsigned int calc_timing(unsigned int hwtm, unsigned int clk_tns, unsigned int *err)

    calculate timing divisor value and check in range.

    :param unsigned int hwtm:
        The hardware timing in 10ths of nanoseconds.

    :param unsigned int clk_tns:
        The clock period in 10ths of nanoseconds.

    :param unsigned int \*err:
        Pointer to err variable to update in event of failure.

.. _`s3c2412_calc_bank`:

s3c2412_calc_bank
=================

.. c:function:: int s3c2412_calc_bank(struct s3c_cpufreq_config *cfg, struct s3c2412_iobank_timing *bt)

    calculate the bank divisor settings.

    :param struct s3c_cpufreq_config \*cfg:
        The current frequency configuration.

    :param struct s3c2412_iobank_timing \*bt:
        The bank timing.

.. _`s3c2412_iotiming_debugfs`:

s3c2412_iotiming_debugfs
========================

.. c:function:: void s3c2412_iotiming_debugfs(struct seq_file *seq, struct s3c_cpufreq_config *cfg, union s3c_iobank *iob)

    debugfs show io bank timing information

    :param struct seq_file \*seq:
        The seq_file to write output to using \ :c:func:`seq_printf`\ .

    :param struct s3c_cpufreq_config \*cfg:
        The current configuration.

    :param union s3c_iobank \*iob:
        The IO bank information to decode.

.. _`s3c2412_iotiming_calc`:

s3c2412_iotiming_calc
=====================

.. c:function:: int s3c2412_iotiming_calc(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *iot)

    calculate all the bank divisor settings.

    :param struct s3c_cpufreq_config \*cfg:
        The current frequency configuration.

    :param struct s3c_iotimings \*iot:
        The bank timing information.

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

    :param struct s3c_cpufreq_config \*cfg:
        The current frequency configuration.

    :param struct s3c_iotimings \*iot:
        The bank timing information.

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

    :param unsigned int bank:
        The bank number.

    :param u32 bankcfg:
        The value of S3C2412_EBI_BANKCFG.

.. This file was automatic generated / don't edit.

