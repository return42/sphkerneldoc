.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm.h

.. _`tpm_transmit_flags`:

enum tpm_transmit_flags
=======================

.. c:type:: enum tpm_transmit_flags

    flags for \ :c:func:`tpm_transmit`\ 

.. _`tpm_transmit_flags.definition`:

Definition
----------

.. code-block:: c

    enum tpm_transmit_flags {
        TPM_TRANSMIT_UNLOCKED,
        TPM_TRANSMIT_NESTED
    };

.. _`tpm_transmit_flags.constants`:

Constants
---------

TPM_TRANSMIT_UNLOCKED
    do not lock the chip

TPM_TRANSMIT_NESTED
    discard setup steps (power management,
    locality) including locking (i.e. implicit
    UNLOCKED)

.. This file was automatic generated / don't edit.

