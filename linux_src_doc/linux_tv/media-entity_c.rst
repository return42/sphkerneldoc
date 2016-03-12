.. -*- coding: utf-8; mode: rst -*-

==============
media-entity.c
==============



.. _xref_dev_dbg_obj:

dev_dbg_obj
===========

.. c:function:: void dev_dbg_obj (const char * event_name, struct media_gobj * gobj)

    Prints in debug mode a change on some object

    :param const char * event_name:
        Name of the event to report. Could be __func__

    :param struct media_gobj * gobj:
        Pointer to the object



Description
-----------

Enabled only if DEBUG or CONFIG_DYNAMIC_DEBUG. Otherwise, it
won't produce any code.




.. _xref_media_entity_graph_walk_init:

media_entity_graph_walk_init
============================

.. c:function:: int media_entity_graph_walk_init (struct media_entity_graph * graph, struct media_device * mdev)

    Allocate resources for graph walk

    :param struct media_entity_graph * graph:
        Media graph structure that will be used to walk the graph

    :param struct media_device * mdev:
        Media device



Description
-----------

Reserve resources for graph walk in media device's current
state. The memory must be released using
:c:func:`media_entity_graph_walk_free`.


Returns error on failure, zero on success.




.. _xref_media_entity_graph_walk_cleanup:

media_entity_graph_walk_cleanup
===============================

.. c:function:: void media_entity_graph_walk_cleanup (struct media_entity_graph * graph)

    Release resources related to graph walking

    :param struct media_entity_graph * graph:
        Media graph structure that was used to walk the graph


