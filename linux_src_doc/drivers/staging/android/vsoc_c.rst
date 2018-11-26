.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/vsoc.c

.. _`vsoc_validate_inode`:

vsoc_validate_inode
===================

.. c:function:: int vsoc_validate_inode(struct inode *inode)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`vsoc_region_from_inode`:

vsoc_region_from_inode
======================

.. c:function:: struct vsoc_device_region *vsoc_region_from_inode(struct inode *inode)

    Dangerous to call before validating the inode/file.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`handle_vsoc_cond_wait`:

handle_vsoc_cond_wait
=====================

.. c:function:: int handle_vsoc_cond_wait(struct file *filp, struct vsoc_cond_wait *arg)

    done in the helper function below.

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param arg:
        *undescribed*
    :type arg: struct vsoc_cond_wait \*

.. _`do_vsoc_cond_wait`:

do_vsoc_cond_wait
=================

.. c:function:: int do_vsoc_cond_wait(struct file *filp, struct vsoc_cond_wait __user *untrusted_in)

    happen on all of the return paths of cond_wait.

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param untrusted_in:
        *undescribed*
    :type untrusted_in: struct vsoc_cond_wait __user \*

.. This file was automatic generated / don't edit.

