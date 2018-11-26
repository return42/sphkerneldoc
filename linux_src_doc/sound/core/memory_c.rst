.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/memory.c

.. _`copy_to_user_fromio`:

copy_to_user_fromio
===================

.. c:function:: int copy_to_user_fromio(void __user *dst, const volatile void __iomem *src, size_t count)

    copy data from mmio-space to user-space

    :param dst:
        the destination pointer on user-space
    :type dst: void __user \*

    :param src:
        the source pointer on mmio
    :type src: const volatile void __iomem \*

    :param count:
        the data size to copy in bytes
    :type count: size_t

.. _`copy_to_user_fromio.description`:

Description
-----------

Copies the data from mmio-space to user-space.

.. _`copy_to_user_fromio.return`:

Return
------

Zero if successful, or non-zero on failure.

.. _`copy_from_user_toio`:

copy_from_user_toio
===================

.. c:function:: int copy_from_user_toio(volatile void __iomem *dst, const void __user *src, size_t count)

    copy data from user-space to mmio-space

    :param dst:
        the destination pointer on mmio-space
    :type dst: volatile void __iomem \*

    :param src:
        the source pointer on user-space
    :type src: const void __user \*

    :param count:
        the data size to copy in bytes
    :type count: size_t

.. _`copy_from_user_toio.description`:

Description
-----------

Copies the data from user-space to mmio-space.

.. _`copy_from_user_toio.return`:

Return
------

Zero if successful, or non-zero on failure.

.. This file was automatic generated / don't edit.

