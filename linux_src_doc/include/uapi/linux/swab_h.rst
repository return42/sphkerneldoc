.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/swab.h

.. _`__swab16`:

__swab16
========

.. c:function::  __swab16( x)

    return a byteswapped 16-bit value

    :param  x:
        value to byteswap

.. _`__swab32`:

__swab32
========

.. c:function::  __swab32( x)

    return a byteswapped 32-bit value

    :param  x:
        value to byteswap

.. _`__swab64`:

__swab64
========

.. c:function::  __swab64( x)

    return a byteswapped 64-bit value

    :param  x:
        value to byteswap

.. _`__swahw32`:

__swahw32
=========

.. c:function::  __swahw32( x)

    return a word-swapped 32-bit value

    :param  x:
        value to wordswap

.. _`__swahw32.description`:

Description
-----------

__swahw32(0x12340000) is 0x00001234

.. _`__swahb32`:

__swahb32
=========

.. c:function::  __swahb32( x)

    return a high and low byte-swapped 32-bit value

    :param  x:
        value to byteswap

.. _`__swahb32.description`:

Description
-----------

__swahb32(0x12345678) is 0x34127856

.. _`__swab16p`:

__swab16p
=========

.. c:function:: __u16 __swab16p(const __u16 *p)

    return a byteswapped 16-bit value from a pointer

    :param const __u16 \*p:
        pointer to a naturally-aligned 16-bit value

.. _`__swab32p`:

__swab32p
=========

.. c:function:: __u32 __swab32p(const __u32 *p)

    return a byteswapped 32-bit value from a pointer

    :param const __u32 \*p:
        pointer to a naturally-aligned 32-bit value

.. _`__swab64p`:

__swab64p
=========

.. c:function:: __u64 __swab64p(const __u64 *p)

    return a byteswapped 64-bit value from a pointer

    :param const __u64 \*p:
        pointer to a naturally-aligned 64-bit value

.. _`__swahw32p`:

__swahw32p
==========

.. c:function:: __u32 __swahw32p(const __u32 *p)

    return a wordswapped 32-bit value from a pointer

    :param const __u32 \*p:
        pointer to a naturally-aligned 32-bit value

.. _`__swahw32p.description`:

Description
-----------

See \\ :c:func:`__swahw32`\  for details of wordswapping.

.. _`__swahb32p`:

__swahb32p
==========

.. c:function:: __u32 __swahb32p(const __u32 *p)

    return a high and low byteswapped 32-bit value from a pointer

    :param const __u32 \*p:
        pointer to a naturally-aligned 32-bit value

.. _`__swahb32p.description`:

Description
-----------

See \\ :c:func:`__swahb32`\  for details of high/low byteswapping.

.. _`__swab16s`:

__swab16s
=========

.. c:function:: void __swab16s(__u16 *p)

    byteswap a 16-bit value in-place

    :param __u16 \*p:
        pointer to a naturally-aligned 16-bit value

.. _`__swab32s`:

__swab32s
=========

.. c:function:: void __swab32s(__u32 *p)

    byteswap a 32-bit value in-place

    :param __u32 \*p:
        pointer to a naturally-aligned 32-bit value

.. _`__swab64s`:

__swab64s
=========

.. c:function:: void __swab64s(__u64 *p)

    byteswap a 64-bit value in-place

    :param __u64 \*p:
        pointer to a naturally-aligned 64-bit value

.. _`__swahw32s`:

__swahw32s
==========

.. c:function:: void __swahw32s(__u32 *p)

    wordswap a 32-bit value in-place

    :param __u32 \*p:
        pointer to a naturally-aligned 32-bit value

.. _`__swahw32s.description`:

Description
-----------

See \\ :c:func:`__swahw32`\  for details of wordswapping

.. _`__swahb32s`:

__swahb32s
==========

.. c:function:: void __swahb32s(__u32 *p)

    high and low byteswap a 32-bit value in-place

    :param __u32 \*p:
        pointer to a naturally-aligned 32-bit value

.. _`__swahb32s.description`:

Description
-----------

See \\ :c:func:`__swahb32`\  for details of high and low byte swapping

.. This file was automatic generated / don't edit.

