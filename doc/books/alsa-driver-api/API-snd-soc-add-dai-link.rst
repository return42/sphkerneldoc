
.. _API-snd-soc-add-dai-link:

====================
snd_soc_add_dai_link
====================

*man snd_soc_add_dai_link(9)*

*4.6.0-rc1*

Add a DAI link dynamically


Synopsis
========

.. c:function:: int snd_soc_add_dai_link( struct snd_soc_card * card, struct snd_soc_dai_link * dai_link )

Arguments
=========

``card``
    The ASoC card to which the DAI link is added

``dai_link``
    The new DAI link to add


Description
===========

This function adds a DAI link to the ASoC card's link list.


Note
====

Topology can use this API to add DAI links when probing the topology component. And machine drivers can still define static DAI links in dai_link array.
