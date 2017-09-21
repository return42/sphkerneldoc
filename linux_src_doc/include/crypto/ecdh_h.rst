.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/ecdh.h

.. _`ecdh-helper-functions`:

ECDH Helper Functions
=====================

To use ECDH with the KPP cipher API, the following data structure and
functions should be used.

The ECC curves known to the ECDH implementation are specified in this
header file.

To use ECDH with KPP, the following functions should be used to operate on
an ECDH private key. The packet private key that can be set with
the KPP API function call of crypto_kpp_set_secret.

.. _`ecdh`:

struct ecdh
===========

.. c:type:: struct ecdh

    define an ECDH private key

.. _`ecdh.definition`:

Definition
----------

.. code-block:: c

    struct ecdh {
        unsigned short curve_id;
        char *key;
        unsigned short key_size;
    }

.. _`ecdh.members`:

Members
-------

curve_id
    ECC curve the key is based on.

key
    Private ECDH key

key_size
    Size of the private ECDH key

.. _`crypto_ecdh_key_len`:

crypto_ecdh_key_len
===================

.. c:function:: int crypto_ecdh_key_len(const struct ecdh *params)

    Obtain the size of the private ECDH key

    :param const struct ecdh \*params:
        private ECDH key

.. _`crypto_ecdh_key_len.description`:

Description
-----------

This function returns the packet ECDH key size. A caller can use that
with the provided ECDH private key reference to obtain the required
memory size to hold a packet key.

.. _`crypto_ecdh_key_len.return`:

Return
------

size of the key in bytes

.. _`crypto_ecdh_encode_key`:

crypto_ecdh_encode_key
======================

.. c:function:: int crypto_ecdh_encode_key(char *buf, unsigned int len, const struct ecdh *p)

    encode the private key

    :param char \*buf:
        Buffer allocated by the caller to hold the packet ECDH
        private key. The buffer should be at least crypto_ecdh_key_len
        bytes in size.

    :param unsigned int len:
        Length of the packet private key buffer

    :param const struct ecdh \*p:
        Buffer with the caller-specified private key

.. _`crypto_ecdh_encode_key.description`:

Description
-----------

The ECDH implementations operate on a packet representation of the private
key.

.. _`crypto_ecdh_encode_key.return`:

Return
------

-EINVAL if buffer has insufficient size, 0 on success

.. _`crypto_ecdh_decode_key`:

crypto_ecdh_decode_key
======================

.. c:function:: int crypto_ecdh_decode_key(const char *buf, unsigned int len, struct ecdh *p)

    decode a private key

    :param const char \*buf:
        Buffer holding a packet key that should be decoded

    :param unsigned int len:
        Length of the packet private key buffer

    :param struct ecdh \*p:
        Buffer allocated by the caller that is filled with the
        unpacked ECDH private key.

.. _`crypto_ecdh_decode_key.description`:

Description
-----------

The unpacking obtains the private key by pointing \ ``p``\  to the correct location
in \ ``buf``\ . Thus, both pointers refer to the same memory.

.. _`crypto_ecdh_decode_key.return`:

Return
------

-EINVAL if buffer has insufficient size, 0 on success

.. This file was automatic generated / don't edit.

