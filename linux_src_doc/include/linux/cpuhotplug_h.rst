.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpuhotplug.h

.. _`cpuhp_setup_state`:

cpuhp_setup_state
=================

.. c:function:: int cpuhp_setup_state(enum cpuhp_state state, const char *name, int (*startup)(unsigned int cpu), int (*teardown)(unsigned int cpu))

    Setup hotplug state callbacks with calling the callbacks

    :param enum cpuhp_state state:
        The state for which the calls are installed

    :param const char \*name:
        Name of the callback (will be used in debug output)

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

    :param enum cpuhp_state state:
        The state for which the calls are installed

    :param const char \*name:
        Name of the callback.

    :param int (\*startup)(unsigned int cpu):
        startup callback function

    :param int (\*teardown)(unsigned int cpu):
        teardown callback function

.. _`cpuhp_setup_state_nocalls.description`:

Description
-----------

Same as \ ``cpuhp_setup_state``\  except that no calls are executed are invoked
during installation of this callback. NOP if SMP=n or HOTPLUG_CPU=n.

.. _`cpuhp_remove_state`:

cpuhp_remove_state
==================

.. c:function:: void cpuhp_remove_state(enum cpuhp_state state)

    Remove hotplug state callbacks and invoke the teardown

    :param enum cpuhp_state state:
        The state for which the calls are removed

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

    :param enum cpuhp_state state:
        The state for which the calls are removed

.. This file was automatic generated / don't edit.

