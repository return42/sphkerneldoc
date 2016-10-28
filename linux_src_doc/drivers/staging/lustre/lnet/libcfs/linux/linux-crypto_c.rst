.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/libcfs/linux/linux-crypto.c

.. _`cfs_crypto_hash_alloc`:

cfs_crypto_hash_alloc
=====================

.. c:function:: int cfs_crypto_hash_alloc(enum cfs_crypto_hash_alg hash_alg, const struct cfs_crypto_hash_type **type, struct ahash_request **req, unsigned char *key, unsigned int key_len)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

    :param const struct cfs_crypto_hash_type \*\*type:
        *undescribed*

    :param struct ahash_request \*\*req:
        *undescribed*

    :param unsigned char \*key:
        *undescribed*

    :param unsigned int key_len:
        *undescribed*

.. _`cfs_crypto_hash_alloc.description`:

Description
-----------

An internal routine to allocate the hash-specific state in \a hdesc for
use with \ :c:func:`cfs_crypto_hash_digest`\  to compute the hash of a single message,
though possibly in multiple chunks.  The descriptor internal state should
be freed with \ :c:func:`cfs_crypto_hash_final`\ .

\param[in]     hash_alg      hash algorithm id (CFS_HASH_ALG\_\*)
\param[out]    type          pointer to the hash description in hash_types[]
array
\param[in,out] hdesc         hash state descriptor to be initialized
\param[in]     key           initial hash value/state, NULL to use default
value
\param[in]     key_len       length of \a key

\retval                      0 on success
\retval                      negative errno on failure

.. _`cfs_crypto_hash_digest`:

cfs_crypto_hash_digest
======================

.. c:function:: int cfs_crypto_hash_digest(enum cfs_crypto_hash_alg hash_alg, const void *buf, unsigned int buf_len, unsigned char *key, unsigned int key_len, unsigned char *hash, unsigned int *hash_len)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

    :param const void \*buf:
        *undescribed*

    :param unsigned int buf_len:
        *undescribed*

    :param unsigned char \*key:
        *undescribed*

    :param unsigned int key_len:
        *undescribed*

    :param unsigned char \*hash:
        *undescribed*

    :param unsigned int \*hash_len:
        *undescribed*

.. _`cfs_crypto_hash_digest.description`:

Description
-----------

This should be used when computing the hash on a single contiguous buffer.
It combines the hash initialization, computation, and cleanup.

\param[in]     hash_alg      id of hash algorithm (CFS_HASH_ALG\_\*)
\param[in]     buf           data buffer on which to compute hash
\param[in]     buf_len       length of \a buf in bytes
\param[in]     key           initial value/state for algorithm,
if \a key = NULL use default initial value
\param[in]     key_len       length of \a key in bytes
\param[out]    hash          pointer to computed hash value,
if \a hash = NULL then \a hash_len is to digest
size in bytes, retval -ENOSPC
\param[in,out] hash_len      size of \a hash buffer

\retval -EINVAL              \a buf, \a buf_len, \a hash_len,
\a hash_alg invalid
\retval -ENOENT              \a hash_alg is unsupported
\retval -ENOSPC              \a hash is NULL, or \a hash_len less than
digest size
\retval                      0 for success
\retval                      negative errno for other errors from lower
layers.

.. _`cfs_crypto_hash_init`:

cfs_crypto_hash_init
====================

.. c:function:: struct cfs_crypto_hash_desc *cfs_crypto_hash_init(enum cfs_crypto_hash_alg hash_alg, unsigned char *key, unsigned int key_len)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

    :param unsigned char \*key:
        *undescribed*

    :param unsigned int key_len:
        *undescribed*

.. _`cfs_crypto_hash_init.description`:

Description
-----------

This should be used to initialize a hash descriptor for multiple calls
to a single hash function when computing the hash across multiple
separate buffers or pages using cfs_crypto_hash_update{,_page}().

The hash descriptor should be freed with \ :c:func:`cfs_crypto_hash_final`\ .

\param[in] hash_alg  algorithm id (CFS_HASH_ALG\_\*)
\param[in] key       initial value/state for algorithm, if \a key = NULL
use default initial value
\param[in] key_len   length of \a key in bytes

\retval              pointer to descriptor of hash instance
\retval              ERR_PTR(errno) in case of error

.. _`cfs_crypto_hash_update_page`:

cfs_crypto_hash_update_page
===========================

.. c:function:: int cfs_crypto_hash_update_page(struct cfs_crypto_hash_desc *hdesc, struct page *page, unsigned int offset, unsigned int len)

    :param struct cfs_crypto_hash_desc \*hdesc:
        *undescribed*

    :param struct page \*page:
        *undescribed*

    :param unsigned int offset:
        *undescribed*

    :param unsigned int len:
        *undescribed*

.. _`cfs_crypto_hash_update_page.description`:

Description
-----------

\param[in] hdesc     hash state descriptor
\param[in] page      data page on which to compute the hash
\param[in] offset    offset within \a page at which to start hash
\param[in] len       length of data on which to compute hash

\retval              0 for success
\retval              negative errno on failure

.. _`cfs_crypto_hash_update`:

cfs_crypto_hash_update
======================

.. c:function:: int cfs_crypto_hash_update(struct cfs_crypto_hash_desc *hdesc, const void *buf, unsigned int buf_len)

    :param struct cfs_crypto_hash_desc \*hdesc:
        *undescribed*

    :param const void \*buf:
        *undescribed*

    :param unsigned int buf_len:
        *undescribed*

.. _`cfs_crypto_hash_update.description`:

Description
-----------

\param[in] hdesc     hash state descriptor
\param[in] buf       data buffer on which to compute the hash
\param[in] buf_len   length of \buf on which to compute hash

\retval              0 for success
\retval              negative errno on failure

.. _`cfs_crypto_hash_final`:

cfs_crypto_hash_final
=====================

.. c:function:: int cfs_crypto_hash_final(struct cfs_crypto_hash_desc *hdesc, unsigned char *hash, unsigned int *hash_len)

    :param struct cfs_crypto_hash_desc \*hdesc:
        *undescribed*

    :param unsigned char \*hash:
        *undescribed*

    :param unsigned int \*hash_len:
        *undescribed*

.. _`cfs_crypto_hash_final.description`:

Description
-----------

\param[in]     hdesc         hash descriptor
\param[out]    hash          pointer to hash buffer to store hash digest
\param[in,out] hash_len      pointer to hash buffer size, if \a hdesc = NULL
only free \a hdesc instead of computing the hash

\retval      0 for success
\retval      -EOVERFLOW if hash_len is too small for the hash digest
\retval      negative errno for other errors from lower layers

.. _`cfs_crypto_performance_test`:

cfs_crypto_performance_test
===========================

.. c:function:: void cfs_crypto_performance_test(enum cfs_crypto_hash_alg hash_alg)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

.. _`cfs_crypto_performance_test.description`:

Description
-----------

Run a speed test on the given hash algorithm on buffer of the given size.
The speed is stored internally in the cfs_crypto_hash_speeds[] array, and
is available through the \ :c:func:`cfs_crypto_hash_speed`\  function.

\param[in] hash_alg  hash algorithm id (CFS_HASH_ALG\_\*)
\param[in] buf       data buffer on which to compute the hash
\param[in] buf_len   length of \buf on which to compute hash

.. _`cfs_crypto_hash_speed`:

cfs_crypto_hash_speed
=====================

.. c:function:: int cfs_crypto_hash_speed(enum cfs_crypto_hash_alg hash_alg)

    :param enum cfs_crypto_hash_alg hash_alg:
        *undescribed*

.. _`cfs_crypto_hash_speed.description`:

Description
-----------

Return the performance of the specified \a hash_alg that was previously
computed using \ :c:func:`cfs_crypto_performance_test`\ .

\param[in] hash_alg  hash algorithm id (CFS_HASH_ALG\_\*)

\retval              positive speed of the hash function in MB/s
\retval              -ENOENT if \a hash_alg is unsupported
\retval              negative errno if \a hash_alg speed is unavailable

.. _`cfs_crypto_test_hashes`:

cfs_crypto_test_hashes
======================

.. c:function:: int cfs_crypto_test_hashes( void)

    :param  void:
        no arguments

.. _`cfs_crypto_test_hashes.description`:

Description
-----------

Run the \ :c:func:`cfs_crypto_performance_test`\  benchmark for all of the available
hash functions using a 1MB buffer size.  This is a reasonable buffer size
for Lustre RPCs, even if the actual RPC size is larger or smaller.

Since the setup cost and computation speed of various hash algorithms is
a function of the buffer size (and possibly internal contention of offload
engines), this speed only represents an estimate of the actual speed under
actual usage, but is reasonable for comparing available algorithms.

The actual speeds are available via \ :c:func:`cfs_crypto_hash_speed`\  for later
comparison.

\retval      0 on success
\retval      -ENOMEM if no memory is available for test buffer

.. _`cfs_crypto_register`:

cfs_crypto_register
===================

.. c:function:: int cfs_crypto_register( void)

    :param  void:
        no arguments

.. _`cfs_crypto_register.description`:

Description
-----------

\retval      0

.. _`cfs_crypto_unregister`:

cfs_crypto_unregister
=====================

.. c:function:: void cfs_crypto_unregister( void)

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

