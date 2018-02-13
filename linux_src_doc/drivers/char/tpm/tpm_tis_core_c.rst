.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm_tis_core.c

.. _`tpm_tis_clkrun_enable`:

tpm_tis_clkrun_enable
=====================

.. c:function:: void tpm_tis_clkrun_enable(struct tpm_chip *chip, bool value)

    Keep clkrun protocol disabled for entire duration of a single TPM command

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param bool value:
        1 - Disable CLKRUN protocol, so that clocks are free running
        0 - Enable CLKRUN protocol
        Call this function directly in \ :c:func:`tpm_tis_remove`\  in error or driver removal
        path, since the chip->ops is set to NULL in \ :c:func:`tpm_chip_unregister`\ .

.. This file was automatic generated / don't edit.

