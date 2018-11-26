.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_os.c

.. _`qla2x00_config_dma_addressing`:

qla2x00_config_dma_addressing
=============================

.. c:function:: void qla2x00_config_dma_addressing(struct qla_hw_data *ha)

    Configure OS DMA addressing method.

    :param ha:
        HA context
    :type ha: struct qla_hw_data \*

.. _`qla2x00_config_dma_addressing.description`:

Description
-----------

At exit, the \ ``ha``\ 's flags.enable_64bit_addressing set to indicated
supported addressing method.

.. _`qla2x00_module_init`:

qla2x00_module_init
===================

.. c:function:: int qla2x00_module_init( void)

    Module initialization.

    :param void:
        no arguments
    :type void: 

.. _`qla2x00_module_exit`:

qla2x00_module_exit
===================

.. c:function:: void __exit qla2x00_module_exit( void)

    Module cleanup.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

