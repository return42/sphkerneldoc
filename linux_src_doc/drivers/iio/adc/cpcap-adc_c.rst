.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/cpcap-adc.c

.. _`cpcap_adc_ato`:

struct cpcap_adc_ato
====================

.. c:type:: struct cpcap_adc_ato

    timing settings for cpcap adc

.. _`cpcap_adc_ato.definition`:

Definition
----------

.. code-block:: c

    struct cpcap_adc_ato {
        unsigned short ato_in;
        unsigned short atox_in;
        unsigned short adc_ps_factor_in;
        unsigned short atox_ps_factor_in;
        unsigned short ato_out;
        unsigned short atox_out;
        unsigned short adc_ps_factor_out;
        unsigned short atox_ps_factor_out;
    }

.. _`cpcap_adc_ato.members`:

Members
-------

ato_in
    *undescribed*

atox_in
    *undescribed*

adc_ps_factor_in
    *undescribed*

atox_ps_factor_in
    *undescribed*

ato_out
    *undescribed*

atox_out
    *undescribed*

adc_ps_factor_out
    *undescribed*

atox_ps_factor_out
    *undescribed*

.. _`cpcap_adc_ato.description`:

Description
-----------

Unfortunately no cpcap documentation available, please document when
using these.

.. _`cpcap_adc`:

struct cpcap_adc
================

.. c:type:: struct cpcap_adc

    adc - cpcap adc device driver data

.. _`cpcap_adc.definition`:

Definition
----------

.. code-block:: c

    struct cpcap_adc {
        struct regmap *reg;
        struct device *dev;
        u16 vendor;
        int irq;
        struct mutex lock;
        const struct cpcap_adc_ato *ato;
        wait_queue_head_t wq_data_avail;
        bool done;
    }

.. _`cpcap_adc.members`:

Members
-------

reg
    cpcap regmap

dev
    struct device

vendor
    cpcap vendor

irq
    interrupt

lock
    mutex

ato
    request timings

wq_data_avail
    work queue

done
    work done

.. _`cpcap_adc_channel`:

enum cpcap_adc_channel
======================

.. c:type:: enum cpcap_adc_channel

    cpcap adc channels

.. _`cpcap_adc_channel.definition`:

Definition
----------

.. code-block:: c

    enum cpcap_adc_channel {
        CPCAP_ADC_AD0_BATTDETB,
        CPCAP_ADC_BATTP,
        CPCAP_ADC_VBUS,
        CPCAP_ADC_AD3,
        CPCAP_ADC_BPLUS_AD4,
        CPCAP_ADC_CHG_ISENSE,
        CPCAP_ADC_BATTI,
        CPCAP_ADC_USB_ID,
        CPCAP_ADC_AD8,
        CPCAP_ADC_AD9,
        CPCAP_ADC_LICELL,
        CPCAP_ADC_HV_BATTP,
        CPCAP_ADC_TSX1_AD12,
        CPCAP_ADC_TSX2_AD13,
        CPCAP_ADC_TSY1_AD14,
        CPCAP_ADC_TSY2_AD15,
        CPCAP_ADC_BATTP_PI16,
        CPCAP_ADC_BATTI_PI17,
        CPCAP_ADC_CHANNEL_NUM
    };

.. _`cpcap_adc_channel.constants`:

Constants
---------

CPCAP_ADC_AD0_BATTDETB
    *undescribed*

CPCAP_ADC_BATTP
    *undescribed*

CPCAP_ADC_VBUS
    *undescribed*

CPCAP_ADC_AD3
    *undescribed*

CPCAP_ADC_BPLUS_AD4
    *undescribed*

CPCAP_ADC_CHG_ISENSE
    *undescribed*

CPCAP_ADC_BATTI
    *undescribed*

CPCAP_ADC_USB_ID
    *undescribed*

CPCAP_ADC_AD8
    *undescribed*

CPCAP_ADC_AD9
    *undescribed*

CPCAP_ADC_LICELL
    *undescribed*

CPCAP_ADC_HV_BATTP
    *undescribed*

CPCAP_ADC_TSX1_AD12
    *undescribed*

CPCAP_ADC_TSX2_AD13
    *undescribed*

CPCAP_ADC_TSY1_AD14
    *undescribed*

CPCAP_ADC_TSY2_AD15
    *undescribed*

CPCAP_ADC_BATTP_PI16
    *undescribed*

CPCAP_ADC_BATTI_PI17
    *undescribed*

CPCAP_ADC_CHANNEL_NUM
    *undescribed*

.. _`cpcap_adc_timing`:

enum cpcap_adc_timing
=====================

.. c:type:: enum cpcap_adc_timing

    cpcap adc timing options

.. _`cpcap_adc_timing.definition`:

Definition
----------

.. code-block:: c

    enum cpcap_adc_timing {
        CPCAP_ADC_TIMING_IMM,
        CPCAP_ADC_TIMING_IN,
        CPCAP_ADC_TIMING_OUT
    };

.. _`cpcap_adc_timing.constants`:

Constants
---------

CPCAP_ADC_TIMING_IMM
    *undescribed*

CPCAP_ADC_TIMING_IN
    *undescribed*

CPCAP_ADC_TIMING_OUT
    *undescribed*

.. _`cpcap_adc_timing.description`:

Description
-----------

CPCAP_ADC_TIMING_IMM seems to be immediate with no timings.
Please document when using.

.. _`cpcap_adc_phasing_tbl`:

struct cpcap_adc_phasing_tbl
============================

.. c:type:: struct cpcap_adc_phasing_tbl

    cpcap phasing table

.. _`cpcap_adc_phasing_tbl.definition`:

Definition
----------

.. code-block:: c

    struct cpcap_adc_phasing_tbl {
        short offset;
        unsigned short multiplier;
        unsigned short divider;
        short min;
        short max;
    }

.. _`cpcap_adc_phasing_tbl.members`:

Members
-------

offset
    offset in the phasing table

multiplier
    multiplier in the phasing table

divider
    divider in the phasing table

min
    minimum value

max
    maximum value

.. _`cpcap_adc_conversion_tbl`:

struct cpcap_adc_conversion_tbl
===============================

.. c:type:: struct cpcap_adc_conversion_tbl

    cpcap conversion table

.. _`cpcap_adc_conversion_tbl.definition`:

Definition
----------

.. code-block:: c

    struct cpcap_adc_conversion_tbl {
        enum iio_chan_info_enum conv_type;
        int align_offset;
        int conv_offset;
        int cal_offset;
        int multiplier;
        int divider;
    }

.. _`cpcap_adc_conversion_tbl.members`:

Members
-------

conv_type
    conversion type

align_offset
    align offset

conv_offset
    conversion offset

cal_offset
    calibration offset

multiplier
    conversion multiplier

divider
    conversion divider

.. _`cpcap_adc_request`:

struct cpcap_adc_request
========================

.. c:type:: struct cpcap_adc_request

    cpcap adc request

.. _`cpcap_adc_request.definition`:

Definition
----------

.. code-block:: c

    struct cpcap_adc_request {
        int channel;
        const struct cpcap_adc_phasing_tbl *phase_tbl;
        const struct cpcap_adc_conversion_tbl *conv_tbl;
        int bank_index;
        enum cpcap_adc_timing timing;
        int result;
    }

.. _`cpcap_adc_request.members`:

Members
-------

channel
    request channel

phase_tbl
    channel phasing table

conv_tbl
    channel conversion table

bank_index
    channel index within the bank

timing
    timing settings

result
    result

.. This file was automatic generated / don't edit.

