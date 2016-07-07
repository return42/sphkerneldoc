.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/rsa_helper.c

.. _`rsa_free_key`:

rsa_free_key
============

.. c:function:: void rsa_free_key(struct rsa_key *key)

    frees rsa key allocated by \ :c:func:`rsa_parse_key`\ 

    :param struct rsa_key \*key:
        *undescribed*

.. _`rsa_parse_pub_key`:

rsa_parse_pub_key
=================

.. c:function:: int rsa_parse_pub_key(struct rsa_key *rsa_key, const void *key, unsigned int key_len)

    extracts an rsa public key from BER encoded buffer and stores it in the provided struct rsa_key

    :param struct rsa_key \*rsa_key:
        struct rsa_key key representation

    :param const void \*key:
        key in BER format

    :param unsigned int key_len:
        length of key

.. _`rsa_parse_pub_key.return`:

Return
------

0 on success or error code in case of error

.. _`rsa_parse_priv_key`:

rsa_parse_priv_key
==================

.. c:function:: int rsa_parse_priv_key(struct rsa_key *rsa_key, const void *key, unsigned int key_len)

    extracts an rsa private key from BER encoded buffer and stores it in the provided struct rsa_key

    :param struct rsa_key \*rsa_key:
        struct rsa_key key representation

    :param const void \*key:
        key in BER format

    :param unsigned int key_len:
        length of key

.. _`rsa_parse_priv_key.return`:

Return
------

0 on success or error code in case of error

.. This file was automatic generated / don't edit.

