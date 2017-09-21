.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/cap.c

.. _`tb_port_find_cap`:

tb_port_find_cap
================

.. c:function:: int tb_port_find_cap(struct tb_port *port, enum tb_port_cap cap)

    Find port capability

    :param struct tb_port \*port:
        Port to find the capability for

    :param enum tb_port_cap cap:
        Capability to look

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

    :param struct tb_switch \*sw:
        Switch to find the capability for

    :param enum tb_switch_vse_cap vsec:
        Vendor specific capability to look

.. _`tb_switch_find_vse_cap.description`:

Description
-----------

Functions enumerates vendor specific capabilities (VSEC) of a switch
and returns offset when capability matching \ ``vsec``\  is found. If no
such capability is found returns \ ``-ENOENT``\ . In case of error returns
negative errno.

.. This file was automatic generated / don't edit.

