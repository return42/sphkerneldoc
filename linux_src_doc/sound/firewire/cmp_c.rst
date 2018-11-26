.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/cmp.c

.. _`cmp_connection_init`:

cmp_connection_init
===================

.. c:function:: int cmp_connection_init(struct cmp_connection *c, struct fw_unit *unit, enum cmp_direction direction, unsigned int pcr_index)

    initializes a connection manager

    :param c:
        the connection manager to initialize
    :type c: struct cmp_connection \*

    :param unit:
        a unit of the target device
    :type unit: struct fw_unit \*

    :param direction:
        input or output
    :type direction: enum cmp_direction

    :param pcr_index:
        the index of the iPCR/oPCR on the target device
    :type pcr_index: unsigned int

.. _`cmp_connection_check_used`:

cmp_connection_check_used
=========================

.. c:function:: int cmp_connection_check_used(struct cmp_connection *c, bool *used)

    check connection is already esablished or not

    :param c:
        the connection manager to be checked
    :type c: struct cmp_connection \*

    :param used:
        the pointer to store the result of checking the connection
    :type used: bool \*

.. _`cmp_connection_destroy`:

cmp_connection_destroy
======================

.. c:function:: void cmp_connection_destroy(struct cmp_connection *c)

    free connection manager resources

    :param c:
        the connection manager
    :type c: struct cmp_connection \*

.. _`cmp_connection_establish`:

cmp_connection_establish
========================

.. c:function:: int cmp_connection_establish(struct cmp_connection *c, unsigned int max_payload_bytes)

    establish a connection to the target

    :param c:
        the connection manager
    :type c: struct cmp_connection \*

    :param max_payload_bytes:
        the amount of data (including CIP headers) per packet
    :type max_payload_bytes: unsigned int

.. _`cmp_connection_establish.description`:

Description
-----------

This function establishes a point-to-point connection from the local
computer to the target by allocating isochronous resources (channel and
bandwidth) and setting the target's input/output plug control register.
When this function succeeds, the caller is responsible for starting
transmitting packets.

.. _`cmp_connection_update`:

cmp_connection_update
=====================

.. c:function:: int cmp_connection_update(struct cmp_connection *c)

    update the connection after a bus reset

    :param c:
        the connection manager
    :type c: struct cmp_connection \*

.. _`cmp_connection_update.description`:

Description
-----------

This function must be called from the driver's .update handler to
reestablish any connection that might have been active.

Returns zero on success, or a negative error code.  On an error, the
connection is broken and the caller must stop transmitting iso packets.

.. _`cmp_connection_break`:

cmp_connection_break
====================

.. c:function:: void cmp_connection_break(struct cmp_connection *c)

    break the connection to the target

    :param c:
        the connection manager
    :type c: struct cmp_connection \*

.. _`cmp_connection_break.description`:

Description
-----------

This function deactives the connection in the target's input/output plug
control register, and frees the isochronous resources of the connection.
Before calling this function, the caller should cease transmitting packets.

.. This file was automatic generated / don't edit.

