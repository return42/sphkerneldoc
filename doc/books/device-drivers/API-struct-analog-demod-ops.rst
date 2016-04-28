.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-analog-demod-ops:

=======================
struct analog_demod_ops
=======================

*man struct analog_demod_ops(9)*

*4.6.0-rc5*

Demodulation information and callbacks for analog TV and radio


Synopsis
========

.. code-block:: c

    struct analog_demod_ops {
      struct analog_demod_info info;
      void (* set_params) (struct dvb_frontend *fe,struct analog_parameters *params);
      int (* has_signal) (struct dvb_frontend *fe, u16 *signal);
      int (* get_afc) (struct dvb_frontend *fe, s32 *afc);
      void (* tuner_status) (struct dvb_frontend *fe);
      void (* standby) (struct dvb_frontend *fe);
      void (* release) (struct dvb_frontend *fe);
      int (* i2c_gate_ctrl) (struct dvb_frontend *fe, int enable);
      int (* set_config) (struct dvb_frontend *fe, void *priv_cfg);
    };


Members
=======

info
    pointer to struct analog_demod_info

set_params
    callback function used to inform the demod to set the demodulator
    parameters needed to decode an analog or radio channel. The
    properties are passed via struct ``analog_params``;.

has_signal
    returns 0xffff if has signal, or 0 if it doesn't.

get_afc
    Used only by analog TV core. Reports the frequency drift due to AFC.

tuner_status
    callback function that returns tuner status bits, e. g.
    TUNER_STATUS_LOCKED and TUNER_STATUS_STEREO.

standby
    set the tuner to standby mode.

release
    callback function called when frontend is dettached. drivers should
    free any allocated memory.

i2c_gate_ctrl
    controls the I2C gate. Newer drivers should use I2C mux support
    instead.

set_config
    callback function used to send some tuner-specific parameters.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
