.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/vsoc.c

.. _`vsoc_validate_inode`:

vsoc_validate_inode
===================

.. c:function:: int vsoc_validate_inode(struct inode *inode)

    :param struct inode \*inode:
        *undescribed*

.. _`vsoc_region_from_inode`:

vsoc_region_from_inode
======================

.. c:function:: struct vsoc_device_region *vsoc_region_from_inode(struct inode *inode)

    Dangerous to call before validating the inode/file.

    :param struct inode \*inode:
        *undescribed*

.. _`handle_vsoc_cond_wait`:

handle_vsoc_cond_wait
=====================

.. c:function:: int handle_vsoc_cond_wait(struct file *filp, struct vsoc_cond_wait *arg)

    done in the helper function below.

    :param struct file \*filp:
        *undescribed*

    :param struct vsoc_cond_wait \*arg:
        *undescribed*

.. _`do_vsoc_cond_wait`:

do_vsoc_cond_wait
=================

.. c:function:: int do_vsoc_cond_wait(struct file *filp, struct vsoc_cond_wait __user *untrusted_in)

    happen on all of the return paths of cond_wait.

    :param struct file \*filp:
        *undescribed*

    :param struct vsoc_cond_wait __user \*untrusted_in:
        *undescribed*

.. This file was automatic generated / don't edit.

