.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/string.c

.. _`strncasecmp`:

strncasecmp
===========

.. c:function:: int strncasecmp(const char *s1, const char *s2, size_t len)

    Case insensitive, length-limited string comparison

    :param s1:
        One string
    :type s1: const char \*

    :param s2:
        The other string
    :type s2: const char \*

    :param len:
        the maximum number of characters to compare
    :type len: size_t

.. _`strcpy`:

strcpy
======

.. c:function:: char *strcpy(char *dest, const char *src)

    Copy a \ ``NUL``\  terminated string

    :param dest:
        Where to copy the string to
    :type dest: char \*

    :param src:
        Where to copy the string from
    :type src: const char \*

.. _`strncpy`:

strncpy
=======

.. c:function:: char *strncpy(char *dest, const char *src, size_t count)

    Copy a length-limited, C-string

    :param dest:
        Where to copy the string to
    :type dest: char \*

    :param src:
        Where to copy the string from
    :type src: const char \*

    :param count:
        The maximum number of bytes to copy
    :type count: size_t

.. _`strncpy.description`:

Description
-----------

The result is not \ ``NUL-terminated``\  if the source exceeds
\ ``count``\  bytes.

In the case where the length of \ ``src``\  is less than  that  of
count, the remainder of \ ``dest``\  will be padded with \ ``NUL``\ .

.. _`strlcpy`:

strlcpy
=======

.. c:function:: size_t strlcpy(char *dest, const char *src, size_t size)

    Copy a C-string into a sized buffer

    :param dest:
        Where to copy the string to
    :type dest: char \*

    :param src:
        Where to copy the string from
    :type src: const char \*

    :param size:
        size of destination buffer
    :type size: size_t

.. _`strlcpy.description`:

Description
-----------

Compatible with ``*BSD``: the result is always a valid
NUL-terminated string that fits in the buffer (unless,
of course, the buffer size is zero). It does not pad
out the result like \ :c:func:`strncpy`\  does.

.. _`strscpy`:

strscpy
=======

.. c:function:: ssize_t strscpy(char *dest, const char *src, size_t count)

    Copy a C-string into a sized buffer

    :param dest:
        Where to copy the string to
    :type dest: char \*

    :param src:
        Where to copy the string from
    :type src: const char \*

    :param count:
        Size of destination buffer
    :type count: size_t

.. _`strscpy.description`:

Description
-----------

Copy the string, or as much of it as fits, into the dest buffer.
The routine returns the number of characters copied (not including
the trailing NUL) or -E2BIG if the destination buffer wasn't big enough.
The behavior is undefined if the string buffers overlap.
The destination buffer is always NUL terminated, unless it's zero-sized.

Preferred to \ :c:func:`strlcpy`\  since the API doesn't require reading memory
from the src string beyond the specified "count" bytes, and since
the return value is easier to error-check than \ :c:func:`strlcpy`\ 's.
In addition, the implementation is robust to the string changing out
from underneath it, unlike the current \ :c:func:`strlcpy`\  implementation.

Preferred to \ :c:func:`strncpy`\  since it always returns a valid string, and
doesn't unnecessarily force the tail of the destination buffer to be
zeroed.  If the zeroing is desired, it's likely cleaner to use \ :c:func:`strscpy`\ 
with an overflow test, then just \ :c:func:`memset`\  the tail of the dest buffer.

.. _`strcat`:

strcat
======

.. c:function:: char *strcat(char *dest, const char *src)

    Append one \ ``NUL-terminated``\  string to another

    :param dest:
        The string to be appended to
    :type dest: char \*

    :param src:
        The string to append to it
    :type src: const char \*

.. _`strncat`:

strncat
=======

.. c:function:: char *strncat(char *dest, const char *src, size_t count)

    Append a length-limited, C-string to another

    :param dest:
        The string to be appended to
    :type dest: char \*

    :param src:
        The string to append to it
    :type src: const char \*

    :param count:
        The maximum numbers of bytes to copy
    :type count: size_t

.. _`strncat.description`:

Description
-----------

Note that in contrast to \ :c:func:`strncpy`\ , \ :c:func:`strncat`\  ensures the result is
terminated.

.. _`strlcat`:

strlcat
=======

.. c:function:: size_t strlcat(char *dest, const char *src, size_t count)

    Append a length-limited, C-string to another

    :param dest:
        The string to be appended to
    :type dest: char \*

    :param src:
        The string to append to it
    :type src: const char \*

    :param count:
        The size of the destination buffer.
    :type count: size_t

.. _`strcmp`:

strcmp
======

.. c:function:: int strcmp(const char *cs, const char *ct)

    Compare two strings

    :param cs:
        One string
    :type cs: const char \*

    :param ct:
        Another string
    :type ct: const char \*

.. _`strncmp`:

strncmp
=======

.. c:function:: int strncmp(const char *cs, const char *ct, size_t count)

    Compare two length-limited strings

    :param cs:
        One string
    :type cs: const char \*

    :param ct:
        Another string
    :type ct: const char \*

    :param count:
        The maximum number of bytes to compare
    :type count: size_t

.. _`strchr`:

strchr
======

.. c:function:: char *strchr(const char *s, int c)

    Find the first occurrence of a character in a string

    :param s:
        The string to be searched
    :type s: const char \*

    :param c:
        The character to search for
    :type c: int

.. _`strchrnul`:

strchrnul
=========

.. c:function:: char *strchrnul(const char *s, int c)

    Find and return a character in a string, or end of string

    :param s:
        The string to be searched
    :type s: const char \*

    :param c:
        The character to search for
    :type c: int

.. _`strchrnul.description`:

Description
-----------

Returns pointer to first occurrence of 'c' in s. If c is not found, then
return a pointer to the null byte at the end of s.

.. _`strrchr`:

strrchr
=======

.. c:function:: char *strrchr(const char *s, int c)

    Find the last occurrence of a character in a string

    :param s:
        The string to be searched
    :type s: const char \*

    :param c:
        The character to search for
    :type c: int

.. _`strnchr`:

strnchr
=======

.. c:function:: char *strnchr(const char *s, size_t count, int c)

    Find a character in a length limited string

    :param s:
        The string to be searched
    :type s: const char \*

    :param count:
        The number of characters to be searched
    :type count: size_t

    :param c:
        The character to search for
    :type c: int

.. _`skip_spaces`:

skip_spaces
===========

.. c:function:: char *skip_spaces(const char *str)

    Removes leading whitespace from \ ``str``\ .

    :param str:
        The string to be stripped.
    :type str: const char \*

.. _`skip_spaces.description`:

Description
-----------

Returns a pointer to the first non-whitespace character in \ ``str``\ .

.. _`strim`:

strim
=====

.. c:function:: char *strim(char *s)

    Removes leading and trailing whitespace from \ ``s``\ .

    :param s:
        The string to be stripped.
    :type s: char \*

.. _`strim.description`:

Description
-----------

Note that the first trailing whitespace is replaced with a \ ``NUL-terminator``\ 
in the given string \ ``s``\ . Returns a pointer to the first non-whitespace
character in \ ``s``\ .

.. _`strlen`:

strlen
======

.. c:function:: size_t strlen(const char *s)

    Find the length of a string

    :param s:
        The string to be sized
    :type s: const char \*

.. _`strnlen`:

strnlen
=======

.. c:function:: size_t strnlen(const char *s, size_t count)

    Find the length of a length-limited string

    :param s:
        The string to be sized
    :type s: const char \*

    :param count:
        The maximum number of bytes to search
    :type count: size_t

.. _`strspn`:

strspn
======

.. c:function:: size_t strspn(const char *s, const char *accept)

    Calculate the length of the initial substring of \ ``s``\  which only contain letters in \ ``accept``\ 

    :param s:
        The string to be searched
    :type s: const char \*

    :param accept:
        The string to search for
    :type accept: const char \*

.. _`strcspn`:

strcspn
=======

.. c:function:: size_t strcspn(const char *s, const char *reject)

    Calculate the length of the initial substring of \ ``s``\  which does not contain letters in \ ``reject``\ 

    :param s:
        The string to be searched
    :type s: const char \*

    :param reject:
        The string to avoid
    :type reject: const char \*

.. _`strpbrk`:

strpbrk
=======

.. c:function:: char *strpbrk(const char *cs, const char *ct)

    Find the first occurrence of a set of characters

    :param cs:
        The string to be searched
    :type cs: const char \*

    :param ct:
        The characters to search for
    :type ct: const char \*

.. _`strsep`:

strsep
======

.. c:function:: char *strsep(char **s, const char *ct)

    Split a string into tokens

    :param s:
        The string to be searched
    :type s: char \*\*

    :param ct:
        The characters to search for
    :type ct: const char \*

.. _`strsep.description`:

Description
-----------

\ :c:func:`strsep`\  updates \ ``s``\  to point after the token, ready for the next call.

It returns empty tokens, too, behaving exactly like the libc function
of that name. In fact, it was stolen from glibc2 and de-fancy-fied.
Same semantics, slimmer shape. ;)

.. _`sysfs_streq`:

sysfs_streq
===========

.. c:function:: bool sysfs_streq(const char *s1, const char *s2)

    return true if strings are equal, modulo trailing newline

    :param s1:
        one string
    :type s1: const char \*

    :param s2:
        another string
    :type s2: const char \*

.. _`sysfs_streq.description`:

Description
-----------

This routine returns true iff two strings are equal, treating both
NUL and newline-then-NUL as equivalent string terminations.  It's
geared for use with sysfs input strings, which generally terminate
with newlines but are compared against values without newlines.

.. _`match_string`:

match_string
============

.. c:function:: int match_string(const char * const *array, size_t n, const char *string)

    matches given string in an array

    :param array:
        array of strings
    :type array: const char \* const \*

    :param n:
        number of strings in the array or -1 for NULL terminated arrays
    :type n: size_t

    :param string:
        string to match with
    :type string: const char \*

.. _`match_string.return`:

Return
------

index of a \ ``string``\  in the \ ``array``\  if matches, or \ ``-EINVAL``\  otherwise.

.. _`__sysfs_match_string`:

__sysfs_match_string
====================

.. c:function:: int __sysfs_match_string(const char * const *array, size_t n, const char *str)

    matches given string in an array

    :param array:
        array of strings
    :type array: const char \* const \*

    :param n:
        number of strings in the array or -1 for NULL terminated arrays
    :type n: size_t

    :param str:
        string to match with
    :type str: const char \*

.. _`__sysfs_match_string.description`:

Description
-----------

Returns index of \ ``str``\  in the \ ``array``\  or -EINVAL, just like \ :c:func:`match_string`\ .
Uses sysfs_streq instead of strcmp for matching.

.. _`memset`:

memset
======

.. c:function:: void *memset(void *s, int c, size_t count)

    Fill a region of memory with the given value

    :param s:
        Pointer to the start of the area.
    :type s: void \*

    :param c:
        The byte to fill the area with
    :type c: int

    :param count:
        The size of the area.
    :type count: size_t

.. _`memset.description`:

Description
-----------

Do not use \ :c:func:`memset`\  to access IO space, use \ :c:func:`memset_io`\  instead.

.. _`memzero_explicit`:

memzero_explicit
================

.. c:function:: void memzero_explicit(void *s, size_t count)

    Fill a region of memory (e.g. sensitive keying data) with 0s.

    :param s:
        Pointer to the start of the area.
    :type s: void \*

    :param count:
        The size of the area.
    :type count: size_t

.. _`memzero_explicit.note`:

Note
----

usually using \ :c:func:`memset`\  is just fine (!), but in cases
where clearing out _local_ data at the end of a scope is
necessary, \ :c:func:`memzero_explicit`\  should be used instead in
order to prevent the compiler from optimising away zeroing.

\ :c:func:`memzero_explicit`\  doesn't need an arch-specific version as
it just invokes the one of \ :c:func:`memset`\  implicitly.

.. _`memset16`:

memset16
========

.. c:function:: void *memset16(uint16_t *s, uint16_t v, size_t count)

    Fill a memory area with a uint16_t

    :param s:
        Pointer to the start of the area.
    :type s: uint16_t \*

    :param v:
        The value to fill the area with
    :type v: uint16_t

    :param count:
        The number of values to store
    :type count: size_t

.. _`memset16.description`:

Description
-----------

Differs from \ :c:func:`memset`\  in that it fills with a uint16_t instead
of a byte.  Remember that \ ``count``\  is the number of uint16_ts to
store, not the number of bytes.

.. _`memset32`:

memset32
========

.. c:function:: void *memset32(uint32_t *s, uint32_t v, size_t count)

    Fill a memory area with a uint32_t

    :param s:
        Pointer to the start of the area.
    :type s: uint32_t \*

    :param v:
        The value to fill the area with
    :type v: uint32_t

    :param count:
        The number of values to store
    :type count: size_t

.. _`memset32.description`:

Description
-----------

Differs from \ :c:func:`memset`\  in that it fills with a uint32_t instead
of a byte.  Remember that \ ``count``\  is the number of uint32_ts to
store, not the number of bytes.

.. _`memset64`:

memset64
========

.. c:function:: void *memset64(uint64_t *s, uint64_t v, size_t count)

    Fill a memory area with a uint64_t

    :param s:
        Pointer to the start of the area.
    :type s: uint64_t \*

    :param v:
        The value to fill the area with
    :type v: uint64_t

    :param count:
        The number of values to store
    :type count: size_t

.. _`memset64.description`:

Description
-----------

Differs from \ :c:func:`memset`\  in that it fills with a uint64_t instead
of a byte.  Remember that \ ``count``\  is the number of uint64_ts to
store, not the number of bytes.

.. _`memcpy`:

memcpy
======

.. c:function:: void *memcpy(void *dest, const void *src, size_t count)

    Copy one area of memory to another

    :param dest:
        Where to copy to
    :type dest: void \*

    :param src:
        Where to copy from
    :type src: const void \*

    :param count:
        The size of the area.
    :type count: size_t

.. _`memcpy.description`:

Description
-----------

You should not use this function to access IO space, use \ :c:func:`memcpy_toio`\ 
or \ :c:func:`memcpy_fromio`\  instead.

.. _`memmove`:

memmove
=======

.. c:function:: void *memmove(void *dest, const void *src, size_t count)

    Copy one area of memory to another

    :param dest:
        Where to copy to
    :type dest: void \*

    :param src:
        Where to copy from
    :type src: const void \*

    :param count:
        The size of the area.
    :type count: size_t

.. _`memmove.description`:

Description
-----------

Unlike \ :c:func:`memcpy`\ , \ :c:func:`memmove`\  copes with overlapping areas.

.. _`memcmp`:

memcmp
======

.. c:function:: __visible int memcmp(const void *cs, const void *ct, size_t count)

    Compare two areas of memory

    :param cs:
        One area of memory
    :type cs: const void \*

    :param ct:
        Another area of memory
    :type ct: const void \*

    :param count:
        The size of the area.
    :type count: size_t

.. _`memscan`:

memscan
=======

.. c:function:: void *memscan(void *addr, int c, size_t size)

    Find a character in an area of memory.

    :param addr:
        The memory area
    :type addr: void \*

    :param c:
        The byte to search for
    :type c: int

    :param size:
        The size of the area.
    :type size: size_t

.. _`memscan.description`:

Description
-----------

returns the address of the first occurrence of \ ``c``\ , or 1 byte past
the area if \ ``c``\  is not found

.. _`strstr`:

strstr
======

.. c:function:: char *strstr(const char *s1, const char *s2)

    Find the first substring in a \ ``NUL``\  terminated string

    :param s1:
        The string to be searched
    :type s1: const char \*

    :param s2:
        The string to search for
    :type s2: const char \*

.. _`strnstr`:

strnstr
=======

.. c:function:: char *strnstr(const char *s1, const char *s2, size_t len)

    Find the first substring in a length-limited string

    :param s1:
        The string to be searched
    :type s1: const char \*

    :param s2:
        The string to search for
    :type s2: const char \*

    :param len:
        the maximum number of characters to search
    :type len: size_t

.. _`memchr`:

memchr
======

.. c:function:: void *memchr(const void *s, int c, size_t n)

    Find a character in an area of memory.

    :param s:
        The memory area
    :type s: const void \*

    :param c:
        The byte to search for
    :type c: int

    :param n:
        The size of the area.
    :type n: size_t

.. _`memchr.description`:

Description
-----------

returns the address of the first occurrence of \ ``c``\ , or \ ``NULL``\ 
if \ ``c``\  is not found

.. _`memchr_inv`:

memchr_inv
==========

.. c:function:: void *memchr_inv(const void *start, int c, size_t bytes)

    Find an unmatching character in an area of memory.

    :param start:
        The memory area
    :type start: const void \*

    :param c:
        Find a character other than c
    :type c: int

    :param bytes:
        The size of the area.
    :type bytes: size_t

.. _`memchr_inv.description`:

Description
-----------

returns the address of the first character other than \ ``c``\ , or \ ``NULL``\ 
if the whole buffer contains just \ ``c``\ .

.. _`strreplace`:

strreplace
==========

.. c:function:: char *strreplace(char *s, char old, char new)

    Replace all occurrences of character in string.

    :param s:
        The string to operate on.
    :type s: char \*

    :param old:
        The character being replaced.
    :type old: char

    :param new:
        The character \ ``old``\  is replaced with.
    :type new: char

.. _`strreplace.description`:

Description
-----------

Returns pointer to the nul byte at the end of \ ``s``\ .

.. This file was automatic generated / don't edit.

