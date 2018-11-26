.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_reqmgr.c

.. _`incr_index`:

incr_index
==========

.. c:function:: int incr_index(int index, int count, int max)

    0x00 - Success Completion with no error 0x43 - ERR_GC_DATA_LEN_INVALID Invalid Data length if Encryption Data length is less than 16 bytes for AES-XTS and AES-CTS. 0x45 - ERR_GC_CTX_LEN_INVALID

    :param index:
        *undescribed*
    :type index: int

    :param count:
        *undescribed*
    :type count: int

    :param max:
        *undescribed*
    :type max: int

.. _`incr_index.invalid-context-length`:

Invalid context length
----------------------

CTXL != 23 words.
0x4F - ERR_GC_DOCSIS_CIPHER_INVALID
DOCSIS support is enabled with other than
AES/DES-CBC mode encryption.
0x50 - ERR_GC_DOCSIS_OFFSET_INVALID
Authentication offset is other than 0 with
Encryption IV source = 0.
Authentication offset is other than 8 (DES)/16 (AES)
with Encryption IV source = 1
0x51 - ERR_GC_CRC32_INVALID_SELECTION
CRC32 is enabled for other than DOCSIS encryption.
0x52 - ERR_GC_AES_CCM_FLAG_INVALID
Invalid flag options in AES-CCM IV.

.. _`softreq_unmap_sgbufs`:

softreq_unmap_sgbufs
====================

.. c:function:: void softreq_unmap_sgbufs(struct nitrox_softreq *sr)

    unmap and free the sg lists.

    :param sr:
        *undescribed*
    :type sr: struct nitrox_softreq \*

.. _`create_sg_component`:

create_sg_component
===================

.. c:function:: int create_sg_component(struct nitrox_softreq *sr, struct nitrox_sgtable *sgtbl, int map_nents)

    create SG componets for N5 device.

    :param sr:
        Request structure
    :type sr: struct nitrox_softreq \*

    :param sgtbl:
        SG table
    :type sgtbl: struct nitrox_sgtable \*

    :param map_nents:
        *undescribed*
    :type map_nents: int

.. _`create_sg_component.description`:

Description
-----------

Component structure

63     48 47     32 31    16 15      0
--------------------------------------
\|   LEN0  \|  LEN1  \|  LEN2  \|  LEN3  \|
\|-------------------------------------
\|               PTR0                 \|
--------------------------------------
\|               PTR1                 \|
--------------------------------------
\|               PTR2                 \|
--------------------------------------
\|               PTR3                 \|
--------------------------------------

Returns 0 if success or a negative errno code on error.

.. _`dma_map_inbufs`:

dma_map_inbufs
==============

.. c:function:: int dma_map_inbufs(struct nitrox_softreq *sr, struct se_crypto_request *req)

    DMA map input sglist and creates sglist component for N5 device.

    :param sr:
        Request structure
    :type sr: struct nitrox_softreq \*

    :param req:
        Crypto request structre
    :type req: struct se_crypto_request \*

.. _`dma_map_inbufs.description`:

Description
-----------

Returns 0 if successful or a negative errno code on error.

.. _`post_se_instr`:

post_se_instr
=============

.. c:function:: void post_se_instr(struct nitrox_softreq *sr, struct nitrox_cmdq *cmdq)

    Post SE instruction to Packet Input ring

    :param sr:
        Request structure
    :type sr: struct nitrox_softreq \*

    :param cmdq:
        *undescribed*
    :type cmdq: struct nitrox_cmdq \*

.. _`post_se_instr.description`:

Description
-----------

Returns 0 if successful or a negative error code,
if no space in ring.

.. _`nitrox_process_se_request`:

nitrox_process_se_request
=========================

.. c:function:: int nitrox_process_se_request(struct nitrox_device *ndev, struct se_crypto_request *req, completion_t callback, struct skcipher_request *skreq)

    Send request to SE core

    :param ndev:
        NITROX device
    :type ndev: struct nitrox_device \*

    :param req:
        Crypto request
    :type req: struct se_crypto_request \*

    :param callback:
        *undescribed*
    :type callback: completion_t

    :param skreq:
        *undescribed*
    :type skreq: struct skcipher_request \*

.. _`nitrox_process_se_request.description`:

Description
-----------

Returns 0 on success, or a negative error code.

.. _`process_response_list`:

process_response_list
=====================

.. c:function:: void process_response_list(struct nitrox_cmdq *cmdq)

    process completed requests

    :param cmdq:
        *undescribed*
    :type cmdq: struct nitrox_cmdq \*

.. _`process_response_list.description`:

Description
-----------

Returns the number of responses processed.

.. _`pkt_slc_resp_tasklet`:

pkt_slc_resp_tasklet
====================

.. c:function:: void pkt_slc_resp_tasklet(unsigned long data)

    post processing of SE responses

    :param data:
        *undescribed*
    :type data: unsigned long

.. This file was automatic generated / don't edit.

