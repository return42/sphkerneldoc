.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/qcom-pdc.c

.. _`qcom_pdc_gic_set_type`:

qcom_pdc_gic_set_type
=====================

.. c:function:: int qcom_pdc_gic_set_type(struct irq_data *d, unsigned int type)

    Configure PDC for the interrupt

    :param d:
        the interrupt data
    :type d: struct irq_data \*

    :param type:
        the interrupt type
    :type type: unsigned int

.. _`qcom_pdc_gic_set_type.description`:

Description
-----------

If \ ``type``\  is edge triggered, forward that as Rising edge as PDC
takes care of converting falling edge to rising edge signal
If \ ``type``\  is level, then forward that as level high as PDC
takes care of converting falling edge to rising edge signal

.. This file was automatic generated / don't edit.

