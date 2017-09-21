.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm-interface.c

.. _`tpm_transmit`:

tpm_transmit
============

.. c:function:: ssize_t tpm_transmit(struct tpm_chip *chip, struct tpm_space *space, u8 *buf, size_t bufsiz, unsigned int flags)

    Internal kernel interface to transmit TPM commands.

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param struct tpm_space \*space:
        *undescribed*

    :param u8 \*buf:
        TPM command buffer

    :param size_t bufsiz:
        length of the TPM command buffer

    :param unsigned int flags:
        tpm transmit flags - bitmap

.. _`tpm_transmit.return`:

Return
------

0 when the operation is successful.
A negative number for system errors (errno).

.. _`tpm_transmit_cmd`:

tpm_transmit_cmd
================

.. c:function:: ssize_t tpm_transmit_cmd(struct tpm_chip *chip, struct tpm_space *space, const void *buf, size_t bufsiz, size_t min_rsp_body_length, unsigned int flags, const char *desc)

    send a tpm command to the device The function extracts tpm out header return code

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param struct tpm_space \*space:
        *undescribed*

    :param const void \*buf:
        TPM command buffer

    :param size_t bufsiz:
        length of the buffer

    :param size_t min_rsp_body_length:
        minimum expected length of response body

    :param unsigned int flags:
        tpm transmit flags - bitmap

    :param const char \*desc:
        command description used in the error message

.. _`tpm_transmit_cmd.return`:

Return
------

0 when the operation is successful.
A negative number for system errors (errno).
A positive number for a TPM error.

.. _`tpm_startup`:

tpm_startup
===========

.. c:function:: int tpm_startup(struct tpm_chip *chip)

    turn on the TPM

    :param struct tpm_chip \*chip:
        TPM chip to use

.. _`tpm_startup.description`:

Description
-----------

Normally the firmware should start the TPM. This function is provided as a
workaround if this does not happen. A legal case for this could be for
example when a TPM emulator is used.

.. _`tpm_startup.return`:

Return
------

same as \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_continue_selftest`:

tpm_continue_selftest
=====================

.. c:function:: int tpm_continue_selftest(struct tpm_chip *chip)

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

.. c:function:: int tpm_is_tpm2(u32 chip_num)

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

.. c:function:: int tpm_pcr_read(u32 chip_num, int pcr_idx, u8 *res_buf)

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

.. _`tpm_pcr_extend`:

tpm_pcr_extend
==============

.. c:function:: int tpm_pcr_extend(u32 chip_num, int pcr_idx, const u8 *hash)

    extend pcr value with hash

    :param u32 chip_num:
        tpm idx # or AN&

    :param int pcr_idx:
        pcr idx to extend

    :param const u8 \*hash:
        hash value used to extend pcr value

.. _`tpm_pcr_extend.description`:

Description
-----------

The TPM driver should be built-in, but for whatever reason it
isn't, protect against the chip disappearing, by incrementing
the module usage count.

.. _`tpm_do_selftest`:

tpm_do_selftest
===============

.. c:function:: int tpm_do_selftest(struct tpm_chip *chip)

    have the TPM continue its selftest and wait until it can receive further commands

    :param struct tpm_chip \*chip:
        TPM chip to use

.. _`tpm_do_selftest.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error or a value > 0 representing
a TPM error code.

.. _`tpm1_auto_startup`:

tpm1_auto_startup
=================

.. c:function:: int tpm1_auto_startup(struct tpm_chip *chip)

    Perform the standard automatic TPM initialization sequence

    :param struct tpm_chip \*chip:
        TPM chip to use

.. _`tpm1_auto_startup.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error.

.. _`tpm_get_random`:

tpm_get_random
==============

.. c:function:: int tpm_get_random(u32 chip_num, u8 *out, size_t max)

    Get random bytes from the tpm's RNG

    :param u32 chip_num:
        A specific chip number for the request or TPM_ANY_NUM

    :param u8 \*out:
        destination buffer for the random bytes

    :param size_t max:
        the max number of bytes to write to \ ``out``\ 

.. _`tpm_get_random.description`:

Description
-----------

Returns < 0 on error and the number of bytes read on success

.. _`tpm_seal_trusted`:

tpm_seal_trusted
================

.. c:function:: int tpm_seal_trusted(u32 chip_num, struct trusted_key_payload *payload, struct trusted_key_options *options)

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

.. c:function:: int tpm_unseal_trusted(u32 chip_num, struct trusted_key_payload *payload, struct trusted_key_options *options)

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

.. This file was automatic generated / don't edit.

