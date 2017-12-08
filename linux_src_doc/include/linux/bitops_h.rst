.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bitops.h

.. _`rol64`:

rol64
=====

.. c:function:: __u64 rol64(__u64 word, unsigned int shift)

    rotate a 64-bit value left

    :param __u64 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`ror64`:

ror64
=====

.. c:function:: __u64 ror64(__u64 word, unsigned int shift)

    rotate a 64-bit value right

    :param __u64 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`rol32`:

rol32
=====

.. c:function:: __u32 rol32(__u32 word, unsigned int shift)

    rotate a 32-bit value left

    :param __u32 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`ror32`:

ror32
=====

.. c:function:: __u32 ror32(__u32 word, unsigned int shift)

    rotate a 32-bit value right

    :param __u32 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`rol16`:

rol16
=====

.. c:function:: __u16 rol16(__u16 word, unsigned int shift)

    rotate a 16-bit value left

    :param __u16 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`ror16`:

ror16
=====

.. c:function:: __u16 ror16(__u16 word, unsigned int shift)

    rotate a 16-bit value right

    :param __u16 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`rol8`:

rol8
====

.. c:function:: __u8 rol8(__u8 word, unsigned int shift)

    rotate an 8-bit value left

    :param __u8 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`ror8`:

ror8
====

.. c:function:: __u8 ror8(__u8 word, unsigned int shift)

    rotate an 8-bit value right

    :param __u8 word:
        value to rotate

    :param unsigned int shift:
        bits to roll

.. _`sign_extend32`:

sign_extend32
=============

.. c:function:: __s32 sign_extend32(__u32 value, int index)

    sign extend a 32-bit value using specified bit as sign-bit

    :param __u32 value:
        value to sign extend

    :param int index:
        0 based bit index (0<=index<32) to sign bit

.. _`sign_extend32.description`:

Description
-----------

This is safe to use for 16- and 8-bit types as well.

.. _`sign_extend64`:

sign_extend64
=============

.. c:function:: __s64 sign_extend64(__u64 value, int index)

    sign extend a 64-bit value using specified bit as sign-bit

    :param __u64 value:
        value to sign extend

    :param int index:
        0 based bit index (0<=index<64) to sign bit

.. _`get_count_order_long`:

get_count_order_long
====================

.. c:function:: int get_count_order_long(unsigned long l)

    get order after rounding \ ``l``\  up to power of 2

    :param unsigned long l:
        parameter

.. _`get_count_order_long.description`:

Description
-----------

it is same as \ :c:func:`get_count_order`\  but with long type parameter

.. _`__ffs64`:

__ffs64
=======

.. c:function:: unsigned long __ffs64(u64 word)

    find first set bit in a 64 bit word

    :param u64 word:
        The 64 bit word

.. _`__ffs64.description`:

Description
-----------

On 64 bit arches this is a synomyn for \__ffs
The result is not defined if no bits are set, so check that \ ``word``\ 
is non-zero before calling this.

.. _`assign_bit`:

assign_bit
==========

.. c:function:: void assign_bit(long nr, volatile unsigned long *addr, bool value)

    Assign value to a bit in memory

    :param long nr:
        the bit to set

    :param volatile unsigned long \*addr:
        the address to start counting from

    :param bool value:
        the value to assign

.. _`find_last_bit`:

find_last_bit
=============

.. c:function:: unsigned long find_last_bit(const unsigned long *addr, unsigned long size)

    find the last set bit in a memory region

    :param const unsigned long \*addr:
        The address to start the search at

    :param unsigned long size:
        The number of bits to search

.. _`find_last_bit.description`:

Description
-----------

Returns the bit number of the last set bit, or size.

.. This file was automatic generated / don't edit.

