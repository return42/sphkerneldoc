.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/digsig_asymmetric.c

.. _`integrity_kernel_module_request`:

integrity_kernel_module_request
===============================

.. c:function:: int integrity_kernel_module_request(char *kmod_name)

    prevent crypto-pkcs1pad(rsa,\*) requests

    :param kmod_name:
        kernel module name
    :type kmod_name: char \*

.. _`integrity_kernel_module_request.description`:

Description
-----------

We have situation, when \ :c:func:`public_key_verify_signature`\  in case of RSA
algorithm use alg_name to store internal information in order to
construct an algorithm on the fly, but \ :c:func:`crypto_larval_lookup`\  will try
to use alg_name in order to load kernel module with same name.
Since we don't have any real "crypto-pkcs1pad(rsa,\*)" kernel modules,
we are safe to fail such module request from \ :c:func:`crypto_larval_lookup`\ .

In this way we prevent modprobe execution during digsig verification
and avoid possible deadlock if modprobe and/or it's dependencies
also signed with digsig.

.. This file was automatic generated / don't edit.

