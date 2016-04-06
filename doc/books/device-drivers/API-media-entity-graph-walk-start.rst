
.. _API-media-entity-graph-walk-start:

=============================
media_entity_graph_walk_start
=============================

*man media_entity_graph_walk_start(9)*

*4.6.0-rc1*

Start walking the media graph at a given entity


Synopsis
========

.. c:function:: void media_entity_graph_walk_start( struct media_entity_graph * graph, struct media_entity * entity )

Arguments
=========

``graph``
    Media graph structure that will be used to walk the graph

``entity``
    Starting entity


Description
===========

Before using this function, ``media_entity_graph_walk_init`` must be used to allocate resources used for walking the graph. This function initializes the graph traversal structure
to walk the entities graph starting at the given entity. The traversal structure must not be modified by the caller during graph traversal. After the graph walk, the resources must
be released using ``media_entity_graph_walk_cleanup``.
