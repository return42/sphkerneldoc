.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm2-cmd.c

.. _`tpm2_pcr_read`:

tpm2_pcr_read
=============

.. c:function:: int tpm2_pcr_read(struct tpm_chip *chip, int pcr_idx, u8 *res_buf)

    read a PCR value

    :param struct tpm_chip \*chip:
        TPM chip to use.

    :param int pcr_idx:
        index of the PCR to read.

    :param u8 \*res_buf:
        buffer to store the resulting hash.

.. _`tpm2_pcr_read.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_pcr_extend`:

tpm2_pcr_extend
===============

.. c:function:: int tpm2_pcr_extend(struct tpm_chip *chip, int pcr_idx, u32 count, struct tpm2_digest *digests)

    extend a PCR value

    :param struct tpm_chip \*chip:
        TPM chip to use.

    :param int pcr_idx:
        index of the PCR.

    :param u32 count:
        number of digests passed.

    :param struct tpm2_digest \*digests:
        list of pcr banks and corresponding digest values to extend.

.. _`tpm2_pcr_extend.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_get_random`:

tpm2_get_random
===============

.. c:function:: int tpm2_get_random(struct tpm_chip *chip, u8 *out, size_t max)

    get random bytes from the TPM RNG

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param u8 \*out:
        destination buffer for the random bytes

    :param size_t max:
        the max number of bytes to write to \ ``out``\ 

.. _`tpm2_get_random.return`:

Return
------

Size of the output buffer, or -EIO on error.

.. _`tpm2_flush_context_cmd`:

tpm2_flush_context_cmd
======================

.. c:function:: void tpm2_flush_context_cmd(struct tpm_chip *chip, u32 handle, unsigned int flags)

    execute a TPM2_FlushContext command

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param u32 handle:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

.. _`tpm2_flush_context_cmd.return`:

Return
------

same as with tpm_transmit_cmd

.. _`tpm2_buf_append_auth`:

tpm2_buf_append_auth
====================

.. c:function:: void tpm2_buf_append_auth(struct tpm_buf *buf, u32 session_handle, const u8 *nonce, u16 nonce_len, u8 attributes, const u8 *hmac, u16 hmac_len)

    append TPMS_AUTH_COMMAND to the buffer.

    :param struct tpm_buf \*buf:
        an allocated tpm_buf instance

    :param u32 session_handle:
        session handle

    :param const u8 \*nonce:
        the session nonce, may be NULL if not used

    :param u16 nonce_len:
        the session nonce length, may be 0 if not used

    :param u8 attributes:
        the session attributes

    :param const u8 \*hmac:
        the session HMAC or password, may be NULL if not used

    :param u16 hmac_len:
        the session HMAC or password length, maybe 0 if not used

.. _`tpm2_seal_trusted`:

tpm2_seal_trusted
=================

.. c:function:: int tpm2_seal_trusted(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options)

    seal the payload of a trusted key

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options

.. _`tpm2_seal_trusted.return`:

Return
------

< 0 on error and 0 on success.

.. _`tpm2_load_cmd`:

tpm2_load_cmd
=============

.. c:function:: int tpm2_load_cmd(struct tpm_chip *chip, struct trusted_key_payload *payload, struct trusted_key_options *options, u32 *blob_handle, unsigned int flags)

    execute a TPM2_Load command

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options

    :param u32 \*blob_handle:
        returned blob handle

    :param unsigned int flags:
        tpm transmit flags

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

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options

    :param u32 blob_handle:
        blob handle

    :param unsigned int flags:
        tpm_transmit_cmd flags

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

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param struct trusted_key_payload \*payload:
        the key data in clear and encrypted form

    :param struct trusted_key_options \*options:
        authentication values and other options

.. _`tpm2_unseal_trusted.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_get_tpm_pt`:

tpm2_get_tpm_pt
===============

.. c:function:: ssize_t tpm2_get_tpm_pt(struct tpm_chip *chip, u32 property_id, u32 *value, const char *desc)

    get value of a TPM_CAP_TPM_PROPERTIES type property

    :param struct tpm_chip \*chip:
        TPM chip to use.

    :param u32 property_id:
        property ID.

    :param u32 \*value:
        output variable.

    :param const char \*desc:
        passed to \ :c:func:`tpm_transmit_cmd`\ 

.. _`tpm2_get_tpm_pt.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_startup`:

tpm2_startup
============

.. c:function:: int tpm2_startup(struct tpm_chip *chip, u16 startup_type)

    send startup command to the TPM chip

    :param struct tpm_chip \*chip:
        TPM chip to use.

    :param u16 startup_type:
        startup type. The value is either
        TPM_SU_CLEAR or TPM_SU_STATE.

.. _`tpm2_startup.return`:

Return
------

Same as with tpm_transmit_cmd.

.. _`tpm2_shutdown`:

tpm2_shutdown
=============

.. c:function:: void tpm2_shutdown(struct tpm_chip *chip, u16 shutdown_type)

    send shutdown command to the TPM chip

    :param struct tpm_chip \*chip:
        TPM chip to use.

    :param u16 shutdown_type:
        shutdown type. The value is either
        TPM_SU_CLEAR or TPM_SU_STATE.

.. _`tpm2_start_selftest`:

tpm2_start_selftest
===================

.. c:function:: int tpm2_start_selftest(struct tpm_chip *chip, bool full)

    start a self test

    :param struct tpm_chip \*chip:
        TPM chip to use

    :param bool full:
        test all commands instead of testing only those that were not
        previously tested.

.. _`tpm2_start_selftest.return`:

Return
------

Same as with tpm_transmit_cmd with exception of RC_TESTING.

.. _`tpm2_do_selftest`:

tpm2_do_selftest
================

.. c:function:: int tpm2_do_selftest(struct tpm_chip *chip)

    run a full self test

    :param struct tpm_chip \*chip:
        TPM chip to use

.. _`tpm2_do_selftest.return`:

Return
------

Same as with tpm_transmit_cmd.

During the self test TPM2 commands return with the error code RC_TESTING.
Waiting is done by issuing PCR read until it executes successfully.

.. _`tpm2_probe`:

tpm2_probe
==========

.. c:function:: int tpm2_probe(struct tpm_chip *chip)

    probe TPM 2.0

    :param struct tpm_chip \*chip:
        TPM chip to use

.. _`tpm2_probe.return`:

Return
------

< 0 error and 0 on success.

Send idempotent TPM 2.0 command and see whether TPM 2.0 chip replied based on
the reply tag.

.. _`tpm2_auto_startup`:

tpm2_auto_startup
=================

.. c:function:: int tpm2_auto_startup(struct tpm_chip *chip)

    Perform the standard automatic TPM initialization sequence

    :param struct tpm_chip \*chip:
        TPM chip to use

.. _`tpm2_auto_startup.description`:

Description
-----------

Returns 0 on success, < 0 in case of fatal error.

.. This file was automatic generated / don't edit.

