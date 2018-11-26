.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/tunnel_pci.c

.. _`tb_pci_alloc`:

tb_pci_alloc
============

.. c:function:: struct tb_pci_tunnel *tb_pci_alloc(struct tb *tb, struct tb_port *up, struct tb_port *down)

    allocate a pci tunnel

    :param tb:
        *undescribed*
    :type tb: struct tb \*

    :param up:
        *undescribed*
    :type up: struct tb_port \*

    :param down:
        *undescribed*
    :type down: struct tb_port \*

.. _`tb_pci_alloc.description`:

Description
-----------

Allocate a PCI tunnel. The ports must be of type TB_TYPE_PCIE_UP and
TB_TYPE_PCIE_DOWN.

Currently only paths consisting of two hops are supported (that is the
ports must be on "adjacent" switches).

The paths are hard-coded to use hop 8 (the only working hop id available on
my thunderbolt devices). Therefore at most ONE path per device may be
activated.

.. _`tb_pci_alloc.return`:

Return
------

Returns a tb_pci_tunnel on success or NULL on failure.

.. _`tb_pci_free`:

tb_pci_free
===========

.. c:function:: void tb_pci_free(struct tb_pci_tunnel *tunnel)

    free a tunnel

    :param tunnel:
        *undescribed*
    :type tunnel: struct tb_pci_tunnel \*

.. _`tb_pci_free.description`:

Description
-----------

The tunnel must have been deactivated.

.. _`tb_pci_is_invalid`:

tb_pci_is_invalid
=================

.. c:function:: bool tb_pci_is_invalid(struct tb_pci_tunnel *tunnel)

    check whether an activated path is still valid

    :param tunnel:
        *undescribed*
    :type tunnel: struct tb_pci_tunnel \*

.. _`tb_pci_port_active`:

tb_pci_port_active
==================

.. c:function:: int tb_pci_port_active(struct tb_port *port, bool active)

    activate/deactivate PCI capability

    :param port:
        *undescribed*
    :type port: struct tb_port \*

    :param active:
        *undescribed*
    :type active: bool

.. _`tb_pci_port_active.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_pci_restart`:

tb_pci_restart
==============

.. c:function:: int tb_pci_restart(struct tb_pci_tunnel *tunnel)

    activate a tunnel after a hardware reset

    :param tunnel:
        *undescribed*
    :type tunnel: struct tb_pci_tunnel \*

.. _`tb_pci_activate`:

tb_pci_activate
===============

.. c:function:: int tb_pci_activate(struct tb_pci_tunnel *tunnel)

    activate a tunnel

    :param tunnel:
        *undescribed*
    :type tunnel: struct tb_pci_tunnel \*

.. _`tb_pci_activate.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_pci_deactivate`:

tb_pci_deactivate
=================

.. c:function:: void tb_pci_deactivate(struct tb_pci_tunnel *tunnel)

    deactivate a tunnel

    :param tunnel:
        *undescribed*
    :type tunnel: struct tb_pci_tunnel \*

.. This file was automatic generated / don't edit.

