.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/misc.c

.. _`misc_register`:

misc_register
=============

.. c:function:: int misc_register(struct miscdevice *misc)

    register a miscellaneous device

    :param misc:
        device structure
    :type misc: struct miscdevice \*

.. _`misc_register.description`:

Description
-----------

     Register a miscellaneous device with the kernel. If the minor
     number is set to \ ``MISC_DYNAMIC_MINOR``\  a minor number is assigned
     and placed in the minor field of the structure. For other cases
     the minor number requested is used.

     The structure passed is linked into the kernel and may not be
     destroyed until it has been unregistered. By default, an \ :c:func:`open`\ 
     syscall to the device sets file->private_data to point to the
     structure. Drivers don't need open in fops for this.

     A zero is returned on success and a negative errno code for
     failure.

.. _`misc_deregister`:

misc_deregister
===============

.. c:function:: void misc_deregister(struct miscdevice *misc)

    unregister a miscellaneous device

    :param misc:
        device to unregister
    :type misc: struct miscdevice \*

.. _`misc_deregister.description`:

Description
-----------

     Unregister a miscellaneous device that was previously
     successfully registered with \ :c:func:`misc_register`\ .

.. This file was automatic generated / don't edit.

