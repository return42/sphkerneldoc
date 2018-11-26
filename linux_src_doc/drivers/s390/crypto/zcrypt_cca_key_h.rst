.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_cca_key.h

.. _`zcrypt_type6_mex_key_en`:

zcrypt_type6_mex_key_en
=======================

.. c:function:: int zcrypt_type6_mex_key_en(struct ica_rsa_modexpo *mex, void *p)

    strips leading zeroes from the b_key. Note that all numerics in the key token are big-endian, while the entries in the key block header are little-endian.

    :param mex:
        pointer to user input data
    :type mex: struct ica_rsa_modexpo \*

    :param p:
        pointer to memory area for the key
    :type p: void \*

.. _`zcrypt_type6_mex_key_en.description`:

Description
-----------

Returns the size of the key area or negative errno value.

.. _`zcrypt_type6_crt_key`:

zcrypt_type6_crt_key
====================

.. c:function:: int zcrypt_type6_crt_key(struct ica_rsa_modexpo_crt *crt, void *p)

    Note that all numerics in the key token are big-endian, while the entries in the key block header are little-endian.

    :param crt:
        *undescribed*
    :type crt: struct ica_rsa_modexpo_crt \*

    :param p:
        pointer to memory area for the key
    :type p: void \*

.. _`zcrypt_type6_crt_key.description`:

Description
-----------

Returns the size of the key area or -EFAULT

.. This file was automatic generated / don't edit.

