.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/buffer.c

.. _`hcd_buffer_create`:

hcd_buffer_create
=================

.. c:function:: int hcd_buffer_create(struct usb_hcd *hcd)

    initialize buffer pools

    :param hcd:
        the bus whose buffer pools are to be initialized
    :type hcd: struct usb_hcd \*

.. _`hcd_buffer_create.context`:

Context
-------

!in_interrupt()

.. _`hcd_buffer_create.description`:

Description
-----------

Call this as part of initializing a host controller that uses the dma
memory allocators.  It initializes some pools of dma-coherent memory that
will be shared by all drivers using that controller.

Call \ :c:func:`hcd_buffer_destroy`\  to clean up after using those pools.

.. _`hcd_buffer_create.return`:

Return
------

0 if successful. A negative errno value otherwise.

.. _`hcd_buffer_destroy`:

hcd_buffer_destroy
==================

.. c:function:: void hcd_buffer_destroy(struct usb_hcd *hcd)

    deallocate buffer pools

    :param hcd:
        the bus whose buffer pools are to be destroyed
    :type hcd: struct usb_hcd \*

.. _`hcd_buffer_destroy.context`:

Context
-------

!in_interrupt()

.. _`hcd_buffer_destroy.description`:

Description
-----------

This frees the buffer pools created by \ :c:func:`hcd_buffer_create`\ .

.. This file was automatic generated / don't edit.

