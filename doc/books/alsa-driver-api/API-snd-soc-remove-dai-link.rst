
.. _API-snd-soc-remove-dai-link:

=======================
snd_soc_remove_dai_link
=======================

*man snd_soc_remove_dai_link(9)*

*4.6.0-rc1*

Remove a DAI link from the list


Synopsis
========

.. c:function:: void snd_soc_remove_dai_link( struct snd_soc_card * card, struct snd_soc_dai_link * dai_link )

Arguments
=========

``card``
    The ASoC card that owns the link

``dai_link``
    The DAI link to remove


Description
===========

This function removes a DAI link from the ASoC card's link list.

For DAI links previously added by topology, topology should remove them by using the dobj embedded in the link.
