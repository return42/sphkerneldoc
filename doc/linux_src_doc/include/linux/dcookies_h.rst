.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dcookies.h

.. _`dcookie_register`:

dcookie_register
================

.. c:function:: struct dcookie_user *dcookie_register( void)

    register a user of dcookies

    :param  void:
        no arguments

.. _`dcookie_register.description`:

Description
-----------

Register as a dcookie user. Returns \ ``NULL``\  on failure.

.. _`dcookie_unregister`:

dcookie_unregister
==================

.. c:function:: void dcookie_unregister(struct dcookie_user *user)

    unregister a user of dcookies

    :param struct dcookie_user \*user:
        *undescribed*

.. _`dcookie_unregister.description`:

Description
-----------

Unregister as a dcookie user. This may invalidate
any dcookie values returned from \ :c:func:`get_dcookie`\ .

.. _`get_dcookie`:

get_dcookie
===========

.. c:function:: int get_dcookie(struct path *path, unsigned long *cookie)

    acquire a dcookie

    :param struct path \*path:
        *undescribed*

    :param unsigned long \*cookie:
        *undescribed*

.. _`get_dcookie.description`:

Description
-----------

Convert the given dentry/vfsmount pair into
a cookie value.

Returns -EINVAL if no living task has registered as a
dcookie user.

Returns 0 on success, with \*cookie filled in

.. This file was automatic generated / don't edit.

