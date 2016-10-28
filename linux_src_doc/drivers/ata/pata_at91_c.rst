.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_at91.c

.. _`smc_range`:

struct smc_range
================

.. c:type:: struct smc_range

    range of valid values for SMC register.

.. _`smc_range.definition`:

Definition
----------

.. code-block:: c

    struct smc_range {
        int min;
        int max;
    }

.. _`smc_range.members`:

Members
-------

min
    *undescribed*

max
    *undescribed*

.. _`adjust_smc_value`:

adjust_smc_value
================

.. c:function:: int adjust_smc_value(int *value, struct smc_range *range, int size)

    adjust value for one of SMC registers.

    :param int \*value:
        adjusted value

    :param struct smc_range \*range:
        array of SMC ranges with valid values

    :param int size:
        SMC ranges array size

.. _`adjust_smc_value.description`:

Description
-----------

This returns the difference between input and output value or negative
in case of invalid input value.
If negative returned, then output value = maximal possible from ranges.

.. _`calc_smc_vals`:

calc_smc_vals
=============

.. c:function:: int calc_smc_vals(struct device *dev, int *setup, int *pulse, int *cycle, int *cs_pulse)

    calculate SMC register values

    :param struct device \*dev:
        ATA device

    :param int \*setup:
        SMC_SETUP register value

    :param int \*pulse:
        SMC_PULSE register value

    :param int \*cycle:
        SMC_CYCLE register value

    :param int \*cs_pulse:
        *undescribed*

.. _`calc_smc_vals.this-returns-negative-in-case-of-invalid-values-for-smc-registers`:

This returns negative in case of invalid values for SMC registers
-----------------------------------------------------------------

-ER_SMC_RECALC - recalculation required for SMC values,
-ER_SMC_CALC - calculation failed (invalid input values).

SMC use special coding scheme, see "Coding and Range of Timing
Parameters" table from AT91SAM9 datasheets.

SMC_SETUP = 128\*setup[5] + setup[4:0]
SMC_PULSE = 256\*pulse[6] + pulse[5:0]
SMC_CYCLE = 256\*cycle[8:7] + cycle[6:0]

.. _`to_smc_format`:

to_smc_format
=============

.. c:function:: void to_smc_format(int *setup, int *pulse, int *cycle, int *cs_pulse)

    convert values into SMC format

    :param int \*setup:
        SETUP value of SMC Setup Register

    :param int \*pulse:
        PULSE value of SMC Pulse Register

    :param int \*cycle:
        CYCLE value of SMC Cycle Register

    :param int \*cs_pulse:
        NCS_PULSE value of SMC Pulse Register

.. _`set_smc_timing`:

set_smc_timing
==============

.. c:function:: void set_smc_timing(struct device *dev, struct ata_device *adev, struct at91_ide_info *info, const struct ata_timing *ata)

    SMC timings setup.

    :param struct device \*dev:
        device

    :param struct ata_device \*adev:
        *undescribed*

    :param struct at91_ide_info \*info:
        AT91 IDE info

    :param const struct ata_timing \*ata:
        ATA timings

.. _`set_smc_timing.description`:

Description
-----------

Its assumed that write timings are same as read timings,
cs_setup = 0 and cs_pulse = cycle.

.. This file was automatic generated / don't edit.

