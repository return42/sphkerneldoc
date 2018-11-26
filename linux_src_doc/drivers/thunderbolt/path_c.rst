.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/path.c

.. _`tb_path_alloc`:

tb_path_alloc
=============

.. c:function:: struct tb_path *tb_path_alloc(struct tb *tb, int num_hops)

    allocate a thunderbolt path

    :param tb:
        *undescribed*
    :type tb: struct tb \*

    :param num_hops:
        *undescribed*
    :type num_hops: int

.. _`tb_path_alloc.return`:

Return
------

Returns a tb_path on success or NULL on failure.

.. _`tb_path_free`:

tb_path_free
============

.. c:function:: void tb_path_free(struct tb_path *path)

    free a deactivated path

    :param path:
        *undescribed*
    :type path: struct tb_path \*

.. _`tb_path_activate`:

tb_path_activate
================

.. c:function:: int tb_path_activate(struct tb_path *path)

    activate a path

    :param path:
        *undescribed*
    :type path: struct tb_path \*

.. _`tb_path_activate.description`:

Description
-----------

Activate a path starting with the last hop and iterating backwards. The
caller must fill path->hops before calling \ :c:func:`tb_path_activate`\ .

.. _`tb_path_activate.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_path_is_invalid`:

tb_path_is_invalid
==================

.. c:function:: bool tb_path_is_invalid(struct tb_path *path)

    check whether any ports on the path are invalid

    :param path:
        *undescribed*
    :type path: struct tb_path \*

.. _`tb_path_is_invalid.return`:

Return
------

Returns true if the path is invalid, false otherwise.

.. This file was automatic generated / don't edit.

