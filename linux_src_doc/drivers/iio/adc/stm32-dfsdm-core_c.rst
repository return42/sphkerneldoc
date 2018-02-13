.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-dfsdm-core.c

.. _`stm32_dfsdm_start_dfsdm`:

stm32_dfsdm_start_dfsdm
=======================

.. c:function:: int stm32_dfsdm_start_dfsdm(struct stm32_dfsdm *dfsdm)

    start global dfsdm interface.

    :param struct stm32_dfsdm \*dfsdm:
        Handle used to retrieve dfsdm context.

.. _`stm32_dfsdm_start_dfsdm.description`:

Description
-----------

Enable interface if n_active_ch is not null.

.. _`stm32_dfsdm_stop_dfsdm`:

stm32_dfsdm_stop_dfsdm
======================

.. c:function:: int stm32_dfsdm_stop_dfsdm(struct stm32_dfsdm *dfsdm)

    stop global DFSDM interface.

    :param struct stm32_dfsdm \*dfsdm:
        Handle used to retrieve dfsdm context.

.. _`stm32_dfsdm_stop_dfsdm.description`:

Description
-----------

Disable interface if n_active_ch is null

.. This file was automatic generated / don't edit.

