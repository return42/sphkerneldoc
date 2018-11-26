.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm-interface.c

.. _`tpm_transmit`:

tpm_transmit
============

.. c:function:: ssize_t tpm_transmit(struct tpm_chip *chip, struct tpm_space *space, u8 *buf, size_t bufsiz, unsigned int flags)

    Internal kernel interface to transmit TPM commands.

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param space:
        tpm space
    :type space: struct tpm_space \*

    :param buf:
        TPM command buffer
    :type buf: u8 \*

    :param bufsiz:
        length of the TPM command buffer
    :type bufsiz: size_t

    :param flags:
        tpm transmit flags - bitmap
    :type flags: unsigned int

.. _`tpm_transmit.description`:

Description
-----------

A wrapper around tpm_try_transmit that handles TPM2_RC_RETRY
returns from the TPM and retransmits the command after a delay up
to a maximum wait of TPM2_DURATION_LONG.

.. _`tpm_transmit.note`:

Note
----

TPM1 never returns TPM2_RC_RETRY so the retry logic is TPM2
only

.. _`tpm_transmit.return`:

Return
------

the length of the return when the operation is successful.
A negative number for system errors (errno).

.. _`tpm_transmit_cmd`:

tpm_transmit_cmd
================

.. c:function:: ssize_t tpm_transmit_cmd(struct tpm_chip *chip, struct tpm_space *space, void *buf, size_t bufsiz, size_t min_rsp_body_length, unsigned int flags, const char *desc)

    send a tpm command to the device The function extracts tpm out header return code

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param space:
        tpm space
    :type space: struct tpm_space \*

    :param buf:
        TPM command buffer
    :type buf: void \*

    :param bufsiz:
        length of the buffer
    :type bufsiz: size_t

    :param min_rsp_body_length:
        minimum expected length of response body
    :type min_rsp_body_length: size_t

    :param flags:
        tpm transmit flags - bitmap
    :type flags: unsigned int

    :param desc:
        command description used in the error message
    :type desc: const char \*

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

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

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

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

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

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

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

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

    :param pcr_idx:
        the PCR to be retrieved
    :type pcr_idx: int

    :param res_buf:
        the value of the PCR
    :type res_buf: u8 \*

.. _`tpm_pcr_read.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_pcr_extend`:

tpm_pcr_extend
==============

.. c:function:: int tpm_pcr_extend(struct tpm_chip *chip, int pcr_idx, const u8 *hash)

    extend a PCR value in SHA1 bank.

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

    :param pcr_idx:
        the PCR to be retrieved
    :type pcr_idx: int

    :param hash:
        the hash value used to extend the PCR value
    :type hash: const u8 \*

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

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

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

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

.. _`tpm1_auto_startup.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error.

.. _`tpm_send`:

tpm_send
========

.. c:function:: int tpm_send(struct tpm_chip *chip, void *cmd, size_t buflen)

    send a TPM command

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

    :param cmd:
        a TPM command buffer
    :type cmd: void \*

    :param buflen:
        the length of the TPM command buffer
    :type buflen: size_t

.. _`tpm_send.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_get_random`:

tpm_get_random
==============

.. c:function:: int tpm_get_random(struct tpm_chip *chip, u8 *out, size_t max)

    get random bytes from the TPM's RNG

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

    :param out:
        destination buffer for the random bytes
    :type out: u8 \*

    :param max:
        the max number of bytes to write to \ ``out``\ 
    :type max: size_t

.. _`tpm_get_random.return`:

Return
------

same as with \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm_seal_trusted`:

tpm_seal_trusted
================

.. c:function:: int tpm_seal_trusted(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options)

    seal a trusted key payload

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

    :param payload:
        the key data in clear and encrypted form
    :type payload: struct trusted_key_payload \*

    :param options:
        authentication values and other options
    :type options: struct trusted_key_options \*

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

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

    :param payload:
        the key data in clear and encrypted form
    :type payload: struct trusted_key_payload \*

    :param options:
        authentication values and other options
    :type options: struct trusted_key_options \*

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

