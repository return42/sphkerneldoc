.. -*- coding: utf-8; mode: rst -*-

==================
csum-wrappers_64.c
==================


.. _`csum_partial_copy_from_user`:

csum_partial_copy_from_user
===========================

.. c:function:: __wsum csum_partial_copy_from_user (const void __user *src, void *dst, int len, __wsum isum, int *errp)

    Copy and checksum from user space.

    :param const void __user \*src:
        source address (user space)

    :param void \*dst:
        destination address

    :param int len:
        number of bytes to be copied.

    :param __wsum isum:
        initial sum that is added into the result (32bit unfolded)

    :param int \*errp:
        set to -EFAULT for an bad source address.



.. _`csum_partial_copy_from_user.description`:

Description
-----------

Returns an 32bit unfolded checksum of the buffer.
src and dst are best aligned to 64bits.



.. _`csum_partial_copy_to_user`:

csum_partial_copy_to_user
=========================

.. c:function:: __wsum csum_partial_copy_to_user (const void *src, void __user *dst, int len, __wsum isum, int *errp)

    Copy and checksum to user space.

    :param const void \*src:
        source address

    :param void __user \*dst:
        destination address (user space)

    :param int len:
        number of bytes to be copied.

    :param __wsum isum:
        initial sum that is added into the result (32bit unfolded)

    :param int \*errp:
        set to -EFAULT for an bad destination address.



.. _`csum_partial_copy_to_user.description`:

Description
-----------

Returns an 32bit unfolded checksum of the buffer.
src and dst are best aligned to 64bits.



.. _`csum_partial_copy_nocheck`:

csum_partial_copy_nocheck
=========================

.. c:function:: __wsum csum_partial_copy_nocheck (const void *src, void *dst, int len, __wsum sum)

    Copy and checksum.

    :param const void \*src:
        source address

    :param void \*dst:
        destination address

    :param int len:
        number of bytes to be copied.

    :param __wsum sum:
        initial sum that is added into the result (32bit unfolded)



.. _`csum_partial_copy_nocheck.description`:

Description
-----------

Returns an 32bit unfolded checksum of the buffer.

