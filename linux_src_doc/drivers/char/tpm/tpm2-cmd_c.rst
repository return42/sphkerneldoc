.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm2-cmd.c

.. _`tpm2_pcr_read`:

tpm2_pcr_read
=============

.. c:function:: int tpm2_pcr_read(struct tpm_chip *chip, int pcr_idx, u8 *res_buf)

    read a PCR value

    :param chip:
        TPM chip to use.
    :type chip: struct tpm_chip \*

    :param pcr_idx:
        index of the PCR to read.
    :type pcr_idx: int

    :param res_buf:
        buffer to store the resulting hash.
    :type res_buf: u8 \*

.. _`tpm2_pcr_read.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_pcr_extend`:

tpm2_pcr_extend
===============

.. c:function:: int tpm2_pcr_extend(struct tpm_chip *chip, int pcr_idx, u32 count, struct tpm2_digest *digests)

    extend a PCR value

    :param chip:
        TPM chip to use.
    :type chip: struct tpm_chip \*

    :param pcr_idx:
        index of the PCR.
    :type pcr_idx: int

    :param count:
        number of digests passed.
    :type count: u32

    :param digests:
        list of pcr banks and corresponding digest values to extend.
    :type digests: struct tpm2_digest \*

.. _`tpm2_pcr_extend.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_get_random`:

tpm2_get_random
===============

.. c:function:: int tpm2_get_random(struct tpm_chip *chip, u8 *dest, size_t max)

    get random bytes from the TPM RNG

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance
    :type chip: struct tpm_chip \*

    :param dest:
        destination buffer
    :type dest: u8 \*

    :param max:
        the max number of random bytes to pull
    :type max: size_t

.. _`tpm2_get_random.return`:

Return
------

size of the buffer on success,
-errno otherwise

.. _`tpm2_flush_context_cmd`:

tpm2_flush_context_cmd
======================

.. c:function:: void tpm2_flush_context_cmd(struct tpm_chip *chip, u32 handle, unsigned int flags)

    execute a TPM2_FlushContext command

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param handle:
        *undescribed*
    :type handle: u32

    :param flags:
        *undescribed*
    :type flags: unsigned int

.. _`tpm2_flush_context_cmd.return`:

Return
------

same as with tpm_transmit_cmd

.. _`tpm2_buf_append_auth`:

tpm2_buf_append_auth
====================

.. c:function:: void tpm2_buf_append_auth(struct tpm_buf *buf, u32 session_handle, const u8 *nonce, u16 nonce_len, u8 attributes, const u8 *hmac, u16 hmac_len)

    append TPMS_AUTH_COMMAND to the buffer.

    :param buf:
        an allocated tpm_buf instance
    :type buf: struct tpm_buf \*

    :param session_handle:
        session handle
    :type session_handle: u32

    :param nonce:
        the session nonce, may be NULL if not used
    :type nonce: const u8 \*

    :param nonce_len:
        the session nonce length, may be 0 if not used
    :type nonce_len: u16

    :param attributes:
        the session attributes
    :type attributes: u8

    :param hmac:
        the session HMAC or password, may be NULL if not used
    :type hmac: const u8 \*

    :param hmac_len:
        the session HMAC or password length, maybe 0 if not used
    :type hmac_len: u16

.. _`tpm2_seal_trusted`:

tpm2_seal_trusted
=================

.. c:function:: int tpm2_seal_trusted(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options)

    seal the payload of a trusted key

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param payload:
        the key data in clear and encrypted form
    :type payload: struct trusted_key_payload \*

    :param options:
        authentication values and other options
    :type options: struct trusted_key_options \*

.. _`tpm2_seal_trusted.return`:

Return
------

< 0 on error and 0 on success.

.. _`tpm2_load_cmd`:

tpm2_load_cmd
=============

.. c:function:: int tpm2_load_cmd(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options, u32 *blob_handle, unsigned int flags)

    execute a TPM2_Load command

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param payload:
        the key data in clear and encrypted form
    :type payload: struct trusted_key_payload \*

    :param options:
        authentication values and other options
    :type options: struct trusted_key_options \*

    :param blob_handle:
        returned blob handle
    :type blob_handle: u32 \*

    :param flags:
        tpm transmit flags
    :type flags: unsigned int

.. _`tpm2_load_cmd.return`:

Return
------

0 on success.
-E2BIG on wrong payload size.
-EPERM on tpm error status.
< 0 error from tpm_transmit_cmd.

.. _`tpm2_unseal_cmd`:

tpm2_unseal_cmd
===============

.. c:function:: int tpm2_unseal_cmd(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options, u32 blob_handle, unsigned int flags)

    execute a TPM2_Unload command

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param payload:
        the key data in clear and encrypted form
    :type payload: struct trusted_key_payload \*

    :param options:
        authentication values and other options
    :type options: struct trusted_key_options \*

    :param blob_handle:
        blob handle
    :type blob_handle: u32

    :param flags:
        tpm_transmit_cmd flags
    :type flags: unsigned int

.. _`tpm2_unseal_cmd.return`:

Return
------

0 on success
-EPERM on tpm error status
< 0 error from tpm_transmit_cmd

.. _`tpm2_unseal_trusted`:

tpm2_unseal_trusted
===================

.. c:function:: int tpm2_unseal_trusted(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options)

    unseal the payload of a trusted key

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

    :param payload:
        the key data in clear and encrypted form
    :type payload: struct trusted_key_payload \*

    :param options:
        authentication values and other options
    :type options: struct trusted_key_options \*

.. _`tpm2_unseal_trusted.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_get_tpm_pt`:

tpm2_get_tpm_pt
===============

.. c:function:: ssize_t tpm2_get_tpm_pt(struct tpm_chip *chip, u32 property_id, u32 *value, const char *desc)

    get value of a TPM_CAP_TPM_PROPERTIES type property

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance
    :type chip: struct tpm_chip \*

    :param property_id:
        property ID.
    :type property_id: u32

    :param value:
        output variable.
    :type value: u32 \*

    :param desc:
        passed to \ :c:func:`tpm_transmit_cmd`\ 
    :type desc: const char \*

.. _`tpm2_get_tpm_pt.return`:

Return
------

0 on success,
-errno or a TPM return code otherwise

.. _`tpm2_shutdown`:

tpm2_shutdown
=============

.. c:function:: void tpm2_shutdown(struct tpm_chip *chip, u16 shutdown_type)

    send a TPM shutdown command

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance
    :type chip: struct tpm_chip \*

    :param shutdown_type:
        TPM_SU_CLEAR or TPM_SU_STATE.
    :type shutdown_type: u16

.. _`tpm2_shutdown.description`:

Description
-----------

Sends a TPM shutdown command. The shutdown command is used in call
sites where the system is going down. If it fails, there is not much
that can be done except print an error message.

.. _`tpm2_do_selftest`:

tpm2_do_selftest
================

.. c:function:: int tpm2_do_selftest(struct tpm_chip *chip)

    ensure that all self tests have passed

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

.. _`tpm2_do_selftest.return`:

Return
------

Same as with tpm_transmit_cmd.

The TPM can either run all self tests synchronously and then return
RC_SUCCESS once all tests were successful. Or it can choose to run the tests
asynchronously and return RC_TESTING immediately while the self tests still
execute in the background. This function handles both cases and waits until
all tests have completed.

.. _`tpm2_probe`:

tpm2_probe
==========

.. c:function:: int tpm2_probe(struct tpm_chip *chip)

    probe for the TPM 2.0 protocol

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance
    :type chip: struct tpm_chip \*

.. _`tpm2_probe.description`:

Description
-----------

Send an idempotent TPM 2.0 command and see whether there is TPM2 chip in the
other end based on the response tag. The flag TPM_CHIP_FLAG_TPM2 is set by
this function if this is the case.

.. _`tpm2_probe.return`:

Return
------

0 on success,
-errno otherwise

.. _`tpm2_auto_startup`:

tpm2_auto_startup
=================

.. c:function:: int tpm2_auto_startup(struct tpm_chip *chip)

    Perform the standard automatic TPM initialization sequence

    :param chip:
        TPM chip to use
    :type chip: struct tpm_chip \*

.. _`tpm2_auto_startup.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error.

.. This file was automatic generated / don't edit.

