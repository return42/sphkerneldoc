.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_bus.c

.. _`snd_hdac_bus_init`:

snd_hdac_bus_init
=================

.. c:function:: int snd_hdac_bus_init(struct hdac_bus *bus, struct device *dev, const struct hdac_bus_ops *ops, const struct hdac_io_ops *io_ops)

    initialize a HD-audio bas bus

    :param bus:
        the pointer to bus object
    :type bus: struct hdac_bus \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param ops:
        bus verb operators
    :type ops: const struct hdac_bus_ops \*

    :param io_ops:
        lowlevel I/O operators
    :type io_ops: const struct hdac_io_ops \*

.. _`snd_hdac_bus_init.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_exit`:

snd_hdac_bus_exit
=================

.. c:function:: void snd_hdac_bus_exit(struct hdac_bus *bus)

    clean up a HD-audio bas bus

    :param bus:
        the pointer to bus object
    :type bus: struct hdac_bus \*

.. _`snd_hdac_bus_exec_verb`:

snd_hdac_bus_exec_verb
======================

.. c:function:: int snd_hdac_bus_exec_verb(struct hdac_bus *bus, unsigned int addr, unsigned int cmd, unsigned int *res)

    execute a HD-audio verb on the given bus

    :param bus:
        bus object
    :type bus: struct hdac_bus \*

    :param addr:
        *undescribed*
    :type addr: unsigned int

    :param cmd:
        HD-audio encoded verb
    :type cmd: unsigned int

    :param res:
        pointer to store the response, NULL if performing asynchronously
    :type res: unsigned int \*

.. _`snd_hdac_bus_exec_verb.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_exec_verb_unlocked`:

snd_hdac_bus_exec_verb_unlocked
===============================

.. c:function:: int snd_hdac_bus_exec_verb_unlocked(struct hdac_bus *bus, unsigned int addr, unsigned int cmd, unsigned int *res)

    unlocked version

    :param bus:
        bus object
    :type bus: struct hdac_bus \*

    :param addr:
        *undescribed*
    :type addr: unsigned int

    :param cmd:
        HD-audio encoded verb
    :type cmd: unsigned int

    :param res:
        pointer to store the response, NULL if performing asynchronously
    :type res: unsigned int \*

.. _`snd_hdac_bus_exec_verb_unlocked.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_queue_event`:

snd_hdac_bus_queue_event
========================

.. c:function:: void snd_hdac_bus_queue_event(struct hdac_bus *bus, u32 res, u32 res_ex)

    add an unsolicited event to queue

    :param bus:
        the BUS
    :type bus: struct hdac_bus \*

    :param res:
        unsolicited event (lower 32bit of RIRB entry)
    :type res: u32

    :param res_ex:
        codec addr and flags (upper 32bit or RIRB entry)
    :type res_ex: u32

.. _`snd_hdac_bus_queue_event.description`:

Description
-----------

Adds the given event to the queue.  The events are processed in
the workqueue asynchronously.  Call this function in the interrupt
hanlder when RIRB receives an unsolicited event.

.. _`snd_hdac_bus_add_device`:

snd_hdac_bus_add_device
=======================

.. c:function:: int snd_hdac_bus_add_device(struct hdac_bus *bus, struct hdac_device *codec)

    Add a codec to bus

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

    :param codec:
        HDA core device to add
    :type codec: struct hdac_device \*

.. _`snd_hdac_bus_add_device.description`:

Description
-----------

Adds the given codec to the list in the bus.  The caddr_tbl array
and codec_powered bits are updated, as well.
Returns zero if success, or a negative error code.

.. _`snd_hdac_bus_remove_device`:

snd_hdac_bus_remove_device
==========================

.. c:function:: void snd_hdac_bus_remove_device(struct hdac_bus *bus, struct hdac_device *codec)

    Remove a codec from bus

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

    :param codec:
        HDA core device to remove
    :type codec: struct hdac_device \*

.. This file was automatic generated / don't edit.

