.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/cpu-freq-core.h

.. _`s3c2410_iobank_timing`:

struct s3c2410_iobank_timing
============================

.. c:type:: struct s3c2410_iobank_timing

    IO bank timings for S3C2410 style timings

.. _`s3c2410_iobank_timing.definition`:

Definition
----------

.. code-block:: c

    struct s3c2410_iobank_timing {
        unsigned long bankcon;
        unsigned int tacp;
        unsigned int tacs;
        unsigned int tcos;
        unsigned int tacc;
        unsigned int tcoh;
        unsigned int tcah;
        unsigned char nwait_en;
    }

.. _`s3c2410_iobank_timing.members`:

Members
-------

bankcon
    The cached version of settings in this structure.

tacp
    *undescribed*

tacs
    Time from address valid to nCS asserted.

tcos
    Time from nCS asserted to nOE or nWE asserted.

tacc
    Time that nOE or nWE is asserted.

tcoh
    Time nCS is held after nOE or nWE are released.

tcah
    Time address is held for after

nwait_en
    Whether nWAIT is enabled for this bank.

.. _`s3c2410_iobank_timing.description`:

Description
-----------

This structure represents the IO timings for a S3C2410 style IO bank
used by the CPU frequency support if it needs to change the settings
of the IO.

.. _`s3c2412_iobank_timing`:

struct s3c2412_iobank_timing
============================

.. c:type:: struct s3c2412_iobank_timing

    io timings for PL092 (S3C2412) style IO

.. _`s3c2412_iobank_timing.definition`:

Definition
----------

.. code-block:: c

    struct s3c2412_iobank_timing {
        unsigned int idcy;
        unsigned int wstrd;
        unsigned int wstwr;
        unsigned int wstoen;
        unsigned int wstwen;
        unsigned int wstbrd;
        unsigned char smbidcyr;
        unsigned char smbwstrd;
        unsigned char smbwstwr;
        unsigned char smbwstoen;
        unsigned char smbwstwen;
        unsigned char smbwstbrd;
    }

.. _`s3c2412_iobank_timing.members`:

Members
-------

idcy
    The idle cycle time between transactions.

wstrd
    nCS release to end of read cycle.

wstwr
    nCS release to end of write cycle.

wstoen
    nCS assertion to nOE assertion time.

wstwen
    nCS assertion to nWE assertion time.

wstbrd
    Burst ready delay.

smbidcyr
    Register cache for smbidcyr value.

smbwstrd
    Register cache for smbwstrd value.

smbwstwr
    Register cache for smbwstwr value.

smbwstoen
    Register cache for smbwstoen value.

smbwstwen
    Register cache for smbwstwen value.

smbwstbrd
    Register cache for smbwstbrd value.

.. _`s3c2412_iobank_timing.description`:

Description
-----------

Timing information for a IO bank on an S3C2412 or similar system which
uses a PL093 block.

.. _`s3c_iotimings`:

struct s3c_iotimings
====================

.. c:type:: struct s3c_iotimings

    Chip IO timings holder

.. _`s3c_iotimings.definition`:

Definition
----------

.. code-block:: c

    struct s3c_iotimings {
        union s3c_iobank bank;
    }

.. _`s3c_iotimings.members`:

Members
-------

bank
    The timings for each IO bank.

.. _`s3c_plltab`:

struct s3c_plltab
=================

.. c:type:: struct s3c_plltab

    PLL table information.

.. _`s3c_plltab.definition`:

Definition
----------

.. code-block:: c

    struct s3c_plltab {
        struct s3c_pllval *vals;
        int size;
    }

.. _`s3c_plltab.members`:

Members
-------

vals
    List of PLL values.

size
    Size of the PLL table \ ``vals``\ .

.. _`s3c_cpufreq_config`:

struct s3c_cpufreq_config
=========================

.. c:type:: struct s3c_cpufreq_config

    current cpu frequency configuration

.. _`s3c_cpufreq_config.definition`:

Definition
----------

.. code-block:: c

    struct s3c_cpufreq_config {
        struct s3c_freq freq;
        struct s3c_freq max;
        struct clk *mpll;
        struct cpufreq_frequency_table pll;
        struct s3c_clkdivs divs;
        struct s3c_cpufreq_info *info;
        struct s3c_cpufreq_board *board;
        unsigned int lock_pll:1;
    }

.. _`s3c_cpufreq_config.members`:

Members
-------

freq
    The current settings for the core clocks.

max
    Maxium settings, derived from core, board and user settings.

mpll
    *undescribed*

pll
    The PLL table entry for the current PLL settings.

divs
    The divisor settings for the core clocks.

info
    The current core driver information.

board
    The information for the board we are running on.

lock_pll
    Set if the PLL settings cannot be changed.

.. _`s3c_cpufreq_config.description`:

Description
-----------

This is for the core drivers that need to know information about
the current settings and values. It should not be needed by any
device drivers.

.. _`s3c_cpufreq_info`:

struct s3c_cpufreq_info
=======================

.. c:type:: struct s3c_cpufreq_info

    Information for the CPU frequency driver.

.. _`s3c_cpufreq_info.definition`:

Definition
----------

.. code-block:: c

    struct s3c_cpufreq_info {
        const char *name;
        struct s3c_freq max;
        unsigned int latency;
        unsigned int locktime_m;
        unsigned int locktime_u;
        unsigned char locktime_bits;
        unsigned int need_pll:1;
        int (*get_iotiming)(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *timings);
        void (*set_iotiming)(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *timings);
        int (*calc_iotiming)(struct s3c_cpufreq_config *cfg, struct s3c_iotimings *timings);
        int (*calc_freqtable)(struct s3c_cpufreq_config *cfg,struct cpufreq_frequency_table *t, size_t table_size);
        void (*debug_io_show)(struct seq_file *seq,struct s3c_cpufreq_config *cfg, union s3c_iobank *iob);
        void (*set_refresh)(struct s3c_cpufreq_config *cfg);
        void (*set_fvco)(struct s3c_cpufreq_config *cfg);
        void (*set_divs)(struct s3c_cpufreq_config *cfg);
        int (*calc_divs)(struct s3c_cpufreq_config *cfg);
    }

.. _`s3c_cpufreq_info.members`:

Members
-------

name
    The name of this implementation.

max
    The maximum frequencies for the system.

latency
    Transition latency to give to cpufreq.

locktime_m
    The lock-time in uS for the MPLL.

locktime_u
    The lock-time in uS for the UPLL.

locktime_bits
    *undescribed*

need_pll
    Set if this driver needs to change the PLL values to achieve
    any frequency changes. This is really only need by devices like the
    S3C2410 where there is no or limited divider between the PLL and the
    ARMCLK.

get_iotiming
    Get the current IO timing data, mainly for use at start.

set_iotiming
    Update the IO timings from the cached copies calculated
    from the \ ``calc_iotiming``\  entry when changing the frequency.

calc_iotiming
    Calculate and update the cached copies of the IO timings
    from the newly calculated frequencies.

calc_freqtable
    Calculate (fill in) the given frequency table from the
    current frequency configuration. If the table passed in is NULL,
    then the return is the number of elements to be filled for allocation
    of the table.

debug_io_show
    *undescribed*

set_refresh
    Set the memory refresh configuration.

set_fvco
    Set the PLL frequencies.

set_divs
    Update the clock divisors.

calc_divs
    Calculate the clock divisors.

.. This file was automatic generated / don't edit.

