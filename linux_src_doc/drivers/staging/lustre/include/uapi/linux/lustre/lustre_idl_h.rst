.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/uapi/linux/lustre/lustre_idl.h

.. _`lu_page_shift`:

LU_PAGE_SHIFT
=============

.. c:function::  LU_PAGE_SHIFT()

.. _`lu_page_shift.description`:

Description
-----------

This is the directory page size packed in MDS_READPAGE RPC.
It's different than PAGE_SIZE because the client needs to
access the struct lu_dirpage header packed at the beginning of
the "page" and without this there isn't any way to know find the
lu_dirpage header is if client and server PAGE_SIZE differ.

.. _`lustre_fnv_1a_64_prime`:

LUSTRE_FNV_1A_64_PRIME
======================

.. c:function::  LUSTRE_FNV_1A_64_PRIME()

    1a hash algorithm is as follows: hash = FNV_offset_basis for each octet_of_data to be hashed hash = hash XOR octet_of_data hash = hash × FNV_prime return hash http://en.wikipedia.org/wiki/Fowler–Noll–Vo_hash_function#FNV-1a_hash

.. _`lustre_fnv_1a_64_prime.description`:

Description
-----------

http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-reference-source
FNV_prime is 2^40 + 2^8 + 0xb3 = 0x100000001b3ULL

.. This file was automatic generated / don't edit.

