.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-s3c24xx/iotiming-s3c2410.c

.. _`s3c2410_print_timing`:

s3c2410_print_timing
====================

.. c:function:: void s3c2410_print_timing(const char *pfx, struct s3c_iotimings *timings)

    print bank timing data for debug purposes

    :param pfx:
        The prefix to put on the output
    :type pfx: const char \*

    :param timings:
        The timing inforamtion to print.
    :type timings: struct s3c_iotimings \*

.. _`bank_reg`:

bank_reg
========

.. c:function:: void __iomem *bank_reg(unsigned int bank)

    convert bank number to pointer to the control register.

    :param bank:
        The IO bank number.
    :type bank: unsigned int

.. _`bank_is_io`:

bank_is_io
==========

.. c:function:: int bank_is_io(unsigned long bankcon)

    test whether bank is used for IO

    :param bankcon:
        The bank control register.
    :type bankcon: unsigned long

.. _`bank_is_io.description`:

Description
-----------

This is a simplistic test to see if any BANKCON[x] is not an IO
bank. It currently does not take into account whether BWSCON has
an illegal width-setting in it, or if the pin connected to nCS[x]
is actually being handled as a chip-select.

.. _`to_div`:

to_div
======

.. c:function:: unsigned int to_div(unsigned int cyc, unsigned int hclk_tns)

    convert cycle time to divisor

    :param cyc:
        The cycle time, in 10ths of nanoseconds.
    :type cyc: unsigned int

    :param hclk_tns:
        The cycle time for HCLK, in 10ths of nanoseconds.
    :type hclk_tns: unsigned int

.. _`to_div.description`:

Description
-----------

Convert the given cycle time into the divisor to use to obtain it from
HCLK.

.. _`calc_0124`:

calc_0124
=========

.. c:function:: unsigned int calc_0124(unsigned int cyc, unsigned long hclk_tns, unsigned long *v, int shift)

    calculate divisor control for divisors that do /0, /1. /2 and /4

    :param cyc:
        The cycle time, in 10ths of nanoseconds.
    :type cyc: unsigned int

    :param hclk_tns:
        The cycle time for HCLK, in 10ths of nanoseconds.
    :type hclk_tns: unsigned long

    :param v:
        Pointer to register to alter.
    :type v: unsigned long \*

    :param shift:
        The shift to get to the control bits.
    :type shift: int

.. _`calc_0124.description`:

Description
-----------

Calculate the divisor, and turn it into the correct control bits to
set in the result, \ ``v``\ .

.. _`calc_tacc`:

calc_tacc
=========

.. c:function:: int calc_tacc(unsigned int cyc, int nwait_en, unsigned long hclk_tns, unsigned long *v)

    calculate divisor control for tacc.

    :param cyc:
        The cycle time, in 10ths of nanoseconds.
    :type cyc: unsigned int

    :param nwait_en:
        IS nWAIT enabled for this bank.
    :type nwait_en: int

    :param hclk_tns:
        The cycle time for HCLK, in 10ths of nanoseconds.
    :type hclk_tns: unsigned long

    :param v:
        Pointer to register to alter.
    :type v: unsigned long \*

.. _`calc_tacc.description`:

Description
-----------

Calculate the divisor control for tACC, taking into account whether
the bank has nWAIT enabled. The result is used to modify the value
pointed to by \ ``v``\ .

.. _`s3c2410_calc_bank`:

s3c2410_calc_bank
=================

.. c:function:: int s3c2410_calc_bank(struct s3c_cpufreq_config *cfg, struct s3c2410_iobank_timing *bt)

    calculate bank timing information

    :param cfg:
        The configuration we need to calculate for.
    :type cfg: struct s3c_cpufreq_config \*

    :param bt:
        The bank timing information.
    :type bt: struct s3c2410_iobank_timing \*

.. _`s3c2410_calc_bank.description`:

Description
-----------

Given the cycle timine for a bank \ ``bt``\ , calculate the new BANKCON
setting for the \ ``cfg``\  timing. This updates the timing information
ready for the cpu frequency change.

.. _`get_tacc`:

get_tacc
========

.. c:function:: unsigned int get_tacc(unsigned long hclk_tns, unsigned long val)

    turn tACC value into cycle time

    :param hclk_tns:
        The cycle time for HCLK, in 10ths of nanoseconds.
    :type hclk_tns: unsigned long

    :param val:
        The bank timing register value, shifed down.
    :type val: unsigned long

.. _`get_0124`:

get_0124
========

.. c:function:: unsigned int get_0124(unsigned long hclk_tns, unsigned long val)

    turn 0/1/2/4 divider into cycle time

    :param hclk_tns:
        The cycle time for HCLK, in 10ths of nanoseconds.
    :type hclk_tns: unsigned long

    :param val:
        The bank timing register value, shifed down.
    :type val: unsigned long

.. _`s3c2410_iotiming_getbank`:

s3c2410_iotiming_getbank
========================

.. c:function:: void s3c2410_iotiming_getbank(struct s3c_cpufreq_config *cfg, struct s3c2410_iobank_timing *bt)

    turn BANKCON into cycle time information

    :param cfg:
        The frequency configuration
    :type cfg: struct s3c_cpufreq_config \*

    :param bt:
        The bank timing to fill in (uses cached BANKCON)
    :type bt: struct s3c2410_iobank_timing \*

.. _`s3c2410_iotiming_getbank.description`:

Description
-----------

Given the BANKCON setting in \ ``bt``\  and the current frequency settings
in \ ``cfg``\ , update the cycle timing information.

.. _`s3c2410_iotiming_debugfs`:

s3c2410_iotiming_debugfs
========================

.. c:function:: void s3c2410_iotiming_debugfs(struct seq_file *seq, struct s3c_cpufreq_config *cfg, union s3c_iobank *iob)

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

.. _`s3c2410_iotiming_calc`:

s3c2410_iotiming_calc
=====================

.. c:function:: int s3c2410_iotiming_calc(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *iot)

    Calculate bank timing for frequency change.

    :param cfg:
        The frequency configuration
    :type cfg: struct s3c_cpufreq_config \*

    :param iot:
        The IO timing information to fill out.
    :type iot: struct s3c_iotimings \*

.. _`s3c2410_iotiming_calc.description`:

Description
-----------

Calculate the new values for the banks in \ ``iot``\  based on the new
frequency information in \ ``cfg``\ . This is then used by \ :c:func:`s3c2410_iotiming_set`\ 
to update the timing when necessary.

.. _`s3c2410_iotiming_set`:

s3c2410_iotiming_set
====================

.. c:function:: void s3c2410_iotiming_set(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *iot)

    set the IO timings from the given setup.

    :param cfg:
        The frequency configuration
    :type cfg: struct s3c_cpufreq_config \*

    :param iot:
        The IO timing information to use.
    :type iot: struct s3c_iotimings \*

.. _`s3c2410_iotiming_set.description`:

Description
-----------

Set all the currently used IO bank timing information generated
by \ :c:func:`s3c2410_iotiming_calc`\  once the core has validated that all
the new values are within permitted bounds.

.. _`s3c2410_iotiming_get`:

s3c2410_iotiming_get
====================

.. c:function:: int s3c2410_iotiming_get(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *timings)

    Get the timing information from current registers.

    :param cfg:
        The frequency configuration
    :type cfg: struct s3c_cpufreq_config \*

    :param timings:
        The IO timing information to fill out.
    :type timings: struct s3c_iotimings \*

.. _`s3c2410_iotiming_get.description`:

Description
-----------

Calculate the \ ``timings``\  timing information from the current frequency
information in \ ``cfg``\ , and the new frequency configuration
through all the IO banks, reading the state and then updating \ ``iot``\ 
as necessary.

This is used at the moment on initialisation to get the current
configuration so that boards do not have to carry their own setup
if the timings are correct on initialisation.

.. This file was automatic generated / don't edit.

