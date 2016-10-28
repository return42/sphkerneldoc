.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/uwbd.c

.. _`uwbd`:

uwbd
====

.. c:function:: int uwbd(void *param)

    :param void \*param:
        *undescribed*

.. _`uwbd.description`:

Description
-----------

Listens to all UWB notifications and takes care to track the state
of the UWB neighbourhood for the kernel. When we do a run, we
spinlock, move the list to a private copy and release the
lock. Hold it as little as possible. Not a conflict: it is
guaranteed we own the events in the private list.

.. _`uwbd.fixme`:

FIXME
-----

should change so we don't have a 1HZ timer all the time, but
only if there are devices.

.. This file was automatic generated / don't edit.

