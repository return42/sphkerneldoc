.. -*- coding: utf-8; mode: rst -*-

===========
bad_inode.c
===========

.. _`make_bad_inode`:

make_bad_inode
==============

.. c:function:: void make_bad_inode (struct inode *inode)

    mark an inode bad due to an I/O error

    :param struct inode \*inode:
        Inode to mark bad


.. _`make_bad_inode.description`:

Description
-----------

When an inode cannot be read due to a media or remote network
failure this function makes the inode "bad" and causes I/O operations
on it to fail from this point on.


.. _`is_bad_inode`:

is_bad_inode
============

.. c:function:: bool is_bad_inode (struct inode *inode)

    is an inode errored

    :param struct inode \*inode:
        inode to test


.. _`is_bad_inode.description`:

Description
-----------

Returns true if the inode in question has been marked as bad.


.. _`iget_failed`:

iget_failed
===========

.. c:function:: void iget_failed (struct inode *inode)

    Mark an under-construction inode as dead and release it

    :param struct inode \*inode:
        The inode to discard


.. _`iget_failed.description`:

Description
-----------

Mark an under-construction inode as dead and release it.

