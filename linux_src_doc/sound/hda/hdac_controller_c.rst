.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_controller.c

.. _`snd_hdac_bus_init_cmd_io`:

snd_hdac_bus_init_cmd_io
========================

.. c:function:: void snd_hdac_bus_init_cmd_io(struct hdac_bus *bus)

    set up CORB/RIRB buffers

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_stop_cmd_io`:

snd_hdac_bus_stop_cmd_io
========================

.. c:function:: void snd_hdac_bus_stop_cmd_io(struct hdac_bus *bus)

    clean up CORB/RIRB buffers

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_send_cmd`:

snd_hdac_bus_send_cmd
=====================

.. c:function:: int snd_hdac_bus_send_cmd(struct hdac_bus *bus, unsigned int val)

    send a command verb via CORB

    :param struct hdac_bus \*bus:
        HD-audio core bus

    :param unsigned int val:
        encoded verb value to send

.. _`snd_hdac_bus_send_cmd.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_bus_update_rirb`:

snd_hdac_bus_update_rirb
========================

.. c:function:: void snd_hdac_bus_update_rirb(struct hdac_bus *bus)

    retrieve RIRB entries

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_update_rirb.description`:

Description
-----------

Usually called from interrupt handler.

.. _`snd_hdac_bus_get_response`:

snd_hdac_bus_get_response
=========================

.. c:function:: int snd_hdac_bus_get_response(struct hdac_bus *bus, unsigned int addr, unsigned int *res)

    receive a response via RIRB

    :param struct hdac_bus \*bus:
        HD-audio core bus

    :param unsigned int addr:
        codec address

    :param unsigned int \*res:
        pointer to store the value, NULL when not needed

.. _`snd_hdac_bus_get_response.description`:

Description
-----------

Returns zero if a value is read, or a negative error code.

.. _`snd_hdac_bus_parse_capabilities`:

snd_hdac_bus_parse_capabilities
===============================

.. c:function:: int snd_hdac_bus_parse_capabilities(struct hdac_bus *bus)

    parse capability structure

    :param struct hdac_bus \*bus:
        the pointer to bus object

.. _`snd_hdac_bus_parse_capabilities.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_enter_link_reset`:

snd_hdac_bus_enter_link_reset
=============================

.. c:function:: void snd_hdac_bus_enter_link_reset(struct hdac_bus *bus)

    enter link reset

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_enter_link_reset.description`:

Description
-----------

Enter to the link reset state.

.. _`snd_hdac_bus_exit_link_reset`:

snd_hdac_bus_exit_link_reset
============================

.. c:function:: void snd_hdac_bus_exit_link_reset(struct hdac_bus *bus)

    exit link reset

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_exit_link_reset.description`:

Description
-----------

Exit from the link reset state.

.. _`snd_hdac_bus_init_chip`:

snd_hdac_bus_init_chip
======================

.. c:function:: bool snd_hdac_bus_init_chip(struct hdac_bus *bus, bool full_reset)

    reset and start the controller registers

    :param struct hdac_bus \*bus:
        HD-audio core bus

    :param bool full_reset:
        Do full reset

.. _`snd_hdac_bus_stop_chip`:

snd_hdac_bus_stop_chip
======================

.. c:function:: void snd_hdac_bus_stop_chip(struct hdac_bus *bus)

    disable the whole IRQ and I/Os

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_handle_stream_irq`:

snd_hdac_bus_handle_stream_irq
==============================

.. c:function:: int snd_hdac_bus_handle_stream_irq(struct hdac_bus *bus, unsigned int status, void (*ack)(struct hdac_bus *, struct hdac_stream *))

    interrupt handler for streams

    :param struct hdac_bus \*bus:
        HD-audio core bus

    :param unsigned int status:
        INTSTS register value

    :param void (\*ack)(struct hdac_bus \*, struct hdac_stream \*):
        *undescribed*

.. _`snd_hdac_bus_handle_stream_irq.description`:

Description
-----------

Returns the bits of handled streams, or zero if no stream is handled.

.. _`snd_hdac_bus_alloc_stream_pages`:

snd_hdac_bus_alloc_stream_pages
===============================

.. c:function:: int snd_hdac_bus_alloc_stream_pages(struct hdac_bus *bus)

    allocate BDL and other buffers

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. _`snd_hdac_bus_alloc_stream_pages.description`:

Description
-----------

Call this after assigning the all streams.
Returns zero for success, or a negative error code.

.. _`snd_hdac_bus_free_stream_pages`:

snd_hdac_bus_free_stream_pages
==============================

.. c:function:: void snd_hdac_bus_free_stream_pages(struct hdac_bus *bus)

    release BDL and other buffers

    :param struct hdac_bus \*bus:
        HD-audio core bus

.. This file was automatic generated / don't edit.

