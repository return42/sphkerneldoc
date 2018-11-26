.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/media-entity.c

.. _`dev_dbg_obj`:

dev_dbg_obj
===========

.. c:function:: void dev_dbg_obj(const char *event_name, struct media_gobj *gobj)

    Prints in debug mode a change on some object

    :param event_name:
        Name of the event to report. Could be \__func__
    :type event_name: const char \*

    :param gobj:
        Pointer to the object
    :type gobj: struct media_gobj \*

.. _`dev_dbg_obj.description`:

Description
-----------

Enabled only if DEBUG or CONFIG_DYNAMIC_DEBUG. Otherwise, it
won't produce any code.

.. _`media_graph_walk_init`:

media_graph_walk_init
=====================

.. c:function:: int media_graph_walk_init(struct media_graph *graph, struct media_device *mdev)

    Allocate resources for graph walk

    :param graph:
        Media graph structure that will be used to walk the graph
    :type graph: struct media_graph \*

    :param mdev:
        Media device
    :type mdev: struct media_device \*

.. _`media_graph_walk_init.description`:

Description
-----------

Reserve resources for graph walk in media device's current
state. The memory must be released using
\ :c:func:`media_graph_walk_free`\ .

Returns error on failure, zero on success.

.. _`media_graph_walk_cleanup`:

media_graph_walk_cleanup
========================

.. c:function:: void media_graph_walk_cleanup(struct media_graph *graph)

    Release resources related to graph walking

    :param graph:
        Media graph structure that was used to walk the graph
    :type graph: struct media_graph \*

.. This file was automatic generated / don't edit.

