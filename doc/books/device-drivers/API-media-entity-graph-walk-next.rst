
.. _API-media-entity-graph-walk-next:

============================
media_entity_graph_walk_next
============================

*man media_entity_graph_walk_next(9)*

*4.6.0-rc1*

Get the next entity in the graph


Synopsis
========

.. c:function:: struct media_entity ⋆ media_entity_graph_walk_next( struct media_entity_graph * graph )

Arguments
=========

``graph``
    Media graph structure


Description
===========

Perform a depth-first traversal of the given media entities graph.

The graph structure must have been previously initialized with a call to ``media_entity_graph_walk_start``.

Return the next entity in the graph or NULL if the whole graph have been traversed.
