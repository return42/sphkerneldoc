.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/livepatch/core.c

.. _`klp_disable_patch`:

klp_disable_patch
=================

.. c:function:: int klp_disable_patch(struct klp_patch *patch)

    disables a registered patch

    :param struct klp_patch \*patch:
        The registered, enabled patch to be disabled

.. _`klp_disable_patch.description`:

Description
-----------

Unregisters the patched functions from ftrace.

.. _`klp_disable_patch.return`:

Return
------

0 on success, otherwise error

.. _`klp_enable_patch`:

klp_enable_patch
================

.. c:function:: int klp_enable_patch(struct klp_patch *patch)

    enables a registered patch

    :param struct klp_patch \*patch:
        The registered, disabled patch to be enabled

.. _`klp_enable_patch.description`:

Description
-----------

Performs the needed symbol lookups and code relocations,
then registers the patched functions with ftrace.

.. _`klp_enable_patch.return`:

Return
------

0 on success, otherwise error

.. _`klp_unregister_patch`:

klp_unregister_patch
====================

.. c:function:: int klp_unregister_patch(struct klp_patch *patch)

    unregisters a patch

    :param struct klp_patch \*patch:
        Disabled patch to be unregistered

.. _`klp_unregister_patch.description`:

Description
-----------

Frees the data structures and removes the sysfs interface.

.. _`klp_unregister_patch.return`:

Return
------

0 on success, otherwise error

.. _`klp_register_patch`:

klp_register_patch
==================

.. c:function:: int klp_register_patch(struct klp_patch *patch)

    registers a patch

    :param struct klp_patch \*patch:
        Patch to be registered

.. _`klp_register_patch.description`:

Description
-----------

Initializes the data structure associated with the patch and
creates the sysfs interface.

There is no need to take the reference on the patch module here. It is done
later when the patch is enabled.

.. _`klp_register_patch.return`:

Return
------

0 on success, otherwise error

.. This file was automatic generated / don't edit.

