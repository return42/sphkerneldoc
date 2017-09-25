.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/vringh.h

.. _`vringh_iov`:

struct vringh_iov
=================

.. c:type:: struct vringh_iov

    iovec mangler.

.. _`vringh_iov.definition`:

Definition
----------

.. code-block:: c

    struct vringh_iov {
        struct iovec *iov;
        size_t consumed;
        unsigned i, used, max_num;
    }

.. _`vringh_iov.members`:

Members
-------

iov
    *undescribed*

consumed
    *undescribed*

i
    *undescribed*

used
    *undescribed*

max_num
    *undescribed*

.. _`vringh_iov.description`:

Description
-----------

Mangles iovec in place, and restores it.
Remaining data is iov + i, of used - i elements.

.. _`vringh_kiov`:

struct vringh_kiov
==================

.. c:type:: struct vringh_kiov

    kvec mangler.

.. _`vringh_kiov.definition`:

Definition
----------

.. code-block:: c

    struct vringh_kiov {
        struct kvec *iov;
        size_t consumed;
        unsigned i, used, max_num;
    }

.. _`vringh_kiov.members`:

Members
-------

iov
    *undescribed*

consumed
    *undescribed*

i
    *undescribed*

used
    *undescribed*

max_num
    *undescribed*

.. _`vringh_kiov.description`:

Description
-----------

Mangles kvec in place, and restores it.
Remaining data is iov + i, of used - i elements.

.. This file was automatic generated / don't edit.

