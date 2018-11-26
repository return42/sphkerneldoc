.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kernel.h

.. _`repeat_byte`:

REPEAT_BYTE
===========

.. c:function::  REPEAT_BYTE( x)

    repeat the value \ ``x``\  multiple times as an unsigned long value

    :param x:
        value to repeat
    :type x: 

.. _`repeat_byte.note`:

NOTE
----

\ ``x``\  is not checked for > 0xff; larger values produce odd results.

.. _`array_size`:

ARRAY_SIZE
==========

.. c:function::  ARRAY_SIZE( arr)

    get the number of elements in array \ ``arr``\ 

    :param arr:
        array to be sized
    :type arr: 

.. _`round_up`:

round_up
========

.. c:function::  round_up( x,  y)

    round up to next specified power of 2

    :param x:
        the value to round
    :type x: 

    :param y:
        multiple to round up to (must be a power of 2)
    :type y: 

.. _`round_up.description`:

Description
-----------

Rounds \ ``x``\  up to next multiple of \ ``y``\  (which must be a power of 2).
To perform arbitrary rounding up, use \ :c:func:`roundup`\  below.

.. _`round_down`:

round_down
==========

.. c:function::  round_down( x,  y)

    round down to next specified power of 2

    :param x:
        the value to round
    :type x: 

    :param y:
        multiple to round down to (must be a power of 2)
    :type y: 

.. _`round_down.description`:

Description
-----------

Rounds \ ``x``\  down to next multiple of \ ``y``\  (which must be a power of 2).
To perform arbitrary rounding down, use \ :c:func:`rounddown`\  below.

.. _`field_sizeof`:

FIELD_SIZEOF
============

.. c:function::  FIELD_SIZEOF( t,  f)

    get the size of a struct's field

    :param t:
        the target struct
    :type t: 

    :param f:
        the target struct's field
    :type f: 

.. _`field_sizeof.return`:

Return
------

the size of \ ``f``\  in the struct definition without having a
declared instance of \ ``t``\ .

.. _`roundup`:

roundup
=======

.. c:function::  roundup( x,  y)

    round up to the next specified multiple

    :param x:
        the value to up
    :type x: 

    :param y:
        multiple to round up to
    :type y: 

.. _`roundup.description`:

Description
-----------

Rounds \ ``x``\  up to next multiple of \ ``y``\ . If \ ``y``\  will always be a power
of 2, consider using the faster \ :c:func:`round_up`\ .

The `const' here prevents gcc-3.3 from calling __divdi3

.. _`rounddown`:

rounddown
=========

.. c:function::  rounddown( x,  y)

    round down to next specified multiple

    :param x:
        the value to round
    :type x: 

    :param y:
        multiple to round down to
    :type y: 

.. _`rounddown.description`:

Description
-----------

Rounds \ ``x``\  down to next multiple of \ ``y``\ . If \ ``y``\  will always be a power
of 2, consider using the faster \ :c:func:`round_down`\ .

.. _`upper_32_bits`:

upper_32_bits
=============

.. c:function::  upper_32_bits( n)

    return bits 32-63 of a number

    :param n:
        the number we're accessing
    :type n: 

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

    :param n:
        the number we're accessing
    :type n: 

.. _`might_sleep`:

might_sleep
===========

.. c:function::  might_sleep( void)

    annotation for functions that can sleep

    :param void:
        no arguments
    :type void: 

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

    :param x:
        the value.  If it is unsigned type, it is converted to signed type first.
        char is treated as if it was signed (regardless of whether it really is)
        but the macro's return type is preserved as char.
    :type x: 

.. _`abs.return`:

Return
------

an absolute value of x.

.. _`reciprocal_scale`:

reciprocal_scale
================

.. c:function:: u32 reciprocal_scale(u32 val, u32 ep_ro)

    "scale" a value into range [0, ep_ro)

    :param val:
        value
    :type val: u32

    :param ep_ro:
        right open interval endpoint
    :type ep_ro: u32

.. _`reciprocal_scale.description`:

Description
-----------

Perform a "reciprocal multiplication" in order to "scale" a value into
range [0, \ ``ep_ro``\ ), where the upper interval endpoint is right-open.
This is useful, e.g. for accessing a index of an array containing
\ ``ep_ro``\  elements, for example. Think of it as sort of modulus, only that
the result isn't that of modulo. ;) Note that if initial input is a
small value, then result will return 0.

.. _`reciprocal_scale.return`:

Return
------

a result based on \ ``val``\  in interval [0, \ ``ep_ro``\ ).

.. _`kstrtoul`:

kstrtoul
========

.. c:function:: int kstrtoul(const char *s, unsigned int base, unsigned long *res)

    convert a string to an unsigned long

    :param s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign, but not a minus sign.
    :type s: const char \*

    :param base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.
    :type base: unsigned int

    :param res:
        Where to write the result of the conversion on success.
    :type res: unsigned long \*

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

    :param s:
        The start of the string. The string must be null-terminated, and may also
        include a single newline before its terminating null. The first character
        may also be a plus sign or a minus sign.
    :type s: const char \*

    :param base:
        The number base to use. The maximum supported base is 16. If base is
        given as 0, then the base of the string is automatically detected with the
        conventional semantics - If it begins with 0x the number will be parsed as a
        hexadecimal (case insensitive), if it otherwise begins with 0, it will be
        parsed as an octal number. Otherwise it will be parsed as a decimal.
    :type base: unsigned int

    :param res:
        Where to write the result of the conversion on success.
    :type res: long \*

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

    :param fmt:
        the printf format for printing
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`trace_printk.note`:

Note
----

__trace_printk is an internal function for \ :c:func:`trace_printk`\  and
      the \ ``ip``\  is passed in via the \ :c:func:`trace_printk`\  macro.

This function allows a kernel developer to debug fast path sections
that printk is not appropriate for. By scattering in various
printk like tracing in the code, a developer can quickly see
where problems are occurring.

This is intended as a debugging tool for the developer only.
Please refrain from leaving trace_printks scattered around in
your code. (Extra memory is used for special buffers that are
allocated when \ :c:func:`trace_printk`\  is used.)

A little optimization trick is done here. If there's only one
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

    :param str:
        the string to record
    :type str: 

.. _`trace_puts.note`:

Note
----

__trace_bputs is an internal function for trace_puts and
      the \ ``ip``\  is passed in via the trace_puts macro.

This is similar to \ :c:func:`trace_printk`\  but is made for those really fast
paths that a developer wants the least amount of "Heisenbug" effects,
where the processing of the print format is still too much.

This function allows a kernel developer to debug fast path sections
that printk is not appropriate for. By scattering in various
printk like tracing in the code, a developer can quickly see
where problems are occurring.

This is intended as a debugging tool for the developer only.
Please refrain from leaving trace_puts scattered around in
your code. (Extra memory is used for special buffers that are
allocated when \ :c:func:`trace_puts`\  is used.)

.. _`trace_puts.return`:

Return
------

0 if nothing was written, positive # if string was.
 (1 when __trace_bputs is used, strlen(str) when __trace_puts is used)

.. _`min`:

min
===

.. c:function::  min( x,  y)

    return minimum of two values of the same or compatible types

    :param x:
        first value
    :type x: 

    :param y:
        second value
    :type y: 

.. _`max`:

max
===

.. c:function::  max( x,  y)

    return maximum of two values of the same or compatible types

    :param x:
        first value
    :type x: 

    :param y:
        second value
    :type y: 

.. _`min3`:

min3
====

.. c:function::  min3( x,  y,  z)

    return minimum of three values

    :param x:
        first value
    :type x: 

    :param y:
        second value
    :type y: 

    :param z:
        third value
    :type z: 

.. _`max3`:

max3
====

.. c:function::  max3( x,  y,  z)

    return maximum of three values

    :param x:
        first value
    :type x: 

    :param y:
        second value
    :type y: 

    :param z:
        third value
    :type z: 

.. _`min_not_zero`:

min_not_zero
============

.. c:function::  min_not_zero( x,  y)

    return the minimum that is _not_ zero, unless both are zero

    :param x:
        value1
    :type x: 

    :param y:
        value2
    :type y: 

.. _`clamp`:

clamp
=====

.. c:function::  clamp( val,  lo,  hi)

    return a value clamped to a given range with strict typechecking

    :param val:
        current value
    :type val: 

    :param lo:
        lowest allowable value
    :type lo: 

    :param hi:
        highest allowable value
    :type hi: 

.. _`clamp.description`:

Description
-----------

This macro does strict typechecking of \ ``lo``\ /@hi to make sure they are of the
same type as \ ``val``\ .  See the unnecessary pointer comparisons.

.. _`min_t`:

min_t
=====

.. c:function::  min_t( type,  x,  y)

    return minimum of two values, using the specified type

    :param type:
        data type to use
    :type type: 

    :param x:
        first value
    :type x: 

    :param y:
        second value
    :type y: 

.. _`max_t`:

max_t
=====

.. c:function::  max_t( type,  x,  y)

    return maximum of two values, using the specified type

    :param type:
        data type to use
    :type type: 

    :param x:
        first value
    :type x: 

    :param y:
        second value
    :type y: 

.. _`clamp_t`:

clamp_t
=======

.. c:function::  clamp_t( type,  val,  lo,  hi)

    return a value clamped to a given range using a given type

    :param type:
        the type of variable to use
    :type type: 

    :param val:
        current value
    :type val: 

    :param lo:
        minimum allowable value
    :type lo: 

    :param hi:
        maximum allowable value
    :type hi: 

.. _`clamp_t.description`:

Description
-----------

This macro does no typechecking and uses temporary variables of type
\ ``type``\  to make all the comparisons.

.. _`clamp_val`:

clamp_val
=========

.. c:function::  clamp_val( val,  lo,  hi)

    return a value clamped to a given range using val's type

    :param val:
        current value
    :type val: 

    :param lo:
        minimum allowable value
    :type lo: 

    :param hi:
        maximum allowable value
    :type hi: 

.. _`clamp_val.description`:

Description
-----------

This macro does no typechecking and uses temporary variables of whatever
type the input argument \ ``val``\  is.  This is useful when \ ``val``\  is an unsigned
type and \ ``lo``\  and \ ``hi``\  are literals that will otherwise be assigned a signed
integer type.

.. _`swap`:

swap
====

.. c:function::  swap( a,  b)

    swap values of \ ``a``\  and \ ``b``\ 

    :param a:
        first value
    :type a: 

    :param b:
        second value
    :type b: 

.. _`container_of`:

container_of
============

.. c:function::  container_of( ptr,  type,  member)

    cast a member of a structure out to the containing structure

    :param ptr:
        the pointer to the member.
    :type ptr: 

    :param type:
        the type of the container struct this is embedded in.
    :type type: 

    :param member:
        the name of the member within the struct.
    :type member: 

.. _`container_of_safe`:

container_of_safe
=================

.. c:function::  container_of_safe( ptr,  type,  member)

    cast a member of a structure out to the containing structure

    :param ptr:
        the pointer to the member.
    :type ptr: 

    :param type:
        the type of the container struct this is embedded in.
    :type type: 

    :param member:
        the name of the member within the struct.
    :type member: 

.. _`container_of_safe.description`:

Description
-----------

If IS_ERR_OR_NULL(ptr), ptr is returned unchanged.

.. This file was automatic generated / don't edit.

