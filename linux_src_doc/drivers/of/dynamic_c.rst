.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/dynamic.c

.. _`of_node_get`:

of_node_get
===========

.. c:function:: struct device_node *of_node_get(struct device_node *node)

    Increment refcount of a node

    :param node:
        Node to inc refcount, NULL is supported to simplify writing of
        callers
    :type node: struct device_node \*

.. _`of_node_get.description`:

Description
-----------

Returns node.

.. _`of_node_put`:

of_node_put
===========

.. c:function:: void of_node_put(struct device_node *node)

    Decrement refcount of a node

    :param node:
        Node to dec refcount, NULL is supported to simplify writing of
        callers
    :type node: struct device_node \*

.. _`of_attach_node`:

of_attach_node
==============

.. c:function:: int of_attach_node(struct device_node *np)

    Plug a device node into the tree and global list.

    :param np:
        *undescribed*
    :type np: struct device_node \*

.. _`of_detach_node`:

of_detach_node
==============

.. c:function:: int of_detach_node(struct device_node *np)

    "Unplug" a node from the device tree.

    :param np:
        *undescribed*
    :type np: struct device_node \*

.. _`of_detach_node.description`:

Description
-----------

The caller must hold a reference to the node.  The memory associated with
the node is not freed until its refcount goes to zero.

.. _`of_node_release`:

of_node_release
===============

.. c:function:: void of_node_release(struct kobject *kobj)

    release a dynamically allocated node

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

.. _`of_node_release.description`:

Description
-----------

In \ :c:func:`of_node_put`\  this function is passed to \ :c:func:`kref_put`\  as the destructor.

.. _`__of_prop_dup`:

\__of_prop_dup
==============

.. c:function:: struct property *__of_prop_dup(const struct property *prop, gfp_t allocflags)

    Copy a property dynamically.

    :param prop:
        Property to copy
    :type prop: const struct property \*

    :param allocflags:
        Allocation flags (typically pass GFP_KERNEL)
    :type allocflags: gfp_t

.. _`__of_prop_dup.description`:

Description
-----------

Copy a property by dynamically allocating the memory of both the
property structure and the property name & contents. The property's
flags have the OF_DYNAMIC bit set so that we can differentiate between
dynamically allocated properties and not.
Returns the newly allocated property or NULL on out of memory error.

.. _`__of_node_dup`:

\__of_node_dup
==============

.. c:function:: struct device_node *__of_node_dup(const struct device_node *np, const char *full_name)

    Duplicate or create an empty device node dynamically.

    :param np:
        if not NULL, contains properties to be duplicated in new node
    :type np: const struct device_node \*

    :param full_name:
        string value to be duplicated into new node's full_name field
    :type full_name: const char \*

.. _`__of_node_dup.description`:

Description
-----------

Create a device tree node, optionally duplicating the properties of
another node.  The node data are dynamically allocated and all the node
flags have the OF_DYNAMIC & OF_DETACHED bits set.

Returns the newly allocated node or NULL on out of memory error.

.. _`of_changeset_init`:

of_changeset_init
=================

.. c:function:: void of_changeset_init(struct of_changeset *ocs)

    Initialize a changeset for use

    :param ocs:
        changeset pointer
    :type ocs: struct of_changeset \*

.. _`of_changeset_init.description`:

Description
-----------

Initialize a changeset structure

.. _`of_changeset_destroy`:

of_changeset_destroy
====================

.. c:function:: void of_changeset_destroy(struct of_changeset *ocs)

    Destroy a changeset

    :param ocs:
        changeset pointer
    :type ocs: struct of_changeset \*

.. _`of_changeset_destroy.description`:

Description
-----------

Destroys a changeset. Note that if a changeset is applied,
its changes to the tree cannot be reverted.

.. _`of_changeset_apply`:

of_changeset_apply
==================

.. c:function:: int of_changeset_apply(struct of_changeset *ocs)

    Applies a changeset

    :param ocs:
        changeset pointer
    :type ocs: struct of_changeset \*

.. _`of_changeset_apply.description`:

Description
-----------

Applies a changeset to the live tree.
Any side-effects of live tree state changes are applied here on
success, like creation/destruction of devices and side-effects
like creation of sysfs properties and directories.
Returns 0 on success, a negative error value in case of an error.
On error the partially applied effects are reverted.

.. _`of_changeset_revert`:

of_changeset_revert
===================

.. c:function:: int of_changeset_revert(struct of_changeset *ocs)

    Reverts an applied changeset

    :param ocs:
        changeset pointer
    :type ocs: struct of_changeset \*

.. _`of_changeset_revert.description`:

Description
-----------

Reverts a changeset returning the state of the tree to what it
was before the application.
Any side-effects like creation/destruction of devices and
removal of sysfs properties and directories are applied.
Returns 0 on success, a negative error value in case of an error.

.. _`of_changeset_action`:

of_changeset_action
===================

.. c:function:: int of_changeset_action(struct of_changeset *ocs, unsigned long action, struct device_node *np, struct property *prop)

    Add an action to the tail of the changeset list

    :param ocs:
        changeset pointer
    :type ocs: struct of_changeset \*

    :param action:
        action to perform
    :type action: unsigned long

    :param np:
        Pointer to device node
    :type np: struct device_node \*

    :param prop:
        Pointer to property
    :type prop: struct property \*

.. _`of_changeset_action.on-action-being-one-of`:

On action being one of
----------------------

+ OF_RECONFIG_ATTACH_NODE
+ OF_RECONFIG_DETACH_NODE,
+ OF_RECONFIG_ADD_PROPERTY
+ OF_RECONFIG_REMOVE_PROPERTY,
+ OF_RECONFIG_UPDATE_PROPERTY
Returns 0 on success, a negative error value in case of an error.

.. This file was automatic generated / don't edit.

