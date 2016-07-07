.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/s3c2410_wdt.c

.. _`s3c2410_wdt_variant`:

struct s3c2410_wdt_variant
==========================

.. c:type:: struct s3c2410_wdt_variant

    Per-variant config data

.. _`s3c2410_wdt_variant.definition`:

Definition
----------

.. code-block:: c

    struct s3c2410_wdt_variant {
        int disable_reg;
        int mask_reset_reg;
        int mask_bit;
        int rst_stat_reg;
        int rst_stat_bit;
        u32 quirks;
    }

.. _`s3c2410_wdt_variant.members`:

Members
-------

disable_reg
    Offset in pmureg for the register that disables the watchdog
    timer reset functionality.

mask_reset_reg
    Offset in pmureg for the register that masks the watchdog
    timer reset functionality.

mask_bit
    Bit number for the watchdog timer in the disable register and the
    mask reset register.

rst_stat_reg
    Offset in pmureg for the register that has the reset status.

rst_stat_bit
    Bit number in the rst_stat register indicating a watchdog
    reset.

quirks
    A bitfield of quirks.

.. This file was automatic generated / don't edit.

