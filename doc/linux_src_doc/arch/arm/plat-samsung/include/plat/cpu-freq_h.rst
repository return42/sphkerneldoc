.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/cpu-freq.h

.. _`s3c_freq`:

struct s3c_freq
===============

.. c:type:: struct s3c_freq

    frequency information (mainly for core drivers)

.. _`s3c_freq.definition`:

Definition
----------

.. code-block:: c

    struct s3c_freq {
        unsigned long fclk;
        unsigned long armclk;
        unsigned long hclk_tns;
        unsigned long hclk;
        unsigned long pclk;
    }

.. _`s3c_freq.members`:

Members
-------

fclk
    The FCLK frequency in Hz.

armclk
    The ARMCLK frequency in Hz.

hclk_tns
    HCLK cycle time in 10ths of nano-seconds.

hclk
    The HCLK frequency in Hz.

pclk
    The PCLK frequency in Hz.

.. _`s3c_freq.description`:

Description
-----------

This contains the frequency information about the current configuration
mainly for the core drivers to ensure we do not end up passing about
a large number of parameters.

The \ ``hclk_tns``\  field is a useful cache for the parts of the drivers that
need to calculate IO timings and suchlike.

.. _`s3c_cpufreq_freqs`:

struct s3c_cpufreq_freqs
========================

.. c:type:: struct s3c_cpufreq_freqs

    s3c cpufreq notification information.

.. _`s3c_cpufreq_freqs.definition`:

Definition
----------

.. code-block:: c

    struct s3c_cpufreq_freqs {
        struct cpufreq_freqs freqs;
        struct s3c_freq old;
        struct s3c_freq new;
        unsigned int pll_changing:1;
    }

.. _`s3c_cpufreq_freqs.members`:

Members
-------

freqs
    The cpufreq setting information.

old
    The old clock settings.

new
    The new clock settings.

pll_changing
    Set if the PLL is changing.

.. _`s3c_cpufreq_freqs.description`:

Description
-----------

Wrapper 'struct cpufreq_freqs' so that any drivers receiving the
notification can use this information that is not provided by just
having the core frequency alone.

The pll_changing flag is used to indicate if the PLL itself is
being set during this change. This is important as the clocks
will temporarily be set to the XTAL clock during this time, so
drivers may want to close down their output during this time.

Note, this is not being used by any current drivers and therefore
may be removed in the future.

.. _`s3c_clkdivs`:

struct s3c_clkdivs
==================

.. c:type:: struct s3c_clkdivs

    clock divisor information

.. _`s3c_clkdivs.definition`:

Definition
----------

.. code-block:: c

    struct s3c_clkdivs {
        int p_divisor;
        int h_divisor;
        int arm_divisor;
        unsigned char dvs;
    }

.. _`s3c_clkdivs.members`:

Members
-------

p_divisor
    Divisor from FCLK to PCLK.

h_divisor
    Divisor from FCLK to HCLK.

arm_divisor
    Divisor from FCLK to ARMCLK (not all CPUs).

dvs
    Non-zero if using DVS mode for ARMCLK.

.. _`s3c_clkdivs.description`:

Description
-----------

Divisor settings for the core clocks.

.. _`s3c_pllval`:

struct s3c_pllval
=================

.. c:type:: struct s3c_pllval

    PLL value entry.

.. _`s3c_pllval.definition`:

Definition
----------

.. code-block:: c

    struct s3c_pllval {
        unsigned long freq;
        unsigned long pll_reg;
    }

.. _`s3c_pllval.members`:

Members
-------

freq
    The frequency for this entry in Hz.

pll_reg
    The PLL register setting for this PLL value.

.. _`s3c_cpufreq_board`:

struct s3c_cpufreq_board
========================

.. c:type:: struct s3c_cpufreq_board

    per-board cpu frequency informatin

.. _`s3c_cpufreq_board.definition`:

Definition
----------

.. code-block:: c

    struct s3c_cpufreq_board {
        unsigned int refresh;
        unsigned int auto_io:1;
        unsigned int need_io:1;
        struct s3c_freq max;
    }

.. _`s3c_cpufreq_board.members`:

Members
-------

refresh
    The SDRAM refresh period in nanoseconds.

auto_io
    Set if the IO timing settings should be generated from the
    initialisation time hardware registers.

need_io
    Set if the board has external IO on any of the chipselect
    lines that will require the hardware timing registers to be
    updated on a clock change.

max
    The maxium frequency limits for the system. Any field that
    is left at zero will use the CPU's settings.

.. _`s3c_cpufreq_board.description`:

Description
-----------

This contains the board specific settings that affect how the CPU
drivers chose settings. These include the memory refresh and IO
timing information.

Registration depends on the driver being used, the ARMCLK only
implementation does not currently need this but the older style
driver requires this to be available.

.. This file was automatic generated / don't edit.

