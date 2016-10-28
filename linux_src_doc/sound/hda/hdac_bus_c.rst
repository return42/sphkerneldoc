.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_bus.c

.. _`snd_hdac_bus_init`:

snd_hdac_bus_init
=================

.. c:function:: int snd_hdac_bus_init(struct hdac_bus *bus, struct device *dev, const struct hdac_bus_ops *ops, const struct hdac_io_ops *io_ops)

    initialize a HD-audio bas bus

    :param struct hdac_bus \*bus:
        the pointer to bus object

    :param struct device \*dev:
        *undescribed*

    :param const struct hdac_bus_ops \*ops:
        bus verb operators

    :param const struct hdac_io_ops \*io_ops:
        lowlevel I/O operators

.. _`snd_hdac_bus_init.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_exit`:

snd_hdac_bus_exit
=================

.. c:function:: void snd_hdac_bus_exit(struct hdac_bus *bus)

    clean up a HD-audio bas bus

    :param struct hdac_bus \*bus:
        the pointer to bus object

.. _`snd_hdac_bus_exec_verb`:

snd_hdac_bus_exec_verb
======================

.. c:function:: int snd_hdac_bus_exec_verb(struct hdac_bus *bus, unsigned int addr, unsigned int cmd, unsigned int *res)

    execute a HD-audio verb on the given bus

    :param struct hdac_bus \*bus:
        bus object

    :param unsigned int addr:
        *undescribed*

    :param unsigned int cmd:
        HD-audio encoded verb

    :param unsigned int \*res:
        pointer to store the response, NULL if performing asynchronously

.. _`snd_hdac_bus_exec_verb.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_exec_verb_unlocked`:

snd_hdac_bus_exec_verb_unlocked
===============================

.. c:function:: int snd_hdac_bus_exec_verb_unlocked(struct hdac_bus *bus, unsigned int addr, unsigned int cmd, unsigned int *res)

    unlocked version

    :param struct hdac_bus \*bus:
        bus object

    :param unsigned int addr:
        *undescribed*

    :param unsigned int cmd:
        HD-audio encoded verb

    :param unsigned int \*res:
        pointer to store the response, NULL if performing asynchronously

.. _`snd_hdac_bus_exec_verb_unlocked.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_bus_queue_event`:

snd_hdac_bus_queue_event
========================

.. c:function:: void snd_hdac_bus_queue_event(struct hdac_bus *bus, u32 res, u32 res_ex)

    add an unsolicited event to queue

    :param struct hdac_bus \*bus:
        the BUS

    :param u32 res:
        unsolicited event (lower 32bit of RIRB entry)

    :param u32 res_ex:
        codec addr and flags (upper 32bit or RIRB entry)

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

    :param struct hdac_bus \*bus:
        HDA core bus

    :param struct hdac_device \*codec:
        HDA core device to add

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

    :param struct hdac_bus \*bus:
        HDA core bus

    :param struct hdac_device \*codec:
        HDA core device to remove

.. This file was automatic generated / don't edit.

