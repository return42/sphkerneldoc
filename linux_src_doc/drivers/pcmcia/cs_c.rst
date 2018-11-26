.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/cs.c

.. _`pcmcia_register_socket`:

pcmcia_register_socket
======================

.. c:function:: int pcmcia_register_socket(struct pcmcia_socket *socket)

    add a new pcmcia socket device

    :param socket:
        the \ :c:type:`struct socket <socket>`\  to register
    :type socket: struct pcmcia_socket \*

.. _`pcmcia_unregister_socket`:

pcmcia_unregister_socket
========================

.. c:function:: void pcmcia_unregister_socket(struct pcmcia_socket *socket)

    remove a pcmcia socket device

    :param socket:
        the \ :c:type:`struct socket <socket>`\  to unregister
    :type socket: struct pcmcia_socket \*

.. _`pcmcia_parse_uevents`:

pcmcia_parse_uevents
====================

.. c:function:: void pcmcia_parse_uevents(struct pcmcia_socket *s, u_int events)

    tell pccardd to issue manual commands

    :param s:
        the PCMCIA socket we wan't to command
    :type s: struct pcmcia_socket \*

    :param events:
        events to pass to pccardd
    :type events: u_int

.. _`pcmcia_parse_uevents.description`:

Description
-----------

userspace-issued insert, eject, suspend and resume commands must be
handled by pccardd to avoid any sysfs-related deadlocks. Valid events
are PCMCIA_UEVENT_EJECT (for eject), PCMCIA_UEVENT__INSERT (for insert),
PCMCIA_UEVENT_RESUME (for resume), PCMCIA_UEVENT_SUSPEND (for suspend)
and PCMCIA_UEVENT_REQUERY (for re-querying the PCMCIA card).

.. This file was automatic generated / don't edit.

