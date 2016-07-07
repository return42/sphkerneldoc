.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/at91_adc.c

.. _`at91_adc_reg_desc`:

struct at91_adc_reg_desc
========================

.. c:type:: struct at91_adc_reg_desc

    Various informations relative to registers

.. _`at91_adc_reg_desc.definition`:

Definition
----------

.. code-block:: c

    struct at91_adc_reg_desc {
        u8 channel_base;
        u32 drdy_mask;
        u8 status_register;
        u8 trigger_register;
        u32 mr_prescal_mask;
        u32 mr_startup_mask;
    }

.. _`at91_adc_reg_desc.members`:

Members
-------

channel_base
    Base offset for the channel data registers

drdy_mask
    Mask of the DRDY field in the relevant registers

status_register
    Offset of the Interrupt Status Register

trigger_register
    Offset of the Trigger setup register

mr_prescal_mask
    Mask of the PRESCAL field in the adc MR register

mr_startup_mask
    Mask of the STARTUP field in the adc MR register

.. This file was automatic generated / don't edit.

