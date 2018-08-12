.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/ctrl.c

.. _`caam_get_era`:

caam_get_era
============

.. c:function:: int caam_get_era(struct caam_ctrl __iomem *ctrl)

    Return the ERA of the SEC on SoC, based on "sec-era" optional property in the DTS. This property is updated by u-boot. In case this property is not passed an attempt to retrieve the CAAM era via register reads will be made.

    :param struct caam_ctrl __iomem \*ctrl:
        *undescribed*

.. This file was automatic generated / don't edit.

