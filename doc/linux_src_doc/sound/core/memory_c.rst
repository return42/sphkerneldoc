.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/memory.c

.. _`copy_to_user_fromio`:

copy_to_user_fromio
===================

.. c:function:: int copy_to_user_fromio(void __user *dst, const volatile void __iomem *src, size_t count)

    copy data from mmio-space to user-space

    :param void __user \*dst:
        the destination pointer on user-space

    :param const volatile void __iomem \*src:
        the source pointer on mmio

    :param size_t count:
        the data size to copy in bytes

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

    :param volatile void __iomem \*dst:
        the destination pointer on mmio-space

    :param const void __user \*src:
        the source pointer on user-space

    :param size_t count:
        the data size to copy in bytes

.. _`copy_from_user_toio.description`:

Description
-----------

Copies the data from user-space to mmio-space.

.. _`copy_from_user_toio.return`:

Return
------

Zero if successful, or non-zero on failure.

.. This file was automatic generated / don't edit.

