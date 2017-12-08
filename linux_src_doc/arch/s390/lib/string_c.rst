.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/lib/string.c

.. _`strlen`:

strlen
======

.. c:function:: size_t strlen(const char *s)

    Find the length of a string

    :param const char \*s:
        The string to be sized

.. _`strlen.description`:

Description
-----------

returns the length of \ ``s``\ 

.. _`strnlen`:

strnlen
=======

.. c:function:: size_t strnlen(const char *s, size_t n)

    Find the length of a length-limited string

    :param const char \*s:
        The string to be sized

    :param size_t n:
        The maximum number of bytes to search

.. _`strnlen.description`:

Description
-----------

returns the minimum of the length of \ ``s``\  and \ ``n``\ 

.. _`strcpy`:

strcpy
======

.. c:function:: char *strcpy(char *dest, const char *src)

    Copy a \ ``NUL``\  terminated string

    :param char \*dest:
        Where to copy the string to

    :param const char \*src:
        Where to copy the string from

.. _`strcpy.description`:

Description
-----------

returns a pointer to \ ``dest``\ 

.. _`strlcpy`:

strlcpy
=======

.. c:function:: size_t strlcpy(char *dest, const char *src, size_t size)

    Copy a \ ``NUL``\  terminated string into a sized buffer

    :param char \*dest:
        Where to copy the string to

    :param const char \*src:
        Where to copy the string from

    :param size_t size:
        size of destination buffer

.. _`strlcpy.description`:

Description
-----------

Compatible with \*BSD: the result is always a valid
NUL-terminated string that fits in the buffer (unless,
of course, the buffer size is zero). It does not pad
out the result like \ :c:func:`strncpy`\  does.

.. _`strncpy`:

strncpy
=======

.. c:function:: char *strncpy(char *dest, const char *src, size_t n)

    Copy a length-limited, \ ``NUL-terminated``\  string

    :param char \*dest:
        Where to copy the string to

    :param const char \*src:
        Where to copy the string from

    :param size_t n:
        The maximum number of bytes to copy

.. _`strncpy.description`:

Description
-----------

The result is not \ ``NUL-terminated``\  if the source exceeds
\ ``n``\  bytes.

.. _`strcat`:

strcat
======

.. c:function:: char *strcat(char *dest, const char *src)

    Append one \ ``NUL-terminated``\  string to another

    :param char \*dest:
        The string to be appended to

    :param const char \*src:
        The string to append to it

.. _`strcat.description`:

Description
-----------

returns a pointer to \ ``dest``\ 

.. _`strlcat`:

strlcat
=======

.. c:function:: size_t strlcat(char *dest, const char *src, size_t n)

    Append a length-limited, \ ``NUL-terminated``\  string to another

    :param char \*dest:
        The string to be appended to

    :param const char \*src:
        The string to append to it

    :param size_t n:
        The size of the destination buffer.

.. _`strncat`:

strncat
=======

.. c:function:: char *strncat(char *dest, const char *src, size_t n)

    Append a length-limited, \ ``NUL-terminated``\  string to another

    :param char \*dest:
        The string to be appended to

    :param const char \*src:
        The string to append to it

    :param size_t n:
        The maximum numbers of bytes to copy

.. _`strncat.description`:

Description
-----------

returns a pointer to \ ``dest``\ 

Note that in contrast to strncpy, strncat ensures the result is
terminated.

.. _`strcmp`:

strcmp
======

.. c:function:: int strcmp(const char *s1, const char *s2)

    Compare two strings

    :param const char \*s1:
        One string

    :param const char \*s2:
        Another string

.. _`strcmp.description`:

Description
-----------

returns   0 if \ ``s1``\  and \ ``s2``\  are equal,
< 0 if \ ``s1``\  is less than \ ``s2``\ 
> 0 if \ ``s1``\  is greater than \ ``s2``\ 

.. _`strrchr`:

strrchr
=======

.. c:function:: char *strrchr(const char *s, int c)

    Find the last occurrence of a character in a string

    :param const char \*s:
        The string to be searched

    :param int c:
        The character to search for

.. _`strstr`:

strstr
======

.. c:function:: char *strstr(const char *s1, const char *s2)

    Find the first substring in a \ ``NUL``\  terminated string

    :param const char \*s1:
        The string to be searched

    :param const char \*s2:
        The string to search for

.. _`memchr`:

memchr
======

.. c:function:: void *memchr(const void *s, int c, size_t n)

    Find a character in an area of memory.

    :param const void \*s:
        The memory area

    :param int c:
        The byte to search for

    :param size_t n:
        The size of the area.

.. _`memchr.description`:

Description
-----------

returns the address of the first occurrence of \ ``c``\ , or \ ``NULL``\ 
if \ ``c``\  is not found

.. _`memcmp`:

memcmp
======

.. c:function:: int memcmp(const void *s1, const void *s2, size_t n)

    Compare two areas of memory

    :param const void \*s1:
        One area of memory

    :param const void \*s2:
        Another area of memory

    :param size_t n:
        *undescribed*

.. _`memscan`:

memscan
=======

.. c:function:: void *memscan(void *s, int c, size_t n)

    Find a character in an area of memory.

    :param void \*s:
        The memory area

    :param int c:
        The byte to search for

    :param size_t n:
        The size of the area.

.. _`memscan.description`:

Description
-----------

returns the address of the first occurrence of \ ``c``\ , or 1 byte past
the area if \ ``c``\  is not found

.. This file was automatic generated / don't edit.

