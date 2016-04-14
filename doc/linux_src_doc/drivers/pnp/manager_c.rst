.. -*- coding: utf-8; mode: rst -*-

=========
manager.c
=========

.. _`pnp_assign_resources`:

pnp_assign_resources
====================

.. c:function:: int pnp_assign_resources (struct pnp_dev *dev, int set)

    assigns resources to the device based on the specified dependent number

    :param struct pnp_dev \*dev:
        pointer to the desired device

    :param int set:
        the dependent function number


.. _`pnp_auto_config_dev`:

pnp_auto_config_dev
===================

.. c:function:: int pnp_auto_config_dev (struct pnp_dev *dev)

    automatically assigns resources to a device

    :param struct pnp_dev \*dev:
        pointer to the desired device


.. _`pnp_start_dev`:

pnp_start_dev
=============

.. c:function:: int pnp_start_dev (struct pnp_dev *dev)

    low-level start of the PnP device

    :param struct pnp_dev \*dev:
        pointer to the desired device


.. _`pnp_start_dev.description`:

Description
-----------

assumes that resources have already been allocated


.. _`pnp_stop_dev`:

pnp_stop_dev
============

.. c:function:: int pnp_stop_dev (struct pnp_dev *dev)

    low-level disable of the PnP device

    :param struct pnp_dev \*dev:
        pointer to the desired device


.. _`pnp_stop_dev.description`:

Description
-----------

does not free resources


.. _`pnp_activate_dev`:

pnp_activate_dev
================

.. c:function:: int pnp_activate_dev (struct pnp_dev *dev)

    activates a PnP device for use

    :param struct pnp_dev \*dev:
        pointer to the desired device


.. _`pnp_activate_dev.description`:

Description
-----------

does not validate or set resources so be careful.


.. _`pnp_disable_dev`:

pnp_disable_dev
===============

.. c:function:: int pnp_disable_dev (struct pnp_dev *dev)

    disables device

    :param struct pnp_dev \*dev:
        pointer to the desired device


.. _`pnp_disable_dev.description`:

Description
-----------

inform the correct pnp protocol so that resources can be used by other devices

