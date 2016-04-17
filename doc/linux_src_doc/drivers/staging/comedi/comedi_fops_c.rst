.. -*- coding: utf-8; mode: rst -*-

=============
comedi_fops.c
=============


.. _`comedi_file`:

struct comedi_file
==================

.. c:type:: comedi_file

    Per-file private data for COMEDI device


.. _`comedi_file.definition`:

Definition
----------

.. code-block:: c

  struct comedi_file {
    struct comedi_device * dev;
    struct comedi_subdevice * read_subdev;
    struct comedi_subdevice * write_subdev;
    unsigned int last_detach_count;
    bool last_attached:1;
  };


.. _`comedi_file.members`:

Members
-------

:``dev``:
    COMEDI device.

:``read_subdev``:
    Current "read" subdevice.

:``write_subdev``:
    Current "write" subdevice.

:``last_detach_count``:
    Last known detach count.

:``last_attached``:
    Last known attached/detached state.




.. _`comedi_dev_put`:

comedi_dev_put
==============

.. c:function:: int comedi_dev_put (struct comedi_device *dev)

    Release a use of a COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.



.. _`comedi_dev_put.description`:

Description
-----------

Must be called when a user of a COMEDI device is finished with it.
When the last user of the COMEDI device calls this function, the
COMEDI device is destroyed.



.. _`comedi_dev_put.return`:

Return
------

1 if the COMEDI device is destroyed by this call or ``dev`` is
NULL, otherwise return 0.  Callers must not assume the COMEDI
device is still valid if this function returns 0.



.. _`comedi_dev_get_from_minor`:

comedi_dev_get_from_minor
=========================

.. c:function:: struct comedi_device *comedi_dev_get_from_minor (unsigned minor)

    Get COMEDI device by minor device number

    :param unsigned minor:
        Minor device number.



.. _`comedi_dev_get_from_minor.description`:

Description
-----------

Finds the COMEDI device associated with the minor device number, if any,
and increments its reference count.  The COMEDI device is prevented from
being freed until a matching call is made to :c:func:`comedi_dev_put`.



.. _`comedi_dev_get_from_minor.return`:

Return
------

A pointer to the COMEDI device if it exists, with its usage
reference incremented.  Return NULL if no COMEDI device exists with the
specified minor device number.



.. _`comedi_is_subdevice_running`:

comedi_is_subdevice_running
===========================

.. c:function:: bool comedi_is_subdevice_running (struct comedi_subdevice *s)

    Check if async command running on subdevice

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.



.. _`comedi_is_subdevice_running.return`:

Return
------

``true`` if an asynchronous COMEDI command is active on the
subdevice, else ``false``\ .



.. _`comedi_set_spriv_auto_free`:

comedi_set_spriv_auto_free
==========================

.. c:function:: void comedi_set_spriv_auto_free (struct comedi_subdevice *s)

    Mark subdevice private data as freeable

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.



.. _`comedi_set_spriv_auto_free.description`:

Description
-----------

Mark the subdevice as having a pointer to private data that can be
automatically freed when the COMEDI device is detached from the low-level
driver.



.. _`comedi_alloc_spriv`:

comedi_alloc_spriv
==================

.. c:function:: void *comedi_alloc_spriv (struct comedi_subdevice *s, size_t size)

    Allocate memory for the subdevice private data

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param size_t size:
        Size of the memory to allocate.



.. _`comedi_alloc_spriv.description`:

Description
-----------

Allocate memory for the subdevice private data and point ``s``\ ->private
to it.  The memory will be freed automatically when the COMEDI device
is detached from the low-level driver.



.. _`comedi_alloc_spriv.return`:

Return
------

A pointer to the allocated memory ``s``\ ->private on success.
Return NULL on failure.



.. _`comedi_event`:

comedi_event
============

.. c:function:: void comedi_event (struct comedi_device *dev, struct comedi_subdevice *s)

    Handle events for asynchronous COMEDI command

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.



.. _`comedi_event.context`:

Context
-------

:c:func:`in_interrupt` (usually), ``s``\ ->spin_lock spin-lock not held.



.. _`comedi_event.description`:

Description
-----------

If an asynchronous COMEDI command is active on the subdevice, process
any ``COMEDI_CB_``\ ... event flags that have been set, usually by an
interrupt handler.  These may change the run state of the asynchronous
command, wake a task, and/or send a ``SIGIO`` signal.

