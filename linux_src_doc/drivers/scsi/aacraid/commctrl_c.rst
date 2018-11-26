.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/commctrl.c

.. _`aac_debug_preamble`:

AAC_DEBUG_PREAMBLE
==================

.. c:function::  AAC_DEBUG_PREAMBLE()

    send a FIB from userspace

.. _`aac_debug_preamble.description`:

Description
-----------

This routine sends a fib to the adapter on behalf of a user level
program.

.. _`open_getadapter_fib`:

open_getadapter_fib
===================

.. c:function:: int open_getadapter_fib(struct aac_dev *dev, void __user *arg)

    Get the next fib

    :param dev:
        *undescribed*
    :type dev: struct aac_dev \*

    :param arg:
        *undescribed*
    :type arg: void __user \*

.. _`open_getadapter_fib.description`:

Description
-----------

This routine will get the next Fib, if available, from the AdapterFibContext
passed in from the user.

.. _`next_getadapter_fib`:

next_getadapter_fib
===================

.. c:function:: int next_getadapter_fib(struct aac_dev *dev, void __user *arg)

    get the next fib

    :param dev:
        adapter to use
    :type dev: struct aac_dev \*

    :param arg:
        ioctl argument
    :type arg: void __user \*

.. _`next_getadapter_fib.description`:

Description
-----------

This routine will get the next Fib, if available, from the AdapterFibContext
passed in from the user.

.. _`close_getadapter_fib`:

close_getadapter_fib
====================

.. c:function:: int close_getadapter_fib(struct aac_dev *dev, void __user *arg)

    close down user fib context

    :param dev:
        adapter
    :type dev: struct aac_dev \*

    :param arg:
        ioctl arguments
    :type arg: void __user \*

.. _`close_getadapter_fib.description`:

Description
-----------

This routine will close down the fibctx passed in from the user.

.. _`check_revision`:

check_revision
==============

.. c:function:: int check_revision(struct aac_dev *dev, void __user *arg)

    close down user fib context

    :param dev:
        adapter
    :type dev: struct aac_dev \*

    :param arg:
        ioctl arguments
    :type arg: void __user \*

.. _`check_revision.description`:

Description
-----------

This routine returns the driver version.
Under Linux, there have been no version incompatibilities, so this is
simple!

.. This file was automatic generated / don't edit.

