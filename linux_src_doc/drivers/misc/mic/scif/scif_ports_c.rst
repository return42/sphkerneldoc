.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_ports.c

.. _`__scif_get_port`:

__scif_get_port
===============

.. c:function:: int __scif_get_port(int start, int end)

    Reserve a specified port # for SCIF and add it to the global list.

    :param int start:
        *undescribed*

    :param int end:
        *undescribed*

.. _`scif_rsrv_port`:

scif_rsrv_port
==============

.. c:function:: int scif_rsrv_port(u16 port)

    Reserve a specified port # for SCIF.

    :param u16 port:
        port # to be reserved.

.. _`scif_get_new_port`:

scif_get_new_port
=================

.. c:function:: int scif_get_new_port( void)

    Get and reserve any port # for SCIF in the range SCIF_PORT_RSVD + 1 to SCIF_PORT_COUNT - 1.

    :param  void:
        no arguments

.. _`scif_get_port`:

scif_get_port
=============

.. c:function:: void scif_get_port(u16 id)

    Increment the reference count for a SCIF port

    :param u16 id:
        SCIF port

.. _`scif_put_port`:

scif_put_port
=============

.. c:function:: void scif_put_port(u16 id)

    Release a reserved SCIF port

    :param u16 id:
        SCIF port to be released.

.. This file was automatic generated / don't edit.

