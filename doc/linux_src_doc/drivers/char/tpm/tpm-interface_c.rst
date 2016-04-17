.. -*- coding: utf-8; mode: rst -*-

===============
tpm-interface.c
===============


.. _`tpm_continue_selftest`:

tpm_continue_selftest
=====================

.. c:function:: int tpm_continue_selftest (struct tpm_chip *chip)

    - run TPM's selftest

    :param struct tpm_chip \*chip:
        TPM chip to use



.. _`tpm_continue_selftest.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error or a value > 0 representing
a TPM error code.



.. _`tpm_is_tpm2`:

tpm_is_tpm2
===========

.. c:function:: int tpm_is_tpm2 (u32 chip_num)

    is the chip a TPM2 chip?

    :param u32 chip_num:
        tpm idx # or ANY



.. _`tpm_is_tpm2.description`:

Description
-----------

Returns < 0 on error, and 1 or 0 on success depending whether the chip
is a TPM2 chip.



.. _`tpm_pcr_read`:

tpm_pcr_read
============

.. c:function:: int tpm_pcr_read (u32 chip_num, int pcr_idx, u8 *res_buf)

    read a pcr value

    :param u32 chip_num:
        tpm idx # or ANY

    :param int pcr_idx:
        pcr idx to retrieve

    :param u8 \*res_buf:
        TPM_PCR value
        size of res_buf is 20 bytes (or NULL if you don't care)



.. _`tpm_pcr_read.description`:

Description
-----------

The TPM driver should be built-in, but for whatever reason it
isn't, protect against the chip disappearing, by incrementing
the module usage count.



.. _`tpm_ord_pcr_extend`:

TPM_ORD_PCR_EXTEND
==================

.. c:function:: TPM_ORD_PCR_EXTEND ()

    extend pcr value with hash



.. _`tpm_ord_pcr_extend.description`:

Description
-----------

The TPM driver should be built-in, but for whatever reason it
isn't, protect against the chip disappearing, by incrementing
the module usage count.



.. _`tpm_do_selftest`:

tpm_do_selftest
===============

.. c:function:: int tpm_do_selftest (struct tpm_chip *chip)

    have the TPM continue its selftest and wait until it can receive further commands

    :param struct tpm_chip \*chip:
        TPM chip to use



.. _`tpm_do_selftest.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error or a value > 0 representing
a TPM error code.



.. _`tpm_get_random`:

tpm_get_random
==============

.. c:function:: int tpm_get_random (u32 chip_num, u8 *out, size_t max)

    Get random bytes from the tpm's RNG

    :param u32 chip_num:
        A specific chip number for the request or TPM_ANY_NUM

    :param u8 \*out:
        destination buffer for the random bytes

    :param size_t max:
        the max number of bytes to write to ``out``



.. _`tpm_get_random.description`:

Description
-----------

Returns < 0 on error and the number of bytes read on success



.. _`tpm_seal_trusted`:

tpm_seal_trusted
================

.. c:function:: int tpm_seal_trusted (u32 chip_num, struct trusted_key_payload *payload, struct trusted_key_options *options)

    seal a trusted key

    :param u32 chip_num:
        A specific chip number for the request or TPM_ANY_NUM

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options



.. _`tpm_seal_trusted.description`:

Description
-----------

Returns < 0 on error and 0 on success. At the moment, only TPM 2.0 chips
are supported.



.. _`tpm_unseal_trusted`:

tpm_unseal_trusted
==================

.. c:function:: int tpm_unseal_trusted (u32 chip_num, struct trusted_key_payload *payload, struct trusted_key_options *options)

    unseal a trusted key

    :param u32 chip_num:
        A specific chip number for the request or TPM_ANY_NUM

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options



.. _`tpm_unseal_trusted.description`:

Description
-----------

Returns < 0 on error and 0 on success. At the moment, only TPM 2.0 chips
are supported.

