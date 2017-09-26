.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/vsprintf.c

.. _`simple_strtoull`:

simple_strtoull
===============

.. c:function:: unsigned long long simple_strtoull(const char *cp, char **endp, unsigned int base)

    convert a string to an unsigned long long

    :param const char \*cp:
        The start of the string

    :param char \*\*endp:
        A pointer to the end of the parsed string will be placed here

    :param unsigned int base:
        The number base to use

.. _`simple_strtoull.description`:

Description
-----------

This function is obsolete. Please use kstrtoull instead.

.. _`simple_strtoul`:

simple_strtoul
==============

.. c:function:: unsigned long simple_strtoul(const char *cp, char **endp, unsigned int base)

    convert a string to an unsigned long

    :param const char \*cp:
        The start of the string

    :param char \*\*endp:
        A pointer to the end of the parsed string will be placed here

    :param unsigned int base:
        The number base to use

.. _`simple_strtoul.description`:

Description
-----------

This function is obsolete. Please use kstrtoul instead.

.. _`simple_strtol`:

simple_strtol
=============

.. c:function:: long simple_strtol(const char *cp, char **endp, unsigned int base)

    convert a string to a signed long

    :param const char \*cp:
        The start of the string

    :param char \*\*endp:
        A pointer to the end of the parsed string will be placed here

    :param unsigned int base:
        The number base to use

.. _`simple_strtol.description`:

Description
-----------

This function is obsolete. Please use kstrtol instead.

.. _`simple_strtoll`:

simple_strtoll
==============

.. c:function:: long long simple_strtoll(const char *cp, char **endp, unsigned int base)

    convert a string to a signed long long

    :param const char \*cp:
        The start of the string

    :param char \*\*endp:
        A pointer to the end of the parsed string will be placed here

    :param unsigned int base:
        The number base to use

.. _`simple_strtoll.description`:

Description
-----------

This function is obsolete. Please use kstrtoll instead.

.. _`vsnprintf`:

vsnprintf
=========

.. c:function:: int vsnprintf(char *buf, size_t size, const char *fmt, va_list args)

    Format a string and place it in a buffer

    :param char \*buf:
        The buffer to place the result into

    :param size_t size:
        The size of the buffer, including the trailing null space

    :param const char \*fmt:
        The format string to use

    :param va_list args:
        Arguments for the format string

.. _`vsnprintf.description`:

Description
-----------

This function generally follows C99 vsnprintf, but has some

.. _`vsnprintf.extensions-and-a-few-limitations`:

extensions and a few limitations
--------------------------------


 - ``%n`` is unsupported
 - ``%p*`` is handled by \ :c:func:`pointer`\ 

See \ :c:func:`pointer`\  or Documentation/printk-formats.txt for more
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

    :param char \*buf:
        The buffer to place the result into

    :param size_t size:
        The size of the buffer, including the trailing null space

    :param const char \*fmt:
        The format string to use

    :param va_list args:
        Arguments for the format string

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

    :param char \*buf:
        The buffer to place the result into

    :param size_t size:
        The size of the buffer, including the trailing null space

    :param const char \*fmt:
        The format string to use

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

    :param char \*buf:
        The buffer to place the result into

    :param size_t size:
        The size of the buffer, including the trailing null space

    :param const char \*fmt:
        The format string to use

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

    :param char \*buf:
        The buffer to place the result into

    :param const char \*fmt:
        The format string to use

    :param va_list args:
        Arguments for the format string

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

    :param char \*buf:
        The buffer to place the result into

    :param const char \*fmt:
        The format string to use

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

    :param u32 \*bin_buf:
        The buffer to place args' binary value

    :param size_t size:
        The size of the buffer(by words(32bits), not characters)

    :param const char \*fmt:
        The format string to use

    :param va_list args:
        Arguments for the format string

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

    :param char \*buf:
        The buffer to place the result into

    :param size_t size:
        The size of the buffer, including the trailing null space

    :param const char \*fmt:
        The format string to use

    :param const u32 \*bin_buf:
        Binary arguments for the format string

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

    :param u32 \*bin_buf:
        The buffer to place args' binary value

    :param size_t size:
        The size of the buffer(by words(32bits), not characters)

    :param const char \*fmt:
        The format string to use

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

    :param const char \*buf:
        input buffer

    :param const char \*fmt:
        format of buffer

    :param va_list args:
        arguments

.. _`sscanf`:

sscanf
======

.. c:function:: int sscanf(const char *buf, const char *fmt,  ...)

    Unformat a buffer into a list of arguments

    :param const char \*buf:
        input buffer

    :param const char \*fmt:
        formatting of buffer

    :param ellipsis ellipsis:
        resulting arguments

.. This file was automatic generated / don't edit.

