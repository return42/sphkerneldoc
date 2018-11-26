.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/caampkc.c

.. _`caam_read_rsa_crt`:

caam_read_rsa_crt
=================

.. c:function:: u8 *caam_read_rsa_crt(const u8 *ptr, size_t nbytes, size_t dstlen)

    Used for reading dP, dQ, qInv CRT members. dP, dQ and qInv could decode to less than corresponding p, q length, as the BER-encoding requires that the minimum number of bytes be used to encode the integer. dP, dQ, qInv decoded values have to be zero-padded to appropriate length.

    :param ptr:
        pointer to {dP, dQ, qInv} CRT member
    :type ptr: const u8 \*

    :param nbytes:
        length in bytes of {dP, dQ, qInv} CRT member
    :type nbytes: size_t

    :param dstlen:
        length in bytes of corresponding p or q prime factor
    :type dstlen: size_t

.. _`caam_read_raw_data`:

caam_read_raw_data
==================

.. c:function:: u8 *caam_read_raw_data(const u8 *buf, size_t *nbytes)

    Read a raw byte stream as a positive integer. The function skips buffer's leading zeros, copies the remained data to a buffer allocated in the GFP_DMA \| GFP_KERNEL zone and returns the address of the new buffer.

    :param buf:
        The data to read
    :type buf: const u8 \*

    :param nbytes:
        The amount of data to read
    :type nbytes: size_t \*

.. This file was automatic generated / don't edit.

