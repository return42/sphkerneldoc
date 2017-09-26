.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kernel.h

.. _`upper_32_bits`:

upper_32_bits
=============

.. c:function::  upper_32_bits( n)

    return bits 32-63 of a number

    :param  n:
        the number we're accessing

.. _`upper_32_bits.description`:

Description
-----------

A basic shift-right of a 64- or 32-bit quantity.  Use this to suppress
the "right shift count >= width of type" warning when that quantity is
32-bits.

.. _`lower_32_bits`:

lower_32_bits
=============

.. c:function::  lower_32_bits( n)

    return bits 0-31 of a number

    :param  n:
        the number we're accessing

.. _`might_sleep`:

might_sleep
===========

.. c:function::  might_sleep( void)

    annotation for functions that can sleep

    :param  void:
        no arguments

.. _`might_sleep.description`:

Description
-----------

this macro will print a stack trace if it is executed in an atomic
context (spinlock, irq-handler, ...).

This is a useful debugging help to be able to catch problems early and not
be bitten later when the calling function happens to sleep when it is not
supposed to.

.. _`abs`:

abs
===

.. c:function::  abs( x)

    return absolute value of an argument

    :param  x:
        the value.  If it is unsigned type, it is converted to signed type first.
        char is treated as if it was signed (regardless of whether it really is)
        but the macro's return type is preserved as char.

.. _`abs.return`:

Return
------

an absolute value of x.

.. _`reciprocal_scale`:

reciprocal_scale
================

.. c:function:: u32 reciprocal_scale(u32 val, u32 ep_ro)

    "scale" a value into range [0, ep_ro)

    :param u32 val:
        value

    :param u32 ep_ro:
        right open interval endpoint

.. _`reciprocal_scale.description`:

Description
-----------

Perform a "reciprocal multiplication" in order to "scale" a value into
range [0, ep_ro), where the upper interval endpoint is right-open.
This is useful, e.g. for accessing a index of an array containing
ep_ro elements, for example. Think of it as sort of modulus, only that
the result isn't that of modulo. ;) Note that if initial input is a
small value, then result will return 0.

.. _`reciprocal_scale.return`:

Return
------

a result based on val in interval [0, ep_ro).

.. _`kstrtoul`:

kstrtoul
========

.. c:function:: int kstrtoul(const char *s, unsigned int base, unsigned long *res)

    convert a string to an unsigned long

    :param const char \*s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign, but not a minus sign.

    :param unsigned int base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.

    :param unsigned long \*res:
        Where to write the result of the conversion on success.

.. _`kstrtoul.description`:

Description
-----------

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code must
be checked.

.. _`kstrtol`:

kstrtol
=======

.. c:function:: int kstrtol(const char *s, unsigned int base, long *res)

    convert a string to a long

    :param const char \*s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign or a minus sign.

    :param unsigned int base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.

    :param long \*res:
        Where to write the result of the conversion on success.

.. _`kstrtol.description`:

Description
-----------

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code must
be checked.

.. _`trace_printk`:

trace_printk
============

.. c:function::  trace_printk( fmt,  ...)

    printf formatting in the ftrace buffer

    :param  fmt:
        the printf format for printing

    :param ellipsis ellipsis:
        variable arguments

.. _`trace_printk.note`:

Note
----

__trace_printk is an internal function for trace_printk and
      the \ ``ip``\  is passed in via the trace_printk macro.

This function allows a kernel developer to debug fast path sections
that printk is not appropriate for. By scattering in various
printk like tracing in the code, a developer can quickly see
where problems are occurring.

This is intended as a debugging tool for the developer only.
Please refrain from leaving trace_printks scattered around in
your code. (Extra memory is used for special buffers that are
allocated when \ :c:func:`trace_printk`\  is used)

A little optization trick is done here. If there's only one
argument, there's no need to scan the string for printf formats.
The \ :c:func:`trace_puts`\  will suffice. But how can we take advantage of
using \ :c:func:`trace_puts`\  when \ :c:func:`trace_printk`\  has only one argument?
By stringifying the args and checking the size we can tell
whether or not there are args. __stringify((__VA_ARGS__)) will
turn into "()\0" with a size of 3 when there are no args, anything
else will be bigger. All we need to do is define a string to this,
and then take its size and compare to 3. If it's bigger, use
\ :c:func:`do_trace_printk`\  otherwise, optimize it to \ :c:func:`trace_puts`\ . Then just
let gcc optimize the rest.

.. _`trace_puts`:

trace_puts
==========

.. c:function::  trace_puts( str)

    write a string into the ftrace buffer

    :param  str:
        the string to record

.. _`trace_puts.note`:

Note
----

__trace_bputs is an internal function for trace_puts and
      the \ ``ip``\  is passed in via the trace_puts macro.

This is similar to \ :c:func:`trace_printk`\  but is made for those really fast
paths that a developer wants the least amount of "Heisenbug" affects,
where the processing of the print format is still too much.

This function allows a kernel developer to debug fast path sections
that printk is not appropriate for. By scattering in various
printk like tracing in the code, a developer can quickly see
where problems are occurring.

This is intended as a debugging tool for the developer only.
Please refrain from leaving trace_puts scattered around in
your code. (Extra memory is used for special buffers that are
allocated when \ :c:func:`trace_puts`\  is used)

.. _`trace_puts.return`:

Return
------

0 if nothing was written, positive # if string was.
 (1 when __trace_bputs is used, strlen(str) when __trace_puts is used)

.. _`min_not_zero`:

min_not_zero
============

.. c:function::  min_not_zero( x,  y)

    return the minimum that is _not_ zero, unless both are zero

    :param  x:
        value1

    :param  y:
        value2

.. _`clamp`:

clamp
=====

.. c:function::  clamp( val,  lo,  hi)

    return a value clamped to a given range with strict typechecking

    :param  val:
        current value

    :param  lo:
        lowest allowable value

    :param  hi:
        highest allowable value

.. _`clamp.description`:

Description
-----------

This macro does strict typechecking of lo/hi to make sure they are of the
same type as val.  See the unnecessary pointer comparisons.

.. _`clamp_t`:

clamp_t
=======

.. c:function::  clamp_t( type,  val,  lo,  hi)

    return a value clamped to a given range using a given type

    :param  type:
        the type of variable to use

    :param  val:
        current value

    :param  lo:
        minimum allowable value

    :param  hi:
        maximum allowable value

.. _`clamp_t.description`:

Description
-----------

This macro does no typechecking and uses temporary variables of type
'type' to make all the comparisons.

.. _`clamp_val`:

clamp_val
=========

.. c:function::  clamp_val( val,  lo,  hi)

    return a value clamped to a given range using val's type

    :param  val:
        current value

    :param  lo:
        minimum allowable value

    :param  hi:
        maximum allowable value

.. _`clamp_val.description`:

Description
-----------

This macro does no typechecking and uses temporary variables of whatever
type the input argument 'val' is.  This is useful when val is an unsigned
type and min and max are literals that will otherwise be assigned a signed
integer type.

.. _`container_of`:

container_of
============

.. c:function::  container_of( ptr,  type,  member)

    cast a member of a structure out to the containing structure

    :param  ptr:
        the pointer to the member.

    :param  type:
        the type of the container struct this is embedded in.

    :param  member:
        the name of the member within the struct.

.. This file was automatic generated / don't edit.

