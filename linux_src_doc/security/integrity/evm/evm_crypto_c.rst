.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/evm/evm_crypto.c

.. _`evm_set_key`:

evm_set_key
===========

.. c:function:: int evm_set_key(void *key, size_t keylen)

    set EVM HMAC key from the kernel

    :param key:
        pointer to a buffer with the key data
    :type key: void \*

    :param keylen:
        *undescribed*
    :type keylen: size_t

.. _`evm_set_key.description`:

Description
-----------

This function allows setting the EVM HMAC key from the kernel
without using the "encrypted" key subsystem keys. It can be used
by the crypto HW kernel module which has its own way of managing
keys.

key length should be between 32 and 128 bytes long

.. This file was automatic generated / don't edit.

