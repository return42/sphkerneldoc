.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qce/sha.h

.. _`qce_sha_reqctx`:

struct qce_sha_reqctx
=====================

.. c:type:: struct qce_sha_reqctx

    holds private ahash objects per request

.. _`qce_sha_reqctx.definition`:

Definition
----------

.. code-block:: c

    struct qce_sha_reqctx {
        u8 buf[QCE_SHA_MAX_BLOCKSIZE];
        u8 tmpbuf[QCE_SHA_MAX_BLOCKSIZE];
        u8 digest[QCE_SHA_MAX_DIGESTSIZE];
        unsigned int buflen;
        unsigned long flags;
        struct scatterlist *src_orig;
        unsigned int nbytes_orig;
        int src_nents;
        __be32 byte_count[2];
        u64 count;
        bool first_blk;
        bool last_blk;
        struct scatterlist sg[2];
        u8 *authkey;
        unsigned int authklen;
        struct scatterlist result_sg;
    }

.. _`qce_sha_reqctx.members`:

Members
-------

buf
    used during update, import and export

tmpbuf
    buffer for internal use

digest
    calculated digest buffer

buflen
    length of the buffer

flags
    operation flags

src_orig
    original request sg list

nbytes_orig
    original request number of bytes

src_nents
    source number of entries

byte_count
    byte count

count
    save count in states during update, import and export

first_blk
    is it the first block

last_blk
    is it the last block

sg
    used to chain sg lists

authkey
    pointer to auth key in sha ctx

authklen
    auth key length

result_sg
    scatterlist used for result buffer

.. This file was automatic generated / don't edit.

