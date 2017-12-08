.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/dh.h

.. _`dh-helper-functions`:

DH Helper Functions
===================

To use DH with the KPP cipher API, the following data structure and
functions should be used.

To use DH with KPP, the following functions should be used to operate on
a DH private key. The packet private key that can be set with
the KPP API function call of crypto_kpp_set_secret.

.. _`dh`:

struct dh
=========

.. c:type:: struct dh

    define a DH private key

.. _`dh.definition`:

Definition
----------

.. code-block:: c

    struct dh {
        void *key;
        void *p;
        void *g;
        unsigned int key_size;
        unsigned int p_size;
        unsigned int g_size;
    }

.. _`dh.members`:

Members
-------

key
    Private DH key

p
    Diffie-Hellman parameter P

g
    Diffie-Hellman generator G

key_size
    Size of the private DH key

p_size
    Size of DH parameter P

g_size
    Size of DH generator G

.. _`crypto_dh_key_len`:

crypto_dh_key_len
=================

.. c:function:: unsigned int crypto_dh_key_len(const struct dh *params)

    Obtain the size of the private DH key

    :param const struct dh \*params:
        private DH key

.. _`crypto_dh_key_len.description`:

Description
-----------

This function returns the packet DH key size. A caller can use that
with the provided DH private key reference to obtain the required
memory size to hold a packet key.

.. _`crypto_dh_key_len.return`:

Return
------

size of the key in bytes

.. _`crypto_dh_encode_key`:

crypto_dh_encode_key
====================

.. c:function:: int crypto_dh_encode_key(char *buf, unsigned int len, const struct dh *params)

    encode the private key

    :param char \*buf:
        Buffer allocated by the caller to hold the packet DH
        private key. The buffer should be at least crypto_dh_key_len
        bytes in size.

    :param unsigned int len:
        Length of the packet private key buffer

    :param const struct dh \*params:
        Buffer with the caller-specified private key

.. _`crypto_dh_encode_key.description`:

Description
-----------

The DH implementations operate on a packet representation of the private
key.

.. _`crypto_dh_encode_key.return`:

Return
------

-EINVAL if buffer has insufficient size, 0 on success

.. _`crypto_dh_decode_key`:

crypto_dh_decode_key
====================

.. c:function:: int crypto_dh_decode_key(const char *buf, unsigned int len, struct dh *params)

    decode a private key

    :param const char \*buf:
        Buffer holding a packet key that should be decoded

    :param unsigned int len:
        Length of the packet private key buffer

    :param struct dh \*params:
        Buffer allocated by the caller that is filled with the
        unpacked DH private key.

.. _`crypto_dh_decode_key.description`:

Description
-----------

The unpacking obtains the private key by pointing \ ``p``\  to the correct location
in \ ``buf``\ . Thus, both pointers refer to the same memory.

.. _`crypto_dh_decode_key.return`:

Return
------

-EINVAL if buffer has insufficient size, 0 on success

.. This file was automatic generated / don't edit.

