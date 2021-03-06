.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/net_namespace.c

.. _`net_ns_get_ownership`:

net_ns_get_ownership
====================

.. c:function:: void net_ns_get_ownership(const struct net *net, kuid_t *uid, kgid_t *gid)

    get sysfs ownership data for \ ``net``\ 

    :param net:
        network namespace in question (can be NULL)
    :type net: const struct net \*

    :param uid:
        kernel user ID for sysfs objects
    :type uid: kuid_t \*

    :param gid:
        kernel group ID for sysfs objects
    :type gid: kgid_t \*

.. _`net_ns_get_ownership.description`:

Description
-----------

Returns the uid/gid pair of root in the user namespace associated with the
given network namespace.

.. _`net_ns_barrier`:

net_ns_barrier
==============

.. c:function:: void net_ns_barrier( void)

    wait until concurrent net_cleanup_work is done

    :param void:
        no arguments
    :type void: 

.. _`net_ns_barrier.description`:

Description
-----------

cleanup_net runs from work queue and will first remove namespaces
from the global list, then run net exit functions.

Call this in module exit path to make sure that all netns
->exit ops have been invoked before the function is removed.

.. _`register_pernet_subsys`:

register_pernet_subsys
======================

.. c:function:: int register_pernet_subsys(struct pernet_operations *ops)

    register a network namespace subsystem

    :param ops:
        pernet operations structure for the subsystem
    :type ops: struct pernet_operations \*

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

.. c:function:: void unregister_pernet_subsys(struct pernet_operations *ops)

    unregister a network namespace subsystem

    :param ops:
        pernet operations structure to manipulate
    :type ops: struct pernet_operations \*

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

.. c:function:: int register_pernet_device(struct pernet_operations *ops)

    register a network namespace device

    :param ops:
        pernet operations structure for the subsystem
    :type ops: struct pernet_operations \*

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

.. c:function:: void unregister_pernet_device(struct pernet_operations *ops)

    unregister a network namespace netdevice

    :param ops:
        pernet operations structure to manipulate
    :type ops: struct pernet_operations \*

.. _`unregister_pernet_device.description`:

Description
-----------

Remove the pernet operations structure from the list to be
used when network namespaces are created or destroyed.  In
addition run the exit method for all existing network
namespaces.

.. This file was automatic generated / don't edit.

