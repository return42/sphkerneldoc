.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpuhotplug.h

.. _`cpuhp_setup_state`:

cpuhp_setup_state
=================

.. c:function:: int cpuhp_setup_state(enum cpuhp_state state, const char *name, int (*startup)(unsigned int cpu), int (*teardown)(unsigned int cpu))

    Setup hotplug state callbacks with calling the callbacks

    :param state:
        The state for which the calls are installed
    :type state: enum cpuhp_state

    :param name:
        Name of the callback (will be used in debug output)
    :type name: const char \*

    :param int (\*startup)(unsigned int cpu):
        startup callback function

    :param int (\*teardown)(unsigned int cpu):
        teardown callback function

.. _`cpuhp_setup_state.description`:

Description
-----------

Installs the callback functions and invokes the startup callback on
the present cpus which have already reached the \ ``state``\ .

.. _`cpuhp_setup_state_nocalls`:

cpuhp_setup_state_nocalls
=========================

.. c:function:: int cpuhp_setup_state_nocalls(enum cpuhp_state state, const char *name, int (*startup)(unsigned int cpu), int (*teardown)(unsigned int cpu))

    Setup hotplug state callbacks without calling the callbacks

    :param state:
        The state for which the calls are installed
    :type state: enum cpuhp_state

    :param name:
        Name of the callback.
    :type name: const char \*

    :param int (\*startup)(unsigned int cpu):
        startup callback function

    :param int (\*teardown)(unsigned int cpu):
        teardown callback function

.. _`cpuhp_setup_state_nocalls.description`:

Description
-----------

Same as \ ``cpuhp_setup_state``\  except that no calls are executed are invoked
during installation of this callback. NOP if SMP=n or HOTPLUG_CPU=n.

.. _`cpuhp_setup_state_multi`:

cpuhp_setup_state_multi
=======================

.. c:function:: int cpuhp_setup_state_multi(enum cpuhp_state state, const char *name, int (*startup)(unsigned int cpu, struct hlist_node *node), int (*teardown)(unsigned int cpu, struct hlist_node *node))

    Add callbacks for multi state

    :param state:
        The state for which the calls are installed
    :type state: enum cpuhp_state

    :param name:
        Name of the callback.
    :type name: const char \*

    :param int (\*startup)(unsigned int cpu, struct hlist_node \*node):
        startup callback function

    :param int (\*teardown)(unsigned int cpu, struct hlist_node \*node):
        teardown callback function

.. _`cpuhp_setup_state_multi.description`:

Description
-----------

Sets the internal multi_instance flag and prepares a state to work as a multi
instance callback. No callbacks are invoked at this point. The callbacks are
invoked once an instance for this state are registered via
\ ``cpuhp_state_add_instance``\  or \ ``cpuhp_state_add_instance_nocalls``\ .

.. _`cpuhp_state_add_instance`:

cpuhp_state_add_instance
========================

.. c:function:: int cpuhp_state_add_instance(enum cpuhp_state state, struct hlist_node *node)

    Add an instance for a state and invoke startup callback.

    :param state:
        The state for which the instance is installed
    :type state: enum cpuhp_state

    :param node:
        The node for this individual state.
    :type node: struct hlist_node \*

.. _`cpuhp_state_add_instance.description`:

Description
-----------

Installs the instance for the \ ``state``\  and invokes the startup callback on
the present cpus which have already reached the \ ``state``\ . The \ ``state``\  must have
been earlier marked as multi-instance by \ ``cpuhp_setup_state_multi``\ .

.. _`cpuhp_state_add_instance_nocalls`:

cpuhp_state_add_instance_nocalls
================================

.. c:function:: int cpuhp_state_add_instance_nocalls(enum cpuhp_state state, struct hlist_node *node)

    Add an instance for a state without invoking the startup callback.

    :param state:
        The state for which the instance is installed
    :type state: enum cpuhp_state

    :param node:
        The node for this individual state.
    :type node: struct hlist_node \*

.. _`cpuhp_state_add_instance_nocalls.description`:

Description
-----------

Installs the instance for the \ ``state``\  The \ ``state``\  must have been earlier
marked as multi-instance by \ ``cpuhp_setup_state_multi``\ .

.. _`cpuhp_remove_state`:

cpuhp_remove_state
==================

.. c:function:: void cpuhp_remove_state(enum cpuhp_state state)

    Remove hotplug state callbacks and invoke the teardown

    :param state:
        The state for which the calls are removed
    :type state: enum cpuhp_state

.. _`cpuhp_remove_state.description`:

Description
-----------

Removes the callback functions and invokes the teardown callback on
the present cpus which have already reached the \ ``state``\ .

.. _`cpuhp_remove_state_nocalls`:

cpuhp_remove_state_nocalls
==========================

.. c:function:: void cpuhp_remove_state_nocalls(enum cpuhp_state state)

    Remove hotplug state callbacks without invoking teardown

    :param state:
        The state for which the calls are removed
    :type state: enum cpuhp_state

.. _`cpuhp_remove_multi_state`:

cpuhp_remove_multi_state
========================

.. c:function:: void cpuhp_remove_multi_state(enum cpuhp_state state)

    Remove hotplug multi state callback

    :param state:
        The state for which the calls are removed
    :type state: enum cpuhp_state

.. _`cpuhp_remove_multi_state.description`:

Description
-----------

Removes the callback functions from a multi state. This is the reverse of
\ :c:func:`cpuhp_setup_state_multi`\ . All instances should have been removed before
invoking this function.

.. _`cpuhp_state_remove_instance`:

cpuhp_state_remove_instance
===========================

.. c:function:: int cpuhp_state_remove_instance(enum cpuhp_state state, struct hlist_node *node)

    Remove hotplug instance from state and invoke the teardown callback

    :param state:
        The state from which the instance is removed
    :type state: enum cpuhp_state

    :param node:
        The node for this individual state.
    :type node: struct hlist_node \*

.. _`cpuhp_state_remove_instance.description`:

Description
-----------

Removes the instance and invokes the teardown callback on the present cpus
which have already reached the \ ``state``\ .

.. _`cpuhp_state_remove_instance_nocalls`:

cpuhp_state_remove_instance_nocalls
===================================

.. c:function:: int cpuhp_state_remove_instance_nocalls(enum cpuhp_state state, struct hlist_node *node)

    Remove hotplug instance from state without invoking the reatdown callback

    :param state:
        The state from which the instance is removed
    :type state: enum cpuhp_state

    :param node:
        The node for this individual state.
    :type node: struct hlist_node \*

.. _`cpuhp_state_remove_instance_nocalls.description`:

Description
-----------

Removes the instance without invoking the teardown callback.

.. This file was automatic generated / don't edit.

