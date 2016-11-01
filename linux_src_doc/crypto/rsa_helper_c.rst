.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/rsa_helper.c

.. _`rsa_parse_pub_key`:

rsa_parse_pub_key
=================

.. c:function:: int rsa_parse_pub_key(struct rsa_key *rsa_key, const void *key, unsigned int key_len)

    decodes the BER encoded buffer and stores in the provided struct rsa_key, pointers to the raw key as is, so that the caller can copy it or MPI parse it, etc.

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

    decodes the BER encoded buffer and stores in the provided struct rsa_key, pointers to the raw key as is, so that the caller can copy it or MPI parse it, etc.

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

