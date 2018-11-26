.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/fsl_utils.c

.. _`fsl_asoc_get_dma_channel`:

fsl_asoc_get_dma_channel
========================

.. c:function:: int fsl_asoc_get_dma_channel(struct device_node *ssi_np, const char *name, struct snd_soc_dai_link *dai, unsigned int *dma_channel_id, unsigned int *dma_id)

    determine the dma channel for a SSI node

    :param ssi_np:
        pointer to the SSI device tree node
    :type ssi_np: struct device_node \*

    :param name:
        name of the phandle pointing to the dma channel
    :type name: const char \*

    :param dai:
        ASoC DAI link pointer to be filled with platform_name
    :type dai: struct snd_soc_dai_link \*

    :param dma_channel_id:
        dma channel id to be returned
    :type dma_channel_id: unsigned int \*

    :param dma_id:
        dma id to be returned
    :type dma_id: unsigned int \*

.. _`fsl_asoc_get_dma_channel.description`:

Description
-----------

This function determines the dma and channel id for given SSI node.  It
also discovers the platform_name for the ASoC DAI link.

.. This file was automatic generated / don't edit.

