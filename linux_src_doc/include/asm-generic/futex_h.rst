.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/futex.h

.. _`arch_futex_atomic_op_inuser`:

arch_futex_atomic_op_inuser
===========================

.. c:function:: int arch_futex_atomic_op_inuser(int op, u32 oparg, int *oval, u32 __user *uaddr)

    Atomic arithmetic operation with constant argument and comparison of the previous futex value with another constant.

    :param int op:
        *undescribed*

    :param u32 oparg:
        *undescribed*

    :param int \*oval:
        *undescribed*

    :param u32 __user \*uaddr:
        pointer to user space address

.. _`arch_futex_atomic_op_inuser.return`:

Return
------

0 - On success
<0 - On error

.. _`futex_atomic_cmpxchg_inatomic`:

futex_atomic_cmpxchg_inatomic
=============================

.. c:function:: int futex_atomic_cmpxchg_inatomic(u32 *uval, u32 __user *uaddr, u32 oldval, u32 newval)

    Compare and exchange the content of the uaddr with newval if the current value is oldval.

    :param u32 \*uval:
        pointer to store content of \ ``uaddr``\ 

    :param u32 __user \*uaddr:
        pointer to user space address

    :param u32 oldval:
        old value

    :param u32 newval:
        new value to store to \ ``uaddr``\ 

.. _`futex_atomic_cmpxchg_inatomic.return`:

Return
------

0 - On success
<0 - On error

.. This file was automatic generated / don't edit.

