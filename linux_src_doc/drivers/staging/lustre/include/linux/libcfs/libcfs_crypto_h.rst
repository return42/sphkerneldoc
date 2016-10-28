.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/linux/libcfs/libcfs_crypto.h

.. _`cfs_crypto_hash_type`:

cfs_crypto_hash_type
====================

.. c:function:: const struct cfs_crypto_hash_type *cfs_crypto_hash_type(enum cfs_crypto_hash_alg hash_alg)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

.. _`cfs_crypto_hash_type.description`:

Description
-----------

Hash information includes algorithm name, initial seed, hash size.

\retval      cfs_crypto_hash_type for valid ID (CFS_HASH_ALG\_\*)
\retval      NULL for unknown algorithm identifier

.. _`cfs_crypto_hash_name`:

cfs_crypto_hash_name
====================

.. c:function:: const char *cfs_crypto_hash_name(enum cfs_crypto_hash_alg hash_alg)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

.. _`cfs_crypto_hash_name.description`:

Description
-----------

\param[in]   hash_alg hash alrgorithm id (CFS_HASH_ALG\_\*)

\retval      string name of known hash algorithm
\retval      "unknown" if hash algorithm is unknown

.. _`cfs_crypto_hash_digestsize`:

cfs_crypto_hash_digestsize
==========================

.. c:function:: int cfs_crypto_hash_digestsize(enum cfs_crypto_hash_alg hash_alg)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

.. _`cfs_crypto_hash_digestsize.description`:

Description
-----------

\param[in]   hash_alg hash alrgorithm id (CFS_HASH_ALG\_\*)

\retval      hash algorithm digest size in bytes
\retval      0 if hash algorithm type is unknown

.. _`cfs_crypto_hash_alg`:

cfs_crypto_hash_alg
===================

.. c:function:: unsigned char cfs_crypto_hash_alg(const char *algname)

    :param const char \*algname:
        *undescribed*

.. _`cfs_crypto_hash_alg.description`:

Description
-----------

\retval      hash algorithm ID for valid ID (CFS_HASH_ALG\_\*)
\retval      CFS_HASH_ALG_UNKNOWN for unknown algorithm name

.. This file was automatic generated / don't edit.

