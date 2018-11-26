.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/configfs/item.c

.. _`config_item_init`:

config_item_init
================

.. c:function:: void config_item_init(struct config_item *item)

    initialize item.

    :param item:
        item in question.
    :type item: struct config_item \*

.. _`config_item_set_name`:

config_item_set_name
====================

.. c:function:: int config_item_set_name(struct config_item *item, const char *fmt,  ...)

    Set the name of an item

    :param item:
        item.
    :type item: struct config_item \*

    :param fmt:
        The \ :c:func:`vsnprintf`\ 's format string.
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`config_item_set_name.description`:

Description
-----------

If strlen(name) >= CONFIGFS_ITEM_NAME_LEN, then use a
dynamically allocated string that \ ``item->ci_name``\  points to.
Otherwise, use the static \ ``item->ci_namebuf``\  array.

.. _`config_item_put`:

config_item_put
===============

.. c:function:: void config_item_put(struct config_item *item)

    decrement refcount for item.

    :param item:
        item.
    :type item: struct config_item \*

.. _`config_item_put.description`:

Description
-----------

Decrement the refcount, and if 0, call \ :c:func:`config_item_cleanup`\ .

.. _`config_group_init`:

config_group_init
=================

.. c:function:: void config_group_init(struct config_group *group)

    initialize a group for use

    :param group:
        config_group
    :type group: struct config_group \*

.. _`config_group_find_item`:

config_group_find_item
======================

.. c:function:: struct config_item *config_group_find_item(struct config_group *group, const char *name)

    search for item in group.

    :param group:
        group we're looking in.
    :type group: struct config_group \*

    :param name:
        item's name.
    :type name: const char \*

.. _`config_group_find_item.description`:

Description
-----------

Iterate over \ ``group->cg_list``\ , looking for a matching config_item.
If matching item is found take a reference and return the item.
Caller must have locked group via \ ``group->cg_subsys->su_mtx``\ .

.. This file was automatic generated / don't edit.

