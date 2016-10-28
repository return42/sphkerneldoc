.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/unistr.c

.. _`ntfs_are_names_equal`:

ntfs_are_names_equal
====================

.. c:function:: bool ntfs_are_names_equal(const ntfschar *s1, size_t s1_len, const ntfschar *s2, size_t s2_len, const IGNORE_CASE_BOOL ic, const ntfschar *upcase, const u32 upcase_size)

    compare two Unicode names for equality

    :param const ntfschar \*s1:
        name to compare to \ ``s2``\ 

    :param size_t s1_len:
        length in Unicode characters of \ ``s1``\ 

    :param const ntfschar \*s2:
        name to compare to \ ``s1``\ 

    :param size_t s2_len:
        length in Unicode characters of \ ``s2``\ 

    :param const IGNORE_CASE_BOOL ic:
        ignore case bool

    :param const ntfschar \*upcase:
        upcase table (only if \ ``ic``\  == IGNORE_CASE)

    :param const u32 upcase_size:
        length in Unicode characters of \ ``upcase``\  (if present)

.. _`ntfs_are_names_equal.description`:

Description
-----------

Compare the names \ ``s1``\  and \ ``s2``\  and return 'true' (1) if the names are
identical, or 'false' (0) if they are not identical. If \ ``ic``\  is IGNORE_CASE,
the \ ``upcase``\  table is used to performa a case insensitive comparison.

.. _`ntfs_collate_names`:

ntfs_collate_names
==================

.. c:function:: int ntfs_collate_names(const ntfschar *name1, const u32 name1_len, const ntfschar *name2, const u32 name2_len, const int err_val, const IGNORE_CASE_BOOL ic, const ntfschar *upcase, const u32 upcase_len)

    collate two Unicode names

    :param const ntfschar \*name1:
        first Unicode name to compare

    :param const u32 name1_len:
        *undescribed*

    :param const ntfschar \*name2:
        second Unicode name to compare

    :param const u32 name2_len:
        *undescribed*

    :param const int err_val:
        if \ ``name1``\  contains an invalid character return this value

    :param const IGNORE_CASE_BOOL ic:
        either CASE_SENSITIVE or IGNORE_CASE

    :param const ntfschar \*upcase:
        upcase table (ignored if \ ``ic``\  is CASE_SENSITIVE)

    :param const u32 upcase_len:
        upcase table size (ignored if \ ``ic``\  is CASE_SENSITIVE)

.. _`ntfs_collate_names.ntfs_collate_names-collates-two-unicode-names-and-returns`:

ntfs_collate_names collates two Unicode names and returns
---------------------------------------------------------


-1 if the first name collates before the second one,
0 if the names match,
1 if the second name collates before the first one, or
\ ``err_val``\  if an invalid character is found in \ ``name1``\  during the comparison.

.. _`ntfs_collate_names.the-following-characters-are-considered-invalid`:

The following characters are considered invalid
-----------------------------------------------

'"', '\*', '<', '>' and '?'.

.. _`ntfs_ucsncmp`:

ntfs_ucsncmp
============

.. c:function:: int ntfs_ucsncmp(const ntfschar *s1, const ntfschar *s2, size_t n)

    compare two little endian Unicode strings

    :param const ntfschar \*s1:
        first string

    :param const ntfschar \*s2:
        second string

    :param size_t n:
        maximum unicode characters to compare

.. _`ntfs_ucsncmp.description`:

Description
-----------

Compare the first \ ``n``\  characters of the Unicode strings \ ``s1``\  and \ ``s2``\ ,
The strings in little endian format and appropriate \ :c:func:`le16_to_cpu`\ 
conversion is performed on non-little endian machines.

The function returns an integer less than, equal to, or greater than zero
if \ ``s1``\  (or the first \ ``n``\  Unicode characters thereof) is found, respectively,
to be less than, to match, or be greater than \ ``s2``\ .

.. _`ntfs_ucsncasecmp`:

ntfs_ucsncasecmp
================

.. c:function:: int ntfs_ucsncasecmp(const ntfschar *s1, const ntfschar *s2, size_t n, const ntfschar *upcase, const u32 upcase_size)

    compare two little endian Unicode strings, ignoring case

    :param const ntfschar \*s1:
        first string

    :param const ntfschar \*s2:
        second string

    :param size_t n:
        maximum unicode characters to compare

    :param const ntfschar \*upcase:
        upcase table

    :param const u32 upcase_size:
        upcase table size in Unicode characters

.. _`ntfs_ucsncasecmp.description`:

Description
-----------

Compare the first \ ``n``\  characters of the Unicode strings \ ``s1``\  and \ ``s2``\ ,
ignoring case. The strings in little endian format and appropriate
\ :c:func:`le16_to_cpu`\  conversion is performed on non-little endian machines.

Each character is uppercased using the \ ``upcase``\  table before the comparison.

The function returns an integer less than, equal to, or greater than zero
if \ ``s1``\  (or the first \ ``n``\  Unicode characters thereof) is found, respectively,
to be less than, to match, or be greater than \ ``s2``\ .

.. _`ntfs_nlstoucs`:

ntfs_nlstoucs
=============

.. c:function:: int ntfs_nlstoucs(const ntfs_volume *vol, const char *ins, const int ins_len, ntfschar **outs)

    convert NLS string to little endian Unicode string

    :param const ntfs_volume \*vol:
        ntfs volume which we are working with

    :param const char \*ins:
        input NLS string buffer

    :param const int ins_len:
        length of input string in bytes

    :param ntfschar \*\*outs:
        on return contains the allocated output Unicode string buffer

.. _`ntfs_nlstoucs.description`:

Description
-----------

Convert the input string \ ``ins``\ , which is in whatever format the loaded NLS
map dictates, into a little endian, 2-byte Unicode string.

This function allocates the string and the caller is responsible for
calling kmem_cache_free(ntfs_name_cache, \*\ ``outs``\ ); when finished with it.

On success the function returns the number of Unicode characters written to
the output string \*\ ``outs``\  (>= 0), not counting the terminating Unicode NULL
character. \*\ ``outs``\  is set to the allocated output string buffer.

On error, a negative number corresponding to the error code is returned. In
that case the output string is not allocated. Both \*\ ``outs``\  and \*\ ``outs_len``\ 
are then undefined.

This might look a bit odd due to fast path optimization...

.. _`ntfs_ucstonls`:

ntfs_ucstonls
=============

.. c:function:: int ntfs_ucstonls(const ntfs_volume *vol, const ntfschar *ins, const int ins_len, unsigned char **outs, int outs_len)

    convert little endian Unicode string to NLS string

    :param const ntfs_volume \*vol:
        ntfs volume which we are working with

    :param const ntfschar \*ins:
        input Unicode string buffer

    :param const int ins_len:
        length of input string in Unicode characters

    :param unsigned char \*\*outs:
        on return contains the (allocated) output NLS string buffer

    :param int outs_len:
        length of output string buffer in bytes

.. _`ntfs_ucstonls.description`:

Description
-----------

Convert the input little endian, 2-byte Unicode string \ ``ins``\ , of length
\ ``ins_len``\  into the string format dictated by the loaded NLS.

If \*\ ``outs``\  is NULL, this function allocates the string and the caller is
responsible for calling kfree(\*\ ``outs``\ ); when finished with it. In this case
\ ``outs_len``\  is ignored and can be 0.

On success the function returns the number of bytes written to the output
string \*\ ``outs``\  (>= 0), not counting the terminating NULL byte. If the output
string buffer was allocated, \*\ ``outs``\  is set to it.

On error, a negative number corresponding to the error code is returned. In
that case the output string is not allocated. The contents of \*\ ``outs``\  are
then undefined.

This might look a bit odd due to fast path optimization...

.. This file was automatic generated / don't edit.

