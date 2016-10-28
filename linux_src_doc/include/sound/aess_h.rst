.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/aess.h

.. _`aess_enable_autogating`:

aess_enable_autogating
======================

.. c:function:: void aess_enable_autogating(void __iomem *base)

    enable AESS internal autogating

    :param void __iomem \*base:
        *undescribed*

.. _`aess_enable_autogating.description`:

Description
-----------

Enable internal autogating on the AESS.  This allows the AESS to
indicate that it is idle to the OMAP PRCM.  Returns 0.

.. This file was automatic generated / don't edit.

