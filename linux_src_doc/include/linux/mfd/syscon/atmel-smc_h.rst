.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/syscon/atmel-smc.h

.. _`atmel_smc_cs_conf`:

struct atmel_smc_cs_conf
========================

.. c:type:: struct atmel_smc_cs_conf

    SMC CS config as described in the datasheet.

.. _`atmel_smc_cs_conf.definition`:

Definition
----------

.. code-block:: c

    struct atmel_smc_cs_conf {
        u32 setup;
        u32 pulse;
        u32 cycle;
        u32 timings;
        u32 mode;
    }

.. _`atmel_smc_cs_conf.members`:

Members
-------

setup
    NCS/NWE/NRD setup timings (not applicable to at91rm9200)

pulse
    NCS/NWE/NRD pulse timings (not applicable to at91rm9200)

cycle
    NWE/NRD cycle timings (not applicable to at91rm9200)

timings
    advanced NAND related timings (only applicable to HSMC)

mode
    all kind of config parameters (see the fields definition above).
    The mode fields are different on at91rm9200

.. This file was automatic generated / don't edit.

