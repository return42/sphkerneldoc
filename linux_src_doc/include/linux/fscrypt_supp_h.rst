.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fscrypt_supp.h

.. _`fscrypt_match_name`:

fscrypt_match_name
==================

.. c:function:: bool fscrypt_match_name(const struct fscrypt_name *fname, const u8 *de_name, u32 de_name_len)

    test whether the given name matches a directory entry

    :param const struct fscrypt_name \*fname:
        the name being searched for

    :param const u8 \*de_name:
        the name from the directory entry

    :param u32 de_name_len:
        the length of \ ``de_name``\  in bytes

.. _`fscrypt_match_name.description`:

Description
-----------

Normally \ ``fname``\ ->disk_name will be set, and in that case we simply compare
that to the name stored in the directory entry.  The only exception is that
if we don't have the key for an encrypted directory and a filename in it is
very long, then we won't have the full disk_name and we'll instead need to
match against the fscrypt_digested_name.

.. _`fscrypt_match_name.return`:

Return
------

%true if the name matches, otherwise \ ``false``\ .

.. This file was automatic generated / don't edit.

