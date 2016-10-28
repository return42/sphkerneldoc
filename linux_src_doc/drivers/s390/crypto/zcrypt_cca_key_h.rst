.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_cca_key.h

.. _`zcrypt_type6_mex_key_de`:

zcrypt_type6_mex_key_de
=======================

.. c:function:: int zcrypt_type6_mex_key_de(struct ica_rsa_modexpo *mex, void *p, int big_endian)

    Note that all numerics in the key token are big-endian, while the entries in the key block header are little-endian.

    :param struct ica_rsa_modexpo \*mex:
        pointer to user input data

    :param void \*p:
        pointer to memory area for the key

    :param int big_endian:
        *undescribed*

.. _`zcrypt_type6_mex_key_de.description`:

Description
-----------

Returns the size of the key area or -EFAULT

.. _`zcrypt_type6_mex_key_en`:

zcrypt_type6_mex_key_en
=======================

.. c:function:: int zcrypt_type6_mex_key_en(struct ica_rsa_modexpo *mex, void *p, int big_endian)

    strips leading zeroes from the b_key. Note that all numerics in the key token are big-endian, while the entries in the key block header are little-endian.

    :param struct ica_rsa_modexpo \*mex:
        pointer to user input data

    :param void \*p:
        pointer to memory area for the key

    :param int big_endian:
        *undescribed*

.. _`zcrypt_type6_mex_key_en.description`:

Description
-----------

Returns the size of the key area or -EFAULT

.. _`zcrypt_type6_crt_key`:

zcrypt_type6_crt_key
====================

.. c:function:: int zcrypt_type6_crt_key(struct ica_rsa_modexpo_crt *crt, void *p, int big_endian)

    Note that all numerics in the key token are big-endian, while the entries in the key block header are little-endian.

    :param struct ica_rsa_modexpo_crt \*crt:
        *undescribed*

    :param void \*p:
        pointer to memory area for the key

    :param int big_endian:
        *undescribed*

.. _`zcrypt_type6_crt_key.description`:

Description
-----------

Returns the size of the key area or -EFAULT

.. This file was automatic generated / don't edit.

