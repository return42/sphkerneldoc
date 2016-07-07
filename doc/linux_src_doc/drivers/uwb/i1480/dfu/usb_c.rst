.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/i1480/dfu/usb.c

.. _`i1480_usb_write`:

i1480_usb_write
===============

.. c:function:: int i1480_usb_write(struct i1480 *i1480, u32 memory_address, const void *buffer, size_t size)

    :param struct i1480 \*i1480:
        i1480 instance

    :param u32 memory_address:
        Address where to write the data buffer to.

    :param const void \*buffer:
        Buffer to the data

    :param size_t size:
        Size of the buffer [has to be < 512].

.. _`i1480_usb_write.description`:

Description
-----------

Data buffers to USB cannot be on the stack or in vmalloc'ed areas,
so we copy it to the local i1480 buffer before proceeding. In any
case, we have a max size we can send.

.. _`i1480_usb_read`:

i1480_usb_read
==============

.. c:function:: int i1480_usb_read(struct i1480 *i1480, u32 addr, size_t size)

    :param struct i1480 \*i1480:
        i1480 instance

    :param u32 addr:
        *undescribed*

    :param size_t size:
        Size to read. Smaller than or equal to 512.

.. _`i1480_usb_read.note`:

NOTE
----

if the memory address or block is incorrect, you might get a
stall or a different memory read. Caller has to verify the
memory address and size passed back in the \ ``neh``\  structure.

.. _`i1480_usb_neep_cb`:

i1480_usb_neep_cb
=================

.. c:function:: void i1480_usb_neep_cb(struct urb *urb)

    :param struct urb \*urb:
        *undescribed*

.. _`i1480_usb_neep_cb.description`:

Description
-----------

Just enables the completion read handler.

.. _`i1480_usb_wait_init_done`:

i1480_usb_wait_init_done
========================

.. c:function:: int i1480_usb_wait_init_done(struct i1480 *i1480)

    :param struct i1480 \*i1480:
        *undescribed*

.. _`i1480_usb_wait_init_done.description`:

Description
-----------

MAC FW sends a 0xfd/0101/00 notification to EP1 when done
initializing. Get that notification into i1480->evt_buf; upper layer
will verify it.

Set i1480->evt_result with the result of getting the event or its
size (if successful).

Delivers the data directly to i1480->evt_buf

.. _`i1480_usb_cmd`:

i1480_usb_cmd
=============

.. c:function:: int i1480_usb_cmd(struct i1480 *i1480, const char *cmd_name, size_t cmd_size)

    :param struct i1480 \*i1480:
        i1480 instance

    :param const char \*cmd_name:
        Name of the command (for error messages)

    :param size_t cmd_size:
        Size of the command buffer

.. _`i1480_usb_cmd.description`:

Description
-----------

Arms the NE handle, issues the command to the device and checks the
basics of the reply event.

.. This file was automatic generated / don't edit.

