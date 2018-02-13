.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/rmi4/rmi_bus.c

.. _`rmi_register_transport_device`:

rmi_register_transport_device
=============================

.. c:function:: int rmi_register_transport_device(struct rmi_transport_dev *xport)

    register a transport device connection on the RMI bus.  Transport drivers provide communication from the devices on a bus (such as SPI, I2C, and so on) to the RMI4 sensor.

    :param struct rmi_transport_dev \*xport:
        the transport device to register

.. _`rmi_unregister_transport_device`:

rmi_unregister_transport_device
===============================

.. c:function:: void rmi_unregister_transport_device(struct rmi_transport_dev *xport)

    unregister a transport device connection

    :param struct rmi_transport_dev \*xport:
        the transport driver to unregister

.. _`__rmi_register_function_handler`:

\__rmi_register_function_handler
================================

.. c:function:: int __rmi_register_function_handler(struct rmi_function_handler *handler, struct module *owner, const char *mod_name)

    register a handler for an RMI function

    :param struct rmi_function_handler \*handler:
        RMI handler that should be registered.

    :param struct module \*owner:
        *undescribed*

    :param const char \*mod_name:
        name of the module implementing the handler

.. _`__rmi_register_function_handler.description`:

Description
-----------

This function performs additional setup of RMI function handler and
registers it with the RMI core so that it can be bound to
RMI function devices.

.. _`rmi_unregister_function_handler`:

rmi_unregister_function_handler
===============================

.. c:function:: void rmi_unregister_function_handler(struct rmi_function_handler *handler)

    unregister given RMI function handler

    :param struct rmi_function_handler \*handler:
        RMI handler that should be unregistered.

.. _`rmi_unregister_function_handler.description`:

Description
-----------

This function unregisters given function handler from RMI core which
causes it to be unbound from the function devices.

.. This file was automatic generated / don't edit.

