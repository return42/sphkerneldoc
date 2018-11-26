.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/vsprintf.c

.. _`simple_strtoull`:

simple_strtoull
===============

.. c:function:: unsigned long long simple_strtoull(const char *cp, char **endp, unsigned int base)

    convert a string to an unsigned long long

    :param cp:
        The start of the string
    :type cp: const char \*

    :param endp:
        A pointer to the end of the parsed string will be placed here
    :type endp: char \*\*

    :param base:
        The number base to use
    :type base: unsigned int

.. _`simple_strtoull.description`:

Description
-----------

This function is obsolete. Please use kstrtoull instead.

.. _`simple_strtoul`:

simple_strtoul
==============

.. c:function:: unsigned long simple_strtoul(const char *cp, char **endp, unsigned int base)

    convert a string to an unsigned long

    :param cp:
        The start of the string
    :type cp: const char \*

    :param endp:
        A pointer to the end of the parsed string will be placed here
    :type endp: char \*\*

    :param base:
        The number base to use
    :type base: unsigned int

.. _`simple_strtoul.description`:

Description
-----------

This function is obsolete. Please use kstrtoul instead.

.. _`simple_strtol`:

simple_strtol
=============

.. c:function:: long simple_strtol(const char *cp, char **endp, unsigned int base)

    convert a string to a signed long

    :param cp:
        The start of the string
    :type cp: const char \*

    :param endp:
        A pointer to the end of the parsed string will be placed here
    :type endp: char \*\*

    :param base:
        The number base to use
    :type base: unsigned int

.. _`simple_strtol.description`:

Description
-----------

This function is obsolete. Please use kstrtol instead.

.. _`simple_strtoll`:

simple_strtoll
==============

.. c:function:: long long simple_strtoll(const char *cp, char **endp, unsigned int base)

    convert a string to a signed long long

    :param cp:
        The start of the string
    :type cp: const char \*

    :param endp:
        A pointer to the end of the parsed string will be placed here
    :type endp: char \*\*

    :param base:
        The number base to use
    :type base: unsigned int

.. _`simple_strtoll.description`:

Description
-----------

This function is obsolete. Please use kstrtoll instead.

.. _`vsnprintf`:

vsnprintf
=========

.. c:function:: int vsnprintf(char *buf, size_t size, const char *fmt, va_list args)

    Format a string and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param size:
        The size of the buffer, including the trailing null space
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param args:
        Arguments for the format string
    :type args: va_list

.. _`vsnprintf.description`:

Description
-----------

This function generally follows C99 vsnprintf, but has some

.. _`vsnprintf.extensions-and-a-few-limitations`:

extensions and a few limitations
--------------------------------


 - ``%n`` is unsupported
 - ``%p*`` is handled by \ :c:func:`pointer`\ 

See \ :c:func:`pointer`\  or Documentation/core-api/printk-formats.rst for more
extensive description.

**Please update the documentation in both places when making changes**

The return value is the number of characters which would
be generated for the given input, excluding the trailing
'\0', as per ISO C99. If you want to have the exact
number of characters written into \ ``buf``\  as return value
(not including the trailing '\0'), use \ :c:func:`vscnprintf`\ . If the
return is greater than or equal to \ ``size``\ , the resulting
string is truncated.

If you're not already dealing with a va_list consider using \ :c:func:`snprintf`\ .

.. _`vscnprintf`:

vscnprintf
==========

.. c:function:: int vscnprintf(char *buf, size_t size, const char *fmt, va_list args)

    Format a string and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param size:
        The size of the buffer, including the trailing null space
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param args:
        Arguments for the format string
    :type args: va_list

.. _`vscnprintf.description`:

Description
-----------

The return value is the number of characters which have been written into
the \ ``buf``\  not including the trailing '\0'. If \ ``size``\  is == 0 the function
returns 0.

If you're not already dealing with a va_list consider using \ :c:func:`scnprintf`\ .

See the \ :c:func:`vsnprintf`\  documentation for format string extensions over C99.

.. _`snprintf`:

snprintf
========

.. c:function:: int snprintf(char *buf, size_t size, const char *fmt,  ...)

    Format a string and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param size:
        The size of the buffer, including the trailing null space
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param ellipsis ellipsis:
        Arguments for the format string

.. _`snprintf.description`:

Description
-----------

The return value is the number of characters which would be
generated for the given input, excluding the trailing null,
as per ISO C99.  If the return is greater than or equal to
\ ``size``\ , the resulting string is truncated.

See the \ :c:func:`vsnprintf`\  documentation for format string extensions over C99.

.. _`scnprintf`:

scnprintf
=========

.. c:function:: int scnprintf(char *buf, size_t size, const char *fmt,  ...)

    Format a string and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param size:
        The size of the buffer, including the trailing null space
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param ellipsis ellipsis:
        Arguments for the format string

.. _`scnprintf.description`:

Description
-----------

The return value is the number of characters written into \ ``buf``\  not including
the trailing '\0'. If \ ``size``\  is == 0 the function returns 0.

.. _`vsprintf`:

vsprintf
========

.. c:function:: int vsprintf(char *buf, const char *fmt, va_list args)

    Format a string and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param args:
        Arguments for the format string
    :type args: va_list

.. _`vsprintf.description`:

Description
-----------

The function returns the number of characters written
into \ ``buf``\ . Use \ :c:func:`vsnprintf`\  or \ :c:func:`vscnprintf`\  in order to avoid
buffer overflows.

If you're not already dealing with a va_list consider using \ :c:func:`sprintf`\ .

See the \ :c:func:`vsnprintf`\  documentation for format string extensions over C99.

.. _`sprintf`:

sprintf
=======

.. c:function:: int sprintf(char *buf, const char *fmt,  ...)

    Format a string and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param ellipsis ellipsis:
        Arguments for the format string

.. _`sprintf.description`:

Description
-----------

The function returns the number of characters written
into \ ``buf``\ . Use \ :c:func:`snprintf`\  or \ :c:func:`scnprintf`\  in order to avoid
buffer overflows.

See the \ :c:func:`vsnprintf`\  documentation for format string extensions over C99.

.. _`vbin_printf`:

vbin_printf
===========

.. c:function:: int vbin_printf(u32 *bin_buf, size_t size, const char *fmt, va_list args)

    Parse a format string and place args' binary value in a buffer

    :param bin_buf:
        The buffer to place args' binary value
    :type bin_buf: u32 \*

    :param size:
        The size of the buffer(by words(32bits), not characters)
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param args:
        Arguments for the format string
    :type args: va_list

.. _`vbin_printf.description`:

Description
-----------

The format follows C99 vsnprintf, except \ ``n``\  is ignored, and its argument
is skipped.

The return value is the number of words(32bits) which would be generated for
the given input.

.. _`vbin_printf.note`:

NOTE
----

If the return value is greater than \ ``size``\ , the resulting bin_buf is NOT
valid for \ :c:func:`bstr_printf`\ .

.. _`bstr_printf`:

bstr_printf
===========

.. c:function:: int bstr_printf(char *buf, size_t size, const char *fmt, const u32 *bin_buf)

    Format a string from binary arguments and place it in a buffer

    :param buf:
        The buffer to place the result into
    :type buf: char \*

    :param size:
        The size of the buffer, including the trailing null space
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param bin_buf:
        Binary arguments for the format string
    :type bin_buf: const u32 \*

.. _`bstr_printf.description`:

Description
-----------

This function like C99 vsnprintf, but the difference is that vsnprintf gets
arguments from stack, and bstr_printf gets arguments from \ ``bin_buf``\  which is
a binary buffer that generated by vbin_printf.

The format follows C99 vsnprintf, but has some extensions:
 see vsnprintf comment for details.

The return value is the number of characters which would
be generated for the given input, excluding the trailing
'\0', as per ISO C99. If you want to have the exact
number of characters written into \ ``buf``\  as return value
(not including the trailing '\0'), use \ :c:func:`vscnprintf`\ . If the
return is greater than or equal to \ ``size``\ , the resulting
string is truncated.

.. _`bprintf`:

bprintf
=======

.. c:function:: int bprintf(u32 *bin_buf, size_t size, const char *fmt,  ...)

    Parse a format string and place args' binary value in a buffer

    :param bin_buf:
        The buffer to place args' binary value
    :type bin_buf: u32 \*

    :param size:
        The size of the buffer(by words(32bits), not characters)
    :type size: size_t

    :param fmt:
        The format string to use
    :type fmt: const char \*

    :param ellipsis ellipsis:
        Arguments for the format string

.. _`bprintf.description`:

Description
-----------

The function returns the number of words(u32) written
into \ ``bin_buf``\ .

.. _`vsscanf`:

vsscanf
=======

.. c:function:: int vsscanf(const char *buf, const char *fmt, va_list args)

    Unformat a buffer into a list of arguments

    :param buf:
        input buffer
    :type buf: const char \*

    :param fmt:
        format of buffer
    :type fmt: const char \*

    :param args:
        arguments
    :type args: va_list

.. _`sscanf`:

sscanf
======

.. c:function:: int sscanf(const char *buf, const char *fmt,  ...)

    Unformat a buffer into a list of arguments

    :param buf:
        input buffer
    :type buf: const char \*

    :param fmt:
        formatting of buffer
    :type fmt: const char \*

    :param ellipsis ellipsis:
        resulting arguments

.. This file was automatic generated / don't edit.

