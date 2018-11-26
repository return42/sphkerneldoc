.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_irq.h

.. _`dpu_irq_preinstall`:

dpu_irq_preinstall
==================

.. c:function:: void dpu_irq_preinstall(struct msm_kms *kms)

    perform pre-installation of MDSS IRQ handler

    :param kms:
        pointer to kms context
    :type kms: struct msm_kms \*

.. _`dpu_irq_postinstall`:

dpu_irq_postinstall
===================

.. c:function:: int dpu_irq_postinstall(struct msm_kms *kms)

    perform post-installation of MDSS IRQ handler

    :param kms:
        pointer to kms context
    :type kms: struct msm_kms \*

.. _`dpu_irq_uninstall`:

dpu_irq_uninstall
=================

.. c:function:: void dpu_irq_uninstall(struct msm_kms *kms)

    uninstall MDSS IRQ handler

    :param kms:
        *undescribed*
    :type kms: struct msm_kms \*

.. _`dpu_irq`:

dpu_irq
=======

.. c:function:: irqreturn_t dpu_irq(struct msm_kms *kms)

    MDSS level IRQ handler

    :param kms:
        pointer to kms context
    :type kms: struct msm_kms \*

.. This file was automatic generated / don't edit.

