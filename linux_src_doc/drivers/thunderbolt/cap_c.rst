.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/cap.c

.. _`tb_port_find_cap`:

tb_port_find_cap
================

.. c:function:: int tb_port_find_cap(struct tb_port *port, enum tb_port_cap cap)

    Find port capability

    :param port:
        Port to find the capability for
    :type port: struct tb_port \*

    :param cap:
        Capability to look
    :type cap: enum tb_port_cap

.. _`tb_port_find_cap.description`:

Description
-----------

Returns offset to start of capability or \ ``-ENOENT``\  if no such
capability was found. Negative errno is returned if there was an
error.

.. _`tb_switch_find_vse_cap`:

tb_switch_find_vse_cap
======================

.. c:function:: int tb_switch_find_vse_cap(struct tb_switch *sw, enum tb_switch_vse_cap vsec)

    Find switch vendor specific capability

    :param sw:
        Switch to find the capability for
    :type sw: struct tb_switch \*

    :param vsec:
        Vendor specific capability to look
    :type vsec: enum tb_switch_vse_cap

.. _`tb_switch_find_vse_cap.description`:

Description
-----------

Functions enumerates vendor specific capabilities (VSEC) of a switch
and returns offset when capability matching \ ``vsec``\  is found. If no
such capability is found returns \ ``-ENOENT``\ . In case of error returns
negative errno.

.. This file was automatic generated / don't edit.

