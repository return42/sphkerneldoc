.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/vcc.c

.. _`vcc_table_add`:

vcc_table_add
=============

.. c:function:: int vcc_table_add(struct vcc_port *port)

    Add VCC port to the VCC table

    :param struct vcc_port \*port:
        pointer to the VCC port

.. _`vcc_table_add.return`:

Return
------

index of the port in the VCC table on success,
-1 on failure

.. _`vcc_table_remove`:

vcc_table_remove
================

.. c:function:: void vcc_table_remove(unsigned long index)

    Removes a VCC port from the VCC table

    :param unsigned long index:
        Index into the VCC table

.. _`vcc_get`:

vcc_get
=======

.. c:function:: struct vcc_port *vcc_get(unsigned long index, bool excl)

    Gets a reference to VCC port

    :param unsigned long index:
        Index into the VCC table

    :param bool excl:
        Indicates if an exclusive access is requested

.. _`vcc_get.return`:

Return
------

reference to the VCC port, if found
NULL, if port not found

.. _`vcc_put`:

vcc_put
=======

.. c:function:: void vcc_put(struct vcc_port *port, bool excl)

    Returns a reference to VCC port

    :param struct vcc_port \*port:
        pointer to VCC port

    :param bool excl:
        Indicates if the returned reference is an exclusive reference

.. _`vcc_put.note`:

Note
----

It's the caller's responsibility to ensure the correct value
for the excl flag

.. _`vcc_get_ne`:

vcc_get_ne
==========

.. c:function:: struct vcc_port *vcc_get_ne(unsigned long index)

    Get a non-exclusive reference to VCC port

    :param unsigned long index:
        Index into the VCC table

.. _`vcc_get_ne.description`:

Description
-----------

Gets a non-exclusive reference to VCC port, if it's not removed

.. _`vcc_get_ne.return`:

Return
------

pointer to the VCC port, if found
NULL, if port not found

.. _`vcc_event`:

vcc_event
=========

.. c:function:: void vcc_event(void *arg, int event)

    LDC event processing engine

    :param void \*arg:
        VCC private data

    :param int event:
        LDC event

.. _`vcc_event.description`:

Description
-----------

Handles LDC events for VCC

.. _`vcc_probe`:

vcc_probe
=========

.. c:function:: int vcc_probe(struct vio_dev *vdev, const struct vio_device_id *id)

    Initialize VCC port

    :param struct vio_dev \*vdev:
        Pointer to VIO device of the new VCC port

    :param const struct vio_device_id \*id:
        VIO device ID

.. _`vcc_probe.description`:

Description
-----------

Initializes a VCC port to receive serial console data from
the guest domain. Sets up a TTY end point on the control
domain. Sets up VIO/LDC link between the guest & control
domain endpoints.

.. _`vcc_probe.return`:

Return
------

status of the probe

.. _`vcc_remove`:

vcc_remove
==========

.. c:function:: int vcc_remove(struct vio_dev *vdev)

    Terminate a VCC port

    :param struct vio_dev \*vdev:
        Pointer to VIO device of the VCC port

.. _`vcc_remove.description`:

Description
-----------

Terminates a VCC port. Sets up the teardown of TTY and
VIO/LDC link between guest and primary domains.

.. _`vcc_remove.return`:

Return
------

status of removal

.. This file was automatic generated / don't edit.

