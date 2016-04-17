.. -*- coding: utf-8; mode: rst -*-

===============
net_namespace.c
===============


.. _`register_pernet_subsys`:

register_pernet_subsys
======================

.. c:function:: int register_pernet_subsys (struct pernet_operations *ops)

    register a network namespace subsystem

    :param struct pernet_operations \*ops:
        pernet operations structure for the subsystem



.. _`register_pernet_subsys.description`:

Description
-----------

Register a subsystem which has init and exit functions
that are called when network namespaces are created and
destroyed respectively.

When registered all network namespace init functions are
called for every existing network namespace.  Allowing kernel
modules to have a race free view of the set of network namespaces.

When a new network namespace is created all of the init
methods are called in the order in which they were registered.

When a network namespace is destroyed all of the exit methods
are called in the reverse of the order with which they were
registered.



.. _`unregister_pernet_subsys`:

unregister_pernet_subsys
========================

.. c:function:: void unregister_pernet_subsys (struct pernet_operations *ops)

    unregister a network namespace subsystem

    :param struct pernet_operations \*ops:
        pernet operations structure to manipulate



.. _`unregister_pernet_subsys.description`:

Description
-----------

Remove the pernet operations structure from the list to be
used when network namespaces are created or destroyed.  In
addition run the exit method for all existing network
namespaces.



.. _`register_pernet_device`:

register_pernet_device
======================

.. c:function:: int register_pernet_device (struct pernet_operations *ops)

    register a network namespace device

    :param struct pernet_operations \*ops:
        pernet operations structure for the subsystem



.. _`register_pernet_device.description`:

Description
-----------

Register a device which has init and exit functions
that are called when network namespaces are created and
destroyed respectively.

When registered all network namespace init functions are
called for every existing network namespace.  Allowing kernel
modules to have a race free view of the set of network namespaces.

When a new network namespace is created all of the init
methods are called in the order in which they were registered.

When a network namespace is destroyed all of the exit methods
are called in the reverse of the order with which they were
registered.



.. _`unregister_pernet_device`:

unregister_pernet_device
========================

.. c:function:: void unregister_pernet_device (struct pernet_operations *ops)

    unregister a network namespace netdevice

    :param struct pernet_operations \*ops:
        pernet operations structure to manipulate



.. _`unregister_pernet_device.description`:

Description
-----------

Remove the pernet operations structure from the list to be
used when network namespaces are created or destroyed.  In
addition run the exit method for all existing network
namespaces.

