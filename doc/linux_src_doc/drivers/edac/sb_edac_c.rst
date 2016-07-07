.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/sb_edac.c

.. _`check_if_ecc_is_active`:

check_if_ecc_is_active
======================

.. c:function:: int check_if_ecc_is_active(const u8 bus, enum type type)

    Checks if ECC is active

    :param const u8 bus:
        Device bus

    :param enum type type:
        Memory controller type

.. _`check_if_ecc_is_active.return`:

Return
------

0 in case ECC is active, -ENODEV if it can't be determined or
disabled

.. This file was automatic generated / don't edit.

