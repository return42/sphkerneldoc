.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/typec/mux.c

.. _`define_mutex`:

DEFINE_MUTEX
============

.. c:function::  DEFINE_MUTEX( switch_lock)

    C Multiplexer/DeMultiplexer Switch support

    :param switch_lock:
        *undescribed*
    :type switch_lock: 

.. _`define_mutex.description`:

Description
-----------

Copyright (C) 2018 Intel Corporation
Author: Heikki Krogerus <heikki.krogerus@linux.intel.com>
        Hans de Goede <hdegoede@redhat.com>

.. _`typec_switch_get`:

typec_switch_get
================

.. c:function:: struct typec_switch *typec_switch_get(struct device *dev)

    Find USB Type-C orientation switch

    :param dev:
        The caller device
    :type dev: struct device \*

.. _`typec_switch_get.description`:

Description
-----------

Finds a switch linked with \ ``dev``\ . Returns a reference to the switch on
success, NULL if no matching connection was found, or
ERR_PTR(-EPROBE_DEFER) when a connection was found but the switch
has not been enumerated yet.

.. _`typec_switch_put`:

typec_switch_put
================

.. c:function:: void typec_switch_put(struct typec_switch *sw)

    Release USB Type-C orientation switch

    :param sw:
        USB Type-C orientation switch
    :type sw: struct typec_switch \*

.. _`typec_switch_put.description`:

Description
-----------

Decrement reference count for \ ``sw``\ .

.. _`typec_switch_register`:

typec_switch_register
=====================

.. c:function:: int typec_switch_register(struct typec_switch *sw)

    Register USB Type-C orientation switch

    :param sw:
        USB Type-C orientation switch
    :type sw: struct typec_switch \*

.. _`typec_switch_register.description`:

Description
-----------

This function registers a switch that can be used for routing the correct
data pairs depending on the cable plug orientation from the USB Type-C
connector to the USB controllers. USB Type-C plugs can be inserted
right-side-up or upside-down.

.. _`typec_switch_unregister`:

typec_switch_unregister
=======================

.. c:function:: void typec_switch_unregister(struct typec_switch *sw)

    Unregister USB Type-C orientation switch

    :param sw:
        USB Type-C orientation switch
    :type sw: struct typec_switch \*

.. _`typec_switch_unregister.description`:

Description
-----------

Unregister switch that was registered with \ :c:func:`typec_switch_register`\ .

.. _`typec_mux_get`:

typec_mux_get
=============

.. c:function:: struct typec_mux *typec_mux_get(struct device *dev, const char *name)

    Find USB Type-C Multiplexer

    :param dev:
        The caller device
    :type dev: struct device \*

    :param name:
        Mux identifier
    :type name: const char \*

.. _`typec_mux_get.description`:

Description
-----------

Finds a mux linked to the caller. This function is primarily meant for the
Type-C drivers. Returns a reference to the mux on success, NULL if no
matching connection was found, or ERR_PTR(-EPROBE_DEFER) when a connection
was found but the mux has not been enumerated yet.

.. _`typec_mux_put`:

typec_mux_put
=============

.. c:function:: void typec_mux_put(struct typec_mux *mux)

    Release handle to a Multiplexer

    :param mux:
        USB Type-C Connector Multiplexer/DeMultiplexer
    :type mux: struct typec_mux \*

.. _`typec_mux_put.description`:

Description
-----------

Decrements reference count for \ ``mux``\ .

.. _`typec_mux_register`:

typec_mux_register
==================

.. c:function:: int typec_mux_register(struct typec_mux *mux)

    Register Multiplexer routing USB Type-C pins

    :param mux:
        USB Type-C Connector Multiplexer/DeMultiplexer
    :type mux: struct typec_mux \*

.. _`typec_mux_register.description`:

Description
-----------

USB Type-C connectors can be used for alternate modes of operation besides
USB when Accessory/Alternate Modes are supported. With some of those modes,
the pins on the connector need to be reconfigured. This function registers
multiplexer switches routing the pins on the connector.

.. _`typec_mux_unregister`:

typec_mux_unregister
====================

.. c:function:: void typec_mux_unregister(struct typec_mux *mux)

    Unregister Multiplexer Switch

    :param mux:
        USB Type-C Connector Multiplexer/DeMultiplexer
    :type mux: struct typec_mux \*

.. _`typec_mux_unregister.description`:

Description
-----------

Unregister mux that was registered with \ :c:func:`typec_mux_register`\ .

.. This file was automatic generated / don't edit.

