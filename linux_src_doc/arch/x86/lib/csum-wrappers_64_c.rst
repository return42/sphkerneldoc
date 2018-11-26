.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/csum-wrappers_64.c

.. _`csum_partial_copy_from_user`:

csum_partial_copy_from_user
===========================

.. c:function:: __wsum csum_partial_copy_from_user(const void __user *src, void *dst, int len, __wsum isum, int *errp)

    Copy and checksum from user space.

    :param src:
        source address (user space)
    :type src: const void __user \*

    :param dst:
        destination address
    :type dst: void \*

    :param len:
        number of bytes to be copied.
    :type len: int

    :param isum:
        initial sum that is added into the result (32bit unfolded)
    :type isum: __wsum

    :param errp:
        set to -EFAULT for an bad source address.
    :type errp: int \*

.. _`csum_partial_copy_from_user.description`:

Description
-----------

Returns an 32bit unfolded checksum of the buffer.
src and dst are best aligned to 64bits.

.. _`csum_partial_copy_to_user`:

csum_partial_copy_to_user
=========================

.. c:function:: __wsum csum_partial_copy_to_user(const void *src, void __user *dst, int len, __wsum isum, int *errp)

    Copy and checksum to user space.

    :param src:
        source address
    :type src: const void \*

    :param dst:
        destination address (user space)
    :type dst: void __user \*

    :param len:
        number of bytes to be copied.
    :type len: int

    :param isum:
        initial sum that is added into the result (32bit unfolded)
    :type isum: __wsum

    :param errp:
        set to -EFAULT for an bad destination address.
    :type errp: int \*

.. _`csum_partial_copy_to_user.description`:

Description
-----------

Returns an 32bit unfolded checksum of the buffer.
src and dst are best aligned to 64bits.

.. _`csum_partial_copy_nocheck`:

csum_partial_copy_nocheck
=========================

.. c:function:: __wsum csum_partial_copy_nocheck(const void *src, void *dst, int len, __wsum sum)

    Copy and checksum.

    :param src:
        source address
    :type src: const void \*

    :param dst:
        destination address
    :type dst: void \*

    :param len:
        number of bytes to be copied.
    :type len: int

    :param sum:
        initial sum that is added into the result (32bit unfolded)
    :type sum: __wsum

.. _`csum_partial_copy_nocheck.description`:

Description
-----------

Returns an 32bit unfolded checksum of the buffer.

.. This file was automatic generated / don't edit.

