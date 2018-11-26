.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spmi/spmi-pmic-arb.c

.. _`pmic_arb_read_data`:

pmic_arb_read_data
==================

.. c:function:: void pmic_arb_read_data(struct spmi_pmic_arb *pmic_arb, u8 *buf, u32 reg, u8 bc)

    reads pmic-arb's register and copy 1..4 bytes to buf

    :param pmic_arb:
        *undescribed*
    :type pmic_arb: struct spmi_pmic_arb \*

    :param buf:
        output parameter, length must be bc + 1
    :type buf: u8 \*

    :param reg:
        register's address
    :type reg: u32

    :param bc:
        byte count -1. range: 0..3
    :type bc: u8

.. _`pmic_arb_write_data`:

pmic_arb_write_data
===================

.. c:function:: void pmic_arb_write_data(struct spmi_pmic_arb *pmic_arb, const u8 *buf, u32 reg, u8 bc)

    write 1..4 bytes from buf to pmic-arb's register

    :param pmic_arb:
        *undescribed*
    :type pmic_arb: struct spmi_pmic_arb \*

    :param buf:
        buffer to write. length must be bc + 1.
    :type buf: const u8 \*

    :param reg:
        register's address.
    :type reg: u32

    :param bc:
        byte-count -1. range: 0..3.
    :type bc: u8

.. This file was automatic generated / don't edit.

