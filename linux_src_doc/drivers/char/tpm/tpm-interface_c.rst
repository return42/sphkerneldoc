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

.. c:function:: int tpm_is_tpm2(struct tpm_chip *chip)

    do we a have a TPM2 chip?

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

.. _`tpm_is_tpm2.return`:

Return
------

1 if we have a TPM2 chip.
0 if we don't have a TPM2 chip.
A negative number for system errors (errno).

.. _`tpm_pcr_read`:

tpm_pcr_read
============

.. c:function:: int tpm_pcr_read(struct tpm_chip *chip, int pcr_idx, u8 *res_buf)

    read a PCR value from SHA1 bank

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

    :param int pcr_idx:
        the PCR to be retrieved

    :param u8 \*res_buf:
        the value of the PCR

.. _`tpm_pcr_read.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_pcr_extend`:

tpm_pcr_extend
==============

.. c:function:: int tpm_pcr_extend(struct tpm_chip *chip, int pcr_idx, const u8 *hash)

    extend a PCR value in SHA1 bank.

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

    :param int pcr_idx:
        the PCR to be retrieved

    :param const u8 \*hash:
        the hash value used to extend the PCR value

.. _`tpm_pcr_extend.note`:

Note
----

with TPM 2.0 extends also those banks with a known digest size to the
cryto subsystem in order to prevent malicious use of those PCR banks. In the
future we should dynamically determine digest sizes.

.. _`tpm_pcr_extend.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

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

.. _`tpm_send`:

tpm_send
========

.. c:function:: int tpm_send(struct tpm_chip *chip, void *cmd, size_t buflen)

    send a TPM command

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

    :param void \*cmd:
        a TPM command buffer

    :param size_t buflen:
        the length of the TPM command buffer

.. _`tpm_send.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_get_random`:

tpm_get_random
==============

.. c:function:: int tpm_get_random(struct tpm_chip *chip, u8 *out, size_t max)

    get random bytes from the TPM's RNG

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

    :param u8 \*out:
        destination buffer for the random bytes

    :param size_t max:
        the max number of bytes to write to \ ``out``\ 

.. _`tpm_get_random.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_seal_trusted`:

tpm_seal_trusted
================

.. c:function:: int tpm_seal_trusted(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options)

    seal a trusted key payload

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options

.. _`tpm_seal_trusted.note`:

Note
----

only TPM 2.0 chip are supported. TPM 1.x implementation is located in
the keyring subsystem.

.. _`tpm_seal_trusted.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_unseal_trusted`:

tpm_unseal_trusted
==================

.. c:function:: int tpm_unseal_trusted(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options)

    unseal a trusted key

    :param struct tpm_chip \*chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options

.. _`tpm_unseal_trusted.note`:

Note
----

only TPM 2.0 chip are supported. TPM 1.x implementation is located in
the keyring subsystem.

.. _`tpm_unseal_trusted.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. This file was automatic generated / don't edit.

