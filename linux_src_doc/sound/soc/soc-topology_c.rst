.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-topology.c

.. _`pcm_new_ver`:

pcm_new_ver
===========

.. c:function:: int pcm_new_ver(struct soc_tplg *tplg, struct snd_soc_tplg_pcm *src, struct snd_soc_tplg_pcm **pcm)

    Create the new version of PCM from the old version.

    :param tplg:
        topology context
    :type tplg: struct soc_tplg \*

    :param src:
        older version of pcm as a source
    :type src: struct snd_soc_tplg_pcm \*

    :param pcm:
        latest version of pcm created from the source
    :type pcm: struct snd_soc_tplg_pcm \*\*

.. _`pcm_new_ver.description`:

Description
-----------

Support from vesion 4. User should free the returned pcm manually.

.. _`set_link_hw_format`:

set_link_hw_format
==================

.. c:function:: void set_link_hw_format(struct snd_soc_dai_link *link, struct snd_soc_tplg_link_config *cfg)

    Set the HW audio format of the physical DAI link.

    :param link:
        \ :c:type:`struct snd_soc_dai_link <snd_soc_dai_link>`\  which should be updated
    :type link: struct snd_soc_dai_link \*

    :param cfg:
        physical link configs.
    :type cfg: struct snd_soc_tplg_link_config \*

.. _`set_link_hw_format.description`:

Description
-----------

Topology context contains a list of supported HW formats (configs) and
a default format ID for the physical link. This function will use this
default ID to choose the HW format to set the link's DAI format for init.

.. _`link_new_ver`:

link_new_ver
============

.. c:function:: int link_new_ver(struct soc_tplg *tplg, struct snd_soc_tplg_link_config *src, struct snd_soc_tplg_link_config **link)

    Create a new physical link config from the old version of source.

    :param tplg:
        topology context
    :type tplg: struct soc_tplg \*

    :param src:
        old version of phyical link config as a source
    :type src: struct snd_soc_tplg_link_config \*

    :param link:
        latest version of physical link config created from the source
    :type link: struct snd_soc_tplg_link_config \*\*

.. _`link_new_ver.description`:

Description
-----------

Support from vesion 4. User need free the returned link config manually.

.. _`soc_tplg_dai_config`:

soc_tplg_dai_config
===================

.. c:function:: int soc_tplg_dai_config(struct soc_tplg *tplg, struct snd_soc_tplg_dai *d)

    Find and configure an existing physical DAI.

    :param tplg:
        topology context
    :type tplg: struct soc_tplg \*

    :param d:
        physical DAI configs.
    :type d: struct snd_soc_tplg_dai \*

.. _`soc_tplg_dai_config.description`:

Description
-----------

The physical dai should already be registered by the platform driver.
The platform driver should specify the DAI name and ID for matching.

.. _`manifest_new_ver`:

manifest_new_ver
================

.. c:function:: int manifest_new_ver(struct soc_tplg *tplg, struct snd_soc_tplg_manifest *src, struct snd_soc_tplg_manifest **manifest)

    Create a new version of manifest from the old version of source.

    :param tplg:
        topology context
    :type tplg: struct soc_tplg \*

    :param src:
        old version of manifest as a source
    :type src: struct snd_soc_tplg_manifest \*

    :param manifest:
        latest version of manifest created from the source
    :type manifest: struct snd_soc_tplg_manifest \*\*

.. _`manifest_new_ver.description`:

Description
-----------

Support from vesion 4. Users need free the returned manifest manually.

.. This file was automatic generated / don't edit.

