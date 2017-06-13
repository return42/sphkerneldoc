.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/pci/atomisp2/css2400/ia_css_stream.h

.. _`ia_css_stream`:

struct ia_css_stream
====================

.. c:type:: struct ia_css_stream


.. _`ia_css_stream.definition`:

Definition
----------

.. code-block:: c

    struct ia_css_stream {
        struct ia_css_stream_config config;
        struct ia_css_stream_info info;
    #if !defined(HAS_NO_INPUT_SYSTEM) && !defined(USE_INPUT_SYSTEM_VERSION_2401)
        rx_cfg_t csi_rx_config;
    #endif
        bool reconfigure_css_rx;
        struct ia_css_pipe *last_pipe;
        int num_pipes;
        struct ia_css_pipe **pipes;
        struct ia_css_pipe *continuous_pipe;
        struct ia_css_isp_parameters *isp_params_configs;
        struct ia_css_isp_parameters *per_frame_isp_params_configs;
        bool cont_capt;
        bool disable_cont_vf;
    #ifndef ISP2401
        bool stop_copy_preview;
    #endif
        bool started;
    }

.. _`ia_css_stream.members`:

Members
-------

config
    *undescribed*

info
    *undescribed*

csi_rx_config
    *undescribed*

reconfigure_css_rx
    *undescribed*

last_pipe
    *undescribed*

num_pipes
    *undescribed*

pipes
    *undescribed*

continuous_pipe
    *undescribed*

isp_params_configs
    *undescribed*

per_frame_isp_params_configs
    *undescribed*

cont_capt
    *undescribed*

disable_cont_vf
    *undescribed*

stop_copy_preview
    *undescribed*

started
    *undescribed*

.. This file was automatic generated / don't edit.

