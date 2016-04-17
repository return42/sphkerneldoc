.. -*- coding: utf-8; mode: rst -*-

========
vringh.h
========


.. _`vringh_iov`:

struct vringh_iov
=================

.. c:type:: vringh_iov

    iovec mangler.


.. _`vringh_iov.definition`:

Definition
----------

.. code-block:: c

  struct vringh_iov {
  };


.. _`vringh_iov.members`:

Members
-------




.. _`vringh_iov.description`:

Description
-----------


Mangles iovec in place, and restores it.
Remaining data is iov + i, of used - i elements.



.. _`vringh_kiov`:

struct vringh_kiov
==================

.. c:type:: vringh_kiov

    kvec mangler.


.. _`vringh_kiov.definition`:

Definition
----------

.. code-block:: c

  struct vringh_kiov {
  };


.. _`vringh_kiov.members`:

Members
-------




.. _`vringh_kiov.description`:

Description
-----------


Mangles kvec in place, and restores it.
Remaining data is iov + i, of used - i elements.

