.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_reqmgr.c

.. _`softreq_unmap_sgbufs`:

softreq_unmap_sgbufs
====================

.. c:function:: void softreq_unmap_sgbufs(struct nitrox_softreq *sr)

    0x00 - Success Completion with no error 0x43 - ERR_GC_DATA_LEN_INVALID Invalid Data length if Encryption Data length is less than 16 bytes for AES-XTS and AES-CTS. 0x45 - ERR_GC_CTX_LEN_INVALID

    :param struct nitrox_softreq \*sr:
        *undescribed*

.. _`softreq_unmap_sgbufs.invalid-context-length`:

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

.. _`create_sg_component`:

create_sg_component
===================

.. c:function:: int create_sg_component(struct nitrox_softreq *sr, struct nitrox_sgtable *sgtbl, int map_nents)

    create SG componets for N5 device.

    :param struct nitrox_softreq \*sr:
        Request structure

    :param struct nitrox_sgtable \*sgtbl:
        SG table

    :param int map_nents:
        *undescribed*

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

    :param struct nitrox_softreq \*sr:
        Request structure

    :param struct se_crypto_request \*req:
        Crypto request structre

.. _`dma_map_inbufs.description`:

Description
-----------

Returns 0 if successful or a negative errno code on error.

.. _`post_se_instr`:

post_se_instr
=============

.. c:function:: void post_se_instr(struct nitrox_softreq *sr, struct nitrox_cmdq *cmdq)

    Post SE instruction to Packet Input ring

    :param struct nitrox_softreq \*sr:
        Request structure

    :param struct nitrox_cmdq \*cmdq:
        *undescribed*

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

    :param struct nitrox_device \*ndev:
        NITROX device

    :param struct se_crypto_request \*req:
        Crypto request

    :param completion_t callback:
        *undescribed*

    :param struct skcipher_request \*skreq:
        *undescribed*

.. _`nitrox_process_se_request.description`:

Description
-----------

Returns 0 on success, or a negative error code.

.. _`process_response_list`:

process_response_list
=====================

.. c:function:: void process_response_list(struct nitrox_cmdq *cmdq)

    process completed requests

    :param struct nitrox_cmdq \*cmdq:
        *undescribed*

.. _`process_response_list.description`:

Description
-----------

Returns the number of responses processed.

.. _`pkt_slc_resp_handler`:

pkt_slc_resp_handler
====================

.. c:function:: void pkt_slc_resp_handler(unsigned long data)

    post processing of SE responses

    :param unsigned long data:
        *undescribed*

.. This file was automatic generated / don't edit.

