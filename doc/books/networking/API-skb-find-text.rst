.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-find-text:

=============
skb_find_text
=============

*man skb_find_text(9)*

*4.6.0-rc5*

Find a text pattern in skb data


Synopsis
========

.. c:function:: unsigned int skb_find_text( struct sk_buff * skb, unsigned int from, unsigned int to, struct ts_config * config )

Arguments
=========

``skb``
    the buffer to look in

``from``
    search offset

``to``
    search limit

``config``
    textsearch configuration


Description
===========

Finds a pattern in the skb data according to the specified textsearch
configuration. Use ``textsearch_next`` to retrieve subsequent
occurrences of the pattern. Returns the offset to the first occurrence
or UINT_MAX if no match was found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
