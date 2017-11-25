.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/math64.h

.. _`div_u64_rem`:

div_u64_rem
===========

.. c:function:: u64 div_u64_rem(u64 dividend, u32 divisor, u32 *remainder)

    unsigned 64bit divide with 32bit divisor with remainder

    :param u64 dividend:
        unsigned 64bit dividend

    :param u32 divisor:
        unsigned 32bit divisor

    :param u32 \*remainder:
        pointer to unsigned 32bit remainder

.. _`div_u64_rem.return`:

Return
------

sets ``*remainder``, then returns dividend / divisor

This is commonly provided by 32bit archs to provide an optimized 64bit
divide.

.. _`div_s64_rem`:

div_s64_rem
===========

.. c:function:: s64 div_s64_rem(s64 dividend, s32 divisor, s32 *remainder)

    signed 64bit divide with 32bit divisor with remainder

    :param s64 dividend:
        signed 64bit dividend

    :param s32 divisor:
        signed 32bit divisor

    :param s32 \*remainder:
        pointer to signed 32bit remainder

.. _`div_s64_rem.return`:

Return
------

sets ``*remainder``, then returns dividend / divisor

.. _`div64_u64_rem`:

div64_u64_rem
=============

.. c:function:: u64 div64_u64_rem(u64 dividend, u64 divisor, u64 *remainder)

    unsigned 64bit divide with 64bit divisor and remainder

    :param u64 dividend:
        unsigned 64bit dividend

    :param u64 divisor:
        unsigned 64bit divisor

    :param u64 \*remainder:
        pointer to unsigned 64bit remainder

.. _`div64_u64_rem.return`:

Return
------

sets ``*remainder``, then returns dividend / divisor

.. _`div64_u64`:

div64_u64
=========

.. c:function:: u64 div64_u64(u64 dividend, u64 divisor)

    unsigned 64bit divide with 64bit divisor

    :param u64 dividend:
        unsigned 64bit dividend

    :param u64 divisor:
        unsigned 64bit divisor

.. _`div64_u64.return`:

Return
------

dividend / divisor

.. _`div64_s64`:

div64_s64
=========

.. c:function:: s64 div64_s64(s64 dividend, s64 divisor)

    signed 64bit divide with 64bit divisor

    :param s64 dividend:
        signed 64bit dividend

    :param s64 divisor:
        signed 64bit divisor

.. _`div64_s64.return`:

Return
------

dividend / divisor

.. _`div_u64`:

div_u64
=======

.. c:function:: u64 div_u64(u64 dividend, u32 divisor)

    unsigned 64bit divide with 32bit divisor

    :param u64 dividend:
        unsigned 64bit dividend

    :param u32 divisor:
        unsigned 32bit divisor

.. _`div_u64.description`:

Description
-----------

This is the most common 64bit divide and should be used if possible,
as many 32bit archs can optimize this variant better than a full 64bit
divide.

.. _`div_s64`:

div_s64
=======

.. c:function:: s64 div_s64(s64 dividend, s32 divisor)

    signed 64bit divide with 32bit divisor

    :param s64 dividend:
        signed 64bit dividend

    :param s32 divisor:
        signed 32bit divisor

.. This file was automatic generated / don't edit.

