.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spmi/spmi-pmic-arb.c

.. _`pmic_arb_read_data`:

pmic_arb_read_data
==================

.. c:function:: void pmic_arb_read_data(struct spmi_pmic_arb *pmic_arb, u8 *buf, u32 reg, u8 bc)

    reads pmic-arb's register and copy 1..4 bytes to buf

    :param struct spmi_pmic_arb \*pmic_arb:
        *undescribed*

    :param u8 \*buf:
        output parameter, length must be bc + 1

    :param u32 reg:
        register's address

    :param u8 bc:
        byte count -1. range: 0..3

.. _`pmic_arb_write_data`:

pmic_arb_write_data
===================

.. c:function:: void pmic_arb_write_data(struct spmi_pmic_arb *pmic_arb, const u8 *buf, u32 reg, u8 bc)

    write 1..4 bytes from buf to pmic-arb's register

    :param struct spmi_pmic_arb \*pmic_arb:
        *undescribed*

    :param const u8 \*buf:
        buffer to write. length must be bc + 1.

    :param u32 reg:
        register's address.

    :param u8 bc:
        byte-count -1. range: 0..3.

.. This file was automatic generated / don't edit.

