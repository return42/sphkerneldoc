.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/cdv_intel_dp.c

.. _`i2c_algo_dp_aux_data`:

struct i2c_algo_dp_aux_data
===========================

.. c:type:: struct i2c_algo_dp_aux_data

    driver interface structure for i2c over dp aux algorithm

.. _`i2c_algo_dp_aux_data.definition`:

Definition
----------

.. code-block:: c

    struct i2c_algo_dp_aux_data {
        bool running;
        u16 address;
        int (*aux_ch)(struct i2c_adapter *adapter,int mode, uint8_t write_byte, uint8_t *read_byte);
    }

.. _`i2c_algo_dp_aux_data.members`:

Members
-------

running
    set by the algo indicating whether an i2c is ongoing or whether
    the i2c bus is quiescent

address
    i2c target address for the currently ongoing transfer

aux_ch
    driver callback to transfer a single byte of the i2c payload

.. _`is_edp`:

is_edp
======

.. c:function:: bool is_edp(struct gma_encoder *encoder)

    is the given port attached to an eDP panel (either CPU or PCH)

    :param struct gma_encoder \*encoder:
        *undescribed*

.. _`is_edp.description`:

Description
-----------

If a CPU or PCH DP output is attached to an eDP panel, this function
will return true, and false otherwise.

.. _`cdv_intel_dp_detect`:

cdv_intel_dp_detect
===================

.. c:function:: enum drm_connector_status cdv_intel_dp_detect(struct drm_connector *connector, bool force)

    :param struct drm_connector \*connector:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`cdv_intel_dp_detect.description`:

Description
-----------

\return true if DP port is connected.
\return false if DP port is disconnected.

.. This file was automatic generated / don't edit.

