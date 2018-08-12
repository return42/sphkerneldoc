.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fsi/fsi-master.h

.. _`fsi_master_register`:

fsi_master_register
===================

.. c:function:: int fsi_master_register(struct fsi_master *master)

    the \ :c:func:`fsi_master_register`\  and \ :c:func:`fsi_master_unregister`\  functions will take ownership of the master, and ->dev in particular. The registration path performs a \ :c:func:`get_device`\ , which takes the first reference on the device. Similarly, the unregistration path performs a \ :c:func:`put_device`\ , which may well drop the last reference.

    :param struct fsi_master \*master:
        *undescribed*

.. _`fsi_master_register.description`:

Description
-----------

This means that master implementations \*may\* need to hold their own
reference (via \ :c:func:`get_device`\ ) on master->dev. In particular, if the device's
->release callback frees the fsi_master, then fsi_master_unregister will
invoke this free if no other reference is held.

The same applies for the error path of fsi_master_register; if the call
fails, dev->release will have been invoked.

.. This file was automatic generated / don't edit.

