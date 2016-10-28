.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spmi/spmi-pmic-arb.c

.. _`pa_read_data`:

pa_read_data
============

.. c:function:: void pa_read_data(struct spmi_pmic_arb_dev *dev, u8 *buf, u32 reg, u8 bc)

    reads pmic-arb's register and copy 1..4 bytes to buf

    :param struct spmi_pmic_arb_dev \*dev:
        *undescribed*

    :param u8 \*buf:
        output parameter, length must be bc + 1

    :param u32 reg:
        register's address

    :param u8 bc:
        byte count -1. range: 0..3

.. _`pa_write_data`:

pa_write_data
=============

.. c:function:: void pa_write_data(struct spmi_pmic_arb_dev *dev, const u8 *buf, u32 reg, u8 bc)

    write 1..4 bytes from buf to pmic-arb's register

    :param struct spmi_pmic_arb_dev \*dev:
        *undescribed*

    :param const u8 \*buf:
        buffer to write. length must be bc + 1.

    :param u32 reg:
        register's address.

    :param u8 bc:
        byte-count -1. range: 0..3.

.. This file was automatic generated / don't edit.

